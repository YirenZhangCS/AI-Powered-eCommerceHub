from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class ActionCheckOrderStatus(Action):
    def name(self) -> Text:
        return "action_check_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        order_number = tracker.get_slot("order_number")
        image_url = tracker.get_slot("image_url")  
        intent = tracker.get_intent_of_latest_message()
        decision = None
        
        if order_number and image_url:
            
            decision = get_decision_from_model(image_url, intent)
            
            if decision:
                response_text = f"Your order status is: {decision}."
                dispatcher.utter_message(text=response_text)
            else:
                dispatcher.utter_message(text="I'm sorry, I couldn't determine your order status.")
        else:
            dispatcher.utter_message(text="Please provide your order number and upload the required image.")
        
        return [AllSlotsReset()]

class ActionAskOrderNumber(Action):
    def name(self) -> Text:
        return "utter_ask_order_number"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="What's your order number?")
        return []

class ActionAskUploadImage(Action):
    def name(self) -> Text:
        return "action_ask_upload_image"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        intent = tracker.get_intent_of_latest_message()

        # 根据意图类型发送不同的图片上传请求
        if intent == "ask_product_status":
            dispatcher.utter_message(text="Please upload a related picture of the delivered product.")
        elif intent == "ask_box_status":
            dispatcher.utter_message(text="Please upload a related picture of the damaged shipping box.")
        elif intent == "report_a_fraudulent_transaction":
            dispatcher.utter_message(text="Please upload a related picture of the OCR.")
        else:
            dispatcher.utter_message(text="Please upload the related picture.")
        
        return []

def get_decision_from_model(image_url: Text, query_type: Text) -> Text:
   
    try:
        response = openai.Image.create(
            file=image_url,
            prompt=f"Analyze {query_type} image and decide whether to Refund, Replace, or Escalate.",
            model="image-davinci-003"
        )
        
        decision = response['choices'][0]['text'].strip()
        return decision
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

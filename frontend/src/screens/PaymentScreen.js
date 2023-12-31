import React, { useState } from 'react'
import { Form, Button, Col } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import FormContainer from '../components/FormContainer'
import { savePaymentMethod } from '../actions/cartActions'
import CheckoutSteps from '../components/CheckoutSteps'

const PaymenScreen = ({ history }) => {
  const cart = useSelector((state) => state.cart)
  const { shippingAddress } = cart

  if (!shippingAddress) {
    history.push('/shipping')
  }
  const [paymentMethod, setPaymentMethod] = useState('Paypal')
  const dispatch = useDispatch()
  const submitHandler = (e) => {
    e.preventDefault()
    dispatch(savePaymentMethod(paymentMethod))
    history.push('/placeorder')
  }
  return (
    <FormContainer>
      <CheckoutSteps step1 step2 step3 />
      <h1>Payment Method</h1>
      <Form onSubmit={submitHandler}>
        <Form.Group>
          <Form.Label as='legend'>Select Payment Method</Form.Label>

          <Col>
            <Form.Check
              type='radio'
              label='Paypal'
              id='Paypal'
              name='paymenMethod'
              value='Paypal'
              checked
              onChange={(e) => setPaymentMethod(e.target.value)}
            ></Form.Check>
            {/* <Form.Check
              type='radio'
              label='支付宝'
              id='支付宝'
              name='paymenMethod'
              value='支付宝'
              checked
              onChange={(e) => setPaymentMethod(e.target.value)}
            ></Form.Check> */}
          </Col>
        </Form.Group>
        <Button type='submit' variant='primary'>
          Next
        </Button>
      </Form>
    </FormContainer>
  )
}

export default PaymenScreen
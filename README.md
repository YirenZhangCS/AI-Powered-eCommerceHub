![Open Banner](MERN.png)

# eCommerceHub-A Full-stack MERN Website

## Project Goal
Built a custom web application with MERN stack, empowering users to add, edit, and delete items.

## Features

* Created a single-page application utilizing React.js, seamlessly integrating container components with Redux to manage actions and reducers. 
* Employed React Hooks lifecycle methods to dynamically generate course modules.
* Established the back-end server with the Express framework in a Node.js environment to facilitate REST APIs implementation.
* Employed MongoDB as the database and deployed both the client and server on AWS.

## Prerequisites
Before running the application, ensure you have the following installed:
*Node.js
*npm (Node Package Manager)
*MongoDB

## Setup
*Clone the repository: git clone https://github.com/YirenZhangCS/AI-Powered-eCommerceHub.git
*Navigate to the project directory:
*Install dependencies for both the client and server:
Install frontend dependencies
cd frontend
npm install

Install backend dependencies
cd backend
npm install

*Configure environment variables:
Modify the .env.txt file in the backend directory and add the following variables and rename it to .env:
```bash
OPENAI_API_KEY=your_openai_api_key
MONGODB_URI=your_mongodb_uri
```
* Start the application:
npm dev run

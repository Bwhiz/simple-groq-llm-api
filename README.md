# Simple LLM API

This project provides a simple API for generating chat completions using large language models (LLMs) via FastAPI. It integrates with the GROQ service to provide fast and versatile responses.

## Features

- **Health Check Endpoint**: Quickly check if the API is running.
- **Chat Completion Endpoint**: Generate responses from a variety of LLM models with customizable temperature settings.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Bwhiz/simple-groq-llm-api.git
   cd simple-groq-llm-api
   ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
- Create a `.env` file in the project root with your GROQ API key 

    ```bash
    GROQ_API_KEY=your_groq_api_key_here
    ```

## Usage

### Run the API:

    ```bash
    uvicorn app:app --host 127.0.0.1 --port 8080
    ```
### Endpoints
- Health Check: `GET /healthcheck/`
    - Returns a JSON response indicating that the application is up and running.
- Chat Completion: `POST /chat`
    - *Request Body:*
    ```json
    {
  "model": "llama-3.1-70b-versatile",
  "questions": "What is the capital of Abia state in Nigeria?",
  "temperature": 0.1
    }
    ```
    - *Response:*
    ```json
    {
  "status": "success",
  "response": "The capital of Abia state in Nigeria is Umuahia."
    }
    ```
### Available Models
- `llama-3.1-405b-reasoning`
- `llama-3.1-70b-versatile`
- `llama-3.1-8b-instant`
- `mixtral-8x7b-32768`


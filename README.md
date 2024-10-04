
# GPTService

GPTService is a Flask-based application that provides an API to interact with OpenAI's GPT models. It is designed to accept queries via a POST request and return responses from the GPT-3.5-turbo model.

## Features
- Simple API endpoint to send queries to GPT.
- OpenAI API key is configurable through environment variables.
- Dockerized for ease of deployment, with support for Docker Compose.

## Project Structure
```bash
GPTService/
├── app
│   ├── gpt_service.py     # Handles the GPT query logic
│   ├── __init__.py        # Initializes the Flask app and OpenAI client
│   └── routes.py          # Defines the API endpoint for querying GPT
├── Dockerfile             # Dockerfile for containerizing the service
├── docker-compose.yml     # Docker Compose configuration file
├── main.py                # Entry point for running the Flask app
└── README.md              # Project documentation 
└── requirements.txt             # libraries required to run the python app
```

## Installation

### Prerequisites
1. **Python 3.9+**: Ensure you have Python installed.
2. **Docker**: For running the app in a container.
3. **Docker Compose**: To easily manage Docker containers.
4. **OpenAI API Key**: Sign up for OpenAI and obtain an API key.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/GPTService.git
cd GPTService
```

### 2. Set up environment variables
Create a `.env` file in the root directory with the following content:

```
OPENAI_API_KEY=your-openai-api-key
```

### 3. Install dependencies (if running locally)
If you're running the application locally, install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory with the following content:
```
# OPENAI Configuration
OPENAI_API_KEY=smtp.example.com

# Flask Configuration
FLASK_PORT=5501
```

### 5. Run the Flask application
To run the application locally, execute the following command:

```bash
python main.py
```

The application will be accessible at `http://localhost:5500`.

### Running with Docker

If you don't want to use Docker Compose, you can run the application directly using Docker.

#### 1. Build the Docker image
```bash
docker build -t gptservice .
```

#### 2. Run the Docker container
```bash
docker run -d -p 5500:5500 --env-file .env gptservice
```

This will start the application in a Docker container, exposing it on port `5500`.

### Docker Compose Setup

Docker Compose simplifies running the app along with its dependencies.

#### 1. Build and Run with Docker Compose
```bash
docker-compose up --build
```

This will build the Docker image and start the application in a container, exposing it on port `5500`.

#### 2. Stopping the Application
You can stop the application using:
```bash
docker-compose down
```

### 5. Sending a Query
You can send a query to the GPTService API by making a POST request to `/query` with the following payload:

#### Example using `curl`:
```bash
curl -X POST http://localhost:5500/query      -H "Content-Type: application/json"      -d '{"query": "Who is the best soccer player?"}'
```

### 6. API Endpoint

#### POST `/query`
This endpoint accepts a JSON payload containing the `query` field and returns a response from the GPT model.

**Request Payload**:
```json
{
    "query": "Your GPT query here"
}
```

**Response**:
```json
{
    "output": "Response from GPT"
}
```

## License
This project is licensed under the MIT License.

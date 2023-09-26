# Flask News API

This is a simple Flask application that functions as a news API using the NewsAPI service. It allows you to retrieve news articles based on a provided keyword.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerization)

### Installation

Clone the repository to your local machine:


   git clone https://github.com/msmagnanijr/puc-es-task-public-api.git
   cd puc-es-task-public-api


### Install Python dependencies:

    pip install -r requirements.txt

### Usage

Set your NewsAPI key:

Get your NewsAPI key by signing up at NewsAPI and replace 'YOUR_NEWS_API_KEY' in app.py with your actual key:


    NEWS_API_KEY = 'YOUR_NEWS_API_KEY'

### Run the Flask application:

python app.py

The application will start and be accessible at http://localhost:6000.


API Endpoint
GET /get_news

Retrieves news articles based on a provided keyword.

Example Request:
http://localhost:6000/get_news?keyword=technology

Example Response:

{
    "news_titles": [
        "News Title 1",
        "News Title 2",
        "News Title 3"
    ]
}

### Docker (Optional)

If you prefer to run the application in a Docker container, follow these instructions:

Build the Docker image:

docker build -t flask-news-api .


Run the Docker container:

docker run -d -p 6000:6000 flask-news-api

## NEWS_SEARCH_APP


## Flask Web App

Welcome to  Flask web app! This application allows users to  search for the latest new on the web by entering a search query.

## Prerequisites

Before you start, make sure you have the following installed:

- Python (version 3.11.6)
- Flask

## Getting Started

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/Wnjoki/NEWS_APP.git
2. Navigate to the project directory
   
    ```
    cd your-flask-app dir
    
3. Create and activate a virtual environment:
  
   python -m venv venv
    `source venv/bin/activate`     
     # On Windows, use
    `venv\Scripts\activate`

4. Install the required dependencies:

    ```pip install -r requirements.txt```

5. Obtain a News API Key
    To fetch news data, you'll need to obtain a News API key. Follow these steps:
    - Visit [News API](https://newsapi.org/) and sign up for an account.
    - Once registered, obtain your API key from the dashboard. 

6. Configure your API key

    - Open the `app.py` file.
    - Replace `NEWS_API_KEY` with the API key you obtained.

## Running the App

To start the Flask app, run the following commands:

``python app.py``


Visit http://localhost:5000 in your web browser to see your app in action.

from flask import Flask, render_template, request
import requests
import os
from routes import *
from datetime import datetime, timedelta



app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['NEWS_API_KEY'] = os.environ.get('NEWS_API_KEY')

#route for the home page
@app.route('/')
def index():
    return render_template('index.html')

#route for form submissions
@app.route('/search', methods=['POST'])
def search():
    if request.method =="POST":
       query = request.form['query']
       language = request.form['language']
       api_key = app.config['NEWS_API_KEY']
     #Fetch articles from the last month
       today = datetime.now()
       one_month_ago = today - timedelta(days=30)
       from_param = one_month_ago.strftime('%Y-%m-%d')
   
     #perform API call  based on query and language
    url = f'https://newsapi.org/v2/everything?q={query}&language={language}&apiKey={app.config["NEWS_API_KEY"]}&from={from_param}'
    response = requests.get(url)
    data = response.json()
    
    # Extract the relevant information from the API response
    if 'articles' in data:
        articles = data['articles']
        results = []


        for article in articles:
            result = {
                'title': article['title'],
                'url': article['url'],
                'image': article['urlToImage']
            }
            results.append(result)

        return render_template('results.html', results=results)
    else:
        return render_template('error.html', message='No articles found')


if __name__ == '__main__':
    app.run(debug=True)
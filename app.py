from flask import Flask, request, jsonify
import requests 

app = Flask(__name__)

NEWS_API_KEY = '657ddaasb64155x987f54axfesfasa956b278cx4c8f8f04261x'

@app.route('/get_news', methods=['GET'])
def get_news():
    try:
        keyword = request.args.get('keyword') 

        if not keyword:
            raise Exception('Keyword not provided')

       
        response = requests.get(f'https://newsapi.org/v2/everything?q={keyword}&apiKey={NEWS_API_KEY}')

        if response.status_code != 200:
            raise Exception('Failed to fetch news from NewsAPI')

        data = response.json()

        articles = data.get('articles', [])
        news_titles = [article.get('title') for article in articles]

        return jsonify({'news_titles': news_titles})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=6000)



# app.py
from flask import Flask, request, jsonify
from tweettweet import get_tweets_by_name, get_tweets_by_word

app = Flask(__name__)

@app.route('/handle/<name>')
def respond(name):
    return jsonify(get_tweets_by_name(name))

@app.route('/search/<word>')
def search(word):
    return jsonify(get_tweets_by_word(word))

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
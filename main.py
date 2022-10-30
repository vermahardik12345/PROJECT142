from flask import Flask, jsonify, request
import csv
from storage import all_articles, liked_articles, not_liked_articles
from demographic import output
from contentfiltering import get_recommendations

all_articles=[]

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

    

liked_articles = []
not_liked_articles = []

app = Flask(__name__)


@app.route("/get-article")
def get_movie():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })



@app.route("/liked-article", methods=["POST"])
def liked_movie():
    article = all_articles[0]
    all_movies = all_movies[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201


@app.route("/unliked-article", methods=["POST"])
def unliked_movie():
    article = all_articles[0]
    all_movies = all_movies[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201    


if __name__ == "__main__":
  app.run()    



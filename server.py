from flask import Flask, render_template
from post import Post
import requests

articlesUrl = "https://api.npoint.io/3aea0a0f6982c28f366c"
posts = requests.get(articlesUrl).json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["background"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route("/")
def index():
    headers = {
        "title": "Another Random Blog",
        "subtitle": "For random blog articles",

    }
    background = f"static/assets/img/home-bg.jpg"
    return render_template("index.html", articles=post_objects, articleNumber="all", headers=headers, background=background)


@app.route("/post/<int:number>")
def show_post(number):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == number:
            requested_post = blog_post
    background = f"../static/assets/img/{requested_post.background}"
    headers = {
        "title": requested_post.title,
        "subtitle": requested_post.subtitle,
    }

    return render_template("post.html", post=requested_post, headers=headers, background=background)


@app.route("/about")
def about():
    headers = {
        "title": "About Me",
        "subtitle": "This is what I do",

    }
    background = f"static/assets/img/about-us.jpg"
    return render_template("about.html", headers=headers, background=background)


@app.route("/contact")
def contact():
    headers = {
        "title": "Contact me",
        "subtitle": "Have a question? I have answers.",

    }
    background = f"static/assets/img/contact.jpg"
    return render_template("contact.html", headers=headers, background=background)


if __name__ == "__main__":
    app.run(debug=True)

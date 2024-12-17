from flask import Flask, render_template

app = Flask(__name__)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in requested_post:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)

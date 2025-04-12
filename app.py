from flask import Flask, render_template, request, redirect

app = Flask(__name__)

posts = []

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def post():
    title = request.form['title']
    content = request.form['content']
    posts.append({'title': title, 'content': content})
    return redirect('/')

# Važno: pokrećemo aplikaciju sa ispravnim portom za Render
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

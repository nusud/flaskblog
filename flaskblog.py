from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Esteban Buniak',
        'title': 'First Blog Post',
        'content': 'First post content',
        'date_posted': 'July 29, 2024'
    },
    {
        'author': 'Esteban Buniak',
        'title': 'Second Blog Post',
        'content': 'Second post content',
        'date_posted': 'July 30, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/blog/')
def blog_listings():
    return render_template('listings.html')

@app.route('/blog/<slug>/')
def blog_post(slug):
    return render_template('article.html')


app.debug = True
app.run()

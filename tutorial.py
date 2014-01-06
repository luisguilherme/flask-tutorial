from flask import Flask, render_template


app = Flask(__name__)


@app.route('/blog/<slug>/')
def blog_post(slug):
    return render_template('article.html')


@app.route('/blog/', defaults={'page':1})
@app.route('/blog/page/<int:page>')
def blog_page(page):
    return render_template('listings.html', page=page)


app.debug = True
app.run()

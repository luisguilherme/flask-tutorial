from flask import Flask, render_template

app = Flask(__name__)

@app.route('/blog/')
def blog_listings():
    return render_template('listings.html')

app.debug = True
app.run()

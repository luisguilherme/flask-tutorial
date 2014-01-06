Flask top-down
==============

A flask tutorial for professional web developers
------------------------------------------------

If you ever worked at a web company, you know things are done in a
certain order: first, designers create a mock, then developers design
the software that will resemble to that mock.

However, most tutorials of web developing forget that completely, and
put styling on the last. They show you lots of things you won't need,
to only in the end you fill in the gaps.

My issue is show how to make a web application from top down with
flask. The corporate order is like this:

1. Craft the HTML pages (mocks);
2. Devise the URL structure;
3. Architecture a storage, services;
4. Write controllers and views;
4. Wrap everything up.

We will follow roughly that sequence, except that we will be more
top-down, our data storage being the last thing we will do. Under each
section there's a git tag with the tag to this repository that shows
this project after the section is done.

Where to start
--------------
_tag: boilerplate_

The first thing we'll do, is write our HTML pages. And we'll craft
them beautifully. 

So, we'll create two folders on our root structure: templates and
static. 

    $ mkdir flask-topdown
    $ cd flask-topdown
    $ mkdir templates
    $ mkdir static

Inside static we'll unzip Zurb's Foundation. Get to http://getbootstrap.com
and download bootstrap. 

    $ wget http://foundation.zurb.com/cdn/releases/foundation-5.0.2.zip
    $ cd static
    $ unzip ../foundation-5.0.2.zip

We'll create a multi-user blog (not a single-user microblog, because
that is easier and everywhere). So, the first thing we'll do is to
create the listings page. 

First page prototype
---------------------

_tag: first_

So, the first thing we'll write is HTML. Pure HTML, nothing more.

We'll have a header with The blog name, and then a listing of the
articles, with one being promoted.

The HTML goes like this:

````html
<!doctype html>
<html class="no-js">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Blog | Welcome</title>
    <link rel="stylesheet" href="../static/css/foundation.css" />
  </head>
  <body>
    <div class="container">
      <div class="row">
	<div class="small-12 columns">
          <h1>Welcome to my blog</h1>
	</div>
      </div>
      
      <div class="row">
	<div class="small-12 large-8 columns">
	  <h2>Article Major</h2>
	  <p>Lorem ipsum  dolor sit amet, consectetur  adipisicing elit,
	    sed do  eiusmod tempor  incididunt ut  labore et  dolore magna
	    aliqua.  Ut enim  ad minim  veniam, quis  nostrud exercitation
	    ullamco laboris nisi ut aliquip  ex ea commodo consequat. Duis
	    aute  irure dolor  in  reprehenderit in  voluptate velit  esse
	    cillum  dolore  eu  fugiat   nulla  pariatur.  Excepteur  sint
	    occaecat  cupidatat non  proident, sunt  in culpa  qui officia
	    deserunt mollit anim id est laborum.</p>
	  <p><a href="article.html">Read more</a></p>
	</div>

	<div class="small-12 medium-6 large-4 columns">
	  <h2>Article Minor</h2>
	  <p class="hide-for-small-only">Lorem  ipsum dolor  sit amet,
	    consectetur  adipisicing  elit,   sed  do  eiusmod  tempor
	    incididunt ut labore  et dolore magna aliqua.   Ut enim ad
	    minim  veniam, quis  nostrud exercitation  ullamco laboris
	    nisi ut aliquip ex ea commodeo consequat.</p>
	  <p><a href="article.html">Read more</a></p>
	</div>

	<div class="small-12 medium-6 large-4 columns">
	  <h2>Article Minor</h2>
	  <p class="hide-for-small-only">Lorem  ipsum dolor  sit amet,
	    consectetur  adipisicing  elit,   sed  do  eiusmod  tempor
	    incididunt ut labore  et dolore magna aliqua.   Ut enim ad
	    minim  veniam, quis  nostrud exercitation  ullamco laboris
	    nisi ut aliquip ex ea commodeo consequat.</p>
	  <p><a href="article.html">Read more</a></p>
	</div>

	<div class="small-12 medium-6 large-4 columns">
	  <h2>Article Minor</h2>
	  <p class="hide-for-small-only">Lorem  ipsum dolor  sit amet,
	    consectetur  adipisicing  elit,   sed  do  eiusmod  tempor
	    incididunt ut labore  et dolore magna aliqua.   Ut enim ad
	    minim  veniam, quis  nostrud exercitation  ullamco laboris
	    nisi ut aliquip ex ea commodeo consequat.</p>
	  <p><a href="article.html">Read more</a></p>
	</div>

	<div class="small-12 medium-6 large-4 columns">
	  <h2>Article Minor</h2>
	  <p class="hide-for-small-only">Lorem  ipsum dolor  sit amet,
	    consectetur  adipisicing  elit,   sed  do  eiusmod  tempor
	    incididunt ut labore  et dolore magna aliqua.   Ut enim ad
	    minim  veniam, quis  nostrud exercitation  ullamco laboris
	    nisi ut aliquip ex ea commodeo consequat.</p>
	  <p><a href="article.html">Read more</a></p>
	</div>
      </div>
    </div>
  </body>
</html>

````

Save this file in `templates/listings.html` and open this file locally
on your browser. You should see a nicely displayed page.

Presenting Flask
-----------------
_tag: flask0_ 

So, normally we would continue writing HTML files with working static
links, but browsing a filesystem is not the best thing we can do with
the browser. So, we will write our simplest web server.

First, we will set up a python virtual environment. I suggest you
install `virtualenvwrapper` and `pip`. Now write:

    $ mkvirtualenv flask-tutorial
    $ pip install flask

Flask will be installed to you. Now, we'll write our web app. Call it
`tutorial.py` or any other name (except `flask.py`)

````python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/blog/')
def blog_listings():
    return render_template('listings.html')

app.debug = True
app.run()
````

This code defines an app, creates the route, and responds with our
template to the route. Then it starts. 

Now, let's run this

    $ python tutorial.py

If you open http://localhost:5000 you will see a 404 page. That's
expected, since we're not reading the route to it. Now open
http://localhost:5000/blog and WOW! Now this looks beautiful.

Flask automatically serves what's inside a static folder
statically. So it's serving the CSS correctly. But there's a small
issue. Our CSS link can be easily broken if we get to another path. So
we'll make it an absolute link. 

Change the CSS file link to `/static/css/foundation.css`. Open the
page again to test it. If everything is ok, we'll move on. 

Clicking on any Read More link will make us get a 404 page. That's
ok too. But we'll now fix that.

Presenting Jinja2 and variable routing
--------------------------------------
_tag: jinja0_

Jinja2 is a templating language completely backwards compatible what
it templates. So the HTML code we've written is not only HTML, but
also a Jinja2 template. 

Jinja uses `{{` and `}}` to print results of a python computation and
``{%`` and ``%}`` to run a test, or other python code. It's almost as
easy as that: write python code inside the brackets, and have fun. 

We'll write the article template, using a Jinja2 nice function. So,
create ``templates/article.html`` with these contents:

````html
<!doctype html>
<html class="no-js">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Blog | Article</title>
    <link rel="stylesheet" href="/static/css/foundation.css" />
  </head>
  <body>
    <div class="container">
      <div class="row">
	<div class="small-10 small-centered medium-7 large-6 columns">
          <h1>Article</h1>
      
	  {{ lipsum() }}

	  <a href="/blog/">Back to blog</a>
	</div>
      </div>
    </div>
  </body>
</html>
````

If you click on Read More you will still get a 404. That's because we
must get the route to the article. Let's go.

````python
@app.route('/blog/<slug>/')
def blog_post(slug):
    return render_template('article.html')
````

Add this code right below the one that creates the route for the
listings. The code inside ``<>`` is caught by the server as a
variable, and sent to the method as a parameter. We are not using that
yet, but we will soon. 

Let's also make our blog template smaller by changing all paragraphs
for ``{{ lipsum(1) }}``

Notice that we have some repeated code in our templates. So we'll
extract them to a base HTML file

````html
<!doctype html>
<html class="no-js">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Blog {% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="/static/css/foundation.css" />
  </head>
  <body>
    <div class="container">
      {% block contents %}{% endblock %}
    </div>
  </body>
</html>
````

We define blocks inside a base template. This blocks can have content
inside, and this content is overriden if a child template defines that
same block. 

Let's show the new ``article.html`` template now:

````html
{% extends "base.html" %}
{% block title %}| Article{% endblock%}
{% block contents %}
      <div class="row">
	<div class="small-10 small-centered medium-7 large-6 columns">
          <h1>Article</h1>
      
	  {{ lipsum() }}

	  <a href="/blog/">Back to blog</a>
	</div>
      </div>
{% endblock %}
````

You can do the same work to ``listings.html``.

Now we have a fully functional mock, with the listings page and the
article page. However, blogs have more than 5 articles, so let's do
some more pages.

Real work
---------

We wrote no more than two mock HTML templates and about 10 lines of
python code. We have no auto-generated code (except for our front-end
library, foundation), and we already have lots of things. This is, for
me, the beauty of Flask. No boilerplate, no code you don't know where
it came. 

Now we will extract more power from it. 

We want to have paginated listings. They will be different from our
normal views for they won't feature a promoted article. 

First, we will think of our urls. After reading about SEO, I think the
best strategy is to go with ``page/N``

So, we'll redefine our route for blog listings:

````python
@app.route('/blog/', defaults={'page':1})
@app.route('/blog/page/<int:page>')
def blog_page(page):
    return render_template('listings.html', page=page)
````

We added a new route that defines a parameter. The `int:` before the
parameter name makes the router assert it's an integer in order to
accept that route. To make things work with our default listings page,
we set a ``defaults`` map with all the parameters that route doesn't
define. Finally, we pass ``page`` as a parameter to our template.

Now let's show our new template. Lots of things have been changed, and
I will walk you through them:

````html
{% extends "base.html" %}
{% block title %}| Welcome {% endblock %}
{% block contents %}
      <div class="row">
	<div class="small-12 columns">
          <h1>Welcome to my blog</h1>
	</div>
      </div>
      
      <div class="row">
	{% set app = 5 if page == 1 else 6 %}
	{% for n in range(app) %}
	{% if page == 1 and loop.first %}
	<div class="large-8 columns">
	  <h2 class="subheader">Article Major</h2>
	{# </div> #}
	{% else %}
	<div class="medium-6 large-4 columns">
	  <h2 class="subheader">Article Minor</h2>
	{% endif %}
	  {{ lipsum(2 if page == 1 and loop.first else 1) }}
	  <p><a href="{{ url_for('blog_post', slug='article') }}">Read more</a></p>
	</div>
	{% if loop.revindex0 is divisibleby 3 %}
	<div class="clearfix show-for-large-only"></div>
	{% endif %}
	{% if loop.revindex0 is divisibleby 2 %}
	<div class="clearfix show-for-medium-only"></div>
	{% endif %}
	{% endfor %}
      </div>

      <div class="row">
	{% if page > 1 %}
	<a class="button left" href="{{ url_for('blog_page', page=page-1) }}">
	  &laquo; Previous page
	</a>
	{% endif %}
	<a class="button right" href="{{ url_for('blog_page', page=page+1) }}">
	  Next page &raquo; 
	</a>
      </div>
{% endblock %}
````

First things first. And the first new thing we have here is: 

    {% set app = 5 if page == 1 else 6 %}

We are setting a template variable (articles per page, or ``app``) as
5 if ``page`` is 1 and 6 otherwise. ``page`` is the template parameter
we defined in our app. 

    {% for n in range(app) %}

This is a no-brainer if you are a python coder. (You could even add a
``:`` after the ``for`` definition if you wanted). We will repeat
that part of the template ``app'` times. 

    {% if page == 1 and loop.first %}

Jinja defines a special object called ``loop`` with several
information about your loop. ``loop.first`` answers ``True`` if this
is the first iteration. We will display the featured article first if
this is the first page.

     {# </div> #}

This is just for my auto-indenter not become crazy with an unclosed
div. ``{#`` is a template comment and does not get evaluated.

     {{ url_for('blog_post', slug='article') }}

``url_for`` is a Flask method that reverses routes to find an
URL. This will generate a link for our method ``blog_post`` with the
slug parameter set as ``article``. 

     {% if loop.revindex0 is divisibleby 3 %}

I've already talked about ``loop``. ``revindex`` and ``revindex0`` are
methods that return the reverse index (how many iterations to the end)
of our loop, 1 or 0 based respectively. We also have ``index`` and
``index0``, so you will never need to enumerate your loops by hand. 

The Jinja keyword ``is`` represents we are doing a test. And
``divisibleby`` is a Jinja-defined test that tests whether a number is
divisible by other. We are testing this to add clear floats after each
ended column (you should have noticed some design flaws after we
started to use auto-generated text). 

At the end of the file we use these concepts to make two pagination
links, one to the next page, other to the previous (present only when
``page`` is bigger than 1). 

Notice how Jinja is loveable. It "just works". Try something there. If
you know python, it will probably work. ``url_for`` is also a reason
to love Flask. Your links are nothing more than your app method calls
in a different syntax.


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

<code>
$ mkdir flask-topdown
$ cd flask-topdown
$ mkdir templates
$ mkdir static
</code>

Inside static we'll unzip Zurb's Foundation. Get to http://getbootstrap.com
and download bootstrap. 

<code>
$ wget http://foundation.zurb.com/cdn/releases/foundation-5.0.2.zip
$ cd static
$ unzip ../foundation-5.0.2.zip
</code>

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

Save this file in templates/listings.html and open this file locally
on your browser. You should see a nicely displayed page.

Presenting Flask
-----------------

So, normally we would continue writing HTML files
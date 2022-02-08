from flask import Blueprint, render_template


site = Blueprint('site', __name__, template_folder='site_templates')

"""
Note that in the above code some arfs are speced the Blueprint object
The first arg, 'site' is the Blueprint's name,
which is used by Flask's routing mechanism.
The second arg is __name__, is the Blueprint's import name,
which Flask uses to locate the Blueprint's resource
"""

@site.route('/') 
def home():
    return render_template('index.html')

@site.route('/about')
def about():
    return 'The About Page - COMMING SOON!!'

@site.route('/blog')
def blog():
    return 'Here is the future Blog page!'

@site.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number: ' + blog_id
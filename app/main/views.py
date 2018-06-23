from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user

# Views
@main.route('/')
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('index.html', title = title )
   


from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User,Comment
from .forms import PitchForm, CommentForm
from flask.views import View,MethodView
from .. import db


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'
    pickuplines = Pitch.query.filter_by(category="pickuplines")
    interviewpitch = Pitch.query.filter_by(category = "interviewpitch")
    promotionpitch = Pitch.query.filter_by(category = "promotionpitch")
    productpitch = Pitch.query.filter_by(category = "productpitch")
    

    return render_template('home.html', title = title,pickuplines=pickuplines, interviewpitch= interviewpitch, promotionpitch = promotionpitch, productpitch = productpitch)
    



@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        description = form.description.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_pitch = Pitch(owner_id =current_user._get_current_object().id,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        
        
        return redirect(url_for('main.index'))
    return render_template('pitches.html',form=form)

@main.route('/pitches/pitch_categories/')
def categories():
    product = Pitch.query.filter_by(category="product pitch").all()
    promotion = Pitch.query.filter_by(category="promotion pitch").all()
    pickupline = Pitch.query.filter_by(category="pickupline pitch").all()
    interview = Pitch.query.filter_by(category="interview pitch").all()
    return render_template('home.html',pickup=pickupline,interview=interview,product=product,promotion=promotion)


		
   


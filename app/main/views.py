from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..models import *
from .forms import *


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    return render_template('home.html', title = title )



@main.route('/pitches/new/<int:id>', methods = ['GET','POST'])
@login_required

def new_pitch(self, id):
    form = PitchForm
    if form.validate_on_submit():
        description = form.description.data
        owner = current_user._get_current_object()
        category = form.category.data
        
        pitch = Pitch(description=form.description.data, owner=current_user._get_current_object(),category=form.category.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.home'))
    pitches = Pitch.query.order_by(Pitch.all())

    return render_template('pitch.html',form=form, pitches=pitches)


@main.route('/pitches/pitch_categories/')
def categories():
    product = Pitch.query.filter_by(category="product pitch").all()
    promotion = Pitch.query.filter_by(category="promotion pitch").all()
    pickupline = Pitch.query.filter_by(category="pickupline pitch").all()
    interview = Pitch.query.filter_by(category="interview pitch").all()
    return render_template('home.html',pickup=pickupline,interview=interview,product=product,promotion=promotion)
   


from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User,Comment
from .forms import PitchForm, CommentForm
from flask.views import View,MethodView
from .. import db
import markdown2


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'
    pitch = Pitch.query.filter_by().all()
    pickuplines = Pitch.query.filter_by(category="pickuplines")
    interviewpitch = Pitch.query.filter_by(category = "interviewpitch")
    promotionpitch = Pitch.query.filter_by(category = "promotionpitch")
    productpitch = Pitch.query.filter_by(category = "productpitch")
    

    return render_template('home.html', title = title,pitch = pitch,pickuplines=pickuplines, interviewpitch= interviewpitch, promotionpitch = promotionpitch, productpitch = productpitch)
    




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




@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('.new_comment', pitch_id= pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comments.html', form = form,comment = all_comments )


@main.route('/pitch/upvote/<int:id>')
@login_required
def upvote(id):
	pitch = Pitch.query.filter_by(id=id)
	upvotes = pitch.upvotes + 1
	db.session.add(pitch)
	db.session.commit()

	return redirect(url_for('main.index'))

@main.route('/pitch/downvote/<int:id>')
def downvote(id):
	pitch = Pitch.query.filter_by(id=id)
	pitch.downvotes = pitch.downvotes + 1
	db.session.add(pitch)
	db.session.commit()

	return redirect(url_for('main.index'))


		
   


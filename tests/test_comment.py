import unittest
from app.models import Pitch, User, Comment
from flask_login import current_user
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(pitch_content = "This is my pitch", pitch_category='Business',user=self.user_joe)
        self.new_comment = Comment(comment_content = "This is my comment", pitch=self.new_pitch, user=self.user_joe)
    
    def tearDown(self):
        db.session.delete(self)
        User.query.commit()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_content,"This is my comment")
        self.assertEquals(self.new_comment.pitch,self.new_pitch)

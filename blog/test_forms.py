from django.test import TestCase
from .forms import CommentForm
# Create your tests here.
class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        # creates an instance of our CommentForm and fills out the body field of the form with a string - This is a great post:
        comment_form = CommentForm({'body': 'Now the test should pass again'})
        # uses an assert to determine if the form is valid:
        self.assertTrue(comment_form.is_valid())
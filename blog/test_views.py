from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

class TestBlogViews(TestCase):

    def setUp(self):
        # creating superuser and a small blog post
        # self references the current class instance
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        # self.user is the foreign key here, thats why we assigned it to author
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()

        

    def test_render_post_detail_page_with_comment_form(self):
        """Test for rendering post"""
        response = self.client.get(reverse(
            'post_detail', args=['blog-title']))
        # confirms that the view responds successfully, a fundamental check for any web page:
        self.assertEqual(response.status_code, 200)
        # both assertions ensure that the content we defined for self.post in setUp (the blog title and content) will be rendered as part of the response, verifying that our view correctly displays the blog post:
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        # checks that the correct form is being used in the context:
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)
        
    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )
    
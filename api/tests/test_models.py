from django.contrib.auth.models import User
from django.test import TestCase
from api.models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_create_post(self):
        # Create a Post object
        post = Post.objects.create(
            title="Test Post",
            content="This is a test post content.",
            author=self.user,
        )

        # Check if the post was created successfully
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "This is a test post content.")
        self.assertEqual(post.author, self.user)

    def test_post_author_required(self):
        # Attempt to create a Post without an author
        with self.assertRaises(Exception):
            Post.objects.create(
                title="Test Post", content="This is a test post content."
            )

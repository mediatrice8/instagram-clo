from django.test import TestCase

# Create your tests here.

from .models import Image,Profile,Follow,Comment




class CommentTestClass(TestCase):

    def setUp(self):
        
        self.new_comment = Comment(comment= "comment")
        self.new_comment.save()
    
    
    
    def test_instance(self):

        self.assertTrue(isinstance(self.test_comments, Comment))
        
        
    def test_save_method(self):
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)

    def test_save_comment(self):
        self.assertEqual(len(Comment.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Comment.objects.all().delete()

        # Testing delete method

    def test_delete_comment(self):
        self.test_review.delete()
        self.assertEqual(len(Comment.objects.all()), 0)


        
class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):


        self.kigali = Location.objects.create(name="kigali")
        self.media= tags.objects.create(name='media')


        self.test_image = Image.objects.create(image='image',
                                name='cat',
                                caption='This is a caption',
                                location=self.kigali,
                                )

        self.test_image.save()

    def test_save_method(self):
        self.test_image.save()
        test_images = Image.objects.all()
        self.assertTrue(len(test_images) > 0)

    # Testing save method
    def test_save_image(self):
        self.assertEqual(len(Image.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Image.objects.all().delete()

    def test_delete_image(self):
        Image.delete_image_by_id(self.test_image.id)
        self.assertEqual(len(Image.objects.all()), 0)

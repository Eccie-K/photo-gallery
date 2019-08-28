from django.test import TestCase
from .models import Photo,Category
# Create your tests here.

class PhotoTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.Healthy= Photo(description = 'Healthy foods ...', image ='https://www.ocf.berkeley.edu/~sather/wp-content/uploads/2018/01/food--1200x600.jpg')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Healthy,Photo))

     # Testing Save Method
    def test_save_method(self):
        self.Healthy.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > 0)
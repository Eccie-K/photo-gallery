from django.test import TestCase
from .models import Photo,Category,Location
# Create your tests here.

class PhotoTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.Cities= Photo(description = 'Beautiful Cities', image ='https://images.pexels.com/photos/1034662/pexels-photo-1034662.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Cities,Photo))

     # Testing Save Method
    def test_save_method(self):
        self.Cities.save_photo()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > 0)
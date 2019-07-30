from django.test import TestCase
from.models import Image,Profile

# Create your tests here.
class ProfileTestClass(TestCase):
         
    def setUp(self):
        self.faith = Profile(user='faith')

    def test_instance(self):
        self.assertTrue(isinstance(self.faith, Profile))

    def tearDown(self):
        Profile.objects.all().delete()
        
    def test_save(self):
        self.image.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete(self):
        self.faith.save()
        self.faith.delete()
        self.assertTrue(len(Profile.objects.all()) == 0)

    def test_update(self):
        self.faith.save()
        self.faith.username = 'faith'
        self.assertTrue(self.mango.username == 'faith')


class ImageTestClass(TestCase):
         
    def setUp(self):
        self.flower = Image(name='flower')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        Image.objects.all().delete()
        
    def test_save(self):
        self.flower.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete(self):
        self.flower.save()
        self.flower.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update(self):
        self.faith.save()
        self.flower.name = 'city'
        self.assertTrue(self.flower.name == 'city')

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class RootTest(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        
class ModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="user", password="password")
        self.profile = Profile.objects.create(user=self.user, pfp=None, desc=".", cash=100.00)
    
    def test_profile(self):
        self.assertEqual(self.profile.user.username, "user")
        self.assertEqual(self.profile.desc, ".")
        self.assertEqual(self.profile.cash, 100.00)
        
    def test_profile_str(self):
        self.assertEqual(str(self.profile), "@user's profile")
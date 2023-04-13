from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile

# Create your tests here.
class RegistrationTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.home_url = reverse('home')
        self.user_data = {
            'first_name': 'Foo',
            'last_name': 'Bar',
            'username': 'Foobar',
            'email': 'Foobar@example.com',
            'password1': 'password123',
            'password2': 'password123',
        }
    
    def test_profile_created(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='Foobar')
        profile = Profile.objects.get(user=user)
        self.assertIsNotNone(profile)
        
    def test_successful_registration_redirects_to_home_page(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertRedirects(response, self.home_url)


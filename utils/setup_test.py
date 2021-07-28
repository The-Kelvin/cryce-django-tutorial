from django.test import TestCase

from faker import Faker

from authentication.models import User


class TestSetup(TestCase):

    def setUp(self):

        self.faker = Faker()
        self.password = self.faker.paragraph(nb_sentences=5)

        self.user = {
            "username": self.faker.name().split(" ")[0],
            "email": self.faker.email(),
            "password": self.password,
            "password2": self.password
        }


    
    def create_test_user(self):
        user = User.objects.create_user(
            username='username2', email='email2@app.com')
        user.set_password('password12!')
        user.save()

        return user

    
    def create_verified_test_user(self):
        user = User.objects.create_user(
            username='username32', email='email22@app.com', is_email_verified=True)
        user.set_password('password123!')
        user.save()

        return user
    

    def tearDown(self):
        return super().tearDown()
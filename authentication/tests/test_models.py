from utils.setup_test import TestSetup

from authentication.models import User



class TestModels(TestSetup):

    def test_should_create_user(self):
        user = self.creat_test_user()
        self.assertEqual(str(user), user.email)
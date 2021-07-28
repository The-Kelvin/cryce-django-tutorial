from utils.setup_test import TestSetup

from todo.models import Todo
from authentication.models import User



class TestModels(TestSetup):

    def test_should_create_todo(self):

        user = self.create_test_user()

        todo = Todo(owner=user, title="Buy milk", description="Get it done")

        todo.save()

        # Checking the str reprisentation of Todo model
        self.assertEqual(str(todo), todo.title)
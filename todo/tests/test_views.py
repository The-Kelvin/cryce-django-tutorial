from django.urls import reverse
from utils.setup_test import TestSetup

from todo.models import Todo
from authentication.models import User



class TestViews(TestSetup):

    def test_should_create_a_todo(self):

        user = self.create_test_user()

        self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password12!'
        })

        todo = Todo.objects.all()

        self.assertEqual(todo.count(), 0)

        response = self.client.post(reverse('create-todo'), {
            "owner": user,
            "title": "Hello todo from tests",
            "description": "Remember to do this"
        })

        print(response)

        todos = Todo.objects.all()

        self.assertEqual(todos.count(), 1)

        self.assertEqual(response.status_code, 302)

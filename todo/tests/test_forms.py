from django.test import TestCase

from todo.forms import TagCreateForm, TaskCreateForm
from todo.models import Tag


class TagCreateFormTests(TestCase):
    def test_form_valid_with_name(self):
        form = TagCreateForm(data={"name": "work"})
        self.assertTrue(form.is_valid())

    def test_form_invalid_without_name(self):
        form = TagCreateForm(data={"name": ""})
        self.assertFalse(form.is_valid())


class TaskCreateFormTests(TestCase):
    def test_form_valid_with_content(self):
        tag = Tag.objects.create(name="home")
        form = TaskCreateForm(
            data={"content": "Clean house", "done": False, "tags": [tag.id]}
        )
        self.assertTrue(form.is_valid())

    def test_form_invalid_without_content(self):
        form = TaskCreateForm(data={"content": "", "done": False})
        self.assertFalse(form.is_valid())

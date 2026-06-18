from django.test import TestCase

from todo.models import Tag, Task


class TagModelTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="work")
        self.assertEqual(str(tag), "work")


class TaskModelTests(TestCase):
    def test_task_str(self):
        task = Task.objects.create(content="Buy milk")
        self.assertEqual(str(task), "Buy milk")

    def test_task_default_not_done(self):
        task = Task.objects.create(content="Buy milk")
        self.assertFalse(task.done)

    def test_task_tags_relationship(self):
        task = Task.objects.create(content="Clean house")
        tag = Tag.objects.create(name="home")
        task.tags.add(tag)
        self.assertIn(tag, task.tags.all())
        self.assertIn(task, tag.tasks.all())

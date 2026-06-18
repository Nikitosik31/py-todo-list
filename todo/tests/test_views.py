from django.test import TestCase
from django.urls import reverse

from todo.models import Task


class TaskListViewTests(TestCase):
    def test_task_list_status_code(self):
        response = self.client.get(reverse("todo:task-list"))
        self.assertEqual(response.status_code, 200)

    def test_task_list_ordering(self):
        done_task = Task.objects.create(content="Done task", done=True)
        not_done_task = Task.objects.create(content="Not done task")
        response = self.client.get(reverse("todo:task-list"))
        tasks = list(response.context["task_list"])
        self.assertEqual(tasks[0], not_done_task)
        self.assertEqual(tasks[1], done_task)


class TaskToggleViewTests(TestCase):
    def test_toggle_changes_done_status(self):
        task = Task.objects.create(content="Toggle me")
        self.client.post(reverse("todo:task-toggle", args=[task.id]))
        task.refresh_from_db()
        self.assertTrue(task.done)

    def test_toggle_get_not_allowed(self):
        task = Task.objects.create(content="Toggle me")
        response = self.client.get(reverse("todo:task-toggle", args=[task.id]))
        self.assertEqual(response.status_code, 405)

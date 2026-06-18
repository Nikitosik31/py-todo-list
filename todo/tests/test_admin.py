from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from todo.models import Tag, Task


class AdminSiteTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
        )
        self.client.force_login(self.admin_user)
        self.tag = Tag.objects.create(name="work")
        self.task = Task.objects.create(content="Finish report")
        self.task.tags.add(self.tag)

    def test_task_changelist_accessible(self):
        url = reverse("admin:todo_task_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_task_changelist_displays_content(self):
        url = reverse("admin:todo_task_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.task.content)

    def test_task_search_by_tag_name(self):
        url = reverse("admin:todo_task_changelist")
        response = self.client.get(url, {"q": "work"})
        self.assertContains(response, self.task.content)

    def test_tag_changelist_accessible(self):
        url = reverse("admin:todo_tag_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_tag_changelist_displays_name(self):
        url = reverse("admin:todo_tag_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.tag.name)

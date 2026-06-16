from django.views import generic

from todo.models import Task


class TaskListView(generic.ListView):
    model = Task
    ordering = ["-created_at"]
    context_object_name = "task_list"
    paginate_by = 5



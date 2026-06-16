from django import forms

from todo.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "done", "tags")
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
        }


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
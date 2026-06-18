from django.contrib import admin

from todo.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "deadline", "done",)
    search_fields = ("tags__name",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
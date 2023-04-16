from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def delete(self, request, todo, important, *args, **kwargs):
        if not important:
            self.all_todos.remove(todo)
        return redirect('/')

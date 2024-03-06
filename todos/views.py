from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm
from crispy_forms.helper import FormHelper


class TodoListView(ListView):
    model = Todo
    template_name = "todo/todo_list.html"


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.form_tag = False
        return form


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")

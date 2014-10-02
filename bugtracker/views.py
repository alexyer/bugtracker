from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Ticket


class BugListView(ListView):
    model = Ticket
    template_name = "list.html"


class BugDetailView(DetailView):
    model = Ticket
    template_name = "detail.html"

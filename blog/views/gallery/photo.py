# Standard Python Library imports.
from functools import reduce
import operator

# Core Django imports.
from django.contrib import messages
from django.db.models import Q
from django.views.generic import (
    DetailView,
    ListView,
)

from django.shortcuts import render, redirect
from django.views.generic import View



class PhotoView(View):
    # context_object_name = "articles"
    # paginate_by = 12
    template_name = "blog/gallery/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
    def get(self, request):
        return render(request, self.template_name)


from django.shortcuts import render, redirect
from .models import SearchList

from django.views import View
from django.views import generic

# Create your views here.


class search(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'search/search.html'
        search_list = SearchList.objects.all()
        return render(request, template_name, {"search_list": search_list})
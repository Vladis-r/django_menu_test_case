from django.shortcuts import render
from django.views.generic import TemplateView

from menu.models import MenuItem


class MenuView(TemplateView):
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = MenuItem.objects.filter(parent=None)
        return context

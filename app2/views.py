from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .forms import CategoryModelForm
from .models import Category


class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryModelForm
    success_url = reverse_lazy('app2:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryModelForm
    success_url = reverse_lazy('app2:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('app2:category_list')

from django.urls import path
from .views import (
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)

app_name = "app2"
urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('create', CategoryCreateView.as_view(), name='category_create'),
    path('update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
]

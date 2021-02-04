from django.urls import path
from .views import NewsView, NewsCreateView, NewsEditView, NewsDetailView

urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('create/', NewsCreateView.as_view(), name='news_create'),
    path('<int:news_id>/edit/', NewsEditView.as_view(), name='news_edit'),
    path('<int:news_id>/', NewsDetailView.as_view(), name='news_detail'),
]

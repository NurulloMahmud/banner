from django.urls import path
from .views import StatusListCreateView, StatusDetailView


urlpatterns = [
    path('statuses/', StatusListCreateView.as_view(), name='status-list-create'),
    path('statuses/<int:pk>/', StatusDetailView.as_view(), name='status-detail'),
]
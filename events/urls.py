from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventsListView.as_view(), name='events'),
    path('<int:pk>', views.EventDetailView.as_view(), name='event-detail')
]

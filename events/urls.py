from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventsListView.as_view(), name='events'),
    path('new/', views.EventCreateView.as_view(), name='add-event'),
    path('<int:pk>/edit', views.EventEditView.as_view(), name='edit-event'),
    path('<int:pk>/delete', views.EventDeleteView.as_view(), name='delete-event'),
    path('<int:pk>/time/new/', views.EventTimeCreateView.as_view(),
         name='add-event-timings'),
    path('<int:eventid>/time/edit/<int:pk>', views.EventTimeEditView.as_view(),
         name='edit-event-timings'),
    path('<int:eventid>/time/delete/<int:pk>', views.EventTimeDeleteView.as_view(),
         name='delete-event-timings'),
    path('<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
]

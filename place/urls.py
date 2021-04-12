from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlaceListView.as_view(), name='places'),
    path('<int:pk>', views.PlaceDetailView.as_view(), name='place-detail'),
    path('create/', views.AddPlaceView.as_view(), name='add-place'),
    path('<int:pk>/edit', views.EditPlaceView.as_view(), name='edit-place'),
    path('<int:pk>/delete', views.DeletePlaceView.as_view(), name='delete-place')
]

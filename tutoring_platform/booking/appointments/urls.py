from django.urls import path
from .views import AppointmentListView, AppointmentDetailView

urlpatterns = [
    path('appointments/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
]

"""These URLs define endpoints for listing all appointments ('/appointments/')
    and for performing CRUD operations on individual appointments"""
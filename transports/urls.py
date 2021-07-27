from django.urls import path
from . import views
urlpatterns = [
	path('transport/list/', views.TransportListView.as_view(), name='transport_list'),
]
# C:\Users\Mohammed\Documents\ECM\parts\urls.py
from django.urls import path
from . import views

app_name = 'parts' # Namespace for this app's URLs

urlpatterns = [
    path('', views.PartListView.as_view(), name='part_list'),
    path('<int:pk>/', views.PartDetailView.as_view(), name='part_detail'),
]
from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stations/', views.stations_index, name='index'),
    path('stations/create/', views.StationCreate.as_view(), name='stations_create'),
    path('stations/<int:pk>/delete/', views.StationDelete.as_view(), name='stations_delete'),
    path('stations/<int:station_id>/', views.stations_detail, name='detail'),
    path('stations/<int:pk>/update/', views.PriceUpdate.as_view(), name='price_update'),
    path('accounts/signup/', views.signup, name='signup'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('stations/<int:station_id>/add_photo/', views.add_photo, name='add_photo'),
]
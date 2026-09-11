from django.urls import path, include
from .views import (
    CityListCreateView,
    CityListDataView,
    DistrictListCreateView,
    DistrictListDataView,
    CategoryListCreateView,
    CategoryListDataView,
    # AmenityListCreateView,
    # AmenityListDataView,
    ApartmentListCreateView, 
    ApartmentListDataView,
    ApartmentImageListCreateView,
    ApartmentImageListDataView,
    AmenityViewSet,
    login,
    logout,
    register,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'amenity', AmenityViewSet)


urlpatterns = [
    path('city/', CityListCreateView.as_view()),
    path('city/<int:pk>/', CityListDataView.as_view()),
    
    path('district/', DistrictListCreateView.as_view()),
    path('district/<int:pk>/', DistrictListDataView.as_view()),

    path('category/', CategoryListCreateView.as_view()),  
    path('category/<int:pk>/', CategoryListDataView.as_view()), 
    
    # path('amenity/', AmenityListCreateView.as_view()),  
    # path('amenity/<int:pk>/', AmenityListDataView.as_view()),   
    
    path('apartnemt/', ApartmentListCreateView.as_view()),  
    path('apartnemt/<int:pk>/', ApartmentListDataView.as_view()),  
    
    path('apartment_image/', ApartmentImageListCreateView.as_view()),
    path('apartment_image/<int:pk>/', ApartmentImageListDataView.as_view()),
    
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('', include(router.urls))
]


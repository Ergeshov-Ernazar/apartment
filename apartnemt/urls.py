from django.urls import path, include
from .views import (
    CityViewSet,
    DistrictViewSet,
    CategoryViewSet,
    AmenityViewSet,
    ApartmentViewSet,
    ApartmentImageViewSet,
    login,
    logout,
    register,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'city', CityViewSet)
router.register(r'district', DistrictViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'amenity', AmenityViewSet)
router.register(r'apartment', ApartmentViewSet)
router.register(r'apartment_image', ApartmentImageViewSet)

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('', include(router.urls))
]

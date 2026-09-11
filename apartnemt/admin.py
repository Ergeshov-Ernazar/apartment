from django.contrib import admin
from .models import City, District, Category, Amenity, Apartment, ApartmentImage


class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    list_filter = ('city',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'category', 'price', 'deal_type', 'status', 'rooms', 'created_at')
    list_filter = ('status', 'deal_type', 'city', 'category', 'rooms', 'renovation', 'building_type')
    search_fields = ('title', 'address', 'description')
    inlines = [ApartmentImageInline]


@admin.register(ApartmentImage)
class ApartmentImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'apartment')

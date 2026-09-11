from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import City, District, Category, Amenity, Apartment, ApartmentImage
from .serializers import (
    CitySerializer,
    DistrictSerializer,
    CategorySerializer, 
    AmenitySerializer,
    ApartmentSerializer,
    ApartmentImageSerializer, 
    RegisterSerializer,
    LoginSerializer,
)
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets



class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer



class ApartmentPagination(PageNumberPagination):
    page_size = 1

class AmenityPagination(PageNumberPagination):
    page_size = 10

class CategoryPagination(PageNumberPagination):
    page_size = 5

class CityPagination(PageNumberPagination):
    page_size = 5

class DistrictPagination(PageNumberPagination):
    page_size = 10

class ApartmentImagePagination(PageNumberPagination):
    page_size = 20

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(
            {
                'Answer': 'Succesfull',
                'username': user.username
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'messages': "Login successful",
            'token': token.key
        })
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def logout(request):
    if request.user.is_authenticated:
        Token.objects.filter(user=request.user).delete()
        return Response({'message': "logout succesful"})
    return Response({'message': "Не был авторизован"})

class CityListCreateView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = CityPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']

class CityListDataView(RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class DistrictListCreateView(ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    pagination_class = DistrictPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'city']

class DistrictListDataView(RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']    

class CategoryListDataView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class AmenityListCreateView(ListCreateAPIView):
#     queryset = Amenity.objects.all()
#     serializer_class = AmenitySerializer
#     pagination_class = AmenityPagination
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['name']    

# class AmenityListDataView(RetrieveUpdateDestroyAPIView):
#     queryset = Amenity.objects.all()
#     serializer_class = AmenitySerializer

class ApartmentListCreateView(ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    pagination_class = ApartmentPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'category', 'amenities', 'city', 'district', 'price', 'rooms', 
        'square_meters', 'status', 'deal_type', 'renovation', 'building_type'
    ]    
    search_fields = ['title', 'description', 'address']

class ApartmentListDataView(RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class ApartmentImageListCreateView(ListCreateAPIView):
    queryset = ApartmentImage.objects.all()
    serializer_class = ApartmentImageSerializer
    pagination_class = ApartmentImagePagination

class ApartmentImageListDataView(RetrieveUpdateDestroyAPIView):
    queryset = ApartmentImage.objects.all()
    serializer_class = ApartmentImageSerializer

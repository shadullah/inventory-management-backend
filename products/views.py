from rest_framework import viewsets
from rest_framework import filters

from .serializers import ProductSerializer
from .models import products

# Create your views here.
class ProductView(viewsets.ModelViewSet):
    queryset = products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
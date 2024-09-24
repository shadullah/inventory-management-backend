from rest_framework import viewsets
from rest_framework import filters,pagination

from .serializers import ProductSerializer
from .models import products

# Create your views here.


class productPagination(pagination.PageNumberPagination):
    page_size=4 # number of items
    page_size_query_param=page_size
    max_page_size=100


# product viewsets here
class ProductView(viewsets.ModelViewSet):
    queryset = products.objects.all().order_by("id")
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = productPagination
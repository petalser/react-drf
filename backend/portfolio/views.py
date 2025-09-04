from rest_framework import viewsets
from .serializers import PortfolioItemSerializer
from .models import PortfolioItem

class PortfolioItemViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItem.objects.all().order_by("created_at")
    serializer_class = PortfolioItemSerializer
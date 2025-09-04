from rest_framework import viewsets, permissions
from .serializers import PortfolioItemSerializer
from .models import PortfolioItem

class PortfolioItemViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItem.objects.all().order_by("created_at")
    serializer_class = PortfolioItemSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()] 
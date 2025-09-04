from rest_framework import serializers
from .models import PortfolioItem

class PortfolioItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioItem
        fields = "__all__"

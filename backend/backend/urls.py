from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from portfolio.views import PorfolioItemViewSet
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls))
]

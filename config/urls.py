from django.contrib import admin
from django.urls import path,include
from core.views import TransactionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("transaction", TransactionViewSet, basename="Transaction")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls))
]
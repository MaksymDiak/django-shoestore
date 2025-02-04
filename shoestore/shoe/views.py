from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Shoe
from .serializers import ShoeSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    permission_classes = [AllowAny] # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Shoe.objects.prefetch_related("sizes")

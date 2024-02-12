from django.shortcuts import render
from rest_framework import viewsets

from .models import Phone
from .serializers import PhoneSerializer, PhoneListSerializer, PhoneDetailSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.prefetch_related("colors, memories").select_related("images")
    serializer_class = PhoneSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PhoneListSerializer
        if self.action == "retrieve":
            return PhoneDetailSerializer
        return self.serializer_class

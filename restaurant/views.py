from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class MenuView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



def index(request):
    return render(request, 'index.html', {})

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message" : "this view is protected"})


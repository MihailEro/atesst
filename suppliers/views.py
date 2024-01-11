from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from suppliers.models import Participant
from suppliers.serializers import ParticipantSerializer, MyTokenObtainPairSerializer


class ParticipantListAPIView(ListAPIView):
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()
    filter_backends = [SearchFilter, ]
    search_fields = ['contact__country', ]
    permission_classes = [IsAuthenticated]


class ParticipantDetailAPIView(RetrieveAPIView):
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()
    permission_classes = [IsAuthenticated]


class ParticipantCreateAPIView(CreateAPIView):
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]


class ParticipantUpdateAPIView(UpdateAPIView):
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()
    permission_classes = [IsAuthenticated]


class ParticipantDestroyAPIView(DestroyAPIView):
    queryset = Participant.objects.all()
    permission_classes = [IsAuthenticated]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

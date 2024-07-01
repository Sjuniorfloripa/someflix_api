from rest_framework import generics
from actors.models import Actor
from rest_framework.permissions import IsAuthenticated
from actors.serializers import ActorSerializer
from app.permissions import GlobalDefaultPermissions


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

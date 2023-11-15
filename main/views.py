from rest_framework import generics
from .permissions import ReadOnlyOrAdminPermission
from .serializers import StatusSerializer
from .models import Status, Location, LocationImage



class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [ReadOnlyOrAdminPermission]


class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [ReadOnlyOrAdminPermission]
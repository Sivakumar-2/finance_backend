from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Record
from .serializers import RecordSerializer
from .permissions import RecordPermission

class RecordViewSet(ModelViewSet):
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated, RecordPermission]

    def get_queryset(self):
        user = self.request.user

        queryset = Record.objects.all().order_by('-date')

        # Role-based restriction
        if user.role != 'admin':
            queryset = queryset.filter(created_by=user)

        type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        date = self.request.query_params.get('date')

        if type:
            queryset = queryset.filter(type=type)
        if category:
            queryset = queryset.filter(category=category)
        if date:
            queryset = queryset.filter(date=date)

        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
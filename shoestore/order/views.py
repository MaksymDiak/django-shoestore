from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission
from rest_framework.decorators import action
from .models import Order
from .serializers import OrderSerializer


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_staff


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("-created_at")
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        order = serializer.save(user=self.request.user)
        return order

    @action(
        detail=True, methods=["patch"], permission_classes=[permissions.IsAdminUser]
    )
    def update_status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get("status")
        if new_status in dict(OrderStatus.choices):
            order.status = new_status
            order.save()
            return Response({"status": "Status updated"})
        return Response({"error": "Incorrect status"}, status=400)

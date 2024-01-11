from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Plan, App, Subscription
from .serializers import PlanSerializer, AppSerializer, AppListSerializer, SubscriptionSerializer

class PlanListView(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class AppListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return AppListSerializer if self.request.method == 'GET' else AppSerializer

    def get_queryset(self):
        return App.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AppDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class SubscriptionListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        app_id = kwargs.get('app_id')
        subscriptions = Subscription.objects.filter(app_id=app_id, active=True)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response({
            'status': 'success',
            'message': 'Subscription retrived!',
            'payload': serializer.data
        }, status=status.HTTP_200_OK)
    
class SubscriptionView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "GET method not allowed on this endpoint."},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class SubscriptionUpdateOrDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = False
        instance.save()
        return Response({
            "message": "Subscription deleted successfully."
            }, status=status.HTTP_200_OK)


    

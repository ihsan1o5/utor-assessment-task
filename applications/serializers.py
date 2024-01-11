from rest_framework import serializers
from .models import App, Plan, Subscription

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'price', 'validity_days']

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'name', 'description']

class AppListSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'user', 'name', 'description', 'created_at']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'app', 'plan', 'active', 'created_at']

from django.contrib import admin
from .models import Plan, App, Subscription

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'validity_days']
    search_fields = ['name']

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'created_at']
    search_fields = ['name', 'user__username']

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'app', 'plan', 'active', 'created_at']
    search_fields = ['app__name', 'plan__name']

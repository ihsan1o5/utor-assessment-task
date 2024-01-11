from django.urls import path
from .views import PlanListView, AppListView, AppDetailView, SubscriptionListView,\
      SubscriptionView, SubscriptionUpdateOrDeleteView

urlpatterns = [
    path('', AppListView.as_view()),
    path('<int:pk>/', AppDetailView.as_view(), name='update_app'),
    path('plan/', PlanListView.as_view(), name='plan'),
    path('subscribe/<int:app_id>/', SubscriptionListView.as_view(), name='subscribe'),
    path('create-subscription/', SubscriptionView.as_view(), name='create_subscription'),
    path('alter-subscription/<int:pk>/', SubscriptionUpdateOrDeleteView.as_view(), name='alter_subscription')
]
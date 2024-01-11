from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    FREE = 'Free'
    PLAN_CHOICES = {
        "FREE": "Free",
        "STANDARD": "Standard",
        "PRO": "Pro"
    }

    name = models.CharField(max_length=255, choices=PLAN_CHOICES, default=FREE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    validity_days = models.PositiveIntegerField(default=30)

    def __str__(self):
        return self.name

class App(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    app = models.OneToOneField(App, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.plan)

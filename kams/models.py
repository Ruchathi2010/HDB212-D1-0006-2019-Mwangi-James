from django.db import models
from django.contrib.auth.models import AbstractUser


# ---------------------------
# Custom User Model
# ---------------------------
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Marketing', 'Marketing'),
        ('Traffic', 'Traffic'),
        ('Monitoring', 'Monitoring'),
        ('Admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"


# ---------------------------
# Client Model
# ---------------------------
class Client(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    package = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)  # track when added
    updated_at = models.DateTimeField(auto_now=True)      # track changes

    def __str__(self):
        return self.name


# ---------------------------
# Advertisement Model
# ---------------------------
class Ad(models.Model):
    CATEGORY_CHOICES = [
        ('TV', 'TV'),
        ('Radio', 'Radio'),
        ('Online', 'Online'),
        ('Other', 'Other'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="ads")
    title = models.CharField(max_length=100, help_text="Short title for the ad")
    content = models.TextField()
    duration = models.PositiveIntegerField(help_text="Duration in seconds")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.client.name})"


# ---------------------------
# Schedule Model
# ---------------------------
class Schedule(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Played', 'Played'),
        ('Cancelled', 'Cancelled'),
    ]

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="schedules")
    play_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ad.title} - {self.status} at {self.play_time}"


# ---------------------------
# Notification Model
# ---------------------------
class Notification(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="notifications")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification to {self.client.name} ({'Sent' if self.sent else 'Pending'})"


# ---------------------------
# Report Model
# ---------------------------
class Report(models.Model):
    campaign_name = models.CharField(max_length=100)
    metrics = models.JSONField(help_text="Analytics data in JSON format (views, clicks, reach, etc.)")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.campaign_name} - {self.date}"

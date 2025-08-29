# populate_test_data.py
import random
from datetime import datetime, timedelta
from kams.models import User, Client, Ad, Schedule, Notification, Report
from django.utils import timezone

# -----------------------------
# Users
# -----------------------------
users_data = [
    {'username': 'marketing1', 'email': 'marketing1@example.com', 'role': 'Marketing'},
    {'username': 'marketing2', 'email': 'marketing2@example.com', 'role': 'Marketing'},
    {'username': 'traffic1', 'email': 'traffic1@example.com', 'role': 'Traffic'},
    {'username': 'traffic2', 'email': 'traffic2@example.com', 'role': 'Traffic'},
    {'username': 'admin1', 'email': 'admin1@example.com', 'role': 'Admin'},
]

for u in users_data:
    if not User.objects.filter(username=u['username']).exists():
        user = User.objects.create_user(
            username=u['username'],
            email=u['email'],
            password='pass1234',
            role=u['role']
        )
        print(f"Created user: {u['username']}")

# -----------------------------
# Clients
# -----------------------------
clients_data = [
    {'name': 'Client A', 'email': 'clientA@example.com', 'contact': '0712345678', 'package': 'Premium'},
    {'name': 'Client B', 'email': 'clientB@example.com', 'contact': '0723456789', 'package': 'Standard'},
    {'name': 'Client C', 'email': 'clientC@example.com', 'contact': '0734567890', 'package': 'Basic'},
]

clients = []
for c in clients_data:
    client, created = Client.objects.get_or_create(
        name=c['name'], defaults={'email': c['email'], 'contact': c['contact'], 'package': c['package']}
    )
    clients.append(client)
    if created:
        print(f"Created client: {c['name']}")

# -----------------------------
# Ads
# -----------------------------
categories = ['TV', 'Radio', 'Online']
ads = []
for client in clients:
    for i in range(2):  # 2 ads per client
        ad = Ad.objects.create(
            client=client,
            category=random.choice(categories),
            content=f"Ad content {i+1} for {client.name}",
            duration=random.randint(15, 60)
        )
        ads.append(ad)
        print(f"Created ad: {ad.content}")

# -----------------------------
# Schedules
# -----------------------------
statuses = ['Pending', 'Played', 'Cancelled']
for ad in ads:
    for j in range(2):  # 2 schedules per ad
        schedule_time = timezone.now() + timedelta(days=random.randint(0, 10), hours=random.randint(0, 23))
        schedule = Schedule.objects.create(
            ad=ad,
            play_time=schedule_time,
            status=random.choice(statuses)
        )
        print(f"Created schedule for ad: {ad.content} at {schedule_time}")

# -----------------------------
# Notifications
# -----------------------------
for ad in ads:
    notification = Notification.objects.create(
        client=ad.client,
        ad=ad,
        message=f"Notification for {ad.content}",
        timestamp=timezone.now()
    )
    print(f"Created notification for ad: {ad.content}")

# -----------------------------
# Reports
# -----------------------------
for i in range(5):
    report_date = timezone.now() - timedelta(days=random.randint(0, 30))
    report = Report.objects.create(
        campaign_name=f"Campaign {i+1}",
        date=report_date
    )
    print(f"Created report: {report.campaign_name} on {report_date.date()}")

print("✅ Test data population complete!")

from django.contrib import admin
from .models import Client, User, Ad, Schedule, Notification, Report

# Inline for Ads under Client
class AdInline(admin.TabularInline):
    model = Ad
    extra = 0
    can_delete = True
    verbose_name_plural = "Ads"
    # Only safe placeholder
    fields = ['id']  

# Client Admin
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']
    search_fields = ['id']
    inlines = [AdInline]
    list_per_page = 20
    ordering = ['id']

# User Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']
    search_fields = ['id']
    list_per_page = 20
    ordering = ['id']

# Ad Admin
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']
    search_fields = ['id']
    list_per_page = 20
    ordering = ['id']

# Schedule Admin
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']
    search_fields = ['id']
    list_per_page = 20
    ordering = ['id']

# Notification Admin
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']
    search_fields = ['id']
    list_per_page = 20
    ordering = ['id']

# Report Admin
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']
    search_fields = ['id']
    list_per_page = 20
    ordering = ['id']

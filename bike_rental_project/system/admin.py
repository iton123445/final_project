from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import path
from django.urls.base import reverse
from .models import Bike, Booking

class BikeAdmin(admin.ModelAdmin):
    list_display = ('bike_name', 'model', 'type', 'price', 'availability', 'stock')
    list_filter = ('availability', 'type')
    search_fields = ('bike_name', 'model')

admin.site.register(Bike, BikeAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'bike', 'booking_date', 'return_date', 'status')
    list_filter = ('status', 'booking_date', 'return_date')
    search_fields = ('customer__user__username', 'bike__bike_name', 'bike__model')

admin.site.register(Booking, BookingAdmin)


class CustomAdminSite(admin.AdminSite):
    site_header = 'Cycle House Iligan Bike Rental System'
    site_title = 'Cycle House Iligan'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('add_admin_account/', self.admin_view(self.add_admin_account), name='add_admin_account'),
            path('view_admin_accounts/', self.admin_view(self.view_admin_accounts), name='view_admin_accounts'),
        ]
        return custom_urls + urls

    def add_admin_account(self, request):
        return HttpResponseRedirect(reverse('admin:auth_user_add'))

    def view_admin_accounts(self, request):
        return HttpResponseRedirect(reverse('admin:auth_user_changelist'))

# Register the custom admin site
admin_site = CustomAdminSite()
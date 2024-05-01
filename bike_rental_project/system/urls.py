from django.urls import path
from . import views

urlpatterns = [
    path('bikes/', views.bike_list, name='bike_list'),
    path('bike/<int:bike_id>/book/', views.book_bike, name='book_bike'),
    path('invoices/', views.view_invoices, name='view_invoices'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),  
    path('booking_success/', views.booking_success, name='booking_success'),  
    path('my_bookings/', views.view_bookings, name='my_bookings'),    
    path('custom_admin/', views.custom_admin, name='custom_admin'),
    path('update_booking/<int:booking_id>/', views.update_booking, name='update_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('admins/logins/', views.admin_login, name='admin_login'),
    path('add_bike/', views.add_bike, name='add_bike'),
    path('bike/<int:bike_id>/update/', views.update_bike, name='update_bike'),
    path('customadmin/', views.customadmin, name='customadmin'),
    path('view_admin_accounts/', views.view_admin_accounts, name='view_admin_accounts'),
    path('add_to_cart/<int:bike_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),


    


]

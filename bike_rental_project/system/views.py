from django.shortcuts import render, redirect, get_object_or_404
from .models import Bike, Booking, Invoice, Customer, Cart
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from datetime import date
from django.contrib.admin.views.decorators import staff_member_required
from django import forms  
from django.contrib.auth import logout

@login_required
def bike_list(request):
    bikes = Bike.objects.filter(availability=True)
    return render(request, 'bike_list.html', {'bikes': bikes})

@login_required
def book_bike(request, bike_id):
    bike = Bike.objects.get(pk=bike_id)

    if request.method == 'POST':
        booking_date = date.today() # Use today's date for booking_date
        return_date = request.POST.get('return_date')  # Retrieve return_date from form

        # Create a new Booking instance
        booking = Booking.objects.create(
            customer=request.user.customer,
            bike=bike,
            booking_date=booking_date,
            return_date=return_date,
            status='Pending'  # Set initial status to 'Pending'
        )

        # Redirect to a success page or display a success message
        return redirect('booking_success')  # Replace 'booking_success' with your success URL

    return render(request, 'book_bike.html', {'bike': bike})

@login_required
def view_invoices(request):
    invoices = Invoice.objects.filter(booking__customer=request.user.customer)
    return render(request, 'invoices.html', {'invoices': invoices})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user using Django's authenticate() function
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login the user using Django's login() function
            login(request, user)
            return redirect('bike_list')  # Redirect to a protected page after successful login
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        phone = request.POST['phone']
        
        # Create a new User instance
        user = User.objects.create_user(username=username, email=email, password=password, firstname=firstname,lastname=lastname )
        
        # Create a new Customer instance linked to the User instance
        customer = Customer.objects.create(
            user=user,
            firstname=firstname,
            lastname=lastname,
            address=address,
            phone=phone
        )
        
        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'register.html')



def booking_success(request):
    return render(request, 'booking_success.html')  # Render a success page

@login_required
def view_bookings(request):
    # Retrieve bookings associated with the current user
    user_bookings = Booking.objects.filter(customer=request.user.customer)

    return render(request, 'bookings.html', {'bookings': user_bookings})



@staff_member_required
def custom_admin(request):
    bookings = Booking.objects.all()
    return render(request, 'base_site.html', {'bookings': bookings})

@staff_member_required
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        booking.status = new_status
        booking.save()
    return redirect('custom_admin')  # Redirect back to custom admin interface

@staff_member_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        booking.delete()
    return redirect('custom_admin')

@login_required
def profile(request):
    customer = request.user.customer

    class CustomerForm(forms.ModelForm):
        class Meta:
            model = Customer
            fields = ['firstname', 'lastname', 'address', 'phone']

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'profile.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  


def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')

@staff_member_required
def add_bike(request):
    class BikeForm(forms.ModelForm):
        class Meta:
            model = Bike
            fields = ['bike_name', 'model', 'type', 'price', 'availability', 'stock']

    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bike_list')  # Redirect to bike list page after successful addition
    else:
        form = BikeForm()
    
    return render(request, 'add_bike.html', {'form': form})

@staff_member_required
def update_bike(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    
    class BikeForm(forms.ModelForm):
        class Meta:
            model = Bike
            fields = ['bike_name', 'model', 'type', 'price', 'availability', 'stock']

    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)
        if form.is_valid():
            form.save()
            return redirect('bike_list')  # Redirect to bike list page after successful update
    else:
        form = BikeForm(instance=bike)
    
    return render(request, 'update_bike.html', {'form': form, 'bike': bike})

@staff_member_required
def view_admin_accounts(request):
    # Retrieve all user accounts
    users = User.objects.all()
    return render(request, 'view_admin_accounts.html', {'users': users})

def add_to_cart(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)
    
    # Debugging output to check bike and customer associations
    print(f"Bike ID: {bike.id}")
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                customer = request.user.customer
                print(f"Customer ID: {customer.id}")
                
                cart, created = Cart.objects.get_or_create(customer=customer, bike=bike)
                
                # Increment quantity if cart already exists for this bike
                if not created:
                    cart.quantity += 1
                    cart.save()

                return redirect('cart_view')
            except Customer.DoesNotExist:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return redirect('bike_list')

def cart_view(request):
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
            cart, created = Cart.objects.get_or_create(customer=customer)
            print(f"Cart ID: {cart.id}, Quantity: {cart.quantity}, Bike: {cart.bike}")
            return render(request, 'cart_view.html', {'cart': cart})
        except Cart.DoesNotExist:
            return render(request, 'cart_view.html', {'cart': None})
    else:
        return redirect('login')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the admin using Django's authenticate() function
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            # Check if the user is staff (admin)
            login(request, user)
            return redirect('custom_admin')  # Redirect to the admin dashboard
        else:
            # Handle invalid login credentials
            return render(request, 'admin_login.html', {'error_message': 'Invalid username or password'})
    
    return render(request, 'admin_login.html')

def customadmin(request):
    bookings = Booking.objects.all()
    return render(request, 'custom_admin.html', {'bookings': bookings})

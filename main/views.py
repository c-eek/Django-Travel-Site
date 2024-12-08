from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

# views.py
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookings')
    else:
        form = BookingForm()
    return render(request, 'main/book.html', {'form': form})

def bookings(request):
    all_bookings = Booking.objects.all()
    return render(request, 'main/bookings.html', {'bookings': all_bookings})


from django.shortcuts import render, get_object_or_404, redirect
def edit_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings')  # Redirect to the bookings list or another page
    else:
        form = BookingForm(instance=booking)
    return render(request, 'main/edit_booking.html', {'form': form})


from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'


def paris_view(request):
    return render(request, 'main/paris.html')

def maldives_view(request):
    return render(request, 'main/maldives.html')

def bali_view(request):
    return render(request, 'main/bali.html')

def nyc_view(request):
    return render(request, 'main/nyc.html')

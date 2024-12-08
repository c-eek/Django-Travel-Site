from django.urls import path
from . import views
from .views import CustomLogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('book/', views.book, name='book'),
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/edit/<int:pk>/', views.edit_booking, name='edit_booking'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('paris/', views.paris_view, name='paris'),
    path('maldives/', views.maldives_view, name='maldives'),
    path('bali/', views.bali_view, name='bali'),
    path('nyc/', views.nyc_view, name='nyc'),
]



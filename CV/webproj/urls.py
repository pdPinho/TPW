"""webproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('eurocv/<str:name>/', views.eurocv, name='eurocv'),
    
    # book urls
    path('books/', views.books, name='books'),
    path('books/<str:title>/', views.book_info, name='book_info'),
    
    # publisher urls
    path('publishers/', views.publishers, name='publishers'),
    path('publishers/<str:name>/', views.publisher_info, name='publisher_info'),
    path('publishers/<str:name>/authors/', views.publisher_authors, name='publisher_authors'),
    
    # author urls
    path('authors/', views.authors, name='authors'),
    path('authors/<str:name>/', views.author_info, name='author_info'),
    path('authors/<str:name>/books/', views.author_books, name='author_books'),
    
    # Searches
    path('booksearch/', views.booksearch, name='booksearch'),
    path('authorsearch/', views.authorsearch, name='authorsearch'),
    path('apsearch/', views.apsearch, name='apsearch'),
    
    # Queries
    path('bookquery/', views.bookquery, name="bookquery"),
    path('authorquery/', views.authorquery, name="authorquery"),
    
    # Django form inserts
    path('authorinsert/', views.authorinsert, name="authorinsert"),
    path('publisherinsert/', views.publisherinsert, name="publisherinsert"),
    path('bookinsert/', views.bookinsert, name="bookinsert"),
    
    # Simple form inserts
    path('simpleauthorinsert/', views.simpleauthorinsert, name="simpleauthorinsert"),
    
    # Django form edit
    path('authoredit/', views.authoredit, name="authoredit"),
    path('authoredit/<str:id>/', views.authoreditchange, name="authoredit"),
    path('publisheredit/', views.publisheredit, name="authoredit"),
    path('publisheredit/<str:id>/', views.publishereditchange, name="authoredit"),
    path('bookedit/', views.bookedit, name="bookedit"),
    path('bookedit/<str:id>/', views.bookeditchange, name="bookeditchange"),
    
    # login area
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    # inventory area
    path('inventory/', views.inventory, name="inventory")
]

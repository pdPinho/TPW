import os
from django.forms import model_to_dict
from django.shortcuts import redirect, render
from datetime import datetime
import json
from app.forms import BookQueryForm, AuthorQueryForm, AuthorInsertForm, PublisherInsertForm, BookInsertForm, AuthorEditForm, PublisherEditForm, BookEditForm
from app.models import Book, Author, Publisher
from django.http import HttpResponse

def home(request):
    version = request.GET.get('version')
    info = loadJsonInfo(version)
    params = paramSet(info)

    return render(request, 'index.html', params)


def contact(request):
    tparams = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)


def about(request):
    tparams = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)

def eurocv(request, name):
    info = loadJsonInfo(name)
    params = paramSet(info)
    
    return render(request, 'eurocv.html', params)


### DB USAGE ###

#####################
# Book pages
#####################
def books(request):
    if request.method == 'POST':
        bookList = []
        for book in Book.objects.all():
            bookList.append(book.title)
        
        request.session['books'] = bookList
        tparams = {
            'title': 'Congratz',
            'text': 'You have bought them all'
        }
        return render(request, 'books.html', tparams)
    
    tparams = {
        'title': 'Books',
        'books': Book.objects.all(),
    }
    return render(request, 'books.html', tparams)

def book_info(request, title):
    book = Book.objects.get(title=title)

    tparams = {
        'title': book.title,
        'authors': book.authors.all(),
        'publisher': book.publisher,
        'date': book.date,
    }
    return render(request, 'book_info.html', tparams)


#####################
# Author pages
#####################
def authors(request):
    if not request.user.is_authenticated or request.user.username != 'pedro':
        return redirect('/login')
    
    tparams = {
        'title': 'Authors',
        'authors': Author.objects.all(),
    }
    return render(request, 'authors.html', tparams)

def author_info(request, name):
    author = Author.objects.get(name=name)
    tparams = {
        'name': author.name,
        'email': author.email,
    }
    return render(request, 'author_info.html', tparams)

def author_books(request, name):
    author = Author.objects.get(name=name)
    author_books = []
    
    for book in Book.objects.all():
        for eachAuthor in book.authors.all():
            if eachAuthor.name in name:
                author_books.append(book)
    
    tparams = {
        'author': author.name,
        'author_books': author_books,
    }
    return render(request, 'author_books.html', tparams)


#####################
## Publisher pages
#####################
def publishers(request):
    tparams = {
        'title': 'Publishers',
        'publishers': Publisher.objects.all(),
    }
    return render(request, 'publishers.html', tparams)

def publisher_info(request, name):
    publishers = Publisher.objects.get(name=name)
    tparams = {
        'name': publishers.name,
        'city': publishers.city,
        'country': publishers.country,
        'website': publishers.website
    }
    return render(request, 'publisher_info.html', tparams)

def publisher_authors(request, name):
    publisher = Publisher.objects.get(name=name)
    publisher_authors = []
    
    # looks very inefficient 
    for book in Book.objects.all():
        if book.publisher.name == name:
            for author in book.authors.all():
                if author not in publisher_authors:
                    publisher_authors.append(author)
    
    tparams = {
        'publisher': publisher.name,
        'publisher_authors': publisher_authors,
    }
    return render(request, 'publisher_authors.html', tparams)


#####################
## Search pages
#####################

# Book search
def booksearch(request):
    if 'query' in request.POST:
        query = request.POST['query']
        if query:
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'booklist.html', {'books': books, 'query': query})
        else:
            return render(request, 'booksearch.html', {'error': True})
    return render(request, 'booksearch.html', {'error': False})

# Author search
def authorsearch(request):
    if 'query' in request.POST:
        query = request.POST['query']
        if query:
            authors = Author.objects.filter(name__icontains=query)
            return render(request, 'authorlist.html', {'authors': authors, 'query': query})
        else:
            return render(request, 'authorsearch.html', {'error': True})
    return render(request, 'authorsearch.html', {'error': False})

# Books search by Author/Publisher name
def apsearch(request):
    if 'author' in request.POST:
        author = request.POST['author']
        if author:
            author_books = Book.objects.filter(authors__name=author)
    if 'publisher' in request.POST:
        publisher = request.POST['publisher']
        if publisher:
            publisher_books = Book.objects.filter(publisher__name=publisher)
            
    if publisher and author:
        author_publisher_books = author_books & publisher_books
        return render(request, 'apbookslist.html', {'author_publisher_books': author_publisher_books, 'author': author, 'publisher': publisher})
    else:
        if publisher:
            return render(request, 'apbookslist.html', {'publisher_books': publisher_books, 'publisher': publisher})
        elif author:
            return render(request, 'apbookslist.html', {'author_books': author_books, 'author': author})
    
    return render(request, 'apsearch.html', {'error': False})

#####################
## Query pages
#####################

# Book Query
def bookquery(request):
    if request.method == 'POST':
        form = BookQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'booklist.html', {'books': books, 'query': query})
    else:
        form = BookQueryForm()
    return render(request, 'bookquery.html', {'form': form})

# Author Query
def authorquery(request):
    if request.method == 'POST':
        form = AuthorQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            authors = Author.objects.filter(name__icontains=query)
            return render(request, 'authorlist.html', {'authors': authors, 'query': query})
    else:
        form = AuthorQueryForm()
    return render(request, 'authorquery.html', {'form': form})


#####################
## Insert Simple Form pages
#####################
def simpleauthorinsert(request):
    if 'name' in request.POST and 'email' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        if name and email:
            Author(name=name, email=email).save()
            return render(request, 'simpleauthorinsert.html', {'insert': True})
        else:
            return render(request, 'simpleauthorinsert.html', {'error': True})
    return render(request, 'simpleauthorinsert.html', {'insert': False})


#####################
## Insert Django Form pages
#####################
# author insert
def authorinsert(request):
    if request.method == 'POST':
        form = AuthorInsertForm(request.POST)
        if form.is_valid():
            Author(name=form.cleaned_data['name'], 
                   email=form.cleaned_data['email']).save()
            return render(request, 'authorinsert.html', {'form': form, 'insert': True})
    else:
        form = AuthorInsertForm()
    return render(request, 'authorinsert.html', {'form': form, 'insert': False})

# publisher insert
def publisherinsert(request):
    if request.method == 'POST':
        form = PublisherInsertForm(request.POST)
        if form.is_valid():
            Publisher(name=form.cleaned_data['name'],
                      city=form.cleaned_data['city'],
                      country=form.cleaned_data['country'],
                      website=form.cleaned_data['website']).save()
            return render(request, 'publisherinsert.html', {'form': form, 'insert': True})
    else:
        form = PublisherInsertForm()
    return render(request, 'publisherinsert.html', {'form': form, 'insert': False})

# book insert
def bookinsert(request):
    if request.method == 'POST':
        form = BookInsertForm(request.POST)
        if form.is_valid():
            authors = form.cleaned_data['authors']
            book = Book.objects.create(title = form.cleaned_data['title'],
                                       date=form.cleaned_data['date'],
                                       publisher=form.cleaned_data['publisher'])
            for author in authors:
                book.authors.add(author)
                
            book.save()
            return render(request, 'bookinsert.html', {'form': form, 'insert': True})
    else:
        form = BookInsertForm()
    return render(request, 'bookinsert.html', {'form': form, 'insert': False})


#####################
## Edit Django Form pages
#####################
# author edit
def authoredit(request):
    form = AuthorEditForm()
    tparams = {
            'authors': Author.objects.all(),
            'form': form, 
    }
    return render(request, 'authoredit.html', tparams)

def authoreditchange(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        form = AuthorEditForm(request.POST)
        if form.is_valid():
            author.name=form.cleaned_data['name']
            author.email=form.cleaned_data['email']
            author.save()
            return render(request, 'authoreditchange.html', {'form': form})
    else:
        form = AuthorEditForm(initial={'name': author.name,
                                       'email': author.email})
    return render(request, 'authoreditchange.html', {'form': form})


# publisher edit
def publisheredit(request):
    form = PublisherEditForm()
    tparams = {
            'publishers': Publisher.objects.all(),
            'form': form, 
    }
    return render(request, 'publisheredit.html', tparams)

def publishereditchange(request, id):
    publisher = Publisher.objects.get(id=id)
    if request.method == 'POST':
        form = PublisherEditForm(request.POST)
        if form.is_valid():
            publisher.name=form.cleaned_data['name']
            publisher.city=form.cleaned_data['city']
            publisher.country=form.cleaned_data['country']
            publisher.website=form.cleaned_data['website']
            publisher.save()
            return render(request, 'publishereditchange.html', {'form': form})
    else:
        form = PublisherEditForm(initial={'name': publisher.name,
                                       'city': publisher.city,
                                       'country': publisher.country,
                                       'website': publisher.website})
    return render(request, 'publishereditchange.html', {'form': form})

# book edit
def bookedit(request):
    form = BookEditForm()
    tparams = {
            'books': Book.objects.all(),
            'form': form, 
    }
    return render(request, 'bookedit.html', tparams)

def bookeditchange(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookEditForm(request.POST)
        if form.is_valid():
            book.title = form.cleaned_data['title']
            book.date = form.cleaned_data['date']
            book.publisher = form.cleaned_data['publisher']
            for author in form.cleaned_data['authors']:
                book.authors.add(author)
                
            book.save()
            return render(request, 'bookeditchange.html', {'form': form})
    else:
        form = BookEditForm(initial={'title': book.title,
                                     'date': book.date,
                                     'authors': book.authors.all(),
                                     'publisher': book.publisher})
        
    return render(request, 'bookeditchange.html', {'form': form})


#####################
## Inventory
#####################
def inventory(request):
    print(request.session['books'])
    return render(request, 'inventory.html', {'username': request.session._session_key, 
                                              'books': request.session['books']})

"""
Json handling and parameter value set
"""

def loadJsonInfo(name):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    if(name == "fernanda"):
        fileName = "eurocv.json"
    else:
        fileName = "eurocv_2.json"
        
    info = json.load(open(os.path.join(BASE_DIR, 'app/static/content/' + fileName)))
    return info['eurocv']

def paramSet(info):
    #personal information
    personalInfo = info['personalInfo']
    name = personalInfo['name']
    contact = personalInfo['contact']
    address = personalInfo['address']
    birthdate = personalInfo['birthdate']
    
    #work experience
    workExperience = info['workexperience']
    position = workExperience['position']
    activities = position['activities']
    employer = position['employer']
    
    tparams = {
        # personal information
        'photo': info['foto'],
        'surname': name['lastname'],
        'first_name': name['firstname'],
        'street': address['street'],
        'local': address['local'],
        'country': address['country'],
        'phone_prefix': contact['phone']['countryprefix'],
        'phone': contact['phone']['number'],
        'fax': contact['fax']['number'],
        'email': contact['email'][0]['value'],
        'nationality': personalInfo['nacionality'],
        'birthdate': birthdate['day'] + " of " + birthdate['month'] + " " + birthdate['year'],
        'gender': personalInfo['gender'],
        
        # work experience
        'start': position['dates']['start']['month'] + " " + position['dates']['start']['year'],
        'end': position['dates']['end']['month'] + " " + position['dates']['end']['year'],
        'occupation': position['occupation'],
        'activities': activities['activity'],
        'employer_name': employer['name'],
        'employer_street': employer['address']['street'],
        'employer_local': employer['address']['local'],
        'employer_country': employer['address']['country'],
        'business_sector': position['businessSector'],
    }
    
    return tparams
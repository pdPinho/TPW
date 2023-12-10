from django import forms
from app.models import Author, Publisher

## Queries ##
class BookQueryForm(forms.Form):
    query = forms.CharField(label='Search:', max_length=100)
    
class AuthorQueryForm(forms.Form):
    query = forms.CharField(label='Search:', max_length=100)
    
    
## Inserts ##   
class AuthorInsertForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    email = forms.EmailField()
    
class PublisherInsertForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    city = forms.CharField(label='City:', max_length=50)
    country = forms.CharField(label='Country:', max_length=50)
    website = forms.URLField()
    
class BookInsertForm(forms.Form):
    title = forms.CharField(label='Title:', max_length=100)
    date = forms.DateField(label='Date:')
    authors = forms.ModelMultipleChoiceField(Author.objects.all())
    publisher = forms.ModelChoiceField(Publisher.objects.all())
    
## Edits ##
class AuthorEditForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    email = forms.EmailField()
    
class PublisherEditForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=70)
    city = forms.CharField(label='City:', max_length=50)
    country = forms.CharField(label='Country:', max_length=50)
    website = forms.URLField()
    
class BookEditForm(forms.Form):
    title = forms.CharField(label='Title:', max_length=100)
    date = forms.DateField(label='Date:')
    authors = forms.ModelMultipleChoiceField(Author.objects.all())
    publisher = forms.ModelChoiceField(Publisher.objects.all())
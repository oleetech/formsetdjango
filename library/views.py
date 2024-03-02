from django.shortcuts import render, redirect,get_object_or_404
from .forms import AuthorForm, BookFormSet,SearchForm,AuthorDetailsForm
from .models import Author,Book

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        formset = BookFormSet(request.POST, prefix='book')

        if form.is_valid() and formset.is_valid():
            author = form.save()
            formset.instance = author
            formset.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
        formset = BookFormSet(prefix='book')

    context = {
        'form': form,
        'formset': formset,
        
    }
    return render(request, 'library/author_create.html', context)

def author_update(request, author_id=None):
    # If author_id is provided, it's an update operation
    if author_id:
        author = get_object_or_404(Author, id=author_id)
        form = AuthorForm(request.POST or None, instance=author)
        formset = BookFormSet(request.POST or None, instance=author, prefix='book')
    else:
        form = AuthorForm(request.POST or None)
        formset = BookFormSet(request.POST or None, prefix='book')

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            author = form.save()
            formset.instance = author
            formset.save()
            return redirect('author_list')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'library/author_create.html', context)



def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'library/author_list.html', context)



def author_delete(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')

    context = {
        'author': author
    }
    return render(request, 'library/author_delete.html', context)    


def find_author(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            filter_kwargs = {}
            for field_name, field_value in form.cleaned_data.items():
                if field_value:
                    filter_kwargs[f'{field_name}__icontains'] = field_value

            authors = Author.objects.filter(**filter_kwargs)
            if authors.count() == 1:
                # Only one result found, show author_details.html with data of the single author
                author = authors.first()
                books = author.book_set.all()
                context = {
                    'author': author,
                    'books': books,
                }
                return render(request, 'library/author_details.html', context)
            else:
                # Multiple results found, show the list of authors
                context = {'authors': authors}
                return render(request, 'library/search_results.html', context)
    else:
        form = SearchForm()

    return render(request, 'library/search_form.html', {'form': form})




def author_details(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    fields = ['title', 'category', 'remarks']  # Define the fields you want to display dynamically
    books = author.book_set.all()
    context = {
        'author': author,
        'fields': fields,
        'books': books,
    }
    return render(request, 'library/author_details.html', context)

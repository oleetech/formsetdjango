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
        form = AuthorForm(request.POST)
        if form.is_valid():
            filter_kwargs = {}

            name = form.cleaned_data['name']
            if name:
                filter_kwargs['name__icontains'] = name


            # Perform the search using the form input
                author = Author.objects.filter(**filter_kwargs)
                if author.count() == 1:
                    # Only one result found, redirect to the update form
                    author = author.first()
                    form = AuthorForm(instance=author)
                    formset = BookFormSet(instance=author)
                    context = {
                        'form': form,
                        'formset': formset,
                    }
                    return render(request, 'library/author_create.html', context)
                # Pass the search results to the template
                context = {'author': author}
                return render(request, 'library/search_results.html', context)
    else:
        form = SearchForm()

        return render(request, 'library/search_form.html', {'form': form})


def author_details(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    context = {'author': author}
    return render(request, 'library/author_details.html', context)
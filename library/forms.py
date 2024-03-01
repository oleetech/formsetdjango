from django import forms
from django.forms.models import inlineformset_factory
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','age']
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
     
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'border rounded-md  w-full',
                'id': f"defaultForm-{field_name}",
            })   


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'category', 'remarks']




    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # Add class to the category field
        self.fields['category'].widget.attrs.update({
            'class': 'border rounded-md  w-full  specific-class',  # Add your specific class here
            'id': 'category',  # Optionally, you can add an id as well
        })
        # Add classes to other fields as before
        for field_name, field in self.fields.items():
            if field_name != 'category':  # Skip adding class to the category field again
                field.widget.attrs.update({
                    'class': 'border rounded-md  w-full ',
                    'id': f"{field_name}",
                })

BookFormSet = forms.inlineformset_factory(
    Author,
    Book,
    form=BookForm,
    extra=1,
    can_delete=True,
)


class SearchForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'age']  # Update fields as per your requirement

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'border rounded-md  w-full',
                'id': f"defaultForm-{field_name}",
            })
            # Set all fields as not required
            self.fields[field_name].required = False


class AuthorDetailsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True

    class Meta:
        model = Author
        fields = ['name']   

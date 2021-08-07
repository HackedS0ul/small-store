from django import forms
from .models import Book


IN_STORE = (
    ("YES", "Yes"),
    ("NO", "No"),
)
class BookForm(forms.ModelForm):
    isbn_number = forms.CharField(label="Barcode")
    name = forms.CharField(label="Book name")
    description = forms.CharField(label="Short Description", max_length=500)
    author= forms.CharField(label="Author")
    in_store = forms.ChoiceField(label="In store", choices=IN_STORE)
    pub_date = forms.DateField(label="Published on")
    class Meta:
        model: Book
        fields = [
            'name',
            'isbn_number',
            'description',
            'author',
            'in_store',
            'pub_date',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if 'test' in name:
            raise forms.ValidationError(_("Book name is not unique"))
        return name
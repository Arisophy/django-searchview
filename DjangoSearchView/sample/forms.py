"""
Definition of forms.
"""

from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.forms import AuthenticationForm


# Test For SearchView
from searchview.forms import SearchForm

class MusicianSearchForm(SearchForm):
    """Search for Musicians."""

    first_name = forms.CharField(
        label='first_name =',
        required = False,
        max_length=50,
    )
    last_name__istartswith = forms.CharField(
        label="last_name like 'val%'",
        required = False,
        max_length=50,
    )
    instrument__contains = forms.CharField(
        label="instrument like '%val%'",
        required = False,
        max_length=32,
    )
    album_count__gte = forms.IntegerField(
        label='album_count >=',
        required = False,
        initial=1,
        min_value=0,
        max_value=999,
    )
    album_count__lt = forms.IntegerField(
        label='album_count <',
        required = False,
        min_value=0,
        max_value=999,
    )

class AlbumSearchForm(SearchForm):
    """Search for Albums."""

    name__contains = forms.CharField(
        label="name like '%val%'",
        required = False,
        max_length=100,
    )
    release_date__gte = forms.DateField(
        label='release_date >=',
        required = False,
        widget=DateInput(),
    )
    release_date__lte = forms.DateField(
        label='release_date <=',
        required = False,
        widget=DateInput(),
    )
    num_stars__gte = forms.IntegerField(
        label='stars >=',
        required = False,
        min_value=0,
        max_value=5,
    )
    artist__first_name__contains = forms.CharField(
        label="Musician.first_name like '%val%'",
        required = False,
        max_length=50,
    )

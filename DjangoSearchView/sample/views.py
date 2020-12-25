"""
Definition of views.
"""

# Test For SearchView
from django.db.models import Count
from searchview.views import SearchView
from .forms import MusicianSearchForm,AlbumSearchForm
from .models import Musician,Album

class AlbumSearchListView(SearchView):
    template_name = 'app/album.html'
    form_class = AlbumSearchForm
    model = Album
    paginate_by = 5
    first_display_all_list = False
    ordering='-release_date'

class MusicianSearchListView(SearchView):
    template_name = 'app/musician.html'
    form_class = MusicianSearchForm
    model = Musician
    paginate_by = 5
    first_display_all_list = True
    ordering='first_name'

    def get_annotated_queryset(self, queryset, cleaned_data):
        # 'album_count'
        queryset = queryset.annotate(
            album_count=Count('album'))

        return queryset

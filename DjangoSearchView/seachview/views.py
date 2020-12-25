# My library for Django: View 

from django.db.models import QuerySet,Q
from django.http.response import Http404
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import BaseFormView
from django.views.generic.list import BaseListView


class BaseSearchView(BaseListView, BaseFormView):
    """ A base view for displaying a form and a list of objects """

    first_display_all_list = False

    def get(self, request, *args, **kwargs):

        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or None
        if page is None:
            """ First Page """
            form = self.get_form()
            self.cleaned_data = form.get_initial_data()
            if not self.first_display_all_list:
                self.cleaned_data['pk'] = None
            return super().get(request, *args, **kwargs)
        else:
            """ Pagination is not allowed """
            raise Http404('Page param is not allowed for GET method.')

    def post(self, request, *args, **kwargs):
        """ Search Action """
        page_kwarg = self.page_kwarg
        form = self.get_form()
        if form.is_valid():
            if form.has_changed():
                self.kwargs[page_kwarg] = 1
            else:
                page = self.kwargs.get(page_kwarg) or self.request.POST.get(page_kwarg) or 1
                self.kwargs[page_kwarg] = page        
            self.cleaned_data = form.cleaned_data
            return super().get(request, *args, **kwargs)
        else:
            return self.form_invalid(form)

    def get_queryset(self):
        # disable ordering and get base queryset
        ordering = self.ordering
        self.ordering = None
        queryset =  super().get_queryset()
        self.ordering = ordering
        # annotate and filtering
        cleaned_data = self.cleaned_data
        queryset = self.get_annotated_queryset(queryset, cleaned_data)
        form_conditions = self.get_form_conditions(cleaned_data)
        if form_conditions is not None:
            queryset = queryset.filter(form_conditions)
        # ordering 
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    def get_annotated_queryset(self, queryset, cleaned_data):
        """
        Override If you want to add 'annotate'.
        """   
        return queryset

    def get_form_conditions(self, cleaned_data):
        """
        Making filtering conditions from Form.cleaned_data.
        Override If you want to make more complex conditions.
        Keys of cleaned_data are names of Field Objects.
        Keys of cleaned_data are used for "lhs of Field Lookup" in Q.
        """
        conditions = None
        if cleaned_data is not None:
            for key in cleaned_data:
                value = cleaned_data[key]
                if key != 'pk' and value is None:
                    continue
                if isinstance(value, str) and len(value) == 0:
                    continue
                # add condition
                if conditions is None:
                    conditions = Q([key, value])
                else:
                    conditions.add(Q([key, value]), Q.AND)

        return conditions

class SearchView(TemplateResponseMixin, BaseSearchView):
    """
    A view for displaying a form and a list of objects.
    Rendering a template response.
    """
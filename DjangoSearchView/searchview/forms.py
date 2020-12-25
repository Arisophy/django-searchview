from django.forms import Form

class SearchForm(Form):
    """ """
    def get_initial_data(self):
        initial_data = {}
        for name, field in self.fields.items():
            initial = self.get_initial_for_field(field, name)
            try:
                value = field.clean(initial)
                initial_data[name] = value
            except ValidationError as e:
                self.add_error(name, e)
        return initial_data
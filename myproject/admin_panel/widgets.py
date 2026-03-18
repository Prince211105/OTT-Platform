from django.forms import TextInput

class TagAutoCompleteWidget(TextInput):
    template_name = 'admin_panel/widgets/tag_autocomplete.html'
    def __init__(self, attrs=None):
        default_attrs = {'class': 'tag-autocomplete'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

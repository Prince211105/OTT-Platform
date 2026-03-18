from django import forms
from myproject.ott.models import Content, Genre, Tag

class ContentForm(forms.ModelForm):
    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Genres'
    )
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Tags'
    )
    class Meta:
        model = Content
        fields = ['title', 'slug', 'content_type', 'description', 'short_description',
                 'release_year', 'release_date', 'duration_minutes', 'rating', 'language',
                 'country', 'thumbnail', 'poster', 'banner', 'trailer_url',
                 'imdb_rating', 'platform_rating', 'is_featured', 'is_free', 'status',
                 'meta_title', 'meta_description', 'genre', 'tag']

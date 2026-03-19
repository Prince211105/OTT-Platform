from django import forms
from myproject.ott.models import (
    Content, Genre, Tag, Person, Season, Episode, HeroSlider, HeroSliderItem,
    HomeSection, SubscriptionPlan, User, Payment, SupportTicket, Language
)


# ========== Content Forms ==========
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
        fields = [
            'title', 'slug', 'content_type', 'description', 'short_description',
            'release_year', 'release_date', 'duration_minutes', 'rating', 'language',
            'country', 'thumbnail', 'poster', 'banner', 'trailer_url',
            'imdb_rating', 'platform_rating', 'is_featured', 'is_free', 'status',
            'meta_title', 'meta_description', 'genre', 'tag'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'short_description': forms.Textarea(attrs={'rows': 2}),
            'meta_description': forms.Textarea(attrs={'rows': 2}),
        }


# ========== Genre Forms ==========
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'slug', 'description', 'thumbnail', 'banner', 'display_order', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


# ========== Tag Forms ==========
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']


# ========== Person Forms ==========
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'photo', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }


# ========== Season Forms ==========
class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['content', 'season_number', 'title', 'description', 'thumbnail', 'release_year', 'episode_count', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


# ========== Episode Forms ==========
class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = [
            'season', 'content', 'episode_number', 'title', 'description',
            'duration_minutes', 'thumbnail', 'video_url', 'video_360p_url',
            'video_720p_url', 'video_1080p_url', 'video_4k_url', 'subtitle_url',
            'release_date', 'status'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


# ========== HeroSlider Forms ==========
class HeroSliderForm(forms.ModelForm):
    class Meta:
        model = HeroSlider
        fields = ['title', 'placement', 'genre', 'is_active']


# ========== HeroSliderItem Forms ==========
class HeroSliderItemForm(forms.ModelForm):
    class Meta:
        model = HeroSliderItem
        fields = [
            'slider', 'content', 'title', 'subtitle', 'background_image',
            'cta_text', 'cta_url', 'sort_order', 'is_active', 'starts_at', 'ends_at'
        ]
        widgets = {
            'subtitle': forms.Textarea(attrs={'rows': 2}),
        }


# ========== HomeSection Forms ==========
class HomeSectionForm(forms.ModelForm):
    class Meta:
        model = HomeSection
        fields = ['title', 'section_type', 'genre', 'content_limit', 'sort_by', 'display_order', 'is_active']


# ========== SubscriptionPlan Forms ==========
class SubscriptionPlanForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = [
            'name', 'slug', 'description', 'price', 'currency', 'billing_cycle',
            'trial_days', 'max_screens', 'max_quality', 'allow_download', 'is_popular', 'is_active', 'sort_order'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


# ========== User Forms ==========
import uuid

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name', 'email', 'phone', 'avatar', 'status', 'role',
            'email_verified_at', 'remember_token', 'deleted_at'
        ]
        widgets = {
            'uuid': forms.HiddenInput(),
        }
    
    def clean_uuid(self):
        uuid_value = self.cleaned_data.get('uuid')
        if not uuid_value:
            return str(uuid.uuid4())
        return uuid_value
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.uuid:
            instance.uuid = str(uuid.uuid4())
        if commit:
            instance.save()
        return instance


# ========== Payment Forms ==========
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'user', 'subscription', 'plan', 'gateway', 'gateway_order_id',
            'gateway_payment_id', 'amount', 'currency', 'status', 'paid_at', 'metadata'
        ]


# ========== SupportTicket Forms ==========
class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['user', 'name', 'email', 'subject', 'message', 'status']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }


# ========== Language Forms ==========
class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['code', 'name', 'is_active']

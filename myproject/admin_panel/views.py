from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from myproject.ott.models import (
    Content, Genre, Tag, Person, Season, Episode, HeroSlider, HeroSliderItem,
    HomeSection, SubscriptionPlan, User, Payment, SupportTicket, Language
)
from .forms import (
    ContentForm, GenreForm, TagForm, PersonForm, SeasonForm, EpisodeForm,
    HeroSliderForm, HeroSliderItemForm, HomeSectionForm, SubscriptionPlanForm,
    UserForm, PaymentForm, SupportTicketForm, LanguageForm
)


# ========== Content Views ==========
class ContentListView(ListView):
    model = Content
    template_name = 'adminlte/content_list.html'
    context_object_name = 'contents'
    paginate_by = 20
    ordering = ['-created_at']


class ContentCreateView(CreateView):
    model = Content
    form_class = ContentForm
    template_name = 'adminlte/content_form.html'
    success_url = reverse_lazy('admin_panel:content_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class ContentUpdateView(UpdateView):
    model = Content
    form_class = ContentForm
    template_name = 'adminlte/content_form.html'
    success_url = reverse_lazy('admin_panel:content_list')


class ContentDeleteView(DeleteView):
    model = Content
    template_name = 'adminlte/content_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:content_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_name'] = self.object.title
        return context


# ========== Genre Views ==========
class GenreListView(ListView):
    model = Genre
    template_name = 'adminlte/genre_list.html'
    context_object_name = 'genres'
    paginate_by = 20
    ordering = ['display_order', 'name']


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'adminlte/genre_form.html'
    success_url = reverse_lazy('admin_panel:genre_list')


class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'adminlte/genre_form.html'
    success_url = reverse_lazy('admin_panel:genre_list')


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'adminlte/genre_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:genre_list')


# ========== Tag Views ==========
class TagListView(ListView):
    model = Tag
    template_name = 'adminlte/tag_list.html'
    context_object_name = 'tags'
    paginate_by = 20
    ordering = ['name']


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'adminlte/tag_form.html'
    success_url = reverse_lazy('admin_panel:tag_list')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'adminlte/tag_form.html'
    success_url = reverse_lazy('admin_panel:tag_list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'adminlte/tag_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:tag_list')


# ========== Person Views ==========
class PersonListView(ListView):
    model = Person
    template_name = 'adminlte/person_list.html'
    context_object_name = 'people'
    paginate_by = 20
    ordering = ['name']


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'adminlte/person_form.html'
    success_url = reverse_lazy('admin_panel:person_list')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'adminlte/person_form.html'
    success_url = reverse_lazy('admin_panel:person_list')


class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'adminlte/person_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:person_list')


# ========== Season Views ==========
class SeasonListView(ListView):
    model = Season
    template_name = 'adminlte/season_list.html'
    context_object_name = 'seasons'
    paginate_by = 20
    ordering = ['-created_at']


class SeasonCreateView(CreateView):
    model = Season
    form_class = SeasonForm
    template_name = 'adminlte/season_form.html'
    success_url = reverse_lazy('admin_panel:season_list')


class SeasonUpdateView(UpdateView):
    model = Season
    form_class = SeasonForm
    template_name = 'adminlte/season_form.html'
    success_url = reverse_lazy('admin_panel:season_list')


class SeasonDeleteView(DeleteView):
    model = Season
    template_name = 'adminlte/season_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:season_list')


# ========== Episode Views ==========
class EpisodeListView(ListView):
    model = Episode
    template_name = 'adminlte/episode_list.html'
    context_object_name = 'episodes'
    paginate_by = 20
    ordering = ['-created_at']


class EpisodeCreateView(CreateView):
    model = Episode
    form_class = EpisodeForm
    template_name = 'adminlte/episode_form.html'
    success_url = reverse_lazy('admin_panel:episode_list')


class EpisodeUpdateView(UpdateView):
    model = Episode
    form_class = EpisodeForm
    template_name = 'adminlte/episode_form.html'
    success_url = reverse_lazy('admin_panel:episode_list')


class EpisodeDeleteView(DeleteView):
    model = Episode
    template_name = 'adminlte/episode_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:episode_list')


# ========== HeroSlider Views ==========
class HeroSliderListView(ListView):
    model = HeroSlider
    template_name = 'adminlte/hero_slider_list.html'
    context_object_name = 'hero_sliders'
    paginate_by = 20
    ordering = ['title']


class HeroSliderCreateView(CreateView):
    model = HeroSlider
    form_class = HeroSliderForm
    template_name = 'adminlte/hero_slider_form.html'
    success_url = reverse_lazy('admin_panel:hero_slider_list')


class HeroSliderUpdateView(UpdateView):
    model = HeroSlider
    form_class = HeroSliderForm
    template_name = 'adminlte/hero_slider_form.html'
    success_url = reverse_lazy('admin_panel:hero_slider_list')


class HeroSliderDeleteView(DeleteView):
    model = HeroSlider
    template_name = 'adminlte/hero_slider_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:hero_slider_list')


# ========== HeroSliderItem Views ==========
class HeroSliderItemListView(ListView):
    model = HeroSliderItem
    template_name = 'adminlte/hero_slider_item_list.html'
    context_object_name = 'hero_slider_items'
    paginate_by = 20
    ordering = ['sort_order']


class HeroSliderItemCreateView(CreateView):
    model = HeroSliderItem
    form_class = HeroSliderItemForm
    template_name = 'adminlte/hero_slider_item_form.html'
    success_url = reverse_lazy('admin_panel:hero_slider_item_list')


class HeroSliderItemUpdateView(UpdateView):
    model = HeroSliderItem
    form_class = HeroSliderItemForm
    template_name = 'adminlte/hero_slider_item_form.html'
    success_url = reverse_lazy('admin_panel:hero_slider_item_list')


class HeroSliderItemDeleteView(DeleteView):
    model = HeroSliderItem
    template_name = 'adminlte/hero_slider_item_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:hero_slider_item_list')


# ========== HomeSection Views ==========
class HomeSectionListView(ListView):
    model = HomeSection
    template_name = 'adminlte/home_section_list.html'
    context_object_name = 'home_sections'
    paginate_by = 20
    ordering = ['display_order']


class HomeSectionCreateView(CreateView):
    model = HomeSection
    form_class = HomeSectionForm
    template_name = 'adminlte/home_section_form.html'
    success_url = reverse_lazy('admin_panel:home_section_list')


class HomeSectionUpdateView(UpdateView):
    model = HomeSection
    form_class = HomeSectionForm
    template_name = 'adminlte/home_section_form.html'
    success_url = reverse_lazy('admin_panel:home_section_list')


class HomeSectionDeleteView(DeleteView):
    model = HomeSection
    template_name = 'adminlte/home_section_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:home_section_list')


# ========== SubscriptionPlan Views ==========
class SubscriptionPlanListView(ListView):
    model = SubscriptionPlan
    template_name = 'adminlte/subscription_plan_list.html'
    context_object_name = 'subscription_plans'
    paginate_by = 20
    ordering = ['sort_order', 'name']


class SubscriptionPlanCreateView(CreateView):
    model = SubscriptionPlan
    form_class = SubscriptionPlanForm
    template_name = 'adminlte/subscription_plan_form.html'
    success_url = reverse_lazy('admin_panel:subscription_plan_list')


class SubscriptionPlanUpdateView(UpdateView):
    model = SubscriptionPlan
    form_class = SubscriptionPlanForm
    template_name = 'adminlte/subscription_plan_form.html'
    success_url = reverse_lazy('admin_panel:subscription_plan_list')


class SubscriptionPlanDeleteView(DeleteView):
    model = SubscriptionPlan
    template_name = 'adminlte/subscription_plan_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:subscription_plan_list')


# ========== User Views ==========
class UserListView(ListView):
    model = User
    template_name = 'adminlte/user_list.html'
    context_object_name = 'users'
    paginate_by = 20
    ordering = ['-created_at']


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'adminlte/user_form.html'
    success_url = reverse_lazy('admin_panel:user_list')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'adminlte/user_form.html'
    success_url = reverse_lazy('admin_panel:user_list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminlte/user_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:user_list')


# ========== Payment Views ==========
class PaymentListView(ListView):
    model = Payment
    template_name = 'adminlte/payment_list.html'
    context_object_name = 'payments'
    paginate_by = 20
    ordering = ['-created_at']


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'adminlte/payment_form.html'
    success_url = reverse_lazy('admin_panel:payment_list')


class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'adminlte/payment_form.html'
    success_url = reverse_lazy('admin_panel:payment_list')


class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'adminlte/payment_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:payment_list')


# ========== SupportTicket Views ==========
class SupportTicketListView(ListView):
    model = SupportTicket
    template_name = 'adminlte/support_ticket_list.html'
    context_object_name = 'support_tickets'
    paginate_by = 20
    ordering = ['-created_at']


class SupportTicketCreateView(CreateView):
    model = SupportTicket
    form_class = SupportTicketForm
    template_name = 'adminlte/support_ticket_form.html'
    success_url = reverse_lazy('admin_panel:support_ticket_list')


class SupportTicketUpdateView(UpdateView):
    model = SupportTicket
    form_class = SupportTicketForm
    template_name = 'adminlte/support_ticket_form.html'
    success_url = reverse_lazy('admin_panel:support_ticket_list')


class SupportTicketDeleteView(DeleteView):
    model = SupportTicket
    template_name = 'adminlte/support_ticket_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:support_ticket_list')


# ========== Language Views ==========
class LanguageListView(ListView):
    model = Language
    template_name = 'adminlte/language_list.html'
    context_object_name = 'languages'
    paginate_by = 20
    ordering = ['name']


class LanguageCreateView(CreateView):
    model = Language
    form_class = LanguageForm
    template_name = 'adminlte/language_form.html'
    success_url = reverse_lazy('admin_panel:language_list')


class LanguageUpdateView(UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = 'adminlte/language_form.html'
    success_url = reverse_lazy('admin_panel:language_list')


class LanguageDeleteView(DeleteView):
    model = Language
    template_name = 'adminlte/language_confirm_delete.html'
    success_url = reverse_lazy('admin_panel:language_list')

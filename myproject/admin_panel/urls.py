from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    # ========== Content Routes ==========
    path('', views.ContentListView.as_view(), name='content_list'),
    path('contents/', views.ContentListView.as_view(), name='content_list'),
    path('contents/add/', views.ContentCreateView.as_view(), name='content_create'),
    path('contents/<int:pk>/edit/', views.ContentUpdateView.as_view(), name='content_update'),
    path('contents/<int:pk>/delete/', views.ContentDeleteView.as_view(), name='content_delete'),
    
    # ========== Genre Routes ==========
    path('genres/', views.GenreListView.as_view(), name='genre_list'),
    path('genres/add/', views.GenreCreateView.as_view(), name='genre_create'),
    path('genres/<int:pk>/edit/', views.GenreUpdateView.as_view(), name='genre_update'),
    path('genres/<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre_delete'),
    
    # ========== Tag Routes ==========
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tags/add/', views.TagCreateView.as_view(), name='tag_create'),
    path('tags/<int:pk>/edit/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tags/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag_delete'),
    
    # ========== Person Routes ==========
    path('people/', views.PersonListView.as_view(), name='person_list'),
    path('people/add/', views.PersonCreateView.as_view(), name='person_create'),
    path('people/<int:pk>/edit/', views.PersonUpdateView.as_view(), name='person_update'),
    path('people/<int:pk>/delete/', views.PersonDeleteView.as_view(), name='person_delete'),
    
    # ========== Season Routes ==========
    path('seasons/', views.SeasonListView.as_view(), name='season_list'),
    path('seasons/add/', views.SeasonCreateView.as_view(), name='season_create'),
    path('seasons/<int:pk>/edit/', views.SeasonUpdateView.as_view(), name='season_update'),
    path('seasons/<int:pk>/delete/', views.SeasonDeleteView.as_view(), name='season_delete'),
    
    # ========== Episode Routes ==========
    path('episodes/', views.EpisodeListView.as_view(), name='episode_list'),
    path('episodes/add/', views.EpisodeCreateView.as_view(), name='episode_create'),
    path('episodes/<int:pk>/edit/', views.EpisodeUpdateView.as_view(), name='episode_update'),
    path('episodes/<int:pk>/delete/', views.EpisodeDeleteView.as_view(), name='episode_delete'),
    
    # ========== HeroSlider Routes ==========
    path('hero-sliders/', views.HeroSliderListView.as_view(), name='hero_slider_list'),
    path('hero-sliders/add/', views.HeroSliderCreateView.as_view(), name='hero_slider_create'),
    path('hero-sliders/<int:pk>/edit/', views.HeroSliderUpdateView.as_view(), name='hero_slider_update'),
    path('hero-sliders/<int:pk>/delete/', views.HeroSliderDeleteView.as_view(), name='hero_slider_delete'),
    
    # ========== HeroSliderItem Routes ==========
    path('hero-slider-items/', views.HeroSliderItemListView.as_view(), name='hero_slider_item_list'),
    path('hero-slider-items/add/', views.HeroSliderItemCreateView.as_view(), name='hero_slider_item_create'),
    path('hero-slider-items/<int:pk>/edit/', views.HeroSliderItemUpdateView.as_view(), name='hero_slider_item_update'),
    path('hero-slider-items/<int:pk>/delete/', views.HeroSliderItemDeleteView.as_view(), name='hero_slider_item_delete'),
    
    # ========== HomeSection Routes ==========
    path('home-sections/', views.HomeSectionListView.as_view(), name='home_section_list'),
    path('home-sections/add/', views.HomeSectionCreateView.as_view(), name='home_section_create'),
    path('home-sections/<int:pk>/edit/', views.HomeSectionUpdateView.as_view(), name='home_section_update'),
    path('home-sections/<int:pk>/delete/', views.HomeSectionDeleteView.as_view(), name='home_section_delete'),
    
    # ========== SubscriptionPlan Routes ==========
    path('subscription-plans/', views.SubscriptionPlanListView.as_view(), name='subscription_plan_list'),
    path('subscription-plans/add/', views.SubscriptionPlanCreateView.as_view(), name='subscription_plan_create'),
    path('subscription-plans/<int:pk>/edit/', views.SubscriptionPlanUpdateView.as_view(), name='subscription_plan_update'),
    path('subscription-plans/<int:pk>/delete/', views.SubscriptionPlanDeleteView.as_view(), name='subscription_plan_delete'),
    
    # ========== User Routes ==========
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/add/', views.UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/edit/', views.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    
    # ========== Payment Routes ==========
    path('payments/', views.PaymentListView.as_view(), name='payment_list'),
    path('payments/add/', views.PaymentCreateView.as_view(), name='payment_create'),
    path('payments/<int:pk>/edit/', views.PaymentUpdateView.as_view(), name='payment_update'),
    path('payments/<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='payment_delete'),
    
    # ========== SupportTicket Routes ==========
    path('support-tickets/', views.SupportTicketListView.as_view(), name='support_ticket_list'),
    path('support-tickets/add/', views.SupportTicketCreateView.as_view(), name='support_ticket_create'),
    path('support-tickets/<int:pk>/edit/', views.SupportTicketUpdateView.as_view(), name='support_ticket_update'),
    path('support-tickets/<int:pk>/delete/', views.SupportTicketDeleteView.as_view(), name='support_ticket_delete'),
    
    # ========== Language Routes ==========
    path('languages/', views.LanguageListView.as_view(), name='language_list'),
    path('languages/add/', views.LanguageCreateView.as_view(), name='language_create'),
    path('languages/<int:pk>/edit/', views.LanguageUpdateView.as_view(), name='language_update'),
    path('languages/<int:pk>/delete/', views.LanguageDeleteView.as_view(), name='language_delete'),
]

from django.db import models

# ---------- Enum choices ----------
class UserStatus(models.TextChoices):
    ACTIVE = 'active', 'Active'
    SUSPENDED = 'suspended', 'Suspended'
    BANNED = 'banned', 'Banned'

class UserRole(models.TextChoices):
    USER = 'user', 'User'
    ADMIN = 'admin', 'Admin'
    MODERATOR = 'moderator', 'Moderator'

class ContentType(models.TextChoices):
    MOVIE = 'movie', 'Movie'
    SERIES = 'series', 'Series'
    DOCUMENTARY = 'documentary', 'Documentary'
    SHORT = 'short', 'Short'

class ContentRating(models.TextChoices):
    U = 'U', 'U'
    UA = 'U/A', 'U/A'
    A = 'A', 'A'
    S = 'S', 'S'
    TV_G = 'TV-G', 'TV-G'
    TV_PG = 'TV-PG', 'TV-PG'
    TV_14 = 'TV-14', 'TV-14'
    TV_MA = 'TV-MA', 'TV-MA'

class ContentStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published', 'Published'
    ARCHIVED = 'archived', 'Archived'
    COMING_SOON = 'coming_soon', 'Coming Soon'

class SeasonStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published', 'Published'
    ARCHIVED = 'archived', 'Archived'

class EpisodeStatus(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published', 'Published'
    ARCHIVED = 'archived', 'Archived'

class PersonRole(models.TextChoices):
    ACTOR = 'actor', 'Actor'
    DIRECTOR = 'director', 'Director'
    PRODUCER = 'producer', 'Producer'
    WRITER = 'writer', 'Writer'
    HOST = 'host', 'Host'

class BillingCycle(models.TextChoices):
    MONTHLY = 'monthly', 'Monthly'
    QUARTERLY = 'quarterly', 'Quarterly'
    YEARLY = 'yearly', 'Yearly'
    LIFETIME = 'lifetime', 'Lifetime'

class SubscriptionStatus(models.TextChoices):
    TRIAL = 'trial', 'Trial'
    ACTIVE = 'active', 'Active'
    PAUSED = 'paused', 'Paused'
    CANCELLED = 'cancelled', 'Cancelled'
    EXPIRED = 'expired', 'Expired'

class Gateway(models.TextChoices):
    STRIPE = 'stripe', 'Stripe'
    RAZORPAY = 'razorpay', 'Razorpay'
    PAYPAL = 'paypal', 'PayPal'
    MANUAL = 'manual', 'Manual'

class PaymentStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    PAID = 'paid', 'Paid'
    FAILED = 'failed', 'Failed'
    REFUNDED = 'refunded', 'Refunded'

class DeviceType(models.TextChoices):
    WEB = 'web', 'Web'
    MOBILE = 'mobile', 'Mobile'
    TV = 'tv', 'TV'
    TABLET = 'tablet', 'Tablet'

class HeroSliderPlacement(models.TextChoices):
    HOME = 'home', 'Home'
    GENRES = 'genres', 'Genres'
    GENRE_SPECIFIC = 'genre_specific', 'Genre Specific'
    POPULAR = 'popular', 'Popular'
    TV_SHOWS = 'tv_shows', 'TV Shows'
    NEW_RELEASES = 'new_releases', 'New Releases'

class HomeSectionType(models.TextChoices):
    CONTINUE_WATCHING = 'continue_watching', 'Continue Watching'
    MOST_POPULAR = 'most_popular', 'Most Popular'
    TV_SHOWS = 'tv_shows', 'TV Shows'
    BY_GENRE = 'by_genre', 'By Genre'
    TOP_10 = 'top_10', 'Top 10'
    NEW_RELEASES = 'new_releases', 'New Releases'
    TRENDING = 'trending', 'Trending'
    SUGGESTED = 'suggested', 'Suggested'

class TicketStatus(models.TextChoices):
    OPEN = 'open', 'Open'
    IN_PROGRESS = 'in_progress', 'In Progress'
    RESOLVED = 'resolved', 'Resolved'
    CLOSED = 'closed', 'Closed'

# ---------- Model definitions ----------
class User(models.Model):
    uuid = models.CharField(max_length=36, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=191, unique=True)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=UserStatus.choices)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER)
    remember_token = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class Language(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField()

class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.CharField(max_length=255, null=True, blank=True)
    banner = models.CharField(max_length=255, null=True, blank=True)
    display_order = models.SmallIntegerField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Content(models.Model):
    uuid = models.CharField(max_length=36, unique=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=280, unique=True)
    content_type = models.CharField(max_length=20, choices=ContentType.choices)
    description = models.TextField(null=True, blank=True)
    short_description = models.CharField(max_length=500, null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration_minutes = models.SmallIntegerField(null=True, blank=True)
    rating = models.CharField(max_length=10, choices=ContentRating.choices, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.RESTRICT, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    thumbnail = models.CharField(max_length=255, null=True, blank=True)
    poster = models.CharField(max_length=255, null=True, blank=True)
    banner = models.CharField(max_length=255, null=True, blank=True)
    trailer_url = models.CharField(max_length=255, null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    platform_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    view_count = models.BigIntegerField(default=0)
    popularity_score = models.DecimalField(max_digits=10, decimal_places=4, default=0.0)
    is_featured = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=ContentStatus.choices)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class ContentGenre(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    is_primary = models.BooleanField()
    class Meta:
        unique_together = (('content', 'genre'),)

class Season(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    season_number = models.SmallIntegerField()
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.CharField(max_length=255, null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    episode_count = models.SmallIntegerField()
    status = models.CharField(max_length=20, choices=SeasonStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=36, unique=True)
    episode_number = models.SmallIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration_minutes = models.SmallIntegerField()
    thumbnail = models.CharField(max_length=255, null=True, blank=True)
    video_url = models.CharField(max_length=255)
    video_360p_url = models.CharField(max_length=255, null=True, blank=True)
    video_720p_url = models.CharField(max_length=255, null=True, blank=True)
    video_1080p_url = models.CharField(max_length=255, null=True, blank=True)
    video_4k_url = models.CharField(max_length=255, null=True, blank=True)
    subtitle_url = models.CharField(max_length=255, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    view_count = models.BigIntegerField(default=0)
    status = models.CharField(max_length=20, choices=EpisodeStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Person(models.Model):
    name = models.CharField(max_length=150)
    photo = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ContentPerson(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=PersonRole.choices)
    character_name = models.CharField(max_length=150, null=True, blank=True)
    order = models.SmallIntegerField()
    class Meta:
        unique_together = (('content', 'person', 'role'),)

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=5)
    billing_cycle = models.CharField(max_length=20, choices=BillingCycle.choices)
    trial_days = models.SmallIntegerField()
    max_screens = models.SmallIntegerField()
    max_quality = models.CharField(max_length=10)
    allow_download = models.BooleanField()
    is_popular = models.BooleanField()
    is_active = models.BooleanField()
    sort_order = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=SubscriptionStatus.choices)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    trial_ends_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    auto_renew = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(UserSubscription, null=True, blank=True, on_delete=models.SET_NULL)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    gateway = models.CharField(max_length=20, choices=Gateway.choices)
    gateway_order_id = models.CharField(max_length=255, null=True, blank=True)
    gateway_payment_id = models.CharField(max_length=255, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=5)
    status = models.CharField(max_length=20, choices=PaymentStatus.choices)
    paid_at = models.DateTimeField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, null=True, blank=True, on_delete=models.SET_NULL)
    watch_position = models.IntegerField()  # seconds
    duration_seconds = models.IntegerField()
    percent_watched = models.DecimalField(max_digits=5, decimal_places=2)
    is_completed = models.BooleanField()
    device_type = models.CharField(max_length=20, choices=DeviceType.choices, null=True, blank=True)
    last_watched_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ContentRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.CharField(max_length=100, unique=True)

class ContentTag(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('content', 'tag'),)

class HeroSlider(models.Model):
    title = models.CharField(max_length=255)
    placement = models.CharField(max_length=20, choices=HeroSliderPlacement.choices)
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class HeroSliderItem(models.Model):
    slider = models.ForeignKey(HeroSlider, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, null=True, blank=True)
    subtitle = models.CharField(max_length=500, null=True, blank=True)
    background_image = models.CharField(max_length=255)
    cta_text = models.CharField(max_length=100, null=True, blank=True)
    cta_url = models.CharField(max_length=255, null=True, blank=True)
    sort_order = models.SmallIntegerField()
    is_active = models.BooleanField()
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)

class HomeSection(models.Model):
    title = models.CharField(max_length=150)
    section_type = models.CharField(max_length=30, choices=HomeSectionType.choices)
    genre = models.ForeignKey(Genre, null=True, blank=True, on_delete=models.SET_NULL)
    content_limit = models.SmallIntegerField()
    sort_by = models.CharField(max_length=30)
    display_order = models.SmallIntegerField()
    is_active = models.BooleanField()

class SupportTicket(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=191)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=TicketStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

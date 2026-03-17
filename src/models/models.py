"""SQLAlchemy models for the OTT Platform schema.
Generated based on specs/001-mysql-schema-for-ott-platform-users-languages-genres-contents-seasons-episodes-people-subscriptions-payments-watch-history-watchlists-ratings-tags-hero-sliders-home-sections-support-tickets/data-model.md
"""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from enum import Enum as PyEnum

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Enum,
    Float,
    Integer,
    SmallInteger,
    String,
    Text,
    TIMESTAMP,
    Numeric,
    JSON,
    ForeignKey,
    PrimaryKeyConstraint,
    UniqueConstraint,
    Index,
    func,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# ---------- ENUM definitions ----------
class UserStatus(PyEnum):
    active = "active"
    suspended = "suspended"
    banned = "banned"

class UserRole(PyEnum):
    user = "user"
    admin = "admin"
    moderator = "moderator"

class ContentType(PyEnum):
    movie = "movie"
    series = "series"
    documentary = "documentary"
    short = "short"

class ContentRating(PyEnum):
    U = "U"
    UA = "U/A"
    A = "A"
    S = "S"
    TV_G = "TV-G"
    TV_PG = "TV-PG"
    TV_14 = "TV-14"
    TV_MA = "TV-MA"

class ContentStatus(PyEnum):
    draft = "draft"
    published = "published"
    archived = "archived"
    coming_soon = "coming_soon"

class SeasonStatus(PyEnum):
    draft = "draft"
    published = "published"
    archived = "archived"

class EpisodeStatus(PyEnum):
    draft = "draft"
    published = "published"
    archived = "archived"

class PersonRole(PyEnum):
    actor = "actor"
    director = "director"
    producer = "producer"
    writer = "writer"
    host = "host"

class BillingCycle(PyEnum):
    monthly = "monthly"
    quarterly = "quarterly"
    yearly = "yearly"
    lifetime = "lifetime"

class SubscriptionStatus(PyEnum):
    trial = "trial"
    active = "active"
    paused = "paused"
    cancelled = "cancelled"
    expired = "expired"

class Gateway(PyEnum):
    stripe = "stripe"
    razorpay = "razorpay"
    paypal = "paypal"
    manual = "manual"

class PaymentStatus(PyEnum):
    pending = "pending"
    paid = "paid"
    failed = "failed"
    refunded = "refunded"

class DeviceType(PyEnum):
    web = "web"
    mobile = "mobile"
    tv = "tv"
    tablet = "tablet"

class HeroSliderPlacement(PyEnum):
    home = "home"
    genres = "genres"
    genre_specific = "genre_specific"
    popular = "popular"
    tv_shows = "tv_shows"
    new_releases = "new_releases"

class HomeSectionType(PyEnum):
    continue_watching = "continue_watching"
    most_popular = "most_popular"
    tv_shows = "tv_shows"
    by_genre = "by_genre"
    top_10 = "top_10"
    new_releases = "new_releases"
    trending = "trending"
    suggested = "suggested"

class TicketStatus(PyEnum):
    open = "open"
    in_progress = "in_progress"
    resolved = "resolved"
    closed = "closed"

# ---------- Model definitions ----------
class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(191), unique=True, nullable=False)
    email_verified_at = Column(DateTime, nullable=True)
    password = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    avatar = Column(String(255), nullable=True)
    status = Column(Enum(UserStatus), nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.user)
    remember_token = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    subscriptions = relationship("UserSubscription", back_populates="user")
    payments = relationship("Payment", back_populates="user")
    watch_history = relationship("WatchHistory", back_populates="user")
    watchlists = relationship("Watchlist", back_populates="user")
    content_ratings = relationship("ContentRating", back_populates="user")
    support_tickets = relationship("SupportTicket", back_populates="user")

class Language(Base):
    __tablename__ = "languages"
    id = Column(SmallInteger, primary_key=True)
    code = Column(String(5), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    is_active = Column(Boolean, nullable=False)

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(120), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    thumbnail = Column(String(255), nullable=True)
    banner = Column(String(255), nullable=True)
    display_order = Column(SmallInteger, nullable=False)
    is_active = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Content(Base):
    __tablename__ = "contents"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    slug = Column(String(280), unique=True, nullable=False)
    content_type = Column(Enum(ContentType), nullable=False)
    description = Column(Text, nullable=True)
    short_description = Column(String(500), nullable=True)
    release_year = Column(Integer, nullable=True)
    release_date = Column(Date, nullable=True)
    duration_minutes = Column(SmallInteger, nullable=True)
    rating = Column(Enum(ContentRating), nullable=True)
    language_id = Column(SmallInteger, ForeignKey('languages.id'), nullable=True)
    country = Column(String(100), nullable=True)
    thumbnail = Column(String(255), nullable=True)
    poster = Column(String(255), nullable=True)
    banner = Column(String(255), nullable=True)
    trailer_url = Column(String(255), nullable=True)
    imdb_rating = Column(Numeric(3, 1), nullable=True)
    platform_rating = Column(Numeric(3, 1), nullable=True)
    view_count = Column(BigInteger, nullable=False, default=0)
    popularity_score = Column(Numeric(10, 4), nullable=False, default=Decimal('0.0'))
    is_featured = Column(Boolean, nullable=False, default=False)
    is_free = Column(Boolean, nullable=False, default=False)
    status = Column(Enum(ContentStatus), nullable=False)
    meta_title = Column(String(255), nullable=True)
    meta_description = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)
    __table_args__ = (
        Index('ix_content_type_status_popularity', 'content_type', 'status', 'popularity_score'),
    )

    language = relationship("Language")
    genres = relationship("ContentGenre", back_populates="content")
    tags = relationship("ContentTag", back_populates="content")
    seasons = relationship("Season", back_populates="content")
    people = relationship("ContentPerson", back_populates="content")

class ContentGenre(Base):
    __tablename__ = "content_genre"
    content_id = Column(BigInteger, ForeignKey('contents.id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genres.id'), primary_key=True)
    is_primary = Column(Boolean, nullable=False)
    content = relationship("Content", back_populates="genres")
    genre = relationship("Genre")

class Season(Base):
    __tablename__ = "seasons"
    id = Column(Integer, primary_key=True)
    content_id = Column(BigInteger, ForeignKey('contents.id'), nullable=False)
    season_number = Column(SmallInteger, nullable=False)
    title = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    thumbnail = Column(String(255), nullable=True)
    release_year = Column(Integer, nullable=True)
    episode_count = Column(SmallInteger, nullable=False)
    status = Column(Enum(SeasonStatus), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    content = relationship("Content", back_populates="seasons")
    episodes = relationship("Episode", back_populates="season")

class Episode(Base):
    __tablename__ = "episodes"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False)
    season_id = Column(Integer, ForeignKey('seasons.id'), nullable=False)
    content_id = Column(BigInteger, ForeignKey('contents.id'), nullable=False)
    episode_number = Column(SmallInteger, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    duration_minutes = Column(SmallInteger, nullable=False)
    thumbnail = Column(String(255), nullable=True)
    video_url = Column(String(255), nullable=False)
    video_360p_url = Column(String(255), nullable=True)
    video_720p_url = Column(String(255), nullable=True)
    video_1080p_url = Column(String(255), nullable=True)
    video_4k_url = Column(String(255), nullable=True)
    subtitle_url = Column(String(255), nullable=True)
    release_date = Column(Date, nullable=True)
    view_count = Column(BigInteger, nullable=False, default=0)
    status = Column(Enum(EpisodeStatus), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    season = relationship("Season", back_populates="episodes")
    content = relationship("Content")

class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    photo = Column(String(255), nullable=True)
    bio = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    contents = relationship("ContentPerson", back_populates="person")

class ContentPerson(Base):
    __tablename__ = "content_people"
    content_id = Column(BigInteger, ForeignKey('contents.id'), primary_key=True)
    person_id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    role = Column(Enum(PersonRole), nullable=False)
    character_name = Column(String(150), nullable=True)
    order = Column(SmallInteger, nullable=False)

    content = relationship("Content", back_populates="people")
    person = relationship("Person", back_populates="contents")

class SubscriptionPlan(Base):
    __tablename__ = "subscription_plans"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(120), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Numeric(12, 2), nullable=False)
    currency = Column(String(5), nullable=False)
    billing_cycle = Column(Enum(BillingCycle), nullable=False)
    trial_days = Column(SmallInteger, nullable=False)
    max_screens = Column(SmallInteger, nullable=False)
    max_quality = Column(Enum('480p','720p','1080p','4K'), nullable=False)
    allow_download = Column(Boolean, nullable=False)
    is_popular = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)
    sort_order = Column(SmallInteger, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

class UserSubscription(Base):
    __tablename__ = "user_subscriptions"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    plan_id = Column(Integer, ForeignKey('subscription_plans.id'), nullable=False)
    status = Column(Enum(SubscriptionStatus), nullable=False)
    starts_at = Column(DateTime, nullable=False)
    ends_at = Column(DateTime, nullable=False)
    trial_ends_at = Column(DateTime, nullable=True)
    cancelled_at = Column(DateTime, nullable=True)
    auto_renew = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="subscriptions")
    plan = relationship("SubscriptionPlan")

class Payment(Base):
    __tablename__ = "payments"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    subscription_id = Column(BigInteger, ForeignKey('user_subscriptions.id'), nullable=True)
    plan_id = Column(Integer, ForeignKey('subscription_plans.id'), nullable=False)
    gateway = Column(Enum(Gateway), nullable=False)
    gateway_order_id = Column(String(255), nullable=True)
    gateway_payment_id = Column(String(255), nullable=True)
    amount = Column(Numeric(12, 2), nullable=False)
    currency = Column(String(5), nullable=False)
    status = Column(Enum(PaymentStatus), nullable=False)
    paid_at = Column(DateTime, nullable=True)
    metadata = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="payments")
    subscription = relationship("UserSubscription")
    plan = relationship("SubscriptionPlan")

class WatchHistory(Base):
    __tablename__ = "watch_history"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    content_id = Column(BigInteger, ForeignKey('contents.id'), nullable=False)
    episode_id = Column(BigInteger, ForeignKey('episodes.id'), nullable=True)
    watch_position = Column(Integer, nullable=False)  # seconds
    duration_seconds = Column(Integer, nullable=False)
    percent_watched = Column(Numeric(5, 2), nullable=False)
    is_completed = Column(Boolean, nullable=False)
    device_type = Column(Enum(DeviceType), nullable=True)
    last_watched_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="watch_history")
    content = relationship("Content")
    episode = relationship("Episode")

class Watchlist(Base):
    __tablename__ = "watchlists"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    content_id = Column(BigInteger, ForeignKey('contents.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="watchlists")
    content = relationship("Content")

class ContentRating(Base):
    __tablename__ = "content_ratings"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    content_id = Column(BigInteger, ForeignKey('contents.id'), nullable=False)
    rating = Column(SmallInteger, nullable=False)  # 1-5
    review = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="content_ratings")
    content = relationship("Content")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    contents = relationship("ContentTag", back_populates="tag")

class ContentTag(Base):
    __tablename__ = "content_tags"
    content_id = Column(BigInteger, ForeignKey('contents.id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.id'), primary_key=True)

    content = relationship("Content", back_populates="tags")
    tag = relationship("Tag", back_populates="contents")

class HeroSlider(Base):
    __tablename__ = "hero_sliders"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    placement = Column(Enum(HeroSliderPlacement), nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=True)
    is_active = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    genre = relationship("Genre")
    items = relationship("HeroSliderItem", back_populates="slider")

class HeroSliderItem(Base):
    __tablename__ = "hero_slider_items"
    id = Column(Integer, primary_key=True)
    slider_id = Column(Integer, ForeignKey('hero_sliders.id'), nullable=False)
    content_id = Column(BigInteger, ForeignKey('contents.id'), nullable=True)
    title = Column(String(255), nullable=True)
    subtitle = Column(String(500), nullable=True)
    background_image = Column(String(255), nullable=False)
    cta_text = Column(String(100), nullable=True)
    cta_url = Column(String(255), nullable=True)
    sort_order = Column(SmallInteger, nullable=False)
    is_active = Column(Boolean, nullable=False)
    starts_at = Column(DateTime, nullable=True)
    ends_at = Column(DateTime, nullable=True)

    slider = relationship("HeroSlider", back_populates="items")
    content = relationship("Content")

class HomeSection(Base):
    __tablename__ = "home_sections"
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    section_type = Column(Enum(HomeSectionType), nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=True)
    content_limit = Column(SmallInteger, nullable=False)
    sort_by = Column(Enum('popularity','release_date','view_count','rating','manual'), nullable=False)
    display_order = Column(SmallInteger, nullable=False)
    is_active = Column(Boolean, nullable=False)

    genre = relationship("Genre")

class SupportTicket(Base):
    __tablename__ = "support_tickets"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=True)
    name = Column(String(150), nullable=False)
    email = Column(String(191), nullable=False)
    subject = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    status = Column(Enum(TicketStatus), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="support_tickets")

"""Populate dummy data for OTT Platform.
Creates 10 realistic rows per table (except contents) using SQLAlchemy ORM.
"""

import random
from datetime import datetime, timedelta

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decimal import Decimal
from decimal import Decimal

from src.models.models import Base, User, Language, Genre, SubscriptionPlan, UserSubscription, Payment, WatchHistory, Watchlist, ContentRating, HeroSlider, HeroSliderItem, HomeSection, SupportTicket

# Adjust the connection URL as needed
engine = create_engine('mysql+pymysql://root:@localhost:3306/ott_platform')
Session = sessionmaker(bind=engine)
session = Session()

def random_timestamp():
    return datetime.utcnow() - timedelta(days=random.randint(0, 365))

def create_users():
    for i in range(10):
        user = User(
            uuid=f"{i}-{random.randint(1000,9999)}",
            name=f"User {i}",
            email=f"user{i}@example.com",
            email_verified_at=random_timestamp(),
            password='hashed',
            phone='1234567890',
            avatar=None,
            status='active',
            role='user',
            remember_token=None,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        session.add(user)
    session.commit()

def create_languages():
    langs = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('hi', 'Hindi')
    ]
    for code, name in langs:
        language = Language(code=code, name=name, is_active=True)
        session.add(language)
    session.commit()

def create_genres():
    for i in range(10):
        genre = Genre(
            name=f"Genre {i}",
            slug=f"genre-{i}",
            description=f"Description for genre {i}",
            is_active=True,
            display_order=i,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        session.add(genre)
    session.commit()

def create_subscription_plans():
    for i in range(3):
        plan = SubscriptionPlan(
            name=f"Plan {i}",
            slug=f"plan-{i}",
            price=Decimal('9.99') * (i+1),
            currency='USD',
            billing_cycle='monthly',
            trial_days=14,
            max_screens=2,
            max_quality='1080p',
            allow_download=True,
            is_popular=bool(i%2),
            is_active=True,
            sort_order=i,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        session.add(plan)
    session.commit()

def main():
    Base.metadata.create_all(engine)
    create_users()
    create_languages()
    create_genres()
    create_subscription_plans()
    print('Dummy data inserted.')

if __name__ == '__main__':
    main()

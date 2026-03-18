# Data Model

## Entities

- **Content**
  - Fields: id (PK), uuid, title, description, rating, status, thumbnail, poster, banner, is_featured, created_at, updated_at
  - Relationships: many‑to‑many **Genre**, many‑to‑many **Tag**, many‑to‑many **Person** (as cast/crew), one‑to‑many **Season** (if series)

- **Season**
  - Fields: id (PK), season_number, title, release_year, content_id (FK)
  - Relationships: one‑to‑many **Episode**

- **Episode**
  - Fields: id (PK), episode_number, title, description, video_file, duration_minutes, thumbnail, release_date, content_id (FK), season_id (FK)

- **Genre**
  - Fields: id (PK), name, display_order, banner_image

- **HeroSlider**
  - Fields: id (PK), content_id (FK), order, start_date, end_date, image

- **HomeLayoutSection**
  - Fields: id (PK), section_type, content_limit, order, configuration_json

- **Person**
  - Fields: id (PK), name, role, photo

- **SubscriptionPlan**
  - Fields: id (PK), name, price, billing_cycle, max_quality, max_screens, features_json

- **User**
  - Fields: id (PK), name, email, role, subscription_id (FK), is_active, created_at

- **PaymentLog**
  - Fields: id (PK), user_id (FK), amount, currency, status, transaction_date

- **Tag**
  - Fields: id (PK), name

- **SupportTicket**
  - Fields: id (PK), user_id (FK), subject, message, status, priority, created_at, updated_at

- **AnalyticsReport**
  - Fields: id (PK), date_range_start, date_range_end, view_count, revenue_total, top_content_json

## Relationships Overview

- Content ↔ Genre: many‑to‑many
- Content ↔ Tag: many‑to‑many
- Content ↔ Person (cast/crew): many‑to‑many with role attribute
- Content ↔ Season: one‑to‑many (only for series)
- Season ↔ Episode: one‑to‑many
- Content ↔ HeroSlider: one‑to‑many (multiple slides can reference same content)
- SubscriptionPlan ↔ User: one‑to‑many
- User ↔ PaymentLog: one‑to‑many
- User ↔ SupportTicket: one‑to‑many

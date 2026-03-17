# Data Model

## Entities and Fields

### users
- **id**: BIGINT UNSIGNED, PK, auto‑increment
- **uuid**: VARCHAR(36), UQ, public‑facing identifier
- **name**: VARCHAR(100), not null
- **email**: VARCHAR(191), UQ, not null
- **email_verified_at**: TIMESTAMP, nullable
- **password**: VARCHAR(255), not null (bcrypt hash)
- **phone**: VARCHAR(20), nullable
- **avatar**: VARCHAR(255), nullable (S3 key)
- **status**: ENUM('active','suspended','banned'), not null
- **role**: ENUM('user','admin','moderator'), not null, default 'user'
- **remember_token**: VARCHAR(100), nullable
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP
- **updated_at**: TIMESTAMP, default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
- **deleted_at**: TIMESTAMP, nullable (soft delete)

### languages
- **id**: TINYINT UNSIGNED, PK
- **code**: VARCHAR(5), UQ, not null (ISO 639‑1)
- **name**: VARCHAR(50), not null
- **is_active**: BOOLEAN, not null

### genres
- **id**: INT UNSIGNED, PK
- **name**: VARCHAR(100), not null
- **slug**: VARCHAR(120), UQ, not null
- **description**: TEXT, nullable
- **thumbnail**: VARCHAR(255), nullable
- **banner**: VARCHAR(255), nullable
- **display_order**: SMALLINT, not null
- **is_active**: BOOLEAN, not null
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP
- **updated_at**: TIMESTAMP, default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP

### contents
- **id**: BIGINT UNSIGNED, PK
- **uuid**: VARCHAR(36), UQ, not null
- **title**: VARCHAR(255), not null
- **slug**: VARCHAR(280), UQ, not null
- **content_type**: ENUM('movie','series','documentary','short'), not null
- **description**: TEXT, nullable
- **short_description**: VARCHAR(500), nullable
- **release_year**: YEAR, nullable
- **release_date**: DATE, nullable
- **duration_minutes**: SMALLINT UNSIGNED, nullable
- **rating**: ENUM('U','U/A','A','S','TV-G','TV-PG','TV-14','TV-MA'), nullable
- **language_id**: TINYINT UNSIGNED, FK → languages.id, nullable
- **country**: VARCHAR(100), nullable
- **thumbnail**: VARCHAR(255), nullable
- **poster**: VARCHAR(255), nullable
- **banner**: VARCHAR(255), nullable
- **trailer_url**: VARCHAR(255), nullable
- **imdb_rating**: DECIMAL(3,1), nullable
- **platform_rating**: DECIMAL(3,1), nullable
- **view_count**: BIGINT UNSIGNED, not null, default 0
- **popularity_score**: DECIMAL(10,4), not null, default 0.0
- **is_featured**: BOOLEAN, not null, default FALSE
- **is_free**: BOOLEAN, not null, default FALSE
- **status**: ENUM('draft','published','archived','coming_soon'), not null
- **meta_title**: VARCHAR(255), nullable
- **meta_description**: VARCHAR(500), nullable
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP
- **updated_at**: TIMESTAMP, default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP
- **deleted_at**: TIMESTAMP, nullable

### content_genre (pivot)
- **content_id**: BIGINT UNSIGNED, FK → contents.id
- **genre_id**: INT UNSIGNED, FK → genres.id
- **is_primary**: BOOLEAN, not null
- **PK**: (content_id, genre_id)

### seasons
- **id**: INT UNSIGNED, PK
- **content_id**: BIGINT UNSIGNED, FK → contents.id
- **season_number**: TINYINT UNSIGNED, not null
- **title**: VARCHAR(255), nullable
- **description**: TEXT, nullable
- **thumbnail**: VARCHAR(255), nullable
- **release_year**: YEAR, nullable
- **episode_count**: TINYINT UNSIGNED, not null
- **status**: ENUM('draft','published','archived'), not null
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP
- **updated_at**: TIMESTAMP, default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP

### episodes
- **id**: BIGINT UNSIGNED, PK
- **uuid**: VARCHAR(36), UQ, not null
- **season_id**: INT UNSIGNED, FK → seasons.id
- **content_id**: BIGINT UNSIGNED, FK → contents.id
- **episode_number**: SMALLINT UNSIGNED, not null
- **title**: VARCHAR(255), not null
- **description**: TEXT, nullable
- **duration_minutes**: SMALLINT UNSIGNED, not null
- **thumbnail**: VARCHAR(255), nullable
- **video_url**: VARCHAR(255), not null
- **video_360p_url**: VARCHAR(255), nullable
- **video_720p_url**: VARCHAR(255), nullable
- **video_1080p_url**: VARCHAR(255), nullable
- **video_4k_url**: VARCHAR(255), nullable
- **subtitle_url**: VARCHAR(255), nullable
- **release_date**: DATE, nullable
- **view_count**: BIGINT UNSIGNED, not null, default 0
- **status**: ENUM('draft','published','archived'), not null
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP
- **updated_at**: TIMESTAMP, default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP

### people
- **id**: INT UNSIGNED, PK
- **name**: VARCHAR(150), not null
- **photo**: VARCHAR(255), nullable
- **bio**: TEXT, nullable
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP

### content_people (pivot)
- **content_id**: BIGINT UNSIGNED, FK → contents.id
- **person_id**: INT UNSIGNED, FK → people.id
- **role**: ENUM('actor','director','producer','writer','host'), not null
- **character_name**: VARCHAR(150), nullable
- **order**: TINYINT UNSIGNED, not null
- **PK**: (content_id, person_id, role)

### subscription_plans
- **id**: INT UNSIGNED, PK
- **name**: VARCHAR(100), not null
- **slug**: VARCHAR(120), UQ, not null
- **description**: TEXT, nullable
- **price**: DECIMAL(10,2), not null
- **currency**: VARCHAR(5), not null
- **billing_cycle**: ENUM('monthly','quarterly','yearly','lifetime'), not null
- **trial_days**: TINYINT UNSIGNED, not null
- **max_screens**: TINYINT UNSIGNED, not null
- **max_quality**: ENUM('480p','720p','1080p','4K'), not null
- **allow_download**: BOOLEAN, not null
- **is_popular**: BOOLEAN, not null
- **is_active**: BOOLEAN, not null
- **sort_order**: TINYINT UNSIGNED, not null
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP
- **updated_at**: TIMESTAMP, default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP

### user_subscriptions
- **id**: BIGINT UNSIGNED, PK
- **user_id**: BIGINT UNSIGNED, FK → users.id
- **plan_id**: INT UNSIGNED, FK → subscription_plans.id
- **status**: ENUM('trial','active','paused','cancelled','expired'), not null
- **starts_at**: TIMESTAMP, not null
- **ends_at**: TIMESTAMP, not null
- **trial_ends_at**: TIMESTAMP, nullable
- **cancelled_at**: TIMESTAMP, nullable
- **auto_renew**: BOOLEAN, not null
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP
- **updated_at**: TIMESTAMP, default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP

### payments
- **id**: BIGINT UNSIGNED, PK
- **user_id**: BIGINT UNSIGNED, FK → users.id
- **subscription_id**: BIGINT UNSIGNED, nullable, FK → user_subscriptions.id
- **plan_id**: INT UNSIGNED, FK → subscription_plans.id
- **gateway**: ENUM('stripe','razorpay','paypal','manual'), not null
- **gateway_order_id**: VARCHAR(255), nullable
- **gateway_payment_id**: VARCHAR(255), nullable
- **amount**: DECIMAL(10,2), not null
- **currency**: VARCHAR(5), not null
- **status**: ENUM('pending','paid','failed','refunded'), not null
- **paid_at**: TIMESTAMP, nullable
- **metadata**: JSON, nullable
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP
- **updated_at**: TIMESTAMP, default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP

### watch_history
- **id**: BIGINT UNSIGNED, PK
- **user_id**: BIGINT UNSIGNED, FK → users.id
- **content_id**: BIGINT UNSIGNED, FK → contents.id
- **episode_id**: BIGINT UNSIGNED, nullable, FK → episodes.id
- **watch_position**: INT UNSIGNED, not null (seconds)
- **duration_seconds**: INT UNSIGNED, not null
- **percent_watched**: DECIMAL(5,2), not null
- **is_completed**: BOOLEAN, not null
- **device_type**: ENUM('web','mobile','tv','tablet'), nullable
- **last_watched_at**: TIMESTAMP, not null
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP
- **updated_at**: TIMESTAMP, default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP

### watchlists
- **id**: BIGINT UNSIGNED, PK
- **user_id**: BIGINT UNSIGNED, FK → users.id
- **content_id**: BIGINT UNSIGNED, FK → contents.id
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP

### content_ratings
- **id**: BIGINT UNSIGNED, PK
- **user_id**: BIGINT UNSIGNED, FK → users.id
- **content_id**: BIGINT UNSIGNED, FK → contents.id
- **rating**: TINYINT UNSIGNED, not null (1‑5)
- **review**: TEXT, nullable
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP

### tags
- **id**: INT UNSIGNED, PK
- **name**: VARCHAR(80), UQ, not null
- **slug**: VARCHAR(100), UQ, not null

### content_tags (pivot)
- **content_id**: BIGINT UNSIGNED, FK → contents.id
- **tag_id**: INT UNSIGNED, FK → tags.id
- **PK**: (content_id, tag_id)

### hero_sliders
- **id**: INT UNSIGNED, PK
- **title**: VARCHAR(255), not null
- **placement**: ENUM('home','genres','genre_specific','popular','tv_shows','new_releases'), not null
- **genre_id**: INT UNSIGNED, nullable, FK → genres.id
- **is_active**: BOOLEAN, not null
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP

### hero_slider_items
- **id**: INT UNSIGNED, PK
- **slider_id**: INT UNSIGNED, FK → hero_sliders.id
- **content_id**: BIGINT UNSIGNED, nullable, FK → contents.id
- **title**: VARCHAR(255), nullable
- **subtitle**: VARCHAR(500), nullable
- **background_image**: VARCHAR(255), not null
- **cta_text**: VARCHAR(100), nullable
- **cta_url**: VARCHAR(255), nullable
- **sort_order**: TINYINT UNSIGNED, not null
- **is_active**: BOOLEAN, not null
- **starts_at**: TIMESTAMP, nullable
- **ends_at**: TIMESTAMP, nullable

### home_sections
- **id**: INT UNSIGNED, PK
- **title**: VARCHAR(150), not null
- **section_type**: ENUM('continue_watching','most_popular','tv_shows','by_genre','top_10','new_releases','trending','suggested'), not null
- **genre_id**: INT UNSIGNED, nullable, FK → genres.id
- **content_limit**: TINYINT UNSIGNED, not null
- **sort_by**: ENUM('popularity','release_date','view_count','rating','manual'), not null
- **display_order**: TINYINT UNSIGNED, not null
- **is_active**: BOOLEAN, not null

### support_tickets
- **id**: BIGINT UNSIGNED, PK
- **user_id**: BIGINT UNSIGNED, nullable, FK → users.id
- **name**: VARCHAR(150), not null
- **email**: VARCHAR(191), not null
- **subject**: VARCHAR(255), not null
- **message**: TEXT, not null
- **status**: ENUM('open','in_progress','resolved','closed'), not null
- **created_at**: TIMESTAMP, default CURRENT_TIMESTAMP
- **updated_at**: TIMESTAMP, default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP

---

**Notes**: All foreign‑key constraints enforce `ON DELETE RESTRICT` unless otherwise specified. Composite primary keys are defined for pivot tables to guarantee many‑to‑many integrity.

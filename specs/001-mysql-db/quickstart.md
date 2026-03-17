# Quickstart Guide

## Prerequisites

- Python 3.11 installed
- MySQL 8.0 server accessible
- `pip install sqlalchemy alembic faker pytest`

## Setup

1. Clone the repository and checkout the feature branch:
   ```bash
   git checkout 001-mysql-schema-for-ott-platform-users-languages-genres-contents-seasons-episodes-people-subscriptions-payments-watch-history-watchlists-ratings-tags-hero-sliders-home-sections-support-tickets
   ```
2. Configure database connection in `alembic.ini` (set `sqlalchemy.url = mysql+pymysql://user:pass@host/dbname`).

## Running Migrations

```bash
alembic upgrade head   # creates all tables
```

## Generating Dummy Data

```bash
python scripts/populate_dummy.py --records-per-table 10
```

The script uses column descriptions to generate realistic values (e.g., Faker for emails, UUIDs, timestamps).

## Verifying Multi‑Genre Support

```bash
python scripts/check_multi_genre.py
```
The utility creates a content record, links it to several genres, and asserts the relationships exist.

## Testing

```bash
pytest -q
```
Runs schema verification tests and dummy‑data insertion tests.

---

**Notes**: All scripts are idempotent; re‑running migrations reports "up‑to‑date" and dummy‑data script skips existing records.

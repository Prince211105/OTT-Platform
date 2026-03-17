# Tasks

## Phase 0 – Research (Completed)
- [x] Clarify language, framework, and storage choices (Python 3.11, SQLAlchemy/Alembic, MySQL 8.0).
- [x] Resolve dummy‑data record count (10 per table).
- [x] Confirm multi‑genre association via pivot table.

## Phase 1 – Design
- [x] Data model documented in `data-model.md`.
- [x] Quickstart guide for setup and migration.
- [x] Research findings compiled in `research.md`.

## Phase 2 – Implementation Planning
- Define CI/CD pipeline steps for migration and dummy data.

## Phase 2 – Implementation Tasks
- [x] **FR‑001** – Implement `users` table with columns `id`, `uuid`, `name`, `email`, `email_verified_at`, `password`, `phone`, `avatar`, `status`, `role`, `remember_token`, timestamps, and `deleted_at` (soft‑delete).
- [x] **FR‑002** – Add UNIQUE constraints on `email`, `uuid`, and any other columns marked unique.
- [x] **FR‑003** – Define all FOREIGN‑KEY relationships (e.g., `contents.language_id → languages.id`).
- [x] **FR‑004** – Create composite index on `(content_type, status, popularity_score DESC)` for the `contents` table.
- [x] **FR‑005** – Implement ENUM columns with the allowed values (e.g., `users.status`, `contents.rating`).
- [x] **FR‑006** – Add `deleted_at` soft‑delete columns to tables that require logical removal.
- [x] **FR‑007** – Build pivot tables `content_genre`, `content_people`, `content_tags` with composite primary keys and proper foreign keys.
- [x] **FR‑008** – Ensure monetary fields (`price`, `amount`) use `DECIMAL(12,2)` (or appropriate precision/scale).
- [x] **FR‑009** – Use `TIMESTAMP` columns (`created_at`, `updated_at`) with `DEFAULT CURRENT_TIMESTAMP` and `ON UPDATE CURRENT_TIMESTAMP` where appropriate.
- [x] **FR‑010** – Provide a fully‑automated Alembic migration script that can be executed on MySQL 8.0+ without manual edits.
- [x] **FR‑011** – Write `populate_dummy.py` to insert 10 realistic rows per table (except `contents`).
- [x] **FR‑012** – Verify that a `contents` record can be linked to multiple genres via `content_genre` (include a test case).

- Create issue tickets for scripts `populate_dummy.py` and `check_multi_genre.py`.
- Draft test plan covering schema verification, dummy data insertion, and multi‑genre linkage.

---

*All tasks up to Phase 1 are completed. The project is ready to move to Phase 2 implementation planning.*

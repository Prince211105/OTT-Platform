# Quickstart Guide

## Prerequisites

- Python 3.11 installed
- MySQL database running and accessible
- FFmpeg installed and available in `$PATH`
- AWS CLI configured for S3 access (or alternative storage)

## Setup Steps

1. **Clone the repository and checkout the feature branch**
   ```bash
   git checkout 002-adminlte-django-crud
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # on Windows
   pip install -r requirements.txt
   ```

3. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser for admin access**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   The custom admin panel will be available at `http://127.0.0.1:8000/admin/` with the AdminLTE theme applied.

## Common Commands

- **Run tests**: `pytest`
- **Start a background transcoding worker** (example using Celery):
  ```bash
  celery -A myproject worker -l info
  ```
- **Export revenue report** (CSV):
  ```bash
  python manage.py export_revenue --start=2026-01-01 --end=2026-03-31
  ```

## Tips

- Use the Django admin UI to manage content, genres, and hero sliders. Drag‑and‑drop reordering works out‑of‑the‑box with the AdminLTE integration.
- Bulk import CSV format is documented in the admin panel under **Import Content**.
- Video uploads are stored in the configured S3 bucket; ensure the bucket policy allows read/write for the application role.

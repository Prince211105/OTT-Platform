# Feature Specification: AdminLTE Django CRUD Admin Panel

**Feature Branch**: `002-adminlte-django-crud`  
**Created**: 2026-03-17  
**Status**: Draft  
**Input**: User description: "Create admin panel with AdminLTE bootstrap Django CRUD operations for content manager, seasons, genre, hero sliders, home layout, cast & crew, subscription plans, user manager, payment logs, tags, support tickets, analytics dashboard. Include bulk import, video upload, transcoding trigger, scheduling, preview, drag-and-drop, export, filters, revenue reports."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Content Management (Priority: P1)

An admin creates, edits, publishes, or deletes movies and series, including assigning genres, cast, and tags.

**Why this priority**: Core business value – content is the primary product of the OTT platform.

**Independent Test**: Verify that an admin can create a new movie with all metadata and publish it, and that the content appears on the public home page.

**Acceptance Scenarios**:

1. **Given** an admin is logged into the admin panel, **When** they fill the content creation form and click *Publish*, **Then** the new content is saved, marked as published, and visible on the home page.
2. **Given** an admin views the content list, **When** they select a content item and click *Delete*, **Then** the content is removed from the catalogue.

---

### User Story 2 - Bulk Import & Video Processing (Priority: P2)

An admin uploads a CSV file with multiple content records and associated video files; the system triggers transcoding jobs and creates HLS streams.

**Why this priority**: Enables rapid onboarding of large catalogs and ensures video availability.

**Independent Test**: Upload a CSV with 10 items and verify that all items are created and their videos are transcoded to the required resolutions.

**Acceptance Scenarios**:

1. **Given** an admin selects a CSV file and a zip of video assets, **When** they start the import, **Then** the system creates all content records and queues transcoding jobs for each video.
2. **Given** a transcoding job fails, **When** the admin views the import log, **Then** an error is displayed with the failed item details.

---

### User Story 3 - Analytics Dashboard (Priority: P3)

An admin views revenue reports, top‑performing content, and subscription statistics on a dashboard with date‑range filters.

**Why this priority**: Provides insight for business decisions and revenue tracking.

**Independent Test**: The dashboard loads within 3 seconds and displays correct aggregated data for the selected period.

**Acceptance Scenarios**:

1. **Given** an admin selects a date range, **When** they open the analytics page, **Then** the revenue total, top 10 content, and subscription breakdown are displayed.
2. **Given** the admin applies a filter for a specific plan, **When** the report refreshes, **Then** only data for that plan is shown.

---

### Edge Cases

- Corrupted video file upload: system must detect corruption, reject the upload, and display an error message to the admin.
- Duplicate content titles in CSV import: system must flag duplicates, skip creation of those items, and report conflicts in the import log.
- Permission error when deleting a published item: system must prevent deletion and show a permission‑denied message to the admin.

## Clarifications

### Session 2026-03-17

- Q: Which authentication method should be used for the admin panel? → A: Django admin authentication (staff/superuser)
- Q: What should be the implementation approach for the admin panel UI? → A: Custom AdminLTE UI (separate from Django admin)
- Q: Should admin actions be logged for audit purposes? → A: Yes, log all admin actions

- What happens when an uploaded video file is corrupted?
- How does the system handle a CSV import that contains duplicate content titles?
- What if the admin lacks permission to delete a published item?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow admins to create, edit, delete, publish, schedule, and preview movies and series with full metadata (at least 10 fields) and support preview before publishing.
- **FR-002**: System MUST support bulk import of content via CSV and associated video files, validating data integrity before creation, and trigger FFmpeg transcoding jobs for each uploaded video to generate HLS streams (360p, 720p, 1080p, 4K).
- **FR-004**: System MUST provide a drag‑and‑drop interface for uploading thumbnails, posters, banners, and video assets with latency < 200 ms.
- **FR-006**: System MUST enable reordering of hero slider items via drag‑and‑drop and schedule start/end dates for each slide.
- **FR-007**: System MUST let admins configure home page sections, set content limits per section, and preview the layout live.
- **FR-008**: System MUST allow creation and management of subscription plans, including pricing, screen limits, and quality tiers.
- **FR-009**: System MUST provide user management features: view users, suspend/ban accounts, and filter by subscription status.
- **FR-010**: System MUST record payment logs, generate daily revenue reports, and allow export of financial data in CSV format.
- **FR-011**: System MUST support tag creation, editing, and auto‑suggestion on content forms.
- **FR-012**: System MUST include a support ticket inbox where admins can view, reply, update status, and filter tickets by priority.
- **FR-013**: System MUST present an analytics dashboard with charts for daily views, sign‑ups, and revenue, filterable by date range and plan.
- **FR-014**: System MUST log all admin actions (create, edit, delete, publish) for audit purposes, retaining timestamps and user identifiers.

### Key Entities *(include if feature involves data)*

- **Content**: Represents movies or series; attributes include title, description, rating, status, thumbnails, video assets.
- **Season**: Belongs to a series; attributes include season number, title, release year.
- **Episode**: Belongs to a season; attributes include episode number, title, video file.
- **Genre**: Categorises content; attributes include name, display order, banner image.
- **HeroSlider**: Carousel item on the home page; attributes include linked content, order, start/end dates, image.
- **HomeLayoutSection**: Configurable section on the home page; attributes include type, content limit, ordering.
- **Person**: Cast or crew member; attributes include name, role, photo.
- **SubscriptionPlan**: Defines pricing and limits; attributes include name, price, max quality, max screens.
- **User**: Platform user; attributes include name, email, role, subscription status.
- **PaymentLog**: Records of transactions; attributes include amount, date, status.
- **Tag**: Keyword attached to content; attributes include name.
- **SupportTicket**: User‑submitted issue; attributes include subject, message, status, priority.
- **AnalyticsReport**: Aggregated metrics; attributes include date range, view counts, revenue totals.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Admins can create and publish a new movie with full metadata in under 2 minutes.
- **SC-002**: Bulk import of 100 content items completes in under 5 minutes, and all associated videos are queued for transcoding.
- **SC-003**: Video transcoding jobs finish and HLS streams become available within 10 minutes of upload for 4K content.
- **SC-004**: The analytics dashboard loads within 3 seconds for any date‑range filter and displays accurate revenue totals.
- **SC-005**: Revenue reports exported as CSV contain all transactions for the selected period with 0% data loss.

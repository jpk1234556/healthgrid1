# HealthGrid foundation

HealthGrid is being established as a clean monorepo for a healthcare coordination platform.

## Current boundaries

- `src/`: React, TypeScript, Vite frontend. The initial screen is an operations dashboard with local placeholder data.
- `backend/`: Django and Django REST Framework service. It exposes a public `GET /api/health/` check plus authenticated facility, patient, and referral endpoints.
- Supabase PostgreSQL is the intended production database. Local development uses the same PostgreSQL settings contract through environment variables.

## Security posture for the foundation

- No patient data is included in the repository.
- Clinical API endpoints must use authenticated access by default.
- The health endpoint is public only so hosting and monitoring can verify process health.
- Consent, role-based access, audit events, facility tenancy, and encryption policies must be designed before patient workflows are connected.
- Placeholder dashboard numbers are not operational or clinical data.

## Planned domain modules

1. Identity and access: providers, roles, consent, and facility tenancy.
2. Records: patient identity is established; encounters, diagnoses, medications, documents, and immutable access events remain next.
3. Coordination: facilities and referrals are established; ambulance dispatch, bed, and facility capacity remain next.
4. Intelligence: aggregate reporting with de-identification and explicit governance.

The next implementation milestone is to agree the identity, tenancy, consent, and audit model before adding the first patient-facing models or API endpoints.

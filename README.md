# HealthGrid

Fresh project foundation for a secure healthcare coordination platform.

## Stack

- Frontend: React, TypeScript, Vite
- Backend: Python, Django, Django REST Framework
- Database target: Supabase PostgreSQL

## Run the frontend

```powershell
npm run dev
```

## Run the backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py runserver 8000
```

Health check: `http://localhost:8000/api/health/`

## Supabase database

For a hosted Supabase environment, set `DATABASE_URL` to the direct or pooled PostgreSQL connection string from the Supabase dashboard. The application adds `sslmode=require` when the URL does not specify an SSL mode. Do not commit the URL or its password; use Render environment variables in hosted deployments.

For local development, omit `DATABASE_URL` to use the SQLite fallback, or use the split `POSTGRES_*` variables for a local PostgreSQL instance.

Run [backend/supabase_schema.sql](backend/supabase_schema.sql) once in the Supabase SQL Editor for the initial Phase 2 schema. Do not add seed data yet.

## Credentials needed

To connect the Django backend to Supabase, provide these values through a local `backend/.env` file or Render environment variables:

- `DATABASE_URL`: Supabase PostgreSQL connection string. Prefer the pooler connection string for hosted Render deployments.
- `DJANGO_SECRET_KEY`: a new long random secret for Django.
- `DJANGO_ALLOWED_HOSTS`: backend hostnames, such as the Render service hostname.
- `CORS_ALLOWED_ORIGINS`: the deployed Vercel frontend URL and any approved local development URLs.

The Supabase dashboard values used to construct `DATABASE_URL` are the database host, database name, database user, database password, and database port. Never commit the password or connection string.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the current system boundary and security notes.

# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some Oxlint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the Oxlint configuration

If you are developing a production application, we recommend enabling type-aware lint rules by installing `oxlint-tsgolint` and editing `.oxlintrc.json`:

```json
{
  "$schema": "./node_modules/oxlint/configuration_schema.json",
  "plugins": ["react", "typescript", "oxc"],
  "options": {
    "typeAware": true
  },
  "rules": {
    "react/rules-of-hooks": "error",
    "react/only-export-components": ["warn", { "allowConstantExport": true }]
  }
}
```

See the [Oxlint rules documentation](https://oxc.rs/docs/guide/usage/linter/rules) for the full list of rules and categories.

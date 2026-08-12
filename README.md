# MetricMind

MetricMind is a full-stack Next.js BI workspace with a premium SaaS interface, a demo mode, and a server-only Snowflake integration path.

## Run locally

```bash
npm install
npm run dev
```

Open `http://localhost:3000`. With no Snowflake variables configured, every data-backed screen is explicitly marked **Demo mode** and uses local sample data.

## Connect Snowflake

1. Copy `.env.example` to `.env.local`.
2. Fill in your Snowflake account settings and password locally. Do not commit `.env.local`.
3. Restart `npm run dev`.

The app reads these server-only variables:

```env
SNOWFLAKE_ACCOUNT=
SNOWFLAKE_USERNAME=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_ROLE=
SNOWFLAKE_WAREHOUSE=
SNOWFLAKE_DATABASE=
SNOWFLAKE_SCHEMA=
SNOWFLAKE_AUTHENTICATOR=
SNOWFLAKE_QUERY_ROW_LIMIT=1000
```

The SQL Explorer only accepts one read-only `SELECT`, `WITH`, `SHOW`, or `DESCRIBE` statement. It rejects data-changing commands and limits result rows. Secrets are never sent to the browser.

## API

- `POST /api/chat` — deterministic BI response adapter
- `POST /api/query` — validated Snowflake read query (or labelled demo result)
- `POST /api/upload` — validates CSV, JSON, PDF, XLSX uploads under 10 MB
- `GET /api/models`, `/api/models/:name` — semantic metadata
- `GET /api/warehouse`, `/api/history`, `/api/dashboard`, `/api/agents`, `/api/health`

Each endpoint returns a `{ success, data, error, meta }` envelope.

## Before production

Add your identity provider, authorization/tenant scoping, rate limits, audit records, durable dashboard/history storage, an object store for uploads, and an LLM provider implementation. The `BIProvider` interface in `lib/providers/rule-based.ts` is the handoff point for an OpenAI/LangChain provider.

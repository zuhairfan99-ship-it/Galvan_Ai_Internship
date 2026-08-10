# Gravity Shift — Vercel + Neon Ready
This build keeps the existing Gravity Shift gameplay, levels, scoring, player registration, per-level Top 10 leaderboards, admin dashboard/CSV, backup controls, external controller support, offline completion queue, and final victory flow.
## What changed for production hosting
- **Local development:** Node 24 + built-in `node:sqlite` if `DATABASE_URL` is empty.
- **Vercel production:** PostgreSQL (recommended: Neon) when `DATABASE_URL` is present.
- The official leaderboard is therefore **not stored in Vercel's filesystem**.
- Admin authentication uses backend environment variables plus a signed, HttpOnly cookie. Admin credentials are never shipped to the browser.
- Admin sessions are stateless/signed so they do not depend on one Vercel instance's memory.
- `EVENT_LIVE=true` disables the testing database reset endpoint.
- No CSV control is shown to public players. CSV is admin-only.
- Level leaderboards remain independent: `/api/leaderboard/level/1` is only Level 1, `/api/leaderboard/level/2` is only Level 2, etc.
- Ranking is `completion_time_ms ASC, completed_at ASC`.
- Completed records use unique game IDs and idempotency keys.
## IMPORTANT: How the hidden `.env` works
You do **not** upload `.env` to GitHub.
The browser does NOT need `.env`.
The browser shows the admin login form at:
`/admin`
When the organizer submits the username/password, the browser sends them to:
`POST /api/admin/login`
The backend reads:
- `ADMIN_USERNAME`
- `ADMIN_PASSWORD`
- `ADMIN_SESSION_SECRET`
from the server environment, verifies the credentials, and sets an HttpOnly authentication cookie.
So the admin can log in normally even though `.env` is hidden.
### On Vercel
Go to:
**Vercel → your project → Settings → Environment Variables**
Add:
```text
ADMIN_USERNAME=event-admin
ADMIN_PASSWORD=YOUR_PRIVATE_STRONG_PASSWORD
ADMIN_SESSION_SECRET=YOUR_LONG_RANDOM_SECRET
GAME_VERSION=1.2.0
EVENT_LIVE=false
DATABASE_URL=YOUR_NEON_POSTGRES_CONNECTION_STRING
```
Then the admin logs in at:
`https://YOUR-VERCEL-DOMAIN/admin`
The password is never placed in frontend JavaScript.
## 1. Local testing
Requirements: Node 24+.
```powershell
npm install
```
Copy `.env.example` to `.env` and set:
```env
ADMIN_USERNAME=event-admin
ADMIN_PASSWORD=your-test-password
ADMIN_SESSION_SECRET=use-a-long-random-secret
EVENT_LIVE=false
```
You may leave `DATABASE_URL` empty locally. The app will create:
`data/leaderboard.db`
Then:
```powershell
npm start
```
Open:
- Game: `http://localhost:3000`
- Admin: `http://localhost:3000/admin`
- Controller: `http://localhost:3000/controller`
## 2. Create the production database
In Vercel, add the **Neon** integration and create/connect a Postgres database. Vercel's Neon integration provisions a managed Postgres database and provides the database connection environment variable.
The app automatically creates the required tables on first backend use.
You can also use `schema.sql` manually in a Postgres/Neon SQL editor.
## 3. Put the project on GitHub
At the project root:
```powershell
git init
git add .
git commit -m "Gravity Shift Vercel production build"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
Do NOT commit `.env`.
The included `.gitignore` excludes `.env`, `node_modules`, and local SQLite database files.
## 4. Import into Vercel
In Vercel:
**Add New → Project → Import Git Repository**
Select the Gravity Shift GitHub repository.
Vercel supports zero-configuration Express deployments.
Set the environment variables before deploying, especially `DATABASE_URL`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`, and `ADMIN_SESSION_SECRET`.
Use Node 24 for the project.
## 5. Test production
After deployment:
```text
https://YOUR-VERCEL-DOMAIN/api/health
```
It should report:
```json
{
  "ok": true,
  "status": "online",
  "database": "postgres"
}
```
Then test:
```text
https://YOUR-VERCEL-DOMAIN/
https://YOUR-VERCEL-DOMAIN/admin
https://YOUR-VERCEL-DOMAIN/controller
```
## 6. Admin login
Open:
`https://YOUR-VERCEL-DOMAIN/admin`
Enter the same values you placed in Vercel:
```text
Username: event-admin
Password: YOUR_PRIVATE_STRONG_PASSWORD
```
The `.env` file being hidden is correct and expected.
## 7. Admin Top 10 CSV
After login:
1. Select a level.
2. Click **Download Top 10 CSV**.
3. The backend generates a CSV for that selected level only.
4. The public game never displays this control.
## 8. Testing reset
While:
```env
EVENT_LIVE=false
```
the admin dashboard has **Clear Test Data**.
It requires:
```text
DELETE ALL TEST DATA
```
When:
```env
EVENT_LIVE=true
```
the reset endpoint is disabled.
Before the real event, set:
```env
EVENT_LIVE=true
```
and redeploy.
## 9. Migrating your existing local SQLite test/event database
If you already have records in `data/leaderboard.db` and want to move them to Postgres:
1. Set `DATABASE_URL` to the target Postgres database.
2. Keep the SQLite file in `data/leaderboard.db`.
3. Run:
```powershell
npm run db:migrate
```
The migration script inserts sessions, attempts, and completed records without duplicating existing `game_id` values.
## 10. Production data model
The production database contains:
- `player_sessions`
- `level_attempts`
- `game_records`
`game_records` is the official completed-level history.
Each completed record includes the player/company identity, level number, completion time, score, level start/completion times, backend completion timestamp, control/connection information, game version, unique game ID and idempotency key.
The public endpoint only returns the requested level's Top 10:
```text
GET /api/leaderboard/level/:levelNumber
```
Admin-only endpoints expose complete history and statistics.
## 11. External controller
The project retains the WebSocket controller at:
`/controller`
The game automatically falls back to local keyboard/touch controls when the external controller disconnects.
Vercel currently supports WebSockets in Public Beta on Fluid Compute. The controller client should still handle reconnections, and the game's backup controls remain the safety mechanism if the external connection fails.
## 12. Event launch checklist
Before the event:
1. Create/connect Neon Postgres.
2. Set all Vercel environment variables.
3. Set `EVENT_LIVE=true`.
4. Deploy.
5. Open `/admin`.
6. Confirm the admin can log in.
7. Confirm Level 1 Top 10 is empty.
8. Confirm Level 2 Top 10 is empty.
9. Confirm the CSV button is only inside admin.
10. Test one participant with `Company - Player`.
11. Complete a test level.
12. Confirm the level result appears in that level's Top 10.
13. Confirm the admin sees the complete history.
14. Confirm the CSV downloads the selected level only.
15. Confirm refresh/redeploy does not erase the database.
16. Do not delete the Neon production database.

## No public event-link sharing

The application does not add public sharing buttons or public administration. Organizers control access to the event deployment URL separately.

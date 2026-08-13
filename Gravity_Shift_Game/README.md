# Gravity Shift
**Gravity Shift** is a browser-based gravity platformer where players navigate increasingly difficult levels while gravity shifts between different directions. Collect crystals, avoid hazards, reach the goal, and try to earn a place in the shared Top 10 leaderboard.
## Play the Game
The game is deployed on Vercel and can be played online:
**https://zuhairfangravityshiftgame.vercel.app/**
No installation is required to play the deployed version.
## Features
- **100 levels** with progressively harder layouts and gravity mechanics.
- **4-way gravity**: Down, Up, Left, and Right.
- Gravity becomes more challenging as the level increases.
- Collect all **crystals** to unlock the goal.
- **Red hazards** cause instant death.
- **3 lives per run**.
- Score tracking throughout the run.
- Level selection and level progression.
- Level replay and next-level controls.
- **Top 10 global leaderboard** backed by a database.
- **CSV export** for played-game records.
- Player and company registration before starting a game.
- Responsive on-screen controls for Left, Right, and Jump.
- Keyboard controls for desktop play.
- Touch controls for supported mobile devices.
- Visual effects, HUD updates, gravity indicators, and game sounds.
- Vercel-ready serverless API.
## How to Play
### 1. Register
Before playing, enter:
- **Player Name**
- **Company Name**
Both fields are required.
### 2. Start the Game
After registration, open the **Quick Start** instructions and select **Start Playing**.
### 3. Controls
| Action | Keyboard | On-Screen Control |
|---|---|---|
| Move left | `←` | **LEFT** |
| Move right | `→` | **RIGHT** |
| Jump / move away from the current gravity surface | `↑`, `↓`, or `Space` | **JUMP** |
The game also provides touch-friendly controls for mobile devices.
### 4. Complete Levels
Each level requires you to:
1. Navigate the level.
2. Adapt to changing gravity.
3. Collect every crystal.
4. Avoid red hazards.
5. Reach the goal.
When all crystals are collected, the goal becomes available.
### 5. Manage Your Lives
You start each run with **3 lives**. Hitting a red hazard costs a life.
If all three lives are lost, the run ends and the final score is submitted to the leaderboard.
Completing the final level also ends the run and saves the final score.
## Gravity System
Gravity can pull the player in four directions:
- `DOWN`
- `UP`
- `LEFT`
- `RIGHT`
The available gravity directions depend on the level:
- **Levels 1–10:** Down and Up
- **Levels 11–35:** Down, Up, and Left
- **Levels 36–100:** Down, Up, Left, and Right
Gravity shifts automatically during gameplay, so timing and positioning are essential.
## Scoring & Leaderboard
Completed runs are submitted to the backend through the game API.
The leaderboard records information such as:
- Player name
- Company name
- Score
- Level reached
- Control method
- Timestamp
- Game/session information
The **Top 10 Leaderboard** is sorted by highest score, with newer records breaking ties.
Scores are saved when a run ends because the player either:
- loses all lives, or
- completes the final level.
The game also provides an **Export CSV** option for exporting played-game records.
## 🏗️ Project Structure
```
Gravity_Game_Leaderboard_Reset/
├── api/
│   └── index.js              # Vercel serverless entry point
├── levels/
│   ├── level1.js
│   ├── level2.js
│   ├── level3.js
│   ├── level4.js
│   ├── level5.js
│   └── level6.js
├── scripts/
│   ├── effects.js            # Particle effects
│   ├── enemy.js              # Enemy behavior
│   ├── leaderboard.js        # Local leaderboard helpers
│   ├── physics.js            # Gravity and physics
│   └── player.js             # Player state
├── index.html                # Main game interface
├── style.css                 # Game styling
├── game.js                   # Main game engine and gameplay logic
├── server.js                 # Express API and static server
├── db.js                     # Database layer
├── vercel.json               # Vercel configuration
├── package.json              # Node.js dependencies/scripts
└── .env.example              # Environment variable template
```
## Technology Stack
### Frontend
- HTML5
- CSS3
- Vanilla JavaScript
- HTML5 Canvas
- Web Audio API
- Browser keyboard and touch events
### Backend
- Node.js
- Express
- CORS
- Vercel Serverless Functions
### Database
- Turso / libSQL for production
- SQLite file fallback for local development
### Deployment
- Vercel
## API Endpoints
The Express backend exposes the following endpoints:
### Health Check
```http
GET /api/health
```
Returns the current API status.
### Validate Player
```http
POST /api/validate-name
```
Validates the submitted player and company information.
### Save Game
```http
POST /api/games
```
Stores the completed game's score and related gameplay information.
### Top 10 Leaderboard
```http
GET /api/leaderboard/top10
```
Returns the current Top 10 leaderboard.
### Export Games
```http
GET /api/export/csv
```
Exports played-game records as a CSV file.
## Database
Production deployments are designed to use **Turso / libSQL** so leaderboard data persists across Vercel serverless invocations.
The application automatically creates the `game_records` table when the database is initialized.
### Production environment variables
```env
TURSO_DATABASE_URL=
TURSO_AUTH_TOKEN=
```
For local development, the project can fall back to a SQLite database file.
```env
PORT=3000
DB_PATH=./data/leaderboard.db
```
> Never commit real database credentials or a real `.env` file to source control.
## Run Locally
### Prerequisites
- Node.js
- npm
### Installation
```bash
npm install
```
### Environment
Copy the example environment file:
```bash
cp .env.example .env
```
For local-only development, you can leave the Turso variables empty and use the SQLite fallback.
### Start the server
```bash
npm start
```
Then open:
```text
http://localhost:3000
```
For development with automatic Node.js restarts:
```bash
npm run dev
```
## Deploy to Vercel
The project already includes a `vercel.json` configuration and a serverless entry point at `api/index.js`.
### Using Vercel CLI
```bash
npm install -g vercel
vercel login
vercel
vercel --prod
```
### Using GitHub + Vercel
1. Push the project to GitHub.
2. Import the repository into Vercel.
3. Use the **Other** framework preset if prompted.
4. Configure the production environment variables:
   - `TURSO_DATABASE_URL`
   - `TURSO_AUTH_TOKEN`
5. Deploy the project.
The API routes under `/api/*` are routed to the Vercel serverless function.
## Gameplay UI
The game interface includes:
- Level name and number
- Current score
- Crystal count
- Remaining lives
- Current gravity direction
- Gravity-shift countdown
- Participant information
- Control status
- Leaderboard panel
- CSV export button
- Level selector
- Fullscreen button
- Replay and next-level actions
## Game Objective
The ultimate goal is to complete all **100 levels** and achieve the highest possible score.
**Collect the crystals. Survive the gravity shifts. Avoid the hazards. Reach the goal. Become #1 on the leaderboard.**
## License
No specific open-source license is included in the project archive. If this project is intended for public distribution, add an appropriate `LICENSE` file.

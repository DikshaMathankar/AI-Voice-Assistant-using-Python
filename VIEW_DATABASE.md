# How to View Your SQLite Database

## Quick Commands

### View all cars:
```bash
sqlite3 auto_db.sqlite "SELECT * FROM cars;"
```

### View table structure:
```bash
sqlite3 auto_db.sqlite ".schema cars"
```

### Interactive mode:
```bash
sqlite3 auto_db.sqlite
```
Then run SQL commands:
- `SELECT * FROM cars;`
- `.tables` - List all tables
- `.schema` - Show table structures
- `.exit` - Exit

## VS Code Extensions

Install one of these extensions to view SQLite files visually:
- **SQLite Viewer** (by Florian Klampfer) - Recommended
- **SQLite** (by alexcvzz)

After installing:
1. Right-click `auto_db.sqlite` in file explorer
2. Select "Open Database" or "SQLite: Open Database"
3. Browse tables visually

## Online SQLite Viewers

Upload `auto_db.sqlite` to:
- https://sqliteviewer.app/
- https://inloop.github.io/sqlite-viewer/

## Desktop Applications

- **DB Browser for SQLite** (Free) - https://sqlitebrowser.org/
- **DBeaver** (Free) - Universal database tool

## Test Your Database

Add a test car through your LiveKit agent, then view it:
```bash
sqlite3 auto_db.sqlite "SELECT * FROM cars;"
```

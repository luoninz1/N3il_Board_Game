# No‑Three‑in‑Line — Interactive Board (Chess‑Style)

An interactive browser tool for exploring ## Planned / Possible Enhancements

- Toggle to hide ≥3 collinear summary lines when Collinearity Detection is ON.
- Option to export only valid stones.
- Dark/light theme toggle.
- Performance optimization for large dense boards (line hashing or sweep algorithms).
- Shareable encoded board states via URL parameter.
- Additional sample solutions for larger board sizes (13+).
- Solution verification and optimality checking tools.ssic "No Three In Line" problem on an n×n lattice. You place stones (points) on a chess‑style grid while trying to maximize the number of valid stones such that no three stones lie on a straight line of any slope.

## Key Features

- Chess‑style square board (default size 3×3; adjustable up to 50×50).
- Click to place a stone; click again to remove it (toggle behavior).
- Stones that create a line of 3+ collinear stones remain visible but turn red (invalid) and don’t count toward your Personal Best.
- Automatic tracking of per‑board‑size Personal Best (counts only valid stones, persisted in localStorage).
- Collinear detection visualization: every line with ≥3 stones is drawn as a solid red segment spanning the extreme stones.
- **Collinearity Detection mode** (toggle button):
	- Draws a faint red line across the whole board for every pair of stones.
	- Highlights (red translucent overlay) every empty square lying on any of those lattice lines.
	- Helps you see future conflicts and potential blocked positions.
- **Show Sample Solution** feature:
	- Loads optimal known solutions for board sizes 3–12.
	- Solutions are not unique—multiple optimal arrangements may exist.
	- Button automatically disables for sizes >12 with explanatory text.
	- Clicking erases current board and loads the sample configuration.
- Import / export coordinates via a simple text box (format: `(x,y);(x2,y2);...`).
- Undo last placement/removal and full board Reset.
- High‑DPI canvas rendering with stable sizing (prevents layout drift) and mobile/touch support.
- Query string parameters to preconfigure the board.

## Rules Recap

Goal: Place as many stones as possible so that no three stones are collinear. Lines include horizontal, vertical, diagonal, and any arbitrary slope (determined by exact lattice alignment).

If you place a stone that causes any triple to become collinear:
- The stone is still added for inspection.
- It is colored red (invalid).
- It does NOT count toward the Personal Best counter.

## Query String Parameters

You can control initial settings by appending parameters to the URL (local file URLs also work):

| Param | Example | Description |
|-------|---------|-------------|
| `n` or `size` | `?n=19` | Sets initial board size (3–50). |
| `complete`, `cd` | `?complete=on` / `?cd=1` | Turns Collinearity Detection ON at load (accepts `1,true,on,yes`). |

Multiple parameters can be combined, e.g. `?n=25&complete=on`.

## Coordinate System

- Internal coordinates are zero‑based (0..n-1) for import/export.
- Displayed labels use A,B,C,… for columns and 1..n for rows.
- A coordinate `(x,y)` in the import/export box refers to column `x` from the left and row `y` from the top (both zero‑based).

## Sample Solutions

The application includes pre-computed optimal solutions for board sizes 3–12. These solutions are:

- Stored in `sample_solutions.json` (generated from `grid_conversion.py`).
- Automatically loaded when the page loads.
- Accessible via the "Show Sample Solution" button.
- Not unique—multiple optimal arrangements exist for each board size.

### Sample Solution Counts by Board Size

| Size | Max Stones | Sample Configuration Available |
|------|------------|--------------------------------|
| 3×3  | 6          | ✓ |
| 4×4  | 8          | ✓ |
| 5×5  | 10         | ✓ |
| 6×6  | 12         | ✓ |
| 7×7  | 14         | ✓ |
| 8×8  | 16         | ✓ |
| 9×9  | 18         | ✓ |
| 10×10| 20         | ✓ |
| 11×11| 22         | ✓ |
| 12×12| 24         | ✓ |
| >12  | —          | ✗ (Button disabled) |

## Data Persistence

Personal bests are stored in `localStorage` under keys of the form `n3il-best-{n}` and scoped per board size.

## Performance Notes

- Collinear detection is O(k²) over current stones (k = number of placed stones).
- Collinearity Detection also loops over O(k²) pairs and traces lines across the board; very large boards with many stones may become slower.
- For exploration, this is typically sufficient. If you need larger scales, consider pruning or incremental line indexing.

## Import / Export Format

Paste or type a semicolon‑separated list:

```
(0,0);(3,5);(10,2)
```

Invalid or out‑of‑range points for the current board size abort the load with a message.

## Planned / Possible Enhancements

- Toggle to hide >=3 collinear summary lines when Complete Detection is ON.
- Option to export only valid stones.
- Dark/light theme toggle.
- Performance optimization for large dense boards (line hashing or sweep algorithms).
- Shareable encoded board states via URL parameter.

## Development

Core application: Single file (`index.html`) — open directly in a modern browser. No build step required.

Additional files:
- `sample_solutions.json` — Pre-computed optimal solutions for board sizes 3–12.
- `grid_conversion.py` — Python script to convert grid arrays to coordinate format and generate the JSON file.

To regenerate sample solutions:
```bash
python grid_conversion.py
```

## License

See `LICENSE` file (project retains original licensing terms).

---
Enjoy experimenting with lattice placements and pushing the no‑three‑in‑line bounds!
# Python Fundamentals

My Python learning playground from February to July 2023. It starts with printing strings and ends with turtle art, a Tkinter calculator and my first class.

## Structure

| Folder | Topics |
|--------|--------|
| `01-basics/` | `print`, variables, f-strings, slicing, input validation |
| `02-data-structures/` | Lists, 2D lists, removing duplicates, tuples and unpacking, sets, dictionaries |
| `03-control-flow/` | `if/elif/else`, logical operators, weight converter, voting-eligibility validator |
| `04-loops/` | `for`, `range`, `while`, nested loops and drawing shapes with characters |
| `05-mini-games/` | Text car simulator and a number-guessing game with rounds and scores |
| `06-turtle-art/` | Spirals and color-cycling patterns with `turtle` + `colorsys`, and `sketchpy` drawings |
| `07-gui/` | Start of a scientific calculator in Tkinter |
| `08-oop/` | First class: an `Item` with a total-price method |

## Run

```bash
python3 04-loops/nested_loops.py
python3 06-turtle-art/py_like_thorn.py     # opens a turtle window
```

`06-turtle-art/canvas.py` and `sketchpy.py` need the `sketchpy` package (`pip install sketchpy`).

## Notes

- `turtle.py` was renamed to `turtle_spiral.py`. A file called `turtle.py` hides Python's built-in `turtle` module and breaks every other turtle script in the same folder.
- Some files are unfinished and some have bugs (for example, the calculator GUI is only half wired up). I kept them as I wrote them.

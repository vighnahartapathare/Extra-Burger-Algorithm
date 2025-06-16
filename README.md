# Extra Burger Algorithm

A Python simulation that models making extra burgers from saved ingredients over multiple days. Each day, one unique ingredient is removed from a standard burger and stored. When a complete set of ingredients is saved, an extra burger is assembled.

## How It Works

- The base burger contains:
  `["bun", "lettuce", "tomato", "cheese", "patty", "onion", "sauce"]`
- Each day, one different ingredient is removed in a rotating fashion and saved.
- When enough saved ingredients can form a full burger, an extra burger is made.

## Algorithm Summary

- **Input:** Number of simulation days (`days = 10`)
- **Process:** Rotate through ingredients, remove and save one per day
- **Output:** Number of extra burgers made

## Complexity

- **Time Complexity:** `O(d·n + e·n·m)`
- **Space Complexity:** `O(d + n)`

Where:
- `d` = number of days
- `n` = number of ingredients
- `e` = number of extra burgers made
- `m` = size of saved ingredients list (≤ d)

## Running the Code

Run the script with Python:

```bash
python extra_burger_algorithm.py

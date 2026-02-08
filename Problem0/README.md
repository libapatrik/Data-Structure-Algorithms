# Problem 0 - Phone Call & Text Analysis

Five tasks on phone call and text message datasets (`calls.csv`, `texts.csv`) from September 2016. Each task targets a specific time complexity.

| File | Question | Complexity |
|------|----------|------------|
| `Task0.py` | First text record, last call record | O(1) |
| `Task1.py` | How many unique phone numbers across both datasets? | O(n) |
| `Task2.py` | Which number spent the most total time on the phone? | O(n) |
| `Task3.py` | Area codes/prefixes called from Bangalore + % of Bangalore-to-Bangalore calls | O(n log n) |
| `Task4.py` | Identify possible telemarketers (numbers that only make outgoing calls, never text or receive) | O(n log n) |

Full complexity analysis in `Analysis.txt`.

## Data

- `texts.csv` - sender, receiver, timestamp
- `calls.csv` - caller, receiver, start timestamp, duration (seconds)

# Overtime Tracker

A Python script for processing and formatting work hours from a Markdown table.

## Features

- Converts time entries from strings to timedelta objects.
- Calculates differences and cumulative differences based on expected work hours.
- Formats time entries for readability.
- Saves the cleaned and formatted data to a Markdown file.

## Usage

1. Place your input file as work_times.md.
2. Run the script: `python3 overtime_tracker.py`
3. The output will be saved to work_times.md with cleaned data.

## Requirements

- Python 3.x
- Pandas: `pip install pandas`
- Tabulate: `pip install tabulate`

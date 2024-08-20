# Overtime Tracker

A Python script for processing and formatting work hours from a Markdown table. Now compatible with Android devices using the Pydroid 3 app.

## Features

1. Converts time entries from strings to timedelta objects.
2. Calculates differences and cumulative differences based on expected work hours.
3. Formats time entries for readability.
4. Saves the cleaned and formatted data to a Markdown file.

## Usage on Android

1. Install Pydroid 3: This app allows you to run Python scripts directly on your Android device.
2. Prepare Your Files on Android
   1. `/storage/emulated/0/Obsidian/Work/Work Times.md`
   2. `/storage/emulated/0/Obsidian/Work/overtime_tracker.py`
3. Run the Script: Open `overtime_tracker.py` on Pydroid 3 (folder icon at top right corner) and run it.
4. View the Results: The output will be saved to that markdown file with the updated and formatted data.

## Requirements

- Pydroid 3: Available on Google Play Store
- Python 3.x (included in Pydroid 3)
- Pandas: Install package in Pydroid 3
- Tabulate: Install package in Pydroid 3

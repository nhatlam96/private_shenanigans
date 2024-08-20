import pandas as pd
from datetime import timedelta
import re


def time_to_timedelta(time_str):
    """Convert time string to timedelta object."""
    try:
        h, m = map(int, time_str.split(':'))
        return timedelta(hours=h, minutes=m)
    except ValueError:
        return timedelta()


def format_timedelta(td):
    """Format timedelta object to string without '0 days'."""
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(abs(total_seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    sign = "-" if total_seconds < 0 else ""
    return f"{sign}{hours}:{minutes:02d}"


def format_time_without_seconds(td):
    """Format timedelta to exclude seconds."""
    return format_timedelta(td)


def calculate_differences(df, expected_work_hours):
    """Calculate differences and format time columns."""
    # Convert time columns to timedelta
    for col in ['Start', 'Pause', 'End']:
        df[col] = df[col].apply(lambda x: time_to_timedelta(x)
                                if isinstance(x, str) else x)

    # Compute work duration and differences
    df['Diff_fx'] = (df['End'] - df['Start'] -
                     df['Pause']) - timedelta(hours=expected_work_hours)
    df['Diff_Fx'] = df['Diff_fx'].cumsum()

    # Format results
    df['Diff_fx'] = df['Diff_fx'].apply(format_time_without_seconds)
    df['Diff_Fx'] = df['Diff_Fx'].apply(format_time_without_seconds)

    return df[['Date', 'Start', 'Pause', 'End', 'Diff_fx', 'Diff_Fx']]


def remove_zero_days_prefix(filename):
    """Remove '0 days' prefix from the markdown file."""
    with open(filename, 'r') as file:
        content = file.read()

    # Use regex to remove '0 days' from the content
    content = re.sub(r'0 days\s+', '', content)

    with open(filename, 'w') as file:
        file.write(content)


# Main script
expected_work_hours = 8
file_path_android = 'Work Times.md'
df = pd.read_csv(file_path_android,
                 sep='\\s*\\|\\s*',
                 engine='python',
                 header=None)

# Clean DataFrame: remove header and separator rows, drop irrelevant columns
df = df.iloc[1:].reset_index(drop=True)
df = df[~df.apply(lambda x: x.astype(str).str.contains('-----').any(), axis=1)]
df = df.iloc[:, 1:-1]
df.columns = ['Date', 'Start', 'Pause', 'End', 'Diff. fx', 'Diff. Fx']

# Calculate differences
df = calculate_differences(df, expected_work_hours)

# Convert time columns to the desired format without seconds
df[['Start', 'Pause',
    'End']] = df[['Start', 'Pause', 'End']].apply(lambda col: col.apply(
        lambda x: format_time_without_seconds(time_to_timedelta(x))
        if isinstance(x, str) else format_time_without_seconds(x)))

# Save to markdown
df.to_markdown(file_path_android, index=False)

# Remove '0 days' prefix from markdown file
remove_zero_days_prefix(file_path_android)

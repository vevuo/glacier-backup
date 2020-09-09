from pathlib import Path


def get_total_size(files):
    return sum(get_file_size(file.get("file_path")) for file in files)


def get_file_size(file_path):
    return Path(file_path).stat().st_size


def count_and_get_ranges(files):
    updated_files = []
    start = 0
    for file in files:
        end = start + file.get("file_size")
        file_range = {"range": (start, end)}
        updated_files.append({**file, **file_range})
        start = end + 1
    return updated_files

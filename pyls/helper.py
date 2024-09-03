from datetime import datetime


def format_time(epoch_time):
    return datetime.fromtimestamp(epoch_time).strftime('%b %d %H:%M')


def size_format(size):
    if size > 1023:
        for unit in ['K', 'M', 'G']:
            size /= 1024
            if size <= 1023:
                return f"{size:.1f}{unit}"
    return f"{size}"

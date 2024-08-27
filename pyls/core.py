import json
import sys
from pyls.helper import format_time
from pyls.helper import size_format


def pyls(path='', include_all=False, detailed=False, reverse=False, sort_by_time=False, filter_option=None):
    with open('structure.json', 'r') as file:
        structure = json.load(file)

    if path:
        for part in path.strip('/').split('/'):
            found = False
            for item in structure.get('contents', []):
                if item['name'] == part:
                    if 'contents' in item:
                        structure = item
                        found = True
                        break
            if not found:
                print(f"error: cannot access '{path}': No such file or directory")
                sys.exit(1)

    contents = [item for item in structure['contents'] if
                (include_all or not item['name'].startswith('.'))]

    if filter_option:
        if filter_option == 'file':
            contents = [item for item in contents if 'contents' not in item]
        elif filter_option == 'dir':
            contents = [item for item in contents if 'contents' in item]
        else:
            print(f"error: '{filter_option}' is not a valid filter criteria. Available filters are 'dir' and 'file'")
            return

    if sort_by_time:
        contents.sort(key=lambda x: x['time_modified'], reverse=reverse)
    elif reverse:
        contents.reverse()

    for item in contents:
        if detailed:
            formatted_time = format_time(item['time_modified'])
            formatted_size = size_format(item['size'])
            print(f"{item['permissions']} {formatted_size} {formatted_time} {item['name']}")
        else:
            print(item['name'], end=" ")

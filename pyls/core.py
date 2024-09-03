import json
import sys
from pyls.helper import format_time
from pyls.helper import size_format


def pyls(path='', include_all=False, detailed=False, reverse=False, sort_by_time=False, human_readable=False,
         filter_option=None):
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

    max_size_len = max(len(str(item['size'])) for item in contents) if contents else 0

    for item in contents:
        if human_readable:
            formatted_size = str(size_format(item['size']).rjust(max_size_len))
        else:
            formatted_size = str(item['size']).rjust(max_size_len)

        if detailed:
            formatted_time = format_time(item['time_modified'])
            print(f"{item['permissions']} {formatted_size} {formatted_time} {item['name']}")
        else:
            print(item['name'], end=" ")

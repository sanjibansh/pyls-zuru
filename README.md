# pyls

`pyls` is a command-line tool for listing files and directories with various options for filtering, sorting, and detailed output.

## Features

- **List files and directories**: Display the contents of a directory with options to include hidden files, show detailed information, sort by modification time, and filter by file type.

    Display the contents of the subdirectory under directory.
    You can use pyls with various command-line options and path handling commands.

### Options

- `-A`: Include all files, including hidden files.
- `-l`: Use a long listing format (detailed view).
- `-r`: Reverse the order of the listing.
- `-t`: Sort by modification time.
- `--filter`: Filter results based on 'file' or 'dir'.
- `-h`: Display the help list of flags.


### Example Commands:
###### Note: Before using the following commands, make sure to install it. Look Installation section below

#### List all files and directories, including hidden ones
pyls -A

#### List files in detailed format
pyls -l

#### List files sorted by modification time, in reverse order
pyls -r -t

#### Filter to show only files
pyls --filter=file

### Path handling
- parser
- token
- lexer

### Example Commands: 
#### list the files under parser
pyls parser


Testing
To run tests, make sure you have pytest installed and then run:
pytest tests/test_pyls.py  


## Installation

To install `pyls`, clone this repository and run the following command:

```bash
pip install .

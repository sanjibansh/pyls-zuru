import pytest
from unittest.mock import mock_open, patch
from datetime import datetime
from pyls.core import pyls
import json


# Fixture to read JSON data from file
@pytest.fixture
def mock_structure():
    with open('tests/mock_structure.json', 'r') as file:
        return json.load(file)


# Mock function to convert epoch time to formatted string
def mock_format_time(epoch_time):
    return datetime.fromtimestamp(epoch_time).strftime('%b %d %H:%M')


# Test for basic listing without arguments
@patch('pyls.core.format_time', side_effect=mock_format_time)
def test_pyls_basic(mock_format_time, mock_structure, capfd):
    mock_file = mock_open(read_data=json.dumps(mock_structure))

    with patch('builtins.open', mock_file):
        pyls()

    captured = capfd.readouterr()
    assert "file1.txt" in captured.out
    assert "dir1" in captured.out


# Test for detailed listing
@patch('pyls.core.format_time', side_effect=mock_format_time)
def test_pyls_detailed(mock_format_time, mock_structure, capfd):
    mock_file = mock_open(read_data=json.dumps(mock_structure))

    with patch('builtins.open', mock_file):
        pyls(detailed=True)

    captured = capfd.readouterr()
    expected_output = "-rw-r--r-- 1024 Oct 01 12:50 file1.txt\ndrwxr-xr-x 4096 Oct 01 12:50 dir1\n"
    assert expected_output == captured.out


# Test for including all files (including hidden files)
@patch('pyls.core.format_time', side_effect=mock_format_time)
def test_pyls_include_all(mock_format_time, mock_structure, capfd):
    mock_file = mock_open(read_data=json.dumps(mock_structure))

    with patch('builtins.open', mock_file):
        pyls(include_all=True)

    captured = capfd.readouterr()
    assert ".hidden_file" in captured.out
    assert "file1.txt" in captured.out


# Test for reverse sorting
@patch('pyls.core.format_time', side_effect=mock_format_time)
def test_pyls_reverse(mock_format_time, mock_structure, capfd):
    mock_file = mock_open(read_data=json.dumps(mock_structure))

    with patch('builtins.open', mock_file):
        pyls(reverse=True)

    captured = capfd.readouterr()
    assert "dir1" in captured.out
    assert "file1.txt" in captured.out


# Test for filtering by file
@patch('pyls.core.format_time', side_effect=mock_format_time)
def test_pyls_filter_file(mock_format_time, mock_structure, capfd):
    mock_file = mock_open(read_data=json.dumps(mock_structure))

    with patch('builtins.open', mock_file):
        pyls(filter_option="file")

    captured = capfd.readouterr()
    assert "file1.txt" in captured.out
    # assert ".hidden_file" in captured.out
    assert "dir1" not in captured.out


# Test for filtering by directory
@patch('pyls.core.format_time', side_effect=mock_format_time)
def test_pyls_filter_dir(mock_format_time, mock_structure, capfd):
    mock_file = mock_open(read_data=json.dumps(mock_structure))

    with patch('builtins.open', mock_file):
        pyls(filter_option="dir")

    captured = capfd.readouterr()
    assert "dir1" in captured.out
    assert "file1.txt" not in captured.out


# Test for path traversal
@patch('pyls.core.format_time', side_effect=mock_format_time)
def test_pyls_path_traversal(mock_format_time, mock_structure, capfd):
    mock_file = mock_open(read_data=json.dumps(mock_structure))

    with patch('builtins.open', mock_file):
        pyls(path="dir1")

    captured = capfd.readouterr()
    assert "file2.txt" in captured.out
    assert "file1.txt" not in captured.out


# Test for invalid path
def test_pyls_invalid_path(mock_structure, capfd):
    mock_file = mock_open(read_data=json.dumps(mock_structure))

    with patch('builtins.open', mock_file):
        with pytest.raises(SystemExit):
            pyls(path="invalid_dir")

    captured = capfd.readouterr()
    assert "error: cannot access 'invalid_dir': No such file or directory" in captured.out


# Test for invalid filter
def test_pyls_invalid_filter(mock_structure, capfd):
    mock_file = mock_open(read_data=json.dumps(mock_structure))

    with patch('builtins.open', mock_file):
        pyls(filter_option="invalid_filter")

    captured = capfd.readouterr()
    assert "error: 'invalid_filter' is not a valid filter criteria." \
           " Available filters are 'dir' and 'file'" in captured.out

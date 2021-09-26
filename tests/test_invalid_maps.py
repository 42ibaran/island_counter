
import os
import stat
import pytest
from src.count_islands import load_file
from src.exceptions import FileLoadingError

def test_unauthorized_file():
    filename = "tests/maps/unauthorized.txt"
    st = os.stat(filename)
    os.chmod(filename, stat.S_IWUSR)
    with pytest.raises(FileLoadingError) as excinfo:
        load_file(filename)
    assert str(excinfo.value) == "Couldn't open map file."
    os.chmod(filename, st.st_mode)


def test_non_existent_file():
    with pytest.raises(FileLoadingError) as excinfo:
        load_file("tests/maps/NO_SUCH_FILE.txt")
    assert str(excinfo.value) == "Map file doesn't exist."


def test_empty():
    with pytest.raises(ValueError) as excinfo:
        load_file("tests/maps/empty.txt")
    assert str(excinfo.value) == "Map cannot be empty."


def test_non_numeric_value():
    with pytest.raises(ValueError) as excinfo:
        load_file("tests/maps/forbidden_char.txt")
    assert str(excinfo.value) == "Map file contains invalid characters."


def test_forbidden_number():
    with pytest.raises(ValueError) as excinfo:
        load_file("tests/maps/forbidden_int.txt")
    assert str(excinfo.value) == "Map file contains invalid characters."


def test_uneven_rows():
    with pytest.raises(ValueError) as excinfo:
        load_file("tests/maps/uneven_rows.txt")
    assert str(excinfo.value) == "Map contains uneven rows."

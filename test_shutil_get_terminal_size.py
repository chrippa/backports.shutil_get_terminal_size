import os
import sys
import subprocess

import pytest

from backports.shutil_get_terminal_size import get_terminal_size


def test_does_not_crash():
    """Check if get_terminal_size() returns a meaningful value.

    There's no easy portable way to actually check the size of the
    terminal, so let's check if it returns something sensible instead.
    """
    size = get_terminal_size()
    assert size.columns >= 0
    assert size.lines >= 0


def test_os_environ_first(monkeypatch):
    "Check if environment variables have precedence"

    monkeypatch.setenv("COLUMNS", 777)
    monkeypatch.setenv("LINES", 888)

    size = get_terminal_size()
    assert size.columns == 777
    assert size.lines == 888


@pytest.mark.skipif("not os.isatty(sys.__stdout__.fileno())", reason="not on tty")
def test_stty_match(monkeypatch):
    """Check if stty returns the same results ignoring env

    This test will fail if stdin and stdout are connected to
    different terminals with different sizes. Nevertheless, such
    situations should be pretty rare.
    """
    try:
        process = subprocess.Popen(["stty", "size"], stdout=subprocess.PIPE)
        output, err = process.communicate()
        if process.poll() != 0:
            raise OSError
        size = output.decode().split()
    except (OSError, subprocess.CalledProcessError):
        pytest.skip("stty invocation failed")

    expected = (int(size[1]), int(size[0])) # reversed order

    monkeypatch.delenv("LINES", raising=False)
    monkeypatch.delenv("COLUMNS", raising=False)
    actual = get_terminal_size()

    assert expected == actual


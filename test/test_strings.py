# Test strings.py

import pytest
import os
import sys

this_dir = os.path.dirname(__file__)
local_src_dir = os.path.join(this_dir, '..', 'src')
sys.path.append(local_src_dir)
import strings

s = "abcdefghijklmnopqrstuvwxyz"

def test_replaceAt():
    expected = "12345fghijklmnopqrstuvwxyz"
    result = strings.replaceAt(s, 0, "12345")
    assert(result == expected)

    expected = "abcdefghijklmnopqrstu12345"
    result = strings.replaceAt(s, 21, "12345")
    assert(result == expected)

    expected = "abcdefghijk12345qrstuvwxyz"
    result = strings.replaceAt(s, 11, "12345")
    assert(result == expected)

    expected = "abcdefghijklmnopqrstuvwxy12345"
    result = strings.replaceAt(s, 25, "12345")
    assert(result == expected)

    expected = "abcdefghijklmnopqrstuvwxyz12345"
    result = strings.replaceAt(s, 26, "12345")
    assert(result == expected)

"""Normalize export destination paths."""

import re

_WINDOWS_SEP = re.compile(r"\\+")


def normalize_path(raw):
    """Return `raw` with separators collapsed to a single forward slash."""
    if not isinstance(raw, str):
        raise TypeError("path must be a string")
    collapsed = _WINDOWS_SEP.sub("/", raw)
    segments = collapsed.split("/")
    root = segments[0]
    if not root:
        return "/" + "/".join([s for s in segments[1:] if s])
    return "/".join([root] + [s for s in segments[1:] if s])

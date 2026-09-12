"""Small text helpers shared by the renderer and the CLI."""

import re

ELLIPSIS = "..."
RESET = "\x1b[0m"
ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*m")


def colorize(text, code):
    """Wrap text in an SGR escape sequence."""
    return "\x1b[%dm%s%s" % (code, text, RESET)


def visible_len(text):
    """Length of text with SGR escape sequences discounted."""
    return len(ESCAPE_RE.sub("", text))


def truncate(text, width):
    """Cut text to width VISIBLE characters, adding an ellipsis when cut.

    Escape sequences are never split and never counted against the width,
    and a cut inside a coloured span re-emits the reset so the colour does
    not leak into whatever is printed next.
    """
    if width <= 0:
        return ""
    if visible_len(text) <= width:
        return text

    keep = width if width <= len(ELLIPSIS) else width - len(ELLIPSIS)
    tail = "" if width <= len(ELLIPSIS) else ELLIPSIS

    out = []
    shown = 0
    open_span = False
    pos = 0
    while pos < len(text) and shown < keep:
        match = ESCAPE_RE.match(text, pos)
        if match:
            out.append(match.group())
            open_span = match.group() != RESET
            pos = match.end()
            continue
        out.append(text[pos])
        shown += 1
        pos += 1

    out.append(tail)
    if open_span:
        out.append(RESET)
    return "".join(out)


def pad(text, width):
    """Left-justify text to width, never shortening it."""
    if len(text) >= width:
        return text
    return text + " " * (width - len(text))


def indent(block, spaces=2):
    prefix = " " * spaces
    return "\n".join(prefix + line if line else line for line in block.split("\n"))

"""Small text helpers shared by the renderer and the CLI."""

ELLIPSIS = "..."
RESET = "\x1b[0m"


def colorize(text, code):
    """Wrap text in an SGR escape sequence."""
    return "\x1b[%dm%s%s" % (code, text, RESET)


def truncate(text, width):
    """Cut text down to width characters, adding an ellipsis when cut."""
    if width <= 0:
        return ""
    if len(text) <= width:
        return text
    if width <= len(ELLIPSIS):
        return text[:width]
    return text[: width - len(ELLIPSIS)] + ELLIPSIS


def pad(text, width):
    """Left-justify text to width, never shortening it."""
    if len(text) >= width:
        return text
    return text + " " * (width - len(text))


def indent(block, spaces=2):
    prefix = " " * spaces
    return "\n".join(prefix + line if line else line for line in block.split("\n"))

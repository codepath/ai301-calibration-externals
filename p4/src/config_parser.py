"""Read a pathreview run configuration out of a plain dict.

The config arrives already deserialised (TOML, JSON, or a literal dict from
the test suite). Everything in here is pure: no file IO, no environment.
"""

DEFAULT_TIMEOUT = 30
DEFAULT_WORKERS = 4
VALID_MODES = ("strict", "lenient")


class ConfigError(ValueError):
    """Raised when a config value is present but unusable."""


def _as_int(name, value):
    try:
        return int(value)
    except (TypeError, ValueError):
        raise ConfigError("%s must be a whole number, got %r" % (name, value))


def _mode(raw):
    mode = raw.get("mode", "strict")
    if mode not in VALID_MODES:
        raise ConfigError(
            "mode must be one of %s, got %r" % (", ".join(VALID_MODES), mode)
        )
    return mode


def _sources(raw):
    sources = raw.get("sources") or []
    if isinstance(sources, str):
        sources = [sources]
    cleaned = []
    for entry in sources:
        entry = str(entry).strip()
        if entry:
            cleaned.append(entry)
    return cleaned


def parse_config(raw):
    """Turn a raw config mapping into the dict the runner consumes."""
    if not isinstance(raw, dict):
        raise ConfigError("config must be a mapping, got %r" % type(raw).__name__)

    timeout = _as_int("timeout", raw.get("timeout", DEFAULT_TIMEOUT))
    workers = _as_int("workers", raw.get("workers", DEFAULT_WORKERS))

    if timeout <= 0:
        raise ConfigError("timeout must be positive, got %d" % timeout)
    if workers <= 0:
        raise ConfigError("workers must be positive, got %d" % workers)

    return {
        "timeout": timeout,
        "workers": workers,
        "mode": _mode(raw),
        "sources": _sources(raw),
        "label": str(raw.get("label", "")).strip(),
    }


def describe(config):
    """One human-readable line summarising a parsed config."""
    return "%s mode, %d worker(s), %ds timeout, %d source(s)" % (
        config["mode"],
        config["workers"],
        config["timeout"],
        len(config["sources"]),
    )

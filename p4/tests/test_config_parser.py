import pytest

from p4.src.config_parser import ConfigError, describe, parse_config


def test_explicit_values_survive():
    config = parse_config({"timeout": 15, "workers": 2, "mode": "lenient"})
    assert config["timeout"] == 15
    assert config["workers"] == 2
    assert config["mode"] == "lenient"


def test_workers_default_when_absent():
    config = parse_config({"timeout": 5})
    assert config["workers"] == 4


def test_sources_are_cleaned():
    config = parse_config({"timeout": 5, "sources": [" a ", "", "b"]})
    assert config["sources"] == ["a", "b"]


def test_single_source_string_becomes_a_list():
    config = parse_config({"timeout": 5, "sources": "only"})
    assert config["sources"] == ["only"]


def test_bad_mode_is_rejected():
    with pytest.raises(ConfigError):
        parse_config({"timeout": 5, "mode": "nope"})


def test_non_positive_timeout_is_rejected():
    with pytest.raises(ConfigError):
        parse_config({"timeout": 0})


def test_describe_reads_as_one_line():
    config = parse_config({"timeout": 5, "workers": 1})
    assert describe(config) == "strict mode, 1 worker(s), 5s timeout, 0 source(s)"

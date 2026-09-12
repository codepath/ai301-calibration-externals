"""Command line entry point for the pathreview demo runner."""

import argparse
import sys

from .config_parser import parse_config, describe
from .report import render

BANNER = "pathreview demo runner"
VERSION = "0.4.1"


def build_parser():
    parser = argparse.ArgumentParser(prog="pathreview", description=BANNER)
    parser.add_argument("--timeout", type=int, default=None)
    parser.add_argument("--workers", type=int, default=None)
    parser.add_argument("--mode", default=None, choices=("strict", "lenient"))
    parser.add_argument("--quiet", action="store_true",
                        help="suppress the banner and the config summary")
    parser.add_argument("--version", action="store_true")
    return parser


def _raw_from_args(args):
    raw = {}
    if args.timeout is not None:
        raw["timeout"] = args.timeout
    if args.workers is not None:
        raw["workers"] = args.workers
    if args.mode is not None:
        raw["mode"] = args.mode
    return raw


def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.version:
        print(VERSION)
        return 0

    print(BANNER)

    config = parse_config(_raw_from_args(args))
    print(describe(config))

    rows = [
        {"item": "pkg-01", "status": "ok", "note": "nothing to report"},
        {"item": "pkg-02", "status": "fail", "note": "held by the noise floor"},
    ]
    print(render(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())

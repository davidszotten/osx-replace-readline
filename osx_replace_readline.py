#! /usr/bin/env python

from __future__ import print_function

from contextlib import contextmanager

import argparse
import os
import shutil
from subprocess import check_output
import tempfile


def setup_argparse():
    parser = argparse.ArgumentParser(
        description='Replace system readline with one from pypi/readline')
    parser.add_argument(
        'python_binary', help='Path to global python binary to fix')
    return parser


def parse_cmdline():
    parser = setup_argparse()
    args = parser.parse_args()
    return args


@contextmanager
def tempdir():
    path = tempfile.mkdtemp(suffix='osx_replace_readline')
    try:
        yield path
    finally:
        shutil.rmtree(path)


def make_virtualenv(python, path):
    check_output(['virtualenv', '--python', python, path])

    python_path = os.path.join(path, 'bin', 'python')
    pip_path = os.path.join(path, 'bin', 'pip')

    return python_path, pip_path


def replace_readline(python_path, pip_path):
    print_readline_cmd = '; '.join([
        'import os',
        'import readline',
        'print (os.path.realpath(readline.__file__))',
    ])

    original_readline = check_output(
        [python_path, '-c', print_readline_cmd]
    ).splitlines()[0]
    os.rename(original_readline, '{}.original'.format(original_readline))

    check_output([pip_path, 'install', 'readline'])
    new_readline = check_output(
        [python_path, '-c', print_readline_cmd]
    ).splitlines()[0]

    os.rename(new_readline, original_readline)


def main():
    args = parse_cmdline()
    with tempdir() as path:
        python, pip = make_virtualenv(args.python_binary, path)
        replace_readline(python, pip)


if __name__ == '__main__':
    main()

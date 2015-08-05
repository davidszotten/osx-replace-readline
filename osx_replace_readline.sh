#! /usr/bin/env bash

set -o nounset
set -o errexit

if [ -z "${1:-}" ]
then
    echo "Usage: $0 global_python_binary"
    exit 1
fi

PYTHON=$1

mktmpenv -p "$PYTHON"
ORIG=$(python -c 'import os; import readline; print (os.path.realpath(readline.__file__))')
pip install readline

mv "$ORIG" "$ORIG".original
NEW=$(python -c 'import os; import readline; print (os.path.realpath(readline.__file__))')
mv "$NEW" "$ORIG"

deactivate

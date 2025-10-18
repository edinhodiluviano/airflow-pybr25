#!/bin/bash


set -e


# creates a python virtual enviroment in current folder

echo "== Virtual env tool =="

if [ ! -d .venv ]; then
    echo "Creating virtual enviroment - python3.13"
    python3.13 -m venv .venv
    
    echo "Creating shortcut to activate"
    ln -s .venv/bin/activate activate || echo "Activate already exists"
fi

echo "Upgrading pip"
source activate && pip install --upgrade pip

echo "Installing wheel"
pip install --upgrade wheel


echo 'Checking activate'
if [ -d .venv ]; then
    INST='
if [ -f "$VIRTUAL_ENV/../.env" ] ; then
    while IFS= read -r line; do
        if [ ! -z "$line" ] ; then
            if [[ ! "$line" == \#* ]] ; then
                export "$line"
            fi
        fi
    done < "$VIRTUAL_ENV/../.env"
fi
'
    if ! grep -q 'export "$line"' activate; then
        echo "Adding .env to activate"
        echo "$INST" >> activate
    fi
fi

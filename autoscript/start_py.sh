#!bin/bash

cd ../back/
PATH_ORIGIN=$(pwd)

set -Ux PYENV_ROOT $HOME/.pyenv
set -Ux PATH $PYENV_ROOT/bin $PATH
status --is-interactive; and . (pyenv init --path | psub)
status --is-interactive; and . (pyenv init - | psub)
source ~/.config/fish/config.fish

pyenv global 3.12.3
python3 --version
source env/bin/activate.fish

cd "$PATH_ORIGIN"

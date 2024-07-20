#!bin/bash

cd ../back/

set -Ux PYENV_ROOT $HOME/.pyenv
set -Ux PATH $PYENV_ROOT/bin $PATH
status --is-interactive; and . (pyenv init --path | psub)
status --is-interactive; and . (pyenv init - | psub)
source ~/.config/fish/config.fish
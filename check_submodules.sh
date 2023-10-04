#!/bin/bash

# Loop through all submodule paths that match the pattern '*JAVAS*'
for submodule_path in $(git config --file .gitmodules --get-regexp path | awk '{ print $2 }' | grep '*JAVASCRIPT*'); do
    echo "Submodule Status for $submodule_path:"
    git submodule status "$submodule_path"
done



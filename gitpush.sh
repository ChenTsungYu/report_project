#!/bin/bash
git add .
read -p "Please input your git commit: " commit
echo "Your commit is '${commit}'"
git commit -m "${commit}"
echo "finish committing!"
git push
echo "Done!"
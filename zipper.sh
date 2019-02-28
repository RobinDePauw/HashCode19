#!/bin/bash
set -xe
git pull
git add *
git commit -m "$1"
git push
COMMIT = $(git log -n 1 --pretty=format:"%H")
TIME = $(date +%s)
NAME = $TIME_$COMMIT
zip $NAME src/*

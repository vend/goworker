#!/bin/bash
git config --global url."git@github.com:".insteadOf "https://github.com/"
go get github.com/Masterminds/glide
glide init
glide install -s -v
#!/bin/sh

cd ../models
rm -rf .*
antlr4 -Dlanguage=Python3 -listener -visitor Syl.g4

cd ../src/
find ./../models -type f -name 'Syl*' -exec ln -s {} ./ \;
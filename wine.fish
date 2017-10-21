#!/usr/local/bin/fish

set dir (pwd)

set args $argv[1..-1]

if test $dir = "/home/greg/Wine/refactor"
    echo "working from test wine"
    command /home/greg/Wine/refactor/Wine.py $args
else
    command /home/greg/Wine/Wine.py $args
end

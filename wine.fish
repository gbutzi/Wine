#!/usr/local/bin/fish

set dir (pwd)

set args (getopt -s sh abc: $argv);

if dir == "/home/greg/Wine/refactor"
    (./home/greg/Wine/refactor/Wine.py args)
else
    (./home/greg/Wine/Wine.py args)  
end

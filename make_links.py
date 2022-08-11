"""
As a Reaper user well-versed in git and version control,
I want a way for Reaper config changes to be reflected in my repository from DAW edits.
"""
import logging
import json
import sys
from pathlib import Path
from subprocess import run

def make_links(fp):
    """
    Creates hard symlinks from the config files in Reaper we care about into the repo.
    """
    with open(Path(fp).absolute(), 'r') as f:
        config_map = json.load(f)

if __name__ == '__main__':
    map_path = './reaperFiles.json'
    try:
        map_path = sys.argv[1]
    except IndexError:
        pass
    make_links(map_path)
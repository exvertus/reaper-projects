"""
Use hardlinks to ensure Reaper config changes are reflected in repository from DAW edits.
"""
import logging
import json
import os
import sys
from pathlib import Path
from subprocess import run

logging.basicConfig(level=logging.DEBUG)

def make_links(fp):
    """
    Creates hard symlinks from the config files in Reaper we care about into the repo.
    """
    with open(Path(fp).absolute(), 'r') as f:
        config_map = json.load(f)
    link_root = os.path.expandvars(config_map['repoPath'])
    target_root = os.path.expandvars(config_map['reaperPath'])
    for repo_f, reaper_f in config_map['fileMap'].items():
        link = Path(link_root, repo_f)
        target = Path(target_root, reaper_f)
        logging.info(f"Linking {link} to {target}...")
        link.hardlink_to(target)
    logging.info(f"Linked {len(config_map['fileMap'])} files.")

if __name__ == '__main__':
    map_path = './reaperFiles.json'
    try:
        map_path = sys.argv[1]
    except IndexError:
        pass
    make_links(map_path)
"""
Keep settings and config synced with files in repo.
"""
import logging
import json
import os
import shutil
import sys
from pathlib import Path
from subprocess import run
from stat import S_IREAD, S_IWRITE

logging.basicConfig(level=logging.DEBUG)

def readonly_handler(function, path, execinfo):
    """
    Remove read-only permission from file.
    """
    path_obj = Path(path)
    if execinfo[0] is PermissionError:
        path_obj.chmod(S_IWRITE)
        path_obj.unlink()

def copy_readonlys(fp):
    """
    Creates read-only copies of reaper config files.
    """
    with open(Path(fp).absolute(), 'r') as f:
        config_map = json.load(f)
    copy_from = Path(os.path.expandvars(config_map['reaperPath']))
    copy_to = Path(os.path.expandvars(config_map['repoPath']), 'configs')
    if copy_to.exists():
        shutil.rmtree(copy_to, onerror=readonly_handler)
    copy_to.mkdir()
    for name, repo_file in config_map['fileMap'].items():
        source = Path(copy_from, repo_file)
        destination = Path(copy_to, name)
        shutil.copy(source, destination)
        destination.chmod(S_IREAD)
        logging.info(f"Copied {source} to {destination}...")
    logging.info(f"Copied {len(config_map['fileMap'])} files.")

if __name__ == '__main__':
    map_path = './reaperFiles.json'
    try:
        map_path = sys.argv[1]
    except IndexError:
        pass
    copy_readonlys(map_path)

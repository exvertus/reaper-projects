# Reaper Projects

Tracking DAW-work in version control with Reaper's human-readable files.
Bigger data files like audio clips tracked by git lfs.

In addition to song projects, this tracks...

- reaper-settings
- default project settings
- templates
- patches

#### Setup locally

1. Set environment variables:
  1. `REAPER_REPO_PATH` root path of this repo's local checkout
  1. `REAPER_INSTALL_PATH` path to reaper.exe, reaper.ini, etc after using *portable* install (this repo is un-tested on normal install)
  1. On windows, make sure the paths are on the same drive, or `mklink /H` will fail 
1. Open Reaper and set to following configuration settings:
  - 
1. Run `py3 make_link.py reaperFiles.json` to sync config files via symlinks
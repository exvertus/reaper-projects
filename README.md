# Reaper Projects

This is an attempt to capture all DAW-work in version control using Reaper's human-readable files.
Bigger data files like audio and video clips are tracked by git lfs.

In addition to song projects, the goal is to track...

- reaper-settings
- default project settings
- templates
- patches

...in an automation fashion.

Note: I am currently assuming a Windows environment with this because it meets my personal requirements,
but will keep things ready for future platform-neutrality.

#### Setup

1. Download [Git LFS](https://git-lfs.github.com/) and install it.
1. Fork this repo and clone the fork.
1. For each machine/environment, setup the following:
  1. Set environment variables:
    1. `REAPER_REPO_PATH` root path of this repo's local checkout
    1. `REAPER_INSTALL_PATH` path to reaper.exe, reaper.ini, etc after using *portable* install (this repo is un-tested on normal install)
    1. Make sure the paths are on the same drive, or `mklink /h` will fail 
  1. Open Reaper and set to following configuration settings:
    1. `General/Paths >`
      1. `Default path to save new projects=%REAPER_REPO_PATH%\git\reaper-projects\projects`
      1. `Default recording path, when project is unsaved and no recording path is configured=%REAPER_REPO_PATH%\git\reaper-projects\projects\new`
  1. Run `python make_links.py reaperFiles.json` to sync config files via hardlinks.

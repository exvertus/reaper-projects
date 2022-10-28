# Reaper Projects

This is an attempt to capture all DAW-work in version control using Reaper's human-readable files.
Bigger data files like audio and video clips are tracked by git lfs.

In addition to song projects, the goal is to track...

- reaper-settings
- default project settings
- templates
- patches

Note: Only currently tested on Windows.

#### Setup

* Download [Git LFS](https://git-lfs.github.com/) and install it.
* Fork this repo and clone the fork.
* For each machine/environment: 

  1. Set REAPER preferences:
      * General
        * Paths
          * *Default path to save new projects*: `%REAPER_REPO_PATH%\git\reaper-projects\projects`
          * *Default recording path, when project is unsaved and no recording path is configured*: `%REAPER_REPO_PATH%\git\reaper-projects\projects\new`
          * Check *Save undo history with project files (in .RPP-UNDO file)* and *Allow load of undo history*
      * Project
        * Check *Prompt to save on new project*, *Look for project media items in project directory before qualified path* and *Save project file references with relative pathnames*
        * Uncheck *When overwriting project file, rename old project to .rpp-bak*, *Save to timestamped file in project directory*, and *Save undo history (RPP-UNDO)* (use repo as backup/back-in-time feature)
      * Media
        * Import
          * Check *Copy imported media to project media directory*
  1. Set environment variables:
    1. `REAPER_REPO_PATH` root path of this repo's local checkout
    1. `REAPER_INSTALL_PATH` path to reaper.exe, reaper.ini, etc after using *portable* install (this repo is un-tested on normal install)
  1. Run `python sync_config.py reaperFiles.json` to sync config files via hardlinks. 
    * TODO: Add sync_config call to an on_save hook in Reaper.

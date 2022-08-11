@ECHO OFF
:: Map hardlinks to from reaper to repo folder. 
SET reaperPath=%1
SET repoPath=%2
SET linkedFiles="reaper.ini"
SET linkedFiles=%linkedFiles%;"reaper-install-rev.txt"
SET linkedFiles=%linkedFiles%;"reaper-mouse.ini"
SET linkedFiles=%linkedFiles%;"reaper-vstplugins64.ini"
SET linkedFiles=%linkedFiles%;"reaper-vstshells64.ini"
FOR %%f in (%linkedFiles%) do (
    ECHO Creating symlink for %f%
    mklink /H %reaperPath%/%f% %repoPath%/%f%
)
ECHO Done.
PAUSE
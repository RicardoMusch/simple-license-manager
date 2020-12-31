# simple-license-manager
 Simple License Manager application to manage file based or env variable based licenses


# Usage


## Check for available licenses in the license repo
Check the repo for available license files, displays a list of used and unused licenses in the specified repo.

    slm.py -check -licenserepo:"PATH/TO/LICENSE/FILES"

## Reset all licenses in the license repo
When a license is in use the file will be renamed to .inuse.hostname
This command will reset all files in the license repository to their original name and therefore "clear" them from being in use.

    slm.py -reset -licenserepo:"PATH/TO/LICENSE/FILES"

## Get a license from the repo and start the application
This will automatically reset the license after the application closes.

    slm.py -check -licenserepo:"PATH/TO/LICENSE/FILES"


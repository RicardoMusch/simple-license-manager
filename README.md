# simple-license-manager
 Simple License Manager application to manage file based or env variable based licenses

# Aim
Some software like Substance Painter gives out individual license files when buying multiple licences.
(Floating licenses/site licences are available but expensive if you only need a few)

Such software usually requires a ENV variable to point to the license file.
i.e.

SUBSTANCE_PAINTER_LICENSE = "path/to/substance/license.key"

To aid in using multiple licenses in a studio environement I created slm.
It's a simple command line tool to aid in file based license key management.

# Requirements
- A Network folder to use as license repository
- License files
- A launcher or batch script to launch the software needing a license key file so that slm can be used to get a license key file and set up the environement prior to starting the application
- Python v2.7+ or 3.6+

# Usage

## Licenserepo
A license repository is simply a folder with license files inside it.
These could be .lic files or any other types of files.

## Check for available licenses in the license repo
Check the repo for available license files, displays a list of used and unused licenses in the specified repo.

    slm.py -check -licenserepo:"PATH/TO/LICENSE/FILES"

## Reset all licenses in the license repo
When a license is in use the file will be renamed to .inuse.hostname
This command will reset all files in the license repository to their original name and therefore "clear" them from being in use.

    slm.py -reset -licenserepo:"PATH/TO/LICENSE/FILES"

## Get a license from the repo and start the application
Attempts to get a license from the license repository, then sets the specified env var to the license path, starts the executable and waits for it to exit.
After exitting the application the license will be "returned" automatically.
If a license is already in use by the current computer (i.e. we start the aplication multiple times) the subsequent application starts will consume the existing license and the original session that got the license will be the one to return the license.

* A feature to look into is to scan the running exectutables and only return the license if the current session is the last running.

    slm.py -get -licenserepo:"PATH/TO/LICENSE/FILES" -env:ENVIRONEMENT_VAR_NAME -exe:"PATH/TO/APPLICATION/EXECUTABLE.exe"


## Example output

    ###########################################
    SIMPLE LICENSE MANAGER
    ###########################################

    Requesting a license...
    -------------------------------------------
    Got a license!
    Starting application...
    Detected application close, returning license...

    Resetting licence(s)...
    -------------------------------------------
    Resetting license: Substance_Painter_lic1.inuse.hostname.key

    DONE!...
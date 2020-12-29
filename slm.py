"""
Simple License Manager application

Usage:

# Request a license and point the var to it
python -m slm.py -env SUBSTANCE_PAINTER_LICENSE -licenserepo:%license_repo% -exe "c:/program files/substance/painter/painter.exe" -args "-arg1 -arg2"

# Check the available licenses and which are in use
python -m slm.py -env SUBSTANCE_PAINTER_LICENSE -licenserepo:%license_repo%

"""
import sys
import os
import socket


def main():

    _header()
    
    if _get_argv("check"):
        # check for licenses
        check_licenses()

    if _get_argv("reset"):
        # Reset all licenses
        reset_licenses()

    if _get_argv("get"):
        # get a license
        get_license()

def get_license():
    "Get's a license from the license pool if one is available, renames the license and tags it with the hostname, then set's the env variable"

    env = _get_argv("env")
    licenserepo = _get_argv("licenserepo")

    free_lic_list = []
    for lic in os.listdir(licenserepo):
        if not ".inuse" in lic:
            free_lic_list.append(lic)

    if free_lic_list == []:
        _div()
        print("NO FREE LICENSES AVAILABLE")
        print(" ")
        print("Use -check to check which machines have taken a license or -reset to reset all licenses.")
        print(" ")
        input("Press enter to exit...")
        sys.exit(1)

    else:
        print("Requesting a license...")
        lic = free_lic_list[0]
        ext = None
        if "." in lic:
            ext = lic.split(".")[-1]

        # rename lic file to .inuse.hostname
        lic_path = os.path.join(licenserepo, lic)

        if ext:
            rlic = lic.split("."+ext)[0]
            rlic = rlic+".inuse."+_get_hostname()+"."+ext
        else:
            rlic = lic+".inuse."+_get_hostname()
        rlic_path = os.path.join(licenserepo, rlic)

        # rename
        os.rename(lic_path, rlic_path)

        # set env to rlic path
        os.environ[env] = rlic_path

        print("Got a license!")
        print("Starting application...")   

def check_licenses():
    "Check's the license repo for available licenses and in use licenses"

    env = _get_argv("env")
    licenserepo = _get_argv("licenserepo")

    _div()
    print("Licenses in use:")
    _paddedLine()
    for lic in os.listdir(licenserepo):
        if ".inuse" in lic:
            print(lic)

    _div()
    print("Licenses not in use:")
    _paddedLine()
    for lic in os.listdir(licenserepo):
        if not ".inuse" in lic:
            print(lic)

def reset_licenses():
    "Resets all licenses in the license repo so they can be picked up again..."

    env = _get_argv("env")
    licenserepo = _get_argv("licenserepo")

    lic_list = []
    for lic in os.listdir(licenserepo):
        if ".inuse" in lic:
            print("Resetting license: {}".format(lic))
            lic_path = os.path.join(licenserepo, lic)

            ext = lic.split(".")[-1]
            rlic = lic.split(".inuse")[0]
            rlic = rlic+"."+ext
            rlic_path = os.path.join(licenserepo, rlic)

            os.rename(lic_path, rlic_path)

    print(" ")
    print("DONE!...")  


# Helper functions _

def _div():
    print(" ")
    _paddedLine()

def _paddedLine():
    print("###########################################")

def _header():
    _div()
    print("SIMPLE LICENSE MANAGER")
    _paddedLine()
    print(" ")

def _get_argv(argv):
    "Get's a argument from the command line args"
    args = sys.argv

    for arg in args:
        if argv in arg.lower():
            try:
                return arg.split("-"+argv+":")[1]
            except:
                return True
    return None

def _get_hostname():
    return socket.gethostname()







if __name__ == "__main__":
    main()



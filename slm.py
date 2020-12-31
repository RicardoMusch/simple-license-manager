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
from os import system
import socket


def main():

    os.system("cls")
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
    "Main functionality called by the -get argument"

    # If no licenses are free, tell user and exit
    if get_free_license_list() == []:
        _div()
        print("NO FREE LICENSES AVAILABLE")
        print(" ")
        print("Use -check to check which machines have taken a license or -reset to reset all licenses.")
        print(" ")
        input("Press enter to exit...")
        sys.exit(1)

    else:
        request_license()

def request_license():
    """
    The actual process of requesting a license file, renaming it, pointing the env var to it 
    and launching the application, waiting for it's exit and then resetting the lic.
    """
    licenserepo = _get_argv("licenserepo").replace("\\", "/")

    print("Requesting a license...")
    _dashingLine()

    # check if a used license with current hostname may exist
    used_hostname_lic = check_if_hostname_in_use()
    if used_hostname_lic:
        print("Found a used license for this computer, using the same license instead...")
        use_license(used_hostname_lic)
        
        # set a lock environ so this session wont rename the lic back but ethe original will do that
        os.environ["SLM_MULTIPLE_SESSIONS"] = "True"

    else:
        lic = get_free_license_list()[0]
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

        # use license and start app
        use_license(rlic_path)

def use_license(license_path):
    "Uses the license file specified, sets the env, calls and waits for the application, then resets the license after closing"
    env = _get_argv("env")
    exe = _get_argv("exe")
    args = _get_argv("args")
    
    # set env to rlic path
    os.environ[env] = license_path
    print("Got a license!")
    print("Starting application...")   
    os.system(r'"'+exe+'"')

    if not "SLM_MULTIPLE_SESSIONS" in os.environ:
        # After application closes, reset the license so it's not in use
        print("Detected application close, returning license...")
        reset_licenses(os.path.basename(license_path))
    else:
        print("Not resetting license as multiple sessions are running...")

def check_licenses():
    "Check's the license repo for available licenses and in use licenses"
    env = _get_argv("env")
    licenserepo = _get_argv("licenserepo")

    print("Licenses in use:")
    _dashingLine()
    lics = False
    for lic in os.listdir(licenserepo):
        if ".inuse" in lic:
            print(lic)
            lics = True
    if not lics:
        print("- None")

    print(" ")
    print("Licenses not in use:")
    _dashingLine()
    for lic in os.listdir(licenserepo):
        if not ".inuse" in lic:
            print(lic)

def reset_licenses(license_name=None):
    "Resets a specific license or all licenses in the license repo so they can be picked up again..."
    licenserepo = _get_argv("licenserepo")    

    print(" ")
    print("Resetting licence(s)...")  
    _dashingLine()
    for lic in os.listdir(licenserepo):
        if ".inuse" in lic:

            def reset_lic():
                print("Resetting license: {}".format(lic))
                lic_path = os.path.join(licenserepo, lic)

                ext = lic.split(".")[-1]
                rlic = lic.split(".inuse")[0]
                rlic = rlic+"."+ext
                rlic_path = os.path.join(licenserepo, rlic)

                os.rename(lic_path, rlic_path)

            if license_name:
                # only reset license_name
                if lic.lower() == license_name.lower():
                    reset_lic()
            else:
                # Reset every license
                reset_lic()

    print(" ")
    print("DONE!...")  

def check_if_hostname_in_use():
    "Returns either a path to a license file that has the current hostname in it so we can reuse it, else returns False"
    licenserepo = _get_argv("licenserepo").replace("\\", "/")
    hostname = _get_hostname()
    # check if we are already using a lic with this hostname, then choose that
    for lic in os.listdir(licenserepo):
        if hostname in lic:
            lic_path = os.path.join(licenserepo, lic).replace("\\", "/")
            return lic_path
    return False                

def get_free_license_list():
    "Returns a list of free license files in the licenserepo or an empty list if none are available"
    licenserepo = _get_argv("licenserepo").replace("\\", "/")
    free_lic_list = []
    for lic in os.listdir(licenserepo):
        if not ".inuse" in lic:
            free_lic_list.append(lic)
    return free_lic_list


# Helper functions _

def _div():
    print(" ")
    _paddedLine()

def _paddedLine():
    print("###########################################")

def _dashingLine():
    print("-------------------------------------------")

def _header():
    system("TITLE SIMPLE LICENSE MANAGER")
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



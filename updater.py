from sys import exit as sys_exit
from os import path

from src.Utilities.os_checker import check_os
from src.Utilities.git_checker import check_git_on_device
from src.Utilities.git_downloader import openBrowser


UPDATER_VER = "0.0.0"
OS_TYPE = check_os()
GIT_STATUS = check_git_on_device()
GIT_DOWNLOAD_PAGE = "http://git-scm.com/"
USER_FOLDER = path.expanduser("~")

print("""
    VIM updater version: {updater_version}
    OS: {os_type}
    Git status: {git_status}
""".format(updater_version=UPDATER_VER,
           os_type=OS_TYPE,
           git_status=GIT_STATUS))

if str(GIT_STATUS).count("git version") != 1:
    openBrowser(GIT_DOWNLOAD_PAGE)
    sys_exit(0)

if path.isdir(USER_FOLDER) and path.exists(USER_FOLDER + "/.vim_updater"):
    print("work folder and updater dir  here, check vim src folder")
elif path.isdir(USER_FOLDER) and not path.exists(USER_FOLDER + ".vim_updater"):
    print("work folder here, create updater dir and vim src folder")
else:
    print(f"{'error with user folder:'} {USER_FOLDER}")


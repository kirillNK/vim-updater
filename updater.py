from sys import exit as sys_exit
from os import path
from os import mkdir

from src.Utilities.os_checker import check_os
from src.Utilities.git_checker import check_git_on_device
from src.Utilities.git_downloader import openBrowser

UPDATER_VER = "0.0.0"
OS_TYPE = check_os()
GIT_STATUS = check_git_on_device()
GIT_DOWNLOAD_PAGE = "http://git-scm.com/"
USER_FOLDER = path.expanduser("~")
UPDATER_DIR = "/.vim_updater"
VIM_FOLDER = "/vim"

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

if path.isdir(USER_FOLDER) and path.exists(USER_FOLDER + UPDATER_DIR):
    print("work folder and updater dir here, check vim src folder")
    if path.exists(USER_FOLDER + UPDATER_DIR + VIM_FOLDER):
        print("vim folder here")
        print("cd vim & start git clone")
    else:
        print("start git clone")

elif path.isdir(USER_FOLDER) and not path.exists(USER_FOLDER + UPDATER_DIR):
    print("can't find work folder")
    print("try to create updater dir")
    try:
        mkdir(USER_FOLDER + UPDATER_DIR)
        print("Directory {user_folder}{updater_dir} successfully created".format(user_folder=USER_FOLDER,
                                                                                 updater_dir=UPDATER_DIR))
    except FileExistsError:
        print("Directory {user_folder}{updater_dir} already exists".format(user_folder=USER_FOLDER,
                                                                           updater_dir=UPDATER_DIR))
        sys_exit(1)

    print("start git clone")

else:
    print("error with user folder: {user_folder}".format(user_folder=USER_FOLDER))
    sys_exit(1)
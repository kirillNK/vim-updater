import subprocess
from os import path
from sys import exit as sys_exit


def check_current_vim_version_in_system():
    print("current vim version in system")
    command = "vim --version"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []

    for line in proc.stdout:
        if b"VIM - Vi IMproved" in line:
            stdout.append(line)
        if b"Included patches" in line:
            stdout.append(line)
    return "".join(map(bytes.decode, stdout))


def check_current_vim_version_in_src_folder(path_to_vim_folder):
    print("current vim version in src folder")
    # TODO: add 'not' to statement
    # if path.isdir(path_to_vim_folder, flag):
    if not path.isdir(path_to_vim_folder):
        sys_exit(1)

    included_patch_output = ""
    try:
        first_version_in_file_flag = False
        with open(path_to_vim_folder + "/src/version.c", "r") as src_version:
            for line in src_version:
                if line.find("static int included_patches[]") != -1:
                    first_version_in_file_flag = True
                if first_version_in_file_flag:
                    if line.find(",") != -1:
                        first_version_in_file_flag = False
                        included_patch_output += line
        return included_patch_output.strip().strip(",")
    except FileNotFoundError:
        print("error")
        sys_exit(1)

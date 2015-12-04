import os, sys, subprocess

def git(repo, args):
    home = os.getenv("HOME")
    git_dir = os.path.join(home,
                           ".config",
                           "homer",
                           repo)
    os.putenv("GIT_DIR", git_dir)
    if not os.path.exists(git_dir):
        os.system("git init --bare %s" % git_dir)
        os.system("git config --local core.bare false")
    os.putenv("GIT_WORK_TREE", home)
    if args:
        subprocess.call(["git"] + args)

def main():
    git(sys.argv[1], sys.argv[2:])

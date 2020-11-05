import subprocess
import os

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

with cd('/media/shaheem/Data/Projects/PycharmProjects/djangoProject/slum-segmentation/slums'):
    list_files = subprocess.run(["python", "testing.py"])
    print("The exit code was: %d" % list_files.returncode)

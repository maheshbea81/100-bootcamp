import glob
import os

search_dir = "C:\Code\Pycharm\pythonProject\cohort6\*.py"

for file in glob.glob(search_dir):
    size = os.path.getsize(file)
    print(file, size, "bytes")

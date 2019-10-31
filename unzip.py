# unzip archives with names like pybites_bite[%NUMBER%].zip to folders with names like [%NUMBER%]
# for supporting submit solution to https://codechalleng.es/bites/ through github repository
# TODO: extract title by requests by regex re.search(r"Bite ([0-9]{1-3}.*?)</title>", str(r.content))
import glob
import re
import os
import zipfile
files_to_unzip = []
files_unzipped = []
for file in glob.glob("*.zip"):
    print(file)
    result = re.search(r".*?([0-9]{1,3})\.zip", file)
    if result:
        files_to_unzip.append(file)
        num = result.group(1)
        if os.path.exists(num):
            continue
        with zipfile.ZipFile(file) as zip_file:
            zip_file.extractall(num)
        files_unzipped.append(file)
        files_to_unzip.remove(file)
        os.remove(file)

if files_unzipped:
    print("Unzipped:\n", files_unzipped)
if files_to_unzip:
    print("Not unzipped, because folders exists:\n", files_to_unzip)

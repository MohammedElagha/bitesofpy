# author: @Flash (https://github.com/etoFlash)
# TODO: 1) extract title, level and tags by requests by regex from codechalleng.es (example:
#  re.search(r"Bite ([0-9]{1-3}.*?)</title>", str(r.content))
# TODO: 2) add info about bite to solved_bites.md
# TODO: 3) add to top in py-file in new folder comment "# TODO: beat it" for made more easy search not solved bites
import glob
import re
import os
import zipfile
files_to_unzip = []
files_unzipped = []
unzip_errors = []
num = 0
bite_page = f"https://codechalleng.es/bites/{num}"
filename_pattern = r".*?([0-9]{1,3})\.zip"
title_pattern = r"Bite ([0-9]{1-3}.*?)</title>"
tag_pattern = r"<a class=\"tag\" href=\"(.*?)\">(.*?)</a>"
level_pattern = r"<img class=\"biteImg\" src=\".*?\" alt=\"(.*?) level\">"

for file in glob.glob("*.zip"):
    result = re.search(filename_pattern, file)
    if result:
        files_to_unzip.append(file)
        num = result.group(1)
        if os.path.exists(num):
            unzip_errors.append("folder exists")
            continue
        with zipfile.ZipFile(file) as zip_file:
            zip_file.extractall(num)
        files_unzipped.append(file)
        files_to_unzip.remove(file)
        os.remove(file)

if files_unzipped:
    print("Unzipped:")
    for file in files_unzipped:
        print(f" {file}")
if files_to_unzip:
    print("Not unzipped (file - reason):")
    for file, reason in zip(files_to_unzip, unzip_errors):
        print(f" {file} - {reason}")
if not (files_unzipped or files_to_unzip):
    print("Nothing to process")

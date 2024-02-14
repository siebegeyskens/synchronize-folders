import time  # Importing time for time operations, built in module

# MANUAL LOOP
#
# Get list of files in source and replica folders
# For every file in the source folder
#   If the file exist in the replica folder
#       If so, compare the files, is the file the same?
#           If so, oké
#           If not, remove file and copy new file
#       If not, copy new file

# USING Filecmp
#
# https://geekpython.in/filecmp-module-in-python
# The dircmp class allow to generate a report object comparing two directories
# https://docs.python.org/3/library/filecmp.html#filecmp.dircmp
# 
# Generate a comparison object (fircmp) which allows to compare directories
# Find files to copy or overwrite: 
# The left only attribute returns a list of files that are only present in the source folder (left folder)
# The different files attribute returns a list of filenames that exist in both directories but have different contents.

sync_periond = 5 # (in seconds)
# Loop to continuously synchronize folders at a specified time interval
while True:
    # TODO: compare folders with filecmp (find all files that are new or alterd)
    # TODO: copy all the altered and new files from source to replica
    print("Synched up!");
    time.sleep(sync_periond) # Sleep for specified time interval

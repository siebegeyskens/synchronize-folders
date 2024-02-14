import time  # Importing time for time operations, built in module
import filecmp # To compare files and directories
import shutil # For high-level file operations
import os 
import sys
import logging # for logging to a file
import argparse

def compare(left_directory, right_directory): 
    dircmp_obj = filecmp.dircmp(left_directory, right_directory); # The dircmp object has different methods and attributes to compare the directories that are passed in as arguments
    new_files = dircmp_obj.left_only # a list of files that are only present in the source folder (left folder)
    updated_files = dircmp_obj.diff_files # a list of files that are updated
    files_to_copy = new_files + updated_files  
    files_to_delete = dircmp_obj.right_only # files that are deleted from the source directory, (files that are only present in the replica folder (right folder))
    return files_to_copy, files_to_delete

def copy_files(files):
    for file in files:
        source_file_path = os.path.join(args.source_dir, file) # get source file path of the file to copy
        shutil.copy2(source_file_path, args.replica_dir) # create and or copy (overwrite) all the files to copy
        log_message = f'{file} has been copied'
        print(log_message)
        logging.info(log_message)

def delete_files(files):
    for file in files: 
        replica_file_path = os.path.join(args.replica_dir, file) # get replica file path of the file to delete
        os.remove(replica_file_path)
        log_message = f'{file} has been deleted'
        print(log_message)
        logging.info(log_message)

def synchronize(source_dir, replica_dir):
    files_to_copy, files_to_delete = compare(source_dir, replica_dir) # compare folders: find which files need to be copied or deleted
    copy_files(files_to_copy) # copy the new and update files 
    delete_files(files_to_delete) # remove the deleted files 

# Initialize command line arguments
parser = argparse.ArgumentParser(description='Folder Synchronization')
parser.add_argument('source_dir', help='Path to the source folder')
parser.add_argument('--replica_dir', default='replica', help='Path to the replica folder')
parser.add_argument('--interval', type=int, default=5, help='Synchronization interval in seconds (default: 5)')
parser.add_argument('--log_file', default='log_file.log', help='Path to the log file (default: log_file.log)')
args = parser.parse_args()

# Check if replica folder exists. If not, create it.
if not (os.path.isdir(args.replica_dir)): 
    os.mkdir(args.replica_dir)
    print("Created replica_dir")

# setup basic logging to a file
# specifies the format paramater to record the timestamp of the logged message
logging.basicConfig(level=logging.INFO, filename=args.log_file, format="%(asctime)s %(levelname)s %(message)s")

# Loop to continuously synchronize folders at a specified time interval
started = False
while True:
    if not (started):
        print("Started synchronization loop ...")
        started = True
    synchronize(args.source_dir, args.replica_dir)
    time.sleep(args.interval) # Sleep for specified time interval

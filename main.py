import time  # Importing time for time operations, built in module
import filecmp # To compare files and directories
import shutil # For high-level file operations
import os 


sync_periond = 5 # (in seconds)
source_dir = "source";
replica_dir = "replica";

def compare(left_directory, right_directory): 
    # The dircmp object has different methods and attributes to compare the directories that are passed in as arguments
    dircmp_obj = filecmp.dircmp(left_directory, right_directory);
    # a list of files that are only present in the source folder (left folder)
    new_files = dircmp_obj.left_only
    print(f'New files: {new_files}')
    # files that are updated
    updated_files = dircmp_obj.diff_files
    print(f'Updated files: {updated_files}')
    files_to_copy = new_files + updated_files
    # files that are deleted from the source directory, files that are only present in the replica folder (right folder)
    files_to_delete = dircmp_obj.right_only
    # TODO: possibly make different logs for files that need update vs creation
    print(f'Deleted files: {files_to_delete}')
    return files_to_copy, files_to_delete

def copy_delete_files(files_to_copy, files_to_delete): 
    for file in files_to_copy:
        source_file_path = os.path.join(source_dir, file) # get source directory of the file to copy
        shutil.copy2(source_file_path, replica_dir) # create and or copy (overwrite) all the files to copy
        print(f'{file} has been copied')
    
    for file in files_to_delete: 
        replica_file_path = os.path.join(replica_dir, file)
        os.remove(replica_file_path)
        print(f'{file} has been deleted')

def synchronize(source_dir, replica_dir):
    files_to_copy, files_to_delete = compare(source_dir, replica_dir) # compare folders: find which files need to be copied or deleted
    copy_delete_files(files_to_copy, files_to_delete) # copy the new and update files and remove the deleted files 
    print("Synched up!");

# Loop to continuously synchronize folders at a specified time interval
while True:
    # TODO: compare folders with filecmp (find all files that are new or alterd)
    # TODO: copy all the altered and new files from source to replica
    synchronize(source_dir, replica_dir)
    time.sleep(sync_periond) # Sleep for specified time interval
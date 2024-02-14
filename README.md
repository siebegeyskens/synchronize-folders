# Synchronize Folders

This program is designed to synchronize two folders: a source folder and a replica folder. The goal is to ensure that the replica folder maintains an identical copy of the content present in the source folder. This synchronization process is one-way, meaning changes in the source folder will be reflected in the replica folder, but not vice versa.

## Features

- One-way synchronization from source to replica folder.
- Periodic synchronization at user-defined intervals.
- Logging of file copying, and removal operations to both console output and a specified log file.
- Command line arguments for specifying folder paths, synchronization interval, and log file path.
- Utilizes built-in and external libraries for efficient implementation.

## Requirements

- Python 3.x installed on the system.

## Usage

To use this program, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the directory where the program files are located.
3. Open a terminal or command prompt.
4. Run the program with the following command:

```
python main.py /path/to/source --replica_dir /path/to/replica --interval 3600 --log_file log_file.log
```

Replace /path/to/source and /path/to/replica with the paths to the source and replica folders you want to synchronize. Adjust the --interval parameter to set the synchronization interval in seconds. Specify the desired log file path using the --log_file option.

- Path to the source folder is required
- --replica: Path to the replica folder (default: "replica").
- --interval: Synchronization interval in seconds (default: 5).
- --log_file: Path to the log file (default: log_file.log).

## Example

```
python main.py ./source --replica_dir ./replica --interval 5 --log_file log_file.log
```

This command will synchronize the contents of the ./source folder with the ./replica folder every 5 seconds, and the operation logs will be saved to the log_file.log file.

## Notes

- Make sure the source folder exist before running the program.

import subprocess
import time
import os
import sys

def check_cd():
    cdrom_path = '/media/priyanshu/testformp3'  # Change this path as necessary
    try:
        # Check if the mount point exists and is a directory
        if os.path.ismount(cdrom_path):
            try:
                # Check if there are any files in the cdrom directory
                if os.listdir(cdrom_path):
                    print("CD Detected with files", flush=True)
                    sys.stdout.flush()  # Flush stdout buffer
                    return True  # CD and files detected
                else:
                    print("CD Detected but no files", flush=True)
                    sys.stdout.flush()  # Flush stdout buffer
                    return False  # CD detected but no files
            except PermissionError as e:
                print("Permission error: CD drive not ready or accessible", flush=True)
                sys.stdout.flush()  # Flush stdout buffer
                return False  # CD detected but CD drive not ready
        else:
            print("No CD Detected", flush=True)
            sys.stdout.flush()  # Flush stdout buffer
            return False  # No CD detected
    except FileNotFoundError:
        print("Mount point not found. Ensure the CD drive is properly mounted.", flush=True)
        sys.stdout.flush()
        return False

if __name__ == "__main__":
    while True:
        if check_cd():
            time.sleep(3)  # Check every 3 seconds
        else:
            time.sleep(3)  # Check every 3 seconds

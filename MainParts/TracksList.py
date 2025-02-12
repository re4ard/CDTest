import os
import shutil

# Path to the D: drive
drive_path = "/media/priyanshu/testformp3/"

# List of MP3 file names you want to check for
target_mp3_names = [
    "CARTITAPE.mp3",
    "CLB.mp3",
    "H&V.mp3",
    "MORELIFE.mp3",
    "TEC.mp3",
    "UTOPIA.mp3",
    "WW.mp3"
]

# Dictionary mapping MP3 names to the associated text file paths
mp3_text_file_mapping = {
    "CARTITAPE.mp3": "C:\\Users\\Priyanshu Bhowmik\\Desktop\\electronCDAPP\\CDMusicPlayer\\Albums\\CARTITAPE\\tracks.json",
    "WW.mp3": "/home/priyanshu/ECDM/Albums/WW/tracks.json",
    "UTOPIA.mp3": "C:\\Users\\Priyanshu Bhowmik\\Desktop\\electronCDAPP\\CDMusicPlayer\\Albums\\UTOPIA\\tracks.json",
    "TEC.mp3": "C:\\Users\\Priyanshu Bhowmik\\Desktop\\electronCDAPP\\CDMusicPlayer\\Albums\\TEC\\tracks.json",
    "MORELIFE.mp3": "C:\\Users\\Priyanshu Bhowmik\\Desktop\\electronCDAPP\\CDMusicPlayer\\Albums\\MORELIFE\\tracks.json",
    "H&V.mp3": "C:\\Users\\Priyanshu Bhowmik\\Desktop\\electronCDAPP\\CDMusicPlayer\\Albums\\H&V\\tracks.json",
    "CLB.mp3": "C:\\Users\\Priyanshu Bhowmik\\Desktop\\electronCDAPP\\CDMusicPlayer\\Albums\\CLB\\tracks.json"
}

# Path to the directory where you want to move the specific text files
move_dir = "/home/priyanshu/ECDM/MainParts"

def find_and_copy_specific_files():
    # Get a list of files in the D: drive
    files = os.listdir(drive_path)

    # Look for the first MP3 file
    for file in files:
        if file.endswith(".mp3"):
            mp3_path = os.path.join(drive_path, file)
            if file in target_mp3_names:
                # Get the corresponding text file to copy
                text_file_to_copy = mp3_text_file_mapping[file]
                # Copy the text file to the specified directory
                shutil.copy(text_file_to_copy, move_dir)
                print(f"Text file {text_file_to_copy} copied successfully.")
                return
    print("No MP3 file with a matching name found.")

# Run the function
find_and_copy_specific_files()

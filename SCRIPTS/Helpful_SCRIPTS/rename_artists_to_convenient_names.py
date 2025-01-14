

import os

# Define the individual artists array
artists = [
    "ΜΑΝΩΛΗΣ ΛΑΓΟΣ", "ΓΙΩΡΓΗΣ ΚΑΛΟΓΡΙΔΗΣ", 
    "ΑΛΕΚΟΣ ΚΑΡΑΒΙΤΗΣ", "ΜΑΝΩΛΗΣ ΣΤΡΑΒΟΣ", "ΝΙΚΟΛΑΟΣ ΧΑΡΧΑΛΗΣ", "ΚΩΣΤΑΣ ΜΟΥΝΤΑΚΗΣ",
    "ΔΕΡΜΙΤΖΟΓΙΑΝΝΗΣ", "ΧΑΡΙΛΑΟΣ ΠΙΠΕΡΑΚΗΣ", "ΘΑΝΑΣΗΣ ΣΚΟΡΔΑΛΟΣ", "ΣΤΕΛΙΟΣ ΦΟΥΣΤΑΛΙΕΡΗΣ",
    "ΝΙΚΟΛΑΟΣ ΣΑΡΙΔΑΚΗΣ", "ΚΩΣΤΑΣ ΠΑΠΑΔΑΚΗΣ", "ΣΤΡΑΤΗΣ ΚΑΛΟΓΕΡΙΔΗΣ", 
    "ΝΙΚΟΣ ΠΑΠΑΔΟΓΙΑΝΝΗΣ", 
    "ΑΝΤΩΝΗΣ ΚΑΡΕΚΛΑΣ", 
    "ΓΙΩΡΓΗΣ ΚΟΥΤΣΟΥΡΕΛΗΣ"
]

# Path to the music folder
music_folder = "music_backup"

# Iterate over all files in the folder
for file_name in os.listdir(music_folder):
    # Check if the file is an mp3
    if file_name.endswith(".mp3"):
        # Check if the file matches an artist
        for artist in artists:
            if artist in file_name:
                # Create the new file name
                new_file_name = f"{artist} __ {file_name}"
                
                # Construct full file paths
                old_path = os.path.join(music_folder, file_name)
                new_path = os.path.join(music_folder, new_file_name)
                
                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed: {file_name} --> {new_file_name}")
                break  # Move to the next file once a match is found




collab_artists = ["ΑΝΔΡΕΑΣ ΡΟΔΙΝΟΣ - ΙΩΑΝΝΗΣ ΜΠΕΡΝΙΔΑΚΗΣ", "ΓΙΩΡΓΗΣ ΚΟΥΤΣΟΥΡΕΛΗΣ - ΧΡΗΣΤΟΣ ΚΟΡΟΝΙΩΤΑΚΗΣ", "ΣΤ.ΦΟΥΣΤΑΛΙΕΡΗΣ - Ι.ΜΠΑΞΕΒΑΝΗΣ", "ΓΙΩΡΓΗΣ - ΣΤΕΛΙΟΣ ΚΟΥΤΣΟΥΡΕΛΗΣ", "ΓΙΑΝΝΗΣ - ΛΑΥΡΕΝΤΙΑ ΜΠΕΡΝΙΔΑΚΗ", "ΓΙΩΡΓΗΣ ΚΟΥΤΣΟΥΡΕΛΗΣ - Ν.ΣΑΡΙΔΑΚΗΣ", "ΓΙΩΡΓΗΣ ΚΟΥΤΣΟΥΡΕΛΗΣ - ΓΙΩΡΓΗΣ ΜΑΡΙΑΝΟΣ",
"ΓΙΩΡΓΗΣ ΚΟΥΤΣΟΥΡΕΛΗΣ - ΘΕΟΧΑΡΗΣ ΤΖΙΝΕΥΡΑΚΗΣ", "ΣΤΕΛΙΟΣ ΦΟΥΣΤΑΛΙΕΡΗΣ - ΜΠΑΞΕΒΑΝΗΣ", "ΣΤΕΛΙΟΣ ΦΟΥΣΤΑΡΕΛΗΣ - ΓΙΩΡΓΗΣ ΤΖΙΜΑΚΗΣ", "ΑΝΤΩΝΗΣ ΚΑΡΕΚΛΑΣ - ΣΤΕΛΙΟΣ ΦΟΥΣΤΑΛΙΕΡΗΣ", "ΓΙΩΡΓΗΣ ΚΟΥΤΣΟΥΡΕΛΗΣ - ΓΙΩΡΓΟΣ ΤΖΙΜΑΚΗΣ", "ΜΑΝΩΛΗΣ ΛΑΓΟΣ - ΛΑΥΡΕΝΤΙΑ ΜΠΕΡΝΙΔΑΚΗ"]


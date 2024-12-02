import os

def get_conversations():
    """
    Returns a list of .txt files in the hardcoded folder path.

    :return: List of .txt file names in the folder.
    """
    current_folder = os.getcwd()
   
   
    
        # List all files in the folder
    files = os.listdir(current_folder)
   
        # Filter and return only .txt files
    txt_files = [file for file in files if file.endswith('.txt')and file !="requirements.txt" ]
    if len(txt_files)==0:
        return ["None"]
    return txt_files
  
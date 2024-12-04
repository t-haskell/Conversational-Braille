import datetime

def save_braille(fileName: str, newLine: str, saveConversation: bool):
    # function should open a txt file, add a new line, then save the file
    if saveConversation:
        now = datetime.datetime.now()  # Get the current date and time
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")  # Use hyphens to avoid issues in filenames
        full_file_name = f"{date_str}_{time_str}.txt"
        with open(full_file_name, "a", encoding="utf-8") as file:
            file.write(newLine + "\n")
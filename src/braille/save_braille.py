from datetime import date
def save_braille(fileName:str, newLine:str,saveConversation:bool):
    #function should open a txt file, add an new line, then save the file
    if saveConversation:
        date_str = date.today().strftime("%Y-%m-%d")
        full_file_name = f"{fileName}_{date_str}.txt"
        with open(full_file_name, "a", encoding="utf-8") as file:
            file.write(newLine + "\n")
from LAS_Classes import InfoCounter

log_file_path = input("Please enter your log file's path:\n")

with open(log_file_path, "r", encoding="utf-8") as file:
    log_file_as_list = [line.strip().split(" | ") for line in file]

info_counter = InfoCounter(log_file_as_list)

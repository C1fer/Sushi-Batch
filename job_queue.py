from colorama import Fore, Style


# Show Job Queue
def show_queue(src_files, dst_files, sub_files, mode):

    print(f"{Fore.CYAN}Job Queue")

    # Show files for each job
    for idx in range(len(src_files)):
        print(f"\n{Fore.LIGHTBLACK_EX}Job #{idx + 1}")
        print(f"{Fore.LIGHTBLUE_EX}Source file: {src_files[idx]}")
        print(f"{Fore.LIGHTYELLOW_EX}Destination file: {dst_files[idx]}")

        # Only show subtitle files in Audio-based sync modes
        if mode == "1" or mode == "3":
            print(f"{Fore.LIGHTRED_EX}Subtitle file: {sub_files[idx]}")

    # Confirm queue processing
    choice = input("\nProcess the queue? (Y/N): ")

    if choice.upper() == "Y":
        print(f"{Fore.LIGHTMAGENTA_EX}Processing Queue...\n")
        return True

    return False
import os
import pygame
import threading

def playM(folder_path):
    pygame.mixer.init()
    for filename in os.listdir(folder_path):
        if filename.endswith('.mp3'):
            pygame.mixer.music.load(os.path.join(folder_path, filename))
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue

def stopM():
    pygame.mixer.music.stop()

def pauseM():
    pygame.mixer.music.pause()

def resumeM():
    pygame.mixer.music.unpause()

def selectF():
    folder_path = input("Enter the path of the folder containing music files: ")
    if os.path.isdir(folder_path):
        return folder_path
    else:
        print("Invalid folder path.")
        return None

def player(folder_path):
    thread = threading.Thread(target=playM, args=(folder_path,))
    thread.start()

def main():
    folder_path = None
    print("Welcome to the Music Player!")
    while True:
        print("\nMenu:")
        print("1. Select Folder")
        print("2. Play Music")
        print("3. Pause the Music")
        print("4. Resume the Music")
        print("5. Stop the Music")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            folder_path = selectF()
        elif choice == '2':
            if folder_path:
                player(folder_path)
            else:
                print("Please select a folder first.")
        elif choice == '3':
            pauseM()
        elif choice == '4':
            resumeM()
        elif choice == '5':
            stopM()
        elif choice == '6':
            print("Thank you for visiting and using the Music Player.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

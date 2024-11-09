import db_handler

def add_new_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    category = input("Enter category: ")
    db_handler.add_note(title, content, category)
    print("Note added successfully!")

def display_notes():
    notes = db_handler.get_all_notes()
    if not notes:
        print("No notes found.")
    else:
        for note in notes:
            print(f"\nID: {note[0]} | Title: {note[1]} | Category: {note[3]} | Date: {note[4]}")
            print(f"Content: {note[2]}")
            print("-" * 30)

def search_for_note():
    keyword = input("Enter keyword to search: ")
    results = db_handler.search_notes(keyword)
    if results:
        for note in results:
            print(f"\nID: {note[0]} | Title: {note[1]} | Category: {note[3]}")
            print(f"Content: {note[2]}")
    else:
        print("No matching notes found.")

def delete_note():
    note_id = int(input("Enter note ID to delete: "))
    db_handler.delete_note(note_id)
    print("Note deleted.")

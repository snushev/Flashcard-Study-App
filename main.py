from flashcard_manager import FlashcardManager

# ANSI escape sequences for colors
COLOR_RESET = '\033[0m'
COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_YELLOW = '\033[33m'
COLOR_BLUE = '\033[34m'
COLOR_MAGENTA = '\033[35m'
COLOR_CYAN = '\033[36m'


def main():

    manager = FlashcardManager()

    while True:

        print("\nFlashcard manager:")
        print(f"{COLOR_GREEN}1. Add flashcard{COLOR_RESET}")
        print(f"{COLOR_YELLOW}2. Edit flashcard{COLOR_RESET}")
        print(f"{COLOR_RED}3. Delete flashcard{COLOR_RESET}")
        print(f"{COLOR_CYAN}4. List of flashcards{COLOR_RESET}")
        print(f"{COLOR_BLUE}5. Review flashcards{COLOR_RESET}")
        print(f"{COLOR_MAGENTA}6. Exit{COLOR_RESET}")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            question = input(f"Enter your {COLOR_GREEN}question{COLOR_RESET}: ")
            answer = input(f"Enter your {COLOR_GREEN}answer{COLOR_RESET}: ")
            manager.add_flashcard(question, answer)
            print("\nFlashcard added successfully!")
        elif choice == "2":
            edit = input("Enter your question to edit:")
            question = input("Enter your question: ")
            answer = input("Enter your answer: ")
            manager.edit_flashcard(edit, question, answer)
        elif choice == "3":
            question = input("Enter question for deletion:")
            manager.delete_flashcard(question)
        elif choice == "4":
            print("\nList of all flashcards:\n")
            manager.list_flashcards()
        elif choice == "5":
            manager.review_flashcard()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


main()
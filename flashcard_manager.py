import random
from flashcard import Flashcard


class FlashcardManager:
    def __init__(self, filename="flashcards.txt"):
        self.flashcards = {}
        self.filename = filename
        self.load_flashcards()

    def add_flashcard(self, question, answer):
        self.flashcards[question] = Flashcard(question, answer)
        self.save_flashcards()

    def edit_flashcard(self, question, new_question, new_answer):
        if question in self.flashcards:
            self.flashcards[new_question] = Flashcard(new_question, new_answer)
            if new_question != question:
                del self.flashcards[question]
            self.save_flashcards()

    def delete_flashcard(self, question):
        if question in self.flashcards:
            del self.flashcards[question]
            self.save_flashcards()

    def list_flashcards(self):
        for question, flashcard in self.flashcards.items():
            print(flashcard.display_question())

    def review_flashcard(self):
        if self.flashcards:
            question = random.choice(list(self.flashcards.keys()))
            flashcard = self.flashcards[question]
            print(flashcard.display_question())
            input("Press Enter to show the answer...")
            print(flashcard.display_answer())
        else:
            print("No flashcards to review!")

    def save_flashcards(self):
        """Save flashcards to a text file."""
        with open(self.filename, 'w') as file:
            for flashcard in self.flashcards.values():
                file.write(f"{flashcard.question} <:> {flashcard.answer}\n")

    def load_flashcards(self):
        """Load flashcards from a text file."""
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    question, answer = line.strip().split(' <:> ')
                    self.flashcards[question] = Flashcard(question, answer)
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty set of flashcards
            print(f"No existing flashcard file found. Starting a new collection.")

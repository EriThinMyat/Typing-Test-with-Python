import time
import random
from datetime import datetime
import difflib

class TypingTest:
    def __init__(self):
        self.history = []

    def print_menu(self, menu_dict):
        for key,val in menu_dict.items():
            print(f"{key}. {val}")
        print("=" * 20)

    def main_menu(self):
        menu_items = {
            "1" : "Practice Typing",
            "2" : "View Records",
            "0" : "Exit Program"
        }

        print("==== Main Menu ====")
        self.print_menu(menu_items)

    def empty_history(self):
        if not self.history:
            print("No records yet.")
            return True
        return False

    def view_history(self):
        if self.empty_history():
            return
        
        print("Your Records")
        for index,record in enumerate(self.history, 1):
            print(f"{index}. {record}")

    def clear_history(self):
        if self.empty_history():
            return
        
        confirm = input("Are you sure to clear all records? (y/n): ").strip().lower()
        if confirm == "y":
            self.history.clear()
            print("All records cleared.")

    def show_history(self):
        history_menu = {
            "1" : "Records",
            "2" : "Clear Records",
            "0" : "Back to Main Menu"
        }

        print("==== Record Menu ====")
        self.print_menu(history_menu)
        
        while True:
            choose = input(">> ").strip()
            if choose not in history_menu:
                print("Invalid input.")
                continue
            
            if choose == "0":
                break
            elif choose == "1":
                self.view_history()
            elif choose == "2":
                self.clear_history()

    def random_sentences(self):
        singular_subjects = [
            "My neighbor's talking parrot",
            "A sleepy panda at the zoo",
            "The confused robot from Mars",
            "An invisible man in a tuxedo",
            "A chicken riding a bicycle",
            "My grandma's ninja cat",
            "A talking cactus",
            "An alien barista",
            "The haunted violin",
            "A ghost with a smartphone"
        ]

        plural_subjects = [
            "Time-traveling hamsters",
            "Zebras in sunglasses",
            "Dancing pineapples",
            "Invisible penguins",
            "Aliens wearing pajamas",
            "Robot chickens",
            "Flying books",
            "Sneezing kangaroos",
            "Llamas in detective hats",
            "Singing jellybeans"
        ]

        verbs_singular = [
            "accidentally orders pizza",
            "dances the tango",
            "starts singing opera",
            "invents a new language",
            "runs away from a shadow",
            "builds a spaceship from spoons",
            "argues with a toaster",
            "teleports into my fridge",
            "trains for the Olympics",
            "dreams of becoming a pancake"
        ]

        verbs_plural = [
            "accidentally order pizza",
            "dance the tango",
            "start singing opera",
            "invent a new language",
            "run away from a shadow",
            "build spaceships from spoons",
            "argue with toasters",
            "teleport into my fridge",
            "train for the Olympics",
            "dream of becoming pancakes"
        ]

        objects = [
            "during a live TV interview",
            "on top of a moving train",
            "while juggling flaming pineapples",
            "at a sushi restaurant in space",
            "inside a haunted library",
            "under a disco ball",
            "at a karaoke contest for ghosts",
            "in a secret meeting of cats",
            "inside a floating teacup",
            "while riding a unicorn-powered bicycle"
        ]

        if random.random() < 0.5:
            sub = random.choice(singular_subjects)
            verb = random.choice(verbs_singular)
        else:
            sub = random.choice(plural_subjects)
            verb = random.choice(verbs_plural)

        obj = random.choice(objects)
        sentence = f"{sub} {verb} {obj}"

        return sentence

    def choose_level(self):
        levels = {
            "1" : "Easy",
            "2" : "Medium",
            "3" : "Hard",
            "0" : "Back to Main Menu"
        }
        print("==== Levels ====")
        self.print_menu(levels)
        
        while True:
            level = input("Choose level: ").strip()
            if level == "0":
                return None
            elif level in ["1","2","3"]:
                return int(level)
            else:
                print("Invalid input")

    def get_level(self,wpm):
        if wpm < 10:
            current_level = "Very Slow"
        elif 10 <= wpm < 20:
            current_level = "Beginner"
        elif 20 <= wpm < 30:
            current_level = "Slow"
        elif 30 <= wpm < 50:
            current_level = "Average"
        elif 50 <= wpm < 60:
            current_level = "Above Average"
        elif 60 <= wpm < 80:
            current_level = "Fast"
        elif 80 <= wpm < 100:
            current_level = "Professional"
        else:
            current_level = "Elite"

        return current_level
    
    def calculate_wpm(self, sentence, elapsed_time):
        word_count = len(sentence.split())
        wpm = round((word_count / 5) / (elapsed_time / 60), 2) if elapsed_time > 0 else 0.0 
        return wpm

    def calculate_accuracy(self, sentence, typing):
        accuracy = round(difflib.SequenceMatcher(None, sentence, typing).ratio() * 100, 2)
        return accuracy
    
    def countdown(self, seconds = 3):
        print("Get ready...")
        for i in range(seconds, 0, -1):
            print(f"{i}.....")
            time.sleep(1)
        print("Go...!")

    def practice_typing(self):
        while True:
            level = self.choose_level()
            if level is None:
                return
            
            practiced_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            num_sentences = self.get_sentence(level)
            total_wpm, total_duration = self.run_typing(num_sentences)

            if num_sentences > 1:
                avg_wpm = round((total_wpm / num_sentences), 2)
            else:
                avg_wpm = total_wpm
            
            session_level = self.get_level(avg_wpm)
            self.saved_records(practiced_time, total_duration, avg_wpm, session_level)
            
    def get_sentence(self, level):
        level_map = {1 : 1, 2 : 2, 3 : 5}
        total_sentence = level_map.get(level, 1)
        return total_sentence
    
    def run_typing(self, total_sentence):
        total_wpm = 0
        total_duration = 0
        completed_sentence = 0
        for _ in range(total_sentence):
            sentence = self.random_sentences()
            print(sentence)
            input("Press enter when you're ready to start typing....")
            self.countdown()
            start = time.time()
            typing = input("Start type here: ").strip()
            if typing == "0":
                self.return_back()
                break
            stop = time.time()
            if not typing:
                print("You didn't type anything.")
                continue

            elapsed_time = round(stop - start, 2)
            total_duration += elapsed_time

            wpm = self.calculate_wpm(sentence, elapsed_time)
            total_wpm += wpm

            accuracy = self.calculate_accuracy(sentence, typing)
            current_level = self.get_level(wpm)

            self.display_result(sentence, typing, wpm, total_duration, current_level, accuracy)
            completed_sentence += 1

        if completed_sentence > 0:
            return total_wpm, total_duration
        
        else:
            return 0, total_duration
    
    def display_result(self, sentence, typing, wpm, total_duration ,current_level, accuracy):
        if sentence.strip() == typing.strip():
            print("✅ Correct")

        else:
            similarity = difflib.SequenceMatcher(None, sentence.strip(), typing.strip()).ratio()
            if similarity > 0.9:
                print("🟡 Almost Correct")
            else:
                print("❌ Incorrect")
                
        print(f"WPM(word per minute): {wpm} wpm")
        print(f"Duration: {total_duration}s")
        print(f"Typing Level: {current_level}")
        print(f"Accuracy: {accuracy}%")
        self.return_back()
        

    def saved_records(self, practiced_time, total_duration, avg_wpm, current_level):
        records = f"{practiced_time} Duration: {total_duration}s WPM(word per minute): {avg_wpm} wpm Level: {current_level}"
        self.history.append(records)

    def return_back(self):
        practice_menu = {
            "1" : "Practice Again",
            "0" : "Return Back"
        }

        print("=" * 20)
        self.print_menu(practice_menu)

        while True:
            choose = input("Practice again or return back: ").strip()
            if choose == "0":
                break
            elif choose == "1":
                self.practice_typing()
            else:
                print("Invalid input")

    def typing_test(self):
    
        while True:
            self.main_menu()
            valid_menu = ["0","1","2"]

            user_input = input(">> ").strip()

            if user_input not in valid_menu:
                print("Please enter valid number.")
                continue

            if user_input == "0":
                print("Thanks for using typing test. Good bye!")
                break
            elif user_input == "1":
                self.practice_typing()
            elif user_input == "2":
                self.show_history()
            else:
                print("Invalid input.")


if __name__ == "__main__":
    typing = TypingTest()
    try:
        typing.typing_test()
    except KeyboardInterrupt:
        print("\nExiting.....Bye!")

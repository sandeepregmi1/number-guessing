import time
import random
from datetime import datetime
import json


class NumberGuessingAI:
    def __init__(self):
        self.stats = {
            "games_played": 0,
            "wins": 0,
            "total_attempts": 0,
            "best_attempts": None,
            "history": []
        }

        try:
            with open("stats.json", "r") as f:
                self.stats = json.load(f)
        except FileNotFoundError:
            pass

    def slow_print(self, text, delay=0.015):
        for ch in text:
            print(ch, end="", flush=True)
            time.sleep(delay)
        print()

    def ai_message(self):
        return random.choice([
            "Processing probability space...",
            "Eliminating impossible ranges...",
            "Simulating optimal guess...",
            "Recalculating best move...",
            "Thinking like a human... but faster.",
        ])

# Input validation loop
    def safe_input(self, prompt, valid=None):
        while True:
            value = input(prompt).strip().lower()
            if valid is None or value in valid:
                return value
            print("Invalid input. Try again.")

    def difficulty(self):
        print("\nChoose Difficulty:")
        print("1. Easy (1–50)")
        print("2. Medium (1–100)")
        print("3. Hard (1–500)")

        choice = self.safe_input("Enter choice: ", ["1", "2", "3"])
        return {"1": 50, "2": 100, "3": 500}[choice]

    def rating(self, attempts, max_range):
        optimal = {50: 5, 100: 7, 500: 9}
        threshold = optimal[max_range]

        if attempts <= threshold:
            return "GENIUS"
        elif attempts <= threshold + 1:
            return "EFFICIENT"
        return "AVERAGE"

    def play(self):
        self.slow_print("\nAI Agent Starting...")

        max_range = self.difficulty()

        self.slow_print(f"\nThink of a number between 1 and {max_range}")
        input("Press ENTER when ready...")

        low, high = 1, max_range
        attempts = 0
        start = time.time()

        while low <= high:
            attempts += 1
            guess = (low + high) // 2

            print(f"\nRange: {low}-{high}")
            print(self.ai_message())
            print(f"AI Guess: {guess}")

            feedback = self.safe_input(
                "low / high / correct: ",
                ["low", "high", "correct"]
            )

            if feedback == "correct":
                duration = round(time.time() - start, 2)
                score = self.rating(attempts, max_range)

                self.slow_print(f"\nFound in {attempts} attempts")
                self.slow_print(f"Time: {duration}s")
                self.slow_print(f"Rating: {score}")

                self.update_stats(attempts, max_range, duration, score)
                return

            elif feedback == "low":
                low = guess + 1
            else:
                high = guess - 1

        self.slow_print("\nInconsistent answers detected!")

    def update_stats(self, attempts, max_range, duration, score):
        self.stats["games_played"] += 1
        self.stats["wins"] += 1
        self.stats["total_attempts"] += attempts

        if self.stats["best_attempts"] is None:
            self.stats["best_attempts"] = attempts
        else:
            self.stats["best_attempts"] = min(self.stats["best_attempts"], attempts)

        self.stats["history"].append({
            "time": str(datetime.now()),
            "range": max_range,
            "attempts": attempts,
            "duration": duration,
            "rating": score
        })

        self.save_stats()

    def show_stats(self):
        print("\n--- STATS ---")
        print(f"Games Played: {self.stats['games_played']}")
        print(f"Wins: {self.stats['wins']}")

        if self.stats["games_played"]:
            avg = self.stats["total_attempts"] / self.stats["games_played"]
            print(f"Average Attempts: {round(avg, 2)}")

        if self.stats["best_attempts"] is not None:
            print(f"Best: {self.stats['best_attempts']} attempts")

        print("\nLast Game History:")
        for h in self.stats["history"][-3:]:
            print(h)

    def save_stats(self):
        with open("stats.json", "w") as f:
            json.dump(self.stats, f, indent=4)

    def run(self):
        self.slow_print("AI Number Guessing System Online")

        while True:
            self.play()

            choice = self.safe_input(
                "\nPlay again? (yes/no/stats): ",
                ["yes", "no", "stats"]
            )

            if choice == "no":
                self.slow_print("Goodbye!")
                self.show_stats()
                break
            elif choice == "stats":
                self.show_stats()


if __name__ == "__main__":
    NumberGuessingAI().run()
import time
import random
from datetime import datetime


class NumberGuessingAI:
    def __init__(self):
        self.stats = {
            "games_played": 0,
            "wins": 0,
            "total_attempts": 0,
            "best_attempts": float("inf")
        }

    # ---------------- UI / UX ----------------
    def slow_print(self, text, delay=0.02):
        for ch in text:
            print(ch, end='', flush=True)
            time.sleep(delay)
        print()

    def ai_thought(self):
        messages = [
            "Analyzing patterns...",
            "Running probability model...",
            "Updating predictions...",
            "Narrowing search space...",
            "Hmm... interesting choice...",
            "Processing logic tree...",
        ]
        return random.choice(messages)

    # ---------------- GAME SETTINGS ----------------
    def choose_difficulty(self):
        print("\n🎮 Choose Difficulty Level")
        print("1. Easy   (1 - 50)")
        print("2. Medium (1 - 100)")
        print("3. Hard   (1 - 500)")

        while True:
            choice = input("👉 Enter choice: ").strip()
            if choice == "1":
                return 50
            elif choice == "2":
                return 100
            elif choice == "3":
                return 500
            print("❌ Invalid input. Try again.")

    # ---------------- PERFORMANCE SYSTEM ----------------
    def rating(self, attempts, max_range):
        optimal = {
            50: (5, 6),
            100: (6, 7),
            500: (8, 9)
        }

        genius, efficient = optimal[max_range]

        if attempts <= genius:
            return "🏆 GENIUS AI PERFORMANCE"
        elif attempts <= efficient:
            return "⚡ EFFICIENT GUESSING"
        return "📉 BELOW EXPECTATION"

    # ---------------- CORE GAME ----------------
    def play(self):
        self.slow_print("\n🤖 Hello! I'm your Guessing AI Agent.")
        max_range = self.choose_difficulty()

        self.slow_print(f"\nThink of a number between 1 and {max_range}.")
        input("Press ENTER when ready...")

        low, high = 1, max_range
        attempts = 0

        start_time = time.time()

        while low <= high:
            attempts += 1
            guess = (low + high) // 2

            print("\n----------------------------")
            print(f"📊 Range: {low} - {high}")
            self.slow_print(f"🧠 {self.ai_thought()}")
            time.sleep(0.5)

            print(f"🤖 My guess: {guess}")

            while True:
                feedback = input("Is it 'low', 'high', or 'correct'? ").strip().lower()
                if feedback in ["low", "high", "correct"]:
                    break
                print("❌ Please enter valid input.")

            if feedback == "correct":
                duration = round(time.time() - start_time, 2)

                self.slow_print(f"\n🎉 I found it in {attempts} attempts!")
                self.slow_print(f"⏱️ Time taken: {duration} seconds")
                print(self.rating(attempts, max_range))

                self.update_stats(attempts)
                return

            elif feedback == "low":
                low = guess + 1
            elif feedback == "high":
                high = guess - 1

        self.slow_print("\n🚨 Inconsistent answers detected!")
        self.slow_print("Either you're messing with me or something went wrong 😄")

    # ---------------- STATS ----------------
    def update_stats(self, attempts):
        self.stats["games_played"] += 1
        self.stats["wins"] += 1
        self.stats["total_attempts"] += attempts

        if attempts < self.stats["best_attempts"]:
            self.stats["best_attempts"] = attempts

    def show_stats(self):
        print("\n📊 GAME STATISTICS")
        print("----------------------")
        print(f"Games Played : {self.stats['games_played']}")
        print(f"Wins         : {self.stats['wins']}")
        print(f"Total Attempts: {self.stats['total_attempts']}")

        if self.stats["games_played"] > 0:
            avg = self.stats["total_attempts"] / self.stats["games_played"]
            print(f"Average Attempts: {round(avg, 2)}")

        if self.stats["best_attempts"] != float("inf"):
            print(f"Best Performance: {self.stats['best_attempts']} attempts")

    # ---------------- MAIN LOOP ----------------
    def run(self):
        self.slow_print("🤖 AI NUMBER GUESSING SYSTEM STARTED")

        while True:
            self.play()

            print("\n==============================")
            choice = input("Play again? (yes/no/stats): ").strip().lower()

            if choice == "no":
                self.slow_print("👋 Goodbye! Thanks for playing.")
                self.show_stats()
                break
            elif choice == "stats":
                self.show_stats()


if __name__ == "__main__":
    game = NumberGuessingAI()
    game.run()
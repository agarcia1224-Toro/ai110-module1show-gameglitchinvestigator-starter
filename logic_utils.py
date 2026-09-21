def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

#Fix: the hints should work correctly now
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    secret_value = int(secret)

    if guess == secret_value:
        return "Win", "🎉 Correct!"

    if guess > secret_value:
        return "Too High", "📈 Go LOWER!"

    return "Too Low", "📉 Go HIGHER!"

# Fix: shared scoring logic prevents incorrect guesses from making the score negative.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score without allowing the score to become negative."""
    if outcome == "Win":
        points = max(10, 100 - 10 * (attempt_number + 1))
        return current_score + points

    return max(0, current_score)

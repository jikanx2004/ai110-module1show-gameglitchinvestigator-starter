import pytest

from logic_utils import check_guess


@pytest.mark.parametrize(
    "guess, secret, expected",
    [
        (50, 50, ("Win", "🎉 Correct!")),
        (60, 50, ("Too High", "📉 Go LOWER!")),
        (40, 50, ("Too Low", "📈 Go HIGHER!")),
        (9, 50, ("Too Low", "📈 Go HIGHER!")),
    ],
)
def test_outcome_and_message_together(guess, secret, expected):
    # The outcome and its hint message must match as a pair
    assert check_guess(guess, secret) == expected

def test_else_branch_too_low_says_go_higher():
    # A guess below the secret falls through to the else branch,
    # which should report "Too Low" and tell the player to go HIGHER
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

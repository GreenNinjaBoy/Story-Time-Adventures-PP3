import pytest
from unittest.mock import patch
from pages import Page
from story_index import create_pages, create_pages_2, end_game_1, end_game_2
from run import get_choice, tick, get_name, intro_to_game

@pytest.fixture
def capsys(capsys):
    return capsys

def test_get_choice_valid_input():
    with patch("builtins.input", side_effect=["1", "2"]):
        assert get_choice(["Option 1", "Option 2"]) == 1
        assert get_choice(["Option 1", "Option 2"]) == 2

def test_get_choice_invalid_input_then_valid_input():
    with patch("builtins.input", side_effect=["3", "1", "2"]):
        assert get_choice(["Option 1", "Option 2"]) == 1


def test_tick_with_end_game_choice(capsys):
    with patch("builtins.input", side_effect=["1"]):
        page = Page(message="End Game Message", choices=["end_game_1"], choices_mapping={1: None})

        with pytest.raises(SystemExit):
            tick(page, "Title", "User")

    captured = capsys.readouterr()
    assert "End Game Message" in captured.out
    assert "Princess User returned to the kingdom" in captured.out

def test_get_name_valid_input(capsys):
    with patch("builtins.input", side_effect=["Alice"]):
        assert get_name("Enter your name: ") == "Alice"

def test_get_name_invalid_input_then_valid_input(capsys):
    with patch("builtins.input", side_effect=["123", "Bob"]):
        assert get_name("Enter your name: ") == "Bob"

def test_intro_to_game(capsys):
    with patch("builtins.input", side_effect=["Alice"]):
        assert intro_to_game() == "Alice"

    captured = capsys.readouterr()
    assert "Welcome Alice, we have two great adventure stories for you:" in captured.out
    # Add more specific assertions for the printed output based on your code logic

if __name__ == "__main__":
    pytest.main()

import pytest
from unittest.mock import patch
from story_index import create_pages, create_pages_2, end_game_1, end_game_2
from pages import Page


def test_end_game_1(capsys):
    user_name = "Alice"
    end_game_1(user_name)
    captured = capsys.readouterr()
    assert f"Princess {user_name} returned to the kingdom" in captured.out
    assert "inspiring children to be resourceful and creative in the face of challenges." in captured.out


def test_create_pages():
    user_name = "Alice"
    pages = create_pages(user_name)
    assert isinstance(pages[0], Page)
    assert len(pages) == 9


def test_end_game_2(capsys):
    user_name = "Bob"
    end_game_2(user_name)
    captured = capsys.readouterr()
    assert f"{user_name}'s cosmic space adventure became legendary," in captured.out
    assert "reminding everyone that the stars were not just distant lights," in captured.out


def test_create_pages_2():
    user_name = "Bob"
    pages = create_pages_2(user_name)
    assert isinstance(pages[0], Page)
    assert len(pages) == 10
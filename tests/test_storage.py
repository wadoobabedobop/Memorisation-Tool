from datetime import datetime

from memorisation_tool.storage import load_cards, save_cards, DATA_FILE
from memorisation_tool.models import Flashcard


def test_save_and_load(tmp_path):
    data_file = tmp_path / 'cards.json'
    import memorisation_tool.storage as storage
    original = storage.DATA_FILE
    try:
        storage.DATA_FILE = data_file
        cards = [Flashcard('q1', 'a1')]
        save_cards(cards)
        assert data_file.exists()

        loaded = load_cards()
        assert len(loaded) == 1
        assert loaded[0].question == 'q1'
        assert loaded[0].answer == 'a1'
        assert isinstance(loaded[0].last_reviewed, datetime)
    finally:
        storage.DATA_FILE = original

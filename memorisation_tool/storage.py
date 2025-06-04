import json
from pathlib import Path
from datetime import datetime
from typing import List

from .models import Flashcard

DATA_FILE = Path('cards.json')


def load_cards() -> List[Flashcard]:
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open('r', encoding='utf-8') as f:
        data = json.load(f)
    cards = []
    for item in data:
        card = Flashcard(
            question=item['question'],
            answer=item['answer'],
            box=item.get('box', 1),
            last_reviewed=datetime.fromisoformat(item['last_reviewed'])
        )
        cards.append(card)
    return cards


def save_cards(cards: List[Flashcard]) -> None:
    data = []
    for card in cards:
        data.append({
            'question': card.question,
            'answer': card.answer,
            'box': card.box,
            'last_reviewed': card.last_reviewed.isoformat()
        })
    with DATA_FILE.open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

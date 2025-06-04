import argparse
from datetime import datetime, timezone

from .storage import load_cards, save_cards
from .models import Flashcard


def add_card(question: str, answer: str) -> None:
    cards = load_cards()
    cards.append(Flashcard(question=question, answer=answer))
    save_cards(cards)
    print('Card added.')


def review_cards() -> None:
    cards = load_cards()
    now = datetime.now(timezone.utc)
    due_cards = [c for c in cards if c.next_review() <= now]
    if not due_cards:
        print('No cards due for review.')
        return
    for card in due_cards:
        print(f'Question: {card.question}')
        input('Press Enter to see the answer...')
        print(f'Answer: {card.answer}')
        resp = input('Did you get it right? [y/N] ').strip().lower()
        if resp == 'y':
            card.box = min(card.box + 1, 5)
        else:
            card.box = 1
        card.last_reviewed = now
    save_cards(cards)


def main(argv=None):
    parser = argparse.ArgumentParser(description='Memorisation Tool')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a flashcard')
    add_parser.add_argument('question')
    add_parser.add_argument('answer')

    subparsers.add_parser('review', help='Review flashcards')

    args = parser.parse_args(argv)
    if args.command == 'add':
        add_card(args.question, args.answer)
    elif args.command == 'review':
        review_cards()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

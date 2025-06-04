# Memorisation Tool

A simple command-line flashcard application using the Leitner system.

## Usage

Add a card:

```bash
python -m memorisation_tool add "Question" "Answer"
```

Review due cards:

```bash
python -m memorisation_tool review
```

Run the package directly with `-m` to get help:

```bash
python -m memorisation_tool --help
```

Cards are stored in `cards.json` in the current directory.

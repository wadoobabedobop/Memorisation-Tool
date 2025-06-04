from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

@dataclass
class Flashcard:
    question: str
    answer: str
    box: int = 1
    last_reviewed: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def next_review(self) -> datetime:
        intervals = {
            1: timedelta(days=1),
            2: timedelta(days=3),
            3: timedelta(days=7),
            4: timedelta(days=14),
            5: timedelta(days=30),
        }
        return self.last_reviewed + intervals.get(self.box, timedelta(days=30))

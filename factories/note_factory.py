from dataclasses import dataclass
from faker import Faker


@dataclass
class NoteData:
    title: str
    content: str


class NoteFactory:
    def __init__(self):
        self.fake = Faker()

    def create_valid_note(self) -> NoteData:
        """Create a valid note with random data"""
        return NoteData(
            title=self.fake.sentence(),
            content=self.fake.paragraph()
        )

    def create_invalid_note(self) -> NoteData:
        """Create an invalid note (empty fields)"""
        return NoteData(title="", content="")

    def create_specific_note(self, title: str, content: str) -> NoteData:
        """Create a note with specific data"""
        return NoteData(title=title, content=content)

import requests


class NotePage:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.notes_endpoint = f"{base_url}/notes"

    def create_note(self, note_data: dict) -> requests.Response:
        """Send POST request to create a note"""
        return requests.post(self.notes_endpoint, json=note_data)

    def get_all_notes(self) -> requests.Response:
        """Send GET request to get all notes"""
        return requests.get(self.notes_endpoint)

    def get_note_by_id(self, note_id: int) -> requests.Response:
        """Send GET request to get note by ID"""
        return requests.get(f"{self.notes_endpoint}/{note_id}")

    def update_note(self, note_id: int, note_data: dict) -> requests.Response:
        """Send PUT request to update note"""
        return requests.put(f"{self.notes_endpoint}/{note_id}", json=note_data)

    def delete_note(self, note_id: int) -> requests.Response:
        """Send DELETE request to delete note"""
        return requests.delete(f"{self.notes_endpoint}/{note_id}")

    def clear_notes(self) -> None:
        """Clear all notes (for test setup)"""
        notes = self.get_all_notes().json()
        for note in notes:
            self.delete_note(note['id'])

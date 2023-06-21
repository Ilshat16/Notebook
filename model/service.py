from model.note import Note
from model.notebook import Notebook


class Service:
    def __init__(self):
        self._notebook = Notebook()

    def add_note(self, header, body):
        note = Note(header, body)
        self._notebook.add_note(note)

    def change_note(self, id_, changed_header, changed_body):
        note = self._notebook.pop_note(id_ - 1)
        note.set_header(changed_header)
        note.set_body(changed_body)
        note.set_date()
        self._notebook.insert_note(id_ - 1, note)

    def get_info(self):
        return self._notebook

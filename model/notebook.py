class Notebook:
    def __init__(self):
        self._note_list = list()

    def add_note(self, note):
        self._note_list.append(note)

    def __str__(self):
        return "\n\n".join(map(str, self._note_list))

    def pop_note(self, id_):
        return self._note_list.pop(id_)

    def insert_note(self, id_, note):
        self._note_list.insert(id_, note)

class Notebook:
    def __init__(self):
        self._note_list = list()

    def add_note(self, note):
        self._note_list.append(note)

    def __str__(self):
        return "\n\n".join(map(str, self._note_list))

    def pop_note(self, id_):
        return self._note_list.pop(id_)

    def del_note(self, id_):
        self.pop_note(id_ - 1)
        for i in range(id_ - 1, len(self._note_list)):
            self._note_list[i].set_id(i + 1)

    def insert_note(self, id_, note):
        self._note_list.insert(id_, note)

    def get_notebook_length(self):
        return len(self._note_list)

    def get_dict(self):
        note_dict = dict()
        for i in range(len(self._note_list)):
            note_dict[i] = self._note_list[i].get_dict()
        return note_dict

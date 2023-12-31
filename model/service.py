import datetime
import json

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

    def del_note(self, id_):
        self._notebook.del_note(id_)


    def get_info(self):
        return self._notebook

    def get_notebook_length(self):
        return self._notebook.get_notebook_length()

    def save_json(self, file_name):
        with open(f'{file_name}', 'w') as outfile:
            json.dump(self._notebook.get_dict(), outfile, indent=4)

    def load_json(self, file_name):
        with open(f'{file_name}') as json_file:
            notebook_dict = json.load(json_file)
            load_notebook = Notebook()
            for i in range(len(notebook_dict)):
                note = Note(notebook_dict[f"{i}"]["header"], notebook_dict[f"{i}"]["body"])
                note.set_id(int(notebook_dict[f"{i}"]["id"]))
                note.set_date_time(self._date_parse(notebook_dict[f"{i}"]["date"]))
                load_notebook.add_note(note)
        self._notebook = load_notebook

    def _date_parse(self, date_time):
        date = date_time.split()[0]
        time = date_time.split()[1]
        date_list = date.split("/")
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
        time_list = time.split(":")
        hour = int(time_list[0])
        min = int(time_list[1])
        sec = int(time_list[2])
        return datetime.datetime(year, month, day, hour, min, sec)

    def selection_by_date(self, date):
        selection_result = Notebook()
        count = 0
        for note in self._notebook.get_notebook():
            if note.get_date() == date:
                count += 1
                note.set_id(count)
                selection_result.add_note(note)
        self.save_json("temp")
        return selection_result


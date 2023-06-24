import datetime


class Note:
    id_ = 0

    def __init__(self, header, body):
        Note.id_ += 1
        self._number = Note.id_
        self._header = header
        self._body = body
        self._date = datetime.datetime.now()

    def __str__(self):
        return f"{self._number}. {self._header}:\n{self._body}\n" \
               f"Дата создания: {self._date.strftime('%d/%m/%Y %H:%M:%S')}"

    def set_id(self, id_):
        self._number = id_

    def set_header(self, header):
        self._header = header

    def set_body(self, body):
        self._body = body

    def set_date(self):
        self._date = datetime.datetime.now()

    def set_date_time(self, date_time):
        self._date = date_time

    def get_dict(self):
        note_dict = dict()
        note_dict["id"] = self._number
        note_dict["header"] = self._header
        note_dict["body"] = self._body
        note_dict["date"] = self._date.strftime('%d/%m/%Y %H:%M:%S')
        return note_dict

    def get_date(self):
        return self._date.strftime("%d/%m/%Y")

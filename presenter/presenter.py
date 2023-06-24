class Presenter:
    def __init__(self, service):
        self._service = service

    def add_note(self, header, body):
        self._service.add_note(header, body)

    def change_note(self, id_, header, body):
        self._service.change_note(id_, header, body)

    def del_note(self, id_):
        self._service.del_note(id_)

    def get_info(self):
        return self._service.get_info()

    def get_notebook_length(self):
        return self._service.get_notebook_length()

    def save_json(self, file_name):
        self._service.save_json(file_name)

    def load_json(self, file_name):
        self._service.load_json(file_name)
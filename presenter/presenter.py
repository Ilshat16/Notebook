class Presenter:
    def __init__(self, service):
        self._service = service

    def add_note(self, header, body):
        self._service.add_note(header, body)

    def change_note(self, id_, header, body):
        self._service.change_note(id_, header, body)

    def get_info(self):
        return self._service.get_info()

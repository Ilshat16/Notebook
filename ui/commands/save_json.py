class Save_json:
    def __init__(self, view):
        self.view = view

    def description(self):
        return "Сохранить записную книжку"

    def execute(self):
        self.view.save_json()

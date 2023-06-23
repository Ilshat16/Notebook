class Load_json:
    def __init__(self, view):
        self.view = view

    def description(self):
        return "Загрузить записную книжку"

    def execute(self):
        self.view.load_json()

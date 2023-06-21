class Finish:
    def __init__(self, view):
        self.view = view

    def description(self):
        return "Выйти из программы"

    def execute(self):
        self.view.finish()

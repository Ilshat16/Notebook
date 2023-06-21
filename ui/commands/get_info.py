class Get_info:
    def __init__(self, view):
        self.view = view

    def description(self):
        return "Показать все заметки"

    def execute(self):
        self.view.get_info()

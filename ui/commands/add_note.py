class Add_note:
    def __init__(self, view):
        self.view = view

    def description(self):
        return "Добавить заметку"

    def execute(self):
        self.view.add_note()

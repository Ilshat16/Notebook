class Change_note:
    def __init__(self, view):
        self.view = view

    def description(self):
        return "Изменить заметку"

    def execute(self):
        self.view.change_note()

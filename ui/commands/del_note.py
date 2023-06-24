class Del_note:
    def __init__(self, view):
        self.view = view

    def description(self):
        return "Удалить заметку"

    def execute(self):
        self.view.del_note()

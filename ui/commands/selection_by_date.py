class Selection_by_date:
    def __init__(self, view):
        self.view = view

    def description(self):
        return "Вывести все заметки для выбранной даты"

    def execute(self):
        self.view.selection_by_date()

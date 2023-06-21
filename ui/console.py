from ui.menu import Menu


class Console:
    def __init__(self, presenter):
        self._presenter = presenter
        self._menu = Menu(self)
        self._work = True

    def start(self):
        while self._work:
            self._menu.show_menu()
            self.execute()

    def execute(self):
        command_id = int(input("Введите номер команды: "))
        self._menu.execute(command_id)

    def add_note(self):
        header = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        self._presenter.add_note(header, body)

    def change_note(self):
        id_ = int(input("Введите номер заметки: "))
        header = input("Введите измененный заголовок: ")
        body = input("Введите измененный текст заметки: ")
        self._presenter.change_note(id_, header, body)

    def get_info(self):
        print(self._presenter.get_info())

    def finish(self):
        self._work = False

from ui.menu import Menu
from ui.errors_handling import numeric_input_exceptions


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
        command_id = self.input_command_number()
        self._menu.execute(command_id)

    def add_note(self):
        header = input("Введите заголовок заметки: ")
        body = input("Введите текст заметки: ")
        self._presenter.add_note(header, body)

    def change_note(self):
        id_ = self.input_note_id()
        header = input("Введите измененный заголовок: ")
        body = input("Введите измененный текст заметки: ")
        self._presenter.change_note(id_, header, body)

    def get_info(self):
        print(self._presenter.get_info())

    def finish(self):
        self._work = False

    def input_command_number(self):
        error = True
        while error:
            command_id = numeric_input_exceptions("Введите номер команды")
            if command_id > self._menu.get_len() or command_id <= 0:
                print("Такой команды не существует")
            else:
                error = False
        return command_id

    def input_note_id(self):
        if self._presenter.get_notebook_length() == 0:
            raise IndexError ("В записной книге нет заметок")
        error = True
        while error:
            id_ = numeric_input_exceptions("Введите номер заметки")
            if id_ > self._presenter.get_notebook_length():
                print(f"В записной книжке не больше {self._presenter.get_notebook_length()} "
                      f"заметок")
            elif id_ <= 0:
                print("Номер команды должен быть больше нуля")
            else:
                error = False
        return id_

    def save_json(self):
        file_name = input("Введите название сохраняемого файла: ")
        self._presenter.save_json(file_name)
        print("Сохренение прошло успешно")

    def load_json(self):
        file_name = input("Введите название загружаемого файла: ")
        try:
            self._presenter.load_json(file_name)
            print("Загрузка прошла успешно")
        except FileNotFoundError:
            print("Нет такого файла")
            self.finish()

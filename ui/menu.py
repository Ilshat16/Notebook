from ui.commands.add_note import Add_note
from ui.commands.change_note import Change_note
from ui.commands.del_note import Del_note
from ui.commands.finish import Finish
from ui.commands.get_info import Get_info
from ui.commands.load_json import Load_json
from ui.commands.save_json import Save_json
from ui.commands.selection_by_date import Selection_by_date


class Menu:
    def __init__(self, view):
        self._menu = list()
        self._menu.append(Add_note(view))
        self._menu.append(Change_note(view))
        self._menu.append(Del_note(view))
        self._menu.append(Get_info(view))
        self._menu.append(Selection_by_date(view))
        self._menu.append(Save_json(view))
        self._menu.append(Load_json(view))
        self._menu.append(Finish(view))

    def show_menu(self):
        for i in range(len(self._menu)):
            print(f"{i + 1}: {self._menu[i].description()}")

    def execute(self, command_id):
        self._menu[command_id - 1].execute()

    def get_len(self):
        return len(self._menu)

from model.service import Service
from presenter.presenter import Presenter
from ui.console import Console

service = Service()
presenter = Presenter(service)
console = Console(presenter)
console.start()

import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._metodoScelto = None

    def fillYear(self):
        self._view._ddyear.options.append(ft.dropdown.Option(key = "2015", data = 2015))
        self._view._ddyear.options.append(ft.dropdown.Option(key = "2016", data = 2016))
        self._view._ddyear.options.append(ft.dropdown.Option(key = "2017", data = 2017))
        self._view._ddyear.options.append(ft.dropdown.Option(key = "2018", data = 2018))
        self._view.update_page()

    def fillMethods(self):
        metodi = self._model.getMetodi()
        for metodo in metodi:
            self._view._ddmetodo.options.append(ft.dropdown.Option(key=str(metodo), data=metodo, on_click=self._sceltaMetodo))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        pass

    def handleProdotti(self, e):
        pass

    def _sceltaMetodo(self, e):
        self._metodoScelto = e.control.data
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
        if self._view._ddyear.value is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Devi prima scegliere un anno!", color = "red"))
            self._view.update_page()
            return
        anno = self._view._ddyear.value
        if self._view._ddmetodo.value is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Devi prima scegliere un metodo", color = "red"))
            self._view.update_page()
            return
        if self._view._txtIn.value is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Devi prima scegliere un valore di s%!", color = "red"))
            self._view.update_page()
            return
        s = self._view._txtIn.value
        try:
            s = float(s)
        except ValueError:
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text("Devi inserire un valore float di %s", color="red"))
                self._view.update_page()
                return
        if s < 0:
                self._view.txt_result.controls.clear()
                self._view.txt_result.controls.append(ft.Text("Devi scegliere un valore di %s maggiore di 0", color="red"))
                self._view.update_page()
                return
        self._view.txt_result.controls.clear()
        self._model.buildGraph(anno, self._metodoScelto.Order_method_code, s)
        n,a = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato."))
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {n} vertici."))
        self._view.txt_result.controls.append(ft.Text(f"Ci sono {a} archi."))
        self._view.txt_result.controls.append(ft.Text(f""))
        self._view._btnProdotti.disabled = False
        self._view.update_page()

    def handleProdotti(self, e):
        prodotti = self._model.prodottiRedditizzi()
        self._view.txt_result.controls.append(ft.Text(f"I prodotti più redditizzi sono:"))
        for prodotto in prodotti:
            self._view.txt_result.controls.append(ft.Text(f"Prodotto {prodotto[0].Product_number}     Archi entranti={prodotto[1]} Ricavo={prodotto[0].VenditaTot}"))
        self._view.update_page()

    def _sceltaMetodo(self, e):
        self._metodoScelto = e.control.data
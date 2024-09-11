import flet as ft
import networkx as nx

from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
    def fillDDanni(self):
        self._view.ddyear.options.clear()
        listaAnni=self._model.getAnni()
        for a in listaAnni:
            self._view.ddyear.options.append(ft.dropdown.Option(f"{a}"))
        self._view.update_page()

    def fillDDforme(self, e): #è una funzione onchange quindi va dato come parametro la "e" !!!!!
        annoSelezionato=self._view.ddyear.value
        self._view.ddshape.options.clear()
        listaForme = self._model.getForme(annoSelezionato)
        listaForme.sort()
        for f in listaForme:
            self._view.ddshape.options.append(ft.dropdown.Option(f"{f}"))
        self._view.update_page()

    def handle_graph(self, e):
        a=self._view.ddyear.value
        f=self._view.ddshape.value
        if a=="" or a=="Anno" or a==None:
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(ft.Text(f"Selezionare un anno e poi una forma"))
            self._view.update_page()
            return
        if f=="" or f=="Shape" or f==None:
            self._view.txt_result1.controls.clear()
            self._view.txt_result1.controls.append(ft.Text(f"Selezionare una forma"))
            self._view.update_page()
            return

        self._model.creaGrafo(a,f)

        self._view.txt_result1.controls.clear() #!!!!

        self._view.txt_result1.controls.append(ft.Text(f"Numero nodi: {len(self._model._grafo.nodes())}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero archi: {self._model._grafo.number_of_edges()}"))
        self._view.txt_result1.controls.append(ft.Text(
            f"Numero comoponenti debolmente connesse: {nx.number_weakly_connected_components(self._model._grafo)}"))

        componenteConnessaMaggiore=max(nx.weakly_connected_components(self._model._grafo), key=len)

        self._view.txt_result1.controls.append(ft.Text(
            f"La componente connessa più grande ha: {len(componenteConnessaMaggiore)} nodi"))

        for nodo in componenteConnessaMaggiore:
            self._view.txt_result1.controls.append(ft.Text(f"{nodo}"))

        self._view.update_page() #!!!!!


    def handle_path(self, e):
        pass

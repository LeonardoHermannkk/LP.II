'''Leonardo Hermann'''
# pesquisei algumas como resolver algumas partes

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:
    def __init__(self):

        self.contador = 0

        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Contador de Cliques")
        janela.set_border_width(20)
        janela.set_default_size(250, 150)

        # organiza o rótulo em cima do botão

        caixa_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)

        # exibe o contador
        self.lb_contador = Gtk.Label(label="0")
        self.lb_contador.set_justify(Gtk.Justification.CENTER)

        bt_clique = Gtk.Button(label="Clica ai ze")
        bt_clique.connect("clicked", self.incrementar)

        caixa_vert.pack_start(self.lb_contador, expand=True, fill=True, padding=0)
        caixa_vert.pack_start(bt_clique, expand=False, fill=False, padding=0)

        janela.add(caixa_vert)
        janela.show_all()

    def incrementar(self, componente=None, dados=None):
        # chama a cada click

        self.contador += 1
        self.lb_contador.set_label(str(self.contador))

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
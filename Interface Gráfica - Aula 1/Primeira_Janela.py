import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
   """ Define a interface da Aplicação """
   def __init__(self):
       """ __init__() -> instância de Aplicação """
       janela = Gtk.Window()
       janela.show()
if __name__ == '__main__':
   prog = Aplicacao()
   Gtk.main()
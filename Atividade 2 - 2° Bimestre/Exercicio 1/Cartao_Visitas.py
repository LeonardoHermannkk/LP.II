# Feito por: Maria Luiza Urbano Delfino

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# janela principal
janela = Gtk.Window()
janela.set_title("Cartão de Visitas Digital")
janela.set_default_size(400, 200)

# Cria a caixa vertical para organizar os elementos
vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
lbl_nome = Gtk.Label(label="Maria Luiza Urbano Delfino")
lbl_curso = Gtk.Label(label="Informática")

# Adiciona os elementos na caixa
vbox.pack_start(lbl_nome, True, True, 0)
vbox.pack_start(lbl_curso, True, True, 0)

# Adiciona a caixa na janela
janela.add(vbox)

# fecha o programa ao clicar no X
janela.connect("destroy", Gtk.main_quit)
janela.show_all()
Gtk.main()
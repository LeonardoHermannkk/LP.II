# Feito por: Maria Luiza Urbano Delfino

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk  

class TelaLogin(Gtk.Window):
    def __init__(self):
        super().__init__(title="Login")
        self.set_default_size(300, 220)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        
        # Usuário
        lbl_usuario = Gtk.Label(label="Usuário:")
        vbox.pack_start(lbl_usuario, False, False, 0)
        self.txt_usuario = Gtk.Entry()
        vbox.pack_start(self.txt_usuario, False, False, 0)
        
        # Senha
        lbl_senha = Gtk.Label(label="Senha:")
        vbox.pack_start(lbl_senha, False, False, 0)
        self.txt_senha = Gtk.Entry()
        self.txt_senha.set_visibility(False)  # Deixa a senha oculta
        vbox.pack_start(self.txt_senha, False, False, 0)
        
        # Botão Entrar
        btn_entrar = Gtk.Button(label="Entrar")
        btn_entrar.connect("clicked", self.autenticar)
        vbox.pack_start(btn_entrar, False, False, 10)
        self.lbl_status = Gtk.Label(label="")
        vbox.pack_start(self.lbl_status, False, False, 5)
        
        self.add(vbox)
        
    def autenticar(self, widget):
        usuario_digitado = self.txt_usuario.get_text()
        senha_digitada = self.txt_senha.get_text()
        
        # Definição das cores 
        cor_verde = Gdk.RGBA(0.0, 0.5, 0.0, 1.0)  
        cor_vermelha = Gdk.RGBA(0.8, 0.0, 0.0, 1.0)   
        if usuario_digitado == "admin" and senha_digitada == "123":
            self.lbl_status.set_text("Acesso Liberado")
            # Aplica a cor verde no rótulo
            self.lbl_status.override_color(Gtk.StateFlags.NORMAL, cor_verde)
        else:
            self.lbl_status.set_text("Acesso Negado")
            # Aplica a cor vermelha no rótulo
            self.lbl_status.override_color(Gtk.StateFlags.NORMAL, cor_vermelha)

# Execução 
win = TelaLogin()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
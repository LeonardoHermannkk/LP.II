# Feito por: Maria Luiza Urbano Delfino

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FormInscricao(Gtk.Window):
    def __init__(self):
        super().__init__(title="Inscrição em Evento")
        self.set_default_size(350, 300)
        self.set_border_width(15)
        self.set_position(Gtk.WindowPosition.CENTER)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

         # Nome
        lbl_nome = Gtk.Label(label="Nome Completo:", xalign=0)
        vbox.pack_start(lbl_nome, False, False, 0)
        self.txt_nome = Gtk.Entry()
        vbox.pack_start(self.txt_nome, False, False, 0)
        
        # Curso
        lbl_curso = Gtk.Label(label="Selecione o seu Curso:", xalign=0)
        vbox.pack_start(lbl_curso, False, False, 0)
        self.cb_curso = Gtk.ComboBoxText()

        # opções de cursos técnicos integrados
        self.cb_curso.append_text("Técnico Integrado em Informática")
        self.cb_curso.append_text("Técnico Integrado em Edificações")
        self.cb_curso.append_text("Técnico Integrado em Mecatrônica")
        self.cb_curso.set_active(0) # Deixa a primeira opção selecionada por padrão
        vbox.pack_start(self.cb_curso, False, False, 0)
        
        # Caixa de Seleção do Certificado
        self.chk_certificado = Gtk.CheckButton(label="Deseja certificado?")
        vbox.pack_start(self.chk_certificado, False, False, 5)
        
        # Botão Salvar
        btn_salvar = Gtk.Button(label="Salvar Inscrição")
        btn_salvar.connect("clicked", self.exibir_resumo)
        vbox.pack_start(btn_salvar, False, False, 10)   
        self.lbl_resumo = Gtk.Label(label="")
        self.lbl_resumo.set_xalign(0)
        vbox.pack_start(self.lbl_resumo, True, True, 10)
        
        self.add(vbox)
        
    def exibir_resumo(self, widget):
        nome_participante = self.txt_nome.get_text()
        curso_selecionado = self.cb_curso.get_active_text()
        
        # Verifica se o CheckButton está marcado (True) ou desmarcado (False)
        precisa_certificado = self.chk_certificado.get_active()
        
        # Define o texto baseado na escolha do CheckButton
        if precisa_certificado:
            texto_certificado = "Sim"
        else:
            texto_certificado = "Não"
            
        resumo = (
            f"--- RESUMO DA INSCRIÇÃO ---\n"
            f"Participante: {nome_participante}\n"
            f"Curso: {curso_selecionado}\n"
            f"Emitir Certificado: {texto_certificado}"
        )  

        self.lbl_resumo.set_text(resumo)
        print(resumo)

# Execução
win = FormInscricao()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
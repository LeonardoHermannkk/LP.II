'''Leonardo Hermann'''
# pesquisei algumas como resolver algumas partes

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Notas Escolares")
        janela.set_border_width(15)
        janela.set_resizable(False)

        caixa_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        # nota 1
        caixa_n1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lb_n1 = Gtk.Label(label="Nota 1:")
        self.txf_n1 = Gtk.Entry()
        caixa_n1.pack_start(lb_n1, expand=False, fill=False, padding=0)
        caixa_n1.pack_start(self.txf_n1, expand=True, fill=True, padding=0)

        # nota 2
        caixa_n2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lb_n2 = Gtk.Label(label="Nota 2:")
        self.txf_n2 = Gtk.Entry()
        caixa_n2.pack_start(lb_n2, expand=False, fill=False, padding=0)
        caixa_n2.pack_start(self.txf_n2, expand=True, fill=True, padding=0)

        # nota 3
        caixa_n3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lb_n3 = Gtk.Label(label="Nota 3:")
        self.txf_n3 = Gtk.Entry()
        caixa_n3.pack_start(lb_n3, expand=False, fill=False, padding=0)
        caixa_n3.pack_start(self.txf_n3, expand=True, fill=True, padding=0)

        bt_media = Gtk.Button(label="Calcular Média")
        bt_media.connect("clicked", self.calcular_media)

        self.lb_resultado = Gtk.Label(label="Informe as 3 notas parciais.")
        self.lb_resultado.set_justify(Gtk.Justification.CENTER)

        # Caixa da recuperação, so aparece se media < 6
        
        self.caixa_recuperacao = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        lb_rec = Gtk.Label(label="Nota da Prova de Recuperação:")
        self.txf_recuperacao = Gtk.Entry()
        bt_recalcular = Gtk.Button(label="Recalcular")
        bt_recalcular.connect("clicked", self.recalcular)
        self.txf_recuperacao.connect("activate", self.recalcular)

        self.caixa_recuperacao.add(lb_rec)
        self.caixa_recuperacao.add(self.txf_recuperacao)
        self.caixa_recuperacao.add(bt_recalcular)

        caixa_vert.pack_start(caixa_n1, expand=False, fill=False, padding=5)
        caixa_vert.pack_start(caixa_n2, expand=False, fill=False, padding=5)
        caixa_vert.pack_start(caixa_n3, expand=False, fill=False, padding=5)
        caixa_vert.pack_start(bt_media, expand=False, fill=False, padding=5)
        caixa_vert.pack_start(self.lb_resultado, expand=False, fill=False, padding=10)
        caixa_vert.pack_start(self.caixa_recuperacao, expand=False, fill=False, padding=5)

        janela.add(caixa_vert)
        janela.show_all()

        self.caixa_recuperacao.hide()

    def calcular_media(self, componente=None, dados=None):
        try:
            n1 = float(self.txf_n1.get_text())
            n2 = float(self.txf_n2.get_text())
            n3 = float(self.txf_n3.get_text())

            # guarda a media pra usar depois
            self.media_parcial = (n1 + n2 + n3) / 3

            if self.media_parcial >= 6.0:
                msg = "<b>Média: {:.2f}</b>\nAprovado"
                msg = msg.format(self.media_parcial)
                self.lb_resultado.set_markup(msg)
                self.caixa_recuperacao.hide()
            else:
                msg = "<b>Média: {:.2f}</b>\nReprovado - recuperação"
                msg = msg.format(self.media_parcial)
                self.lb_resultado.set_markup(msg)
                self.caixa_recuperacao.show()
                self.caixa_recuperacao.show_all()

        except ValueError:
            self.lb_resultado.set_markup(
                "<span color='red'>Digite apenas números nas 3 notas.</span>")

    def recalcular(self, componente=None, dados=None):
        try:
            nota_rec = float(self.txf_recuperacao.get_text())
            media_final = (self.media_parcial + nota_rec) / 2

            if media_final >= 6.0:
                msg = "<b>Nova Média: {:.2f}</b>\nAprovado após recuperação"
            else:
                msg = "<b>Nova Média: {:.2f}</b>\nReprovado"

            msg = msg.format(media_final)
            self.lb_resultado.set_markup(msg)

        except ValueError:
            self.lb_resultado.set_markup(
                "<span color='red'>Digite um número válido </span>")

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
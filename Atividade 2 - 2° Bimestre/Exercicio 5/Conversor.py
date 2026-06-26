# Feito por: Maria Luiza Urbano Delfino

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ConversorMoedas(Gtk.Window):
    def __init__(self):
        super().__init__(title="Conversor de Moedas")
        self.set_default_size(350, 200)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        # Texto de instrução e campo de entrada de texto
        lbl_instrucao = Gtk.Label(label="Digite o valor em Reais (R$):")
        vbox.pack_start(lbl_instrucao, False, False, 0)
        self.txt_reais = Gtk.Entry()
        vbox.pack_start(self.txt_reais, False, False, 0)
        
        hbox_botoes = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        # Criação dos botões
        btn_dolar = Gtk.Button(label="Dólar")
        btn_euro = Gtk.Button(label="Euro")
        btn_bitcoin = Gtk.Button(label="Bitcoin")
        # Conecta cada botão a sua  função
        btn_dolar.connect("clicked", self.converter_dolar)
        btn_euro.connect("clicked", self.converter_euro)
        btn_bitcoin.connect("clicked", self.converter_bitcoin)
        # adiciona os botões na caixa
        hbox_botoes.pack_start(btn_dolar, True, True, 0)
        hbox_botoes.pack_start(btn_euro, True, True, 0)
        hbox_botoes.pack_start(btn_bitcoin, True, True, 0)
        vbox.pack_start(hbox_botoes, False, False, 5)
        # vai exibir o resultado
        self.lbl_resultado = Gtk.Label(label="Resultado: R$ 0,00")
        vbox.pack_start(self.lbl_resultado, True, True, 10)
        
        self.add(vbox)

    def converter_dolar(self, widget):
        valor_reais = float(self.txt_reais.get_text())
        resultado = valor_reais / 5.50
        self.lbl_resultado.set_text(f"US$ {resultado:.2f}")

    def converter_euro(self, widget):
        valor_reais = float(self.txt_reais.get_text())
        resultado = valor_reais / 6.00
        self.lbl_resultado.set_text(f"€ {resultado:.2f}")

    def converter_bitcoin(self, widget):
        valor_reais = float(self.txt_reais.get_text())
        resultado = valor_reais / 350000.00
        self.lbl_resultado.set_text(f"{resultado:.6f} BTC")

# execução
win = ConversorMoedas()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
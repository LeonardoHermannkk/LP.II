""""
Feito por: Maria Luiza Urbano Delfino e Leonardo
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from modelo import Calculadora

# janela da calculadora
class TelaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__(title="Calculadora")
        self.set_default_size(250, 350)
        self.set_border_width(10)
        
        # calculos do arquivo modelo.py       
        self.calc = Calculadora()

        self.valor1 = None
        self.valor2 = None
        self.operador = None
        
        # organiza os elementos
        box_principal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_principal)

        # cria o visor da calculadora
        self.visor = Gtk.Entry()
        self.visor.set_editable(False)
        self.visor.set_alignment(1.0)
        self.visor.set_text("0")
        box_principal.pack_start(self.visor, False, False, 10)

        # cria a grade dos botoes
        grade = Gtk.Grid()
        grade.set_row_spacing(6)
        grade.set_column_spacing(6)
        grade.set_row_homogeneous(True)
        grade.set_column_homogeneous(True)
        box_principal.pack_start(grade, True, True, 0)

        # cria os botoes
        btn_on = Gtk.Button(label="ON")
        btn_c = Gtk.Button(label="C")
        btn_raiz = Gtk.Button(label="√")

        btn_7 = Gtk.Button(label="7")
        btn_8 = Gtk.Button(label="8")
        btn_9 = Gtk.Button(label="9")
        btn_soma = Gtk.Button(label="+")

        btn_4 = Gtk.Button(label="4")
        btn_5 = Gtk.Button(label="5")
        btn_6 = Gtk.Button(label="6")
        btn_sub = Gtk.Button(label="-")

        btn_1 = Gtk.Button(label="1")
        btn_2 = Gtk.Button(label="2")
        btn_3 = Gtk.Button(label="3")
        btn_mult = Gtk.Button(label="*")

        btn_0 = Gtk.Button(label="0")
        btn_igual = Gtk.Button(label="=")
        btn_div = Gtk.Button(label="/")

        # posiciona os botoes na grade
        grade.attach(btn_on, 0, 0, 1, 1)
        grade.attach(btn_c, 1, 0, 1, 1)
        grade.attach(btn_raiz, 3, 0, 1, 1)

        grade.attach(btn_7, 0, 1, 1, 1)
        grade.attach(btn_8, 1, 1, 1, 1)
        grade.attach(btn_9, 2, 1, 1, 1)
        grade.attach(btn_soma, 3, 1, 1, 1)

        grade.attach(btn_4, 0, 2, 1, 1)
        grade.attach(btn_5, 1, 2, 1, 1)
        grade.attach(btn_6, 2, 2, 1, 1)
        grade.attach(btn_sub, 3, 2, 1, 1)

        grade.attach(btn_1, 0, 3, 1, 1)
        grade.attach(btn_2, 1, 3, 1, 1)
        grade.attach(btn_3, 2, 3, 1, 1)
        grade.attach(btn_mult, 3, 3, 1, 1)

        grade.attach(btn_0, 0, 4, 1, 1)
        grade.attach(btn_igual, 1, 4, 2, 1)
        grade.attach(btn_div, 3, 4, 1, 1)

        # conecta os botoes nos metodos
        btn_0.connect("clicked", self.ao_clicar_numero)
        btn_1.connect("clicked", self.ao_clicar_numero)
        btn_2.connect("clicked", self.ao_clicar_numero)
        btn_3.connect("clicked", self.ao_clicar_numero)
        btn_4.connect("clicked", self.ao_clicar_numero)
        btn_5.connect("clicked", self.ao_clicar_numero)
        btn_6.connect("clicked", self.ao_clicar_numero)
        btn_7.connect("clicked", self.ao_clicar_numero)
        btn_8.connect("clicked", self.ao_clicar_numero)
        btn_9.connect("clicked", self.ao_clicar_numero)

        # conecta os botoes de operacao nos metodos 
        btn_soma.connect("clicked", self.ao_clicar_operador)
        btn_sub.connect("clicked", self.ao_clicar_operador)
        btn_mult.connect("clicked", self.ao_clicar_operador)
        btn_div.connect("clicked", self.ao_clicar_operador)

        btn_igual.connect("clicked", self.ao_clicar_igual)
        btn_c.connect("clicked", self.ao_clicar_clear)
        btn_raiz.connect("clicked", self.ao_clicar_raiz)

    def ao_clicar_numero(self, botao):
        digito = botao.get_label()
        texto_atual = self.visor.get_text()

        # limita o tamanho do visor
        if len(texto_atual) >= 12:
            return

        if texto_atual == "0":
            self.visor.set_text(digito)
        else:
            self.visor.set_text(texto_atual + digito)

    def ao_clicar_operador(self, botao):
        self.valor1 = float(self.visor.get_text())
        self.operador = botao.get_label()
        self.visor.set_text("0")
    
    # clica no =
    def ao_clicar_igual(self, botao):
        if self.operador is None or self.valor1 is None:
            return
        self.valor2 = float(self.visor.get_text())
        if self.operador == "/" and self.valor2 == 0:
            self.limparTela()
            self.visor.set_text("Erro: Divisão por 0")
            return
        self.realizaOperacao(self.valor1, self.valor2, self.operador)

    # botao c
    def ao_clicar_clear(self, botao):
        self.limparTela()

    # realiza a operacao de raiz quadrada
    def ao_clicar_raiz(self, botao):
        v1 = float(self.visor.get_text())
        if v1 >= 0:
            resultado = self.calc.raizQuadrada(v1)
            self.visor.set_text(str(resultado))
            self.valor1 = resultado
            self.operador = None
        else:
            self.visor.set_text("Erro")

    # reseta os valores
    def limparTela(self):
        self.visor.set_text("0")
        self.valor1 = None
        self.valor2 = None
        self.operador = None
    
    # realiza a operacao de acordo com o operador selecionado
    def realizaOperacao(self, v1, v2, op):
        if op == "+":
            resultado = self.calc.somar(v1, v2)
        elif op == "-":
            resultado = self.calc.subtrair(v1, v2)
        elif op == "*":
            resultado = self.calc.multiplicar(v1, v2)
        elif op == "/":
            resultado = self.calc.dividir(v1, v2)
        
        # atualiza o visor com o resultado da operacao
        self.visor.set_text(str(resultado))
        self.valor1 = resultado
        self.operador = None

if __name__ == "__main__":
    janela = TelaPrincipal()
    janela.connect("destroy", Gtk.main_quit)
    janela.show_all()
    Gtk.main()
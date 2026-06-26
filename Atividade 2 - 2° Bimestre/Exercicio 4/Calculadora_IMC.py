'''Leonardo Hermann'''
# pesquisei algumas como resolver algumas partes

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Calculadora de IMC")
        janela.set_border_width(15)
        janela.set_resizable(False)

        caixa_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        # peso
        caixa_peso = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lb_peso = Gtk.Label(label="Peso (kg):")
        self.txf_peso = Gtk.Entry()
        caixa_peso.pack_start(lb_peso, expand=False, fill=False, padding=0)
        caixa_peso.pack_start(self.txf_peso, expand=True, fill=True, padding=0)

        # altura
        caixa_altura = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        lb_altura = Gtk.Label(label="Altura (m):")
        self.txf_altura = Gtk.Entry()
        caixa_altura.pack_start(lb_altura, expand=False, fill=False, padding=0)
        caixa_altura.pack_start(self.txf_altura, expand=True, fill=True, padding=0)

        bt_calcular = Gtk.Button(label="Calcular")
        bt_calcular.connect("clicked", self.calcular)

        # apertar Enter na caixa de altura tambem calcula 
        self.txf_altura.connect("activate", self.calcular)

        self.lb_resultado = Gtk.Label(label="Informe peso e altura.")
        self.lb_resultado.set_justify(Gtk.Justification.CENTER)

        caixa_vert.pack_start(caixa_peso, expand=False, fill=False, padding=5)
        caixa_vert.pack_start(caixa_altura, expand=False, fill=False, padding=5)
        caixa_vert.pack_start(bt_calcular, expand=False, fill=False, padding=5)
        caixa_vert.pack_start(self.lb_resultado, expand=False, fill=False, padding=10)

        janela.add(caixa_vert)
        janela.show_all()

    def calcular(self, componente=None, dados=None):
        texto_peso = self.txf_peso.get_text()
        texto_altura = self.txf_altura.get_text()

        try: # unico jeito que achei pra tratar caso digite letra
            
            peso = float(texto_peso)
            altura = float(texto_altura)

            if peso <= 0 or altura <= 0:
                self.lb_resultado.set_markup(
                    "<span color='red'>Peso e altura devem ser maiores que zero.</span>")
                return

            imc = peso / (altura * altura)

            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif imc < 25:
                classificacao = "Peso ideal"
            elif imc < 30:
                classificacao = "Sobrepeso"
            elif imc < 35:
                classificacao = "Obesidade Grau I"
            elif imc < 40:
                classificacao = "Obesidade Grau II"
            else:
                classificacao = "Obesidade Grau III"

            msg = "<b>IMC: {:.2f}</b>\n{}"
            msg = msg.format(imc, classificacao)
            self.lb_resultado.set_markup(msg)

        except ValueError:  #pesquisei e foi a forma de tratar o erro 
                            # caso o usuário digite letras ao invés de números
            self.lb_resultado.set_markup(
                "<span color='red'>Digite apenas números válidos!.</span>")

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
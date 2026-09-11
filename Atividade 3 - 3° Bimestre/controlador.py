#maria clara e leonardo

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from modelo import Conta


class Controlador:
    """Conecta a interface gráfica (Glade) com a classe Conta (modelo)."""

    def __init__(self):
        # Cria o objeto do modelo que vai guardar os dados da conta.
        self.conta = Conta()

        # Carrega a interface a partir do arquivo .glade construído
        # pelo Aluno 1 e conecta os handlers definidos nesta classe.
        self.builder = Gtk.Builder()
        try:
            self.builder.add_from_file('conta.glade')
        except Exception as erro:
            # Se o arquivo não existe ou está no lugar errado, o programa
            # avisa no terminal em vez de simplesmente não abrir nada.
            print('ERRO ao carregar conta.glade:', erro)
            raise

        self.builder.connect_signals(self)

        # Busca os widgets pelos IDs combinados no contrato.
        self.jan_principal = self.builder.get_object('jan_principal')
        self.txt_pessoa = self.builder.get_object('txt_pessoa')
        self.txt_consumo = self.builder.get_object('txt_consumo')
        self.lbl_lista = self.builder.get_object('lbl_lista')
        self.lbl_resultado = self.builder.get_object('lbl_resultado')
        self.lbl_rodape = self.builder.get_object('lbl_rodape')

        # Se algum destes widgets vier None, o ID no Glade está diferente
        # do combinado no contrato - avisa no terminal para facilitar achar
        # o erro de digitação.
        widgets = {
            'jan_principal': self.jan_principal,
            'txt_pessoa': self.txt_pessoa,
            'txt_consumo': self.txt_consumo,
            'lbl_lista': self.lbl_lista,
            'lbl_resultado': self.lbl_resultado,
            'lbl_rodape': self.lbl_rodape,
        }
        for nome_widget, objeto in widgets.items():
            if objeto is None:
                print(f'AVISO: widget "{nome_widget}" não foi encontrado '
                      f'no conta.glade. Confira se o ID está exatamente '
                      f'igual ao do contrato.')

        self._atualizar_tela()
        self.jan_principal.show_all()

    def ao_adicionar(self, widget):
        # Handler do botão "Adicionar" e do "activate" do txt_consumo.
        print('ao_adicionar foi chamado')  # confirma que o clique chegou aqui

        nome = self.txt_pessoa.get_text().strip()
        texto_valor = self.txt_consumo.get_text().strip()
        print(f'nome="{nome}" consumo="{texto_valor}"')

        # Validação simples: nome não pode ser vazio e o valor precisa
        # ser um número válido (aceita vírgula ou ponto decimal).
        if not nome:
            print('Nome vazio - nada foi adicionado.')
            return
        try:
            valor = float(texto_valor.replace(',', '.'))
        except ValueError:
            print(f'Consumo inválido: "{texto_valor}" não é um número.')
            return

        self.conta.adicionar(nome, valor)
        print(f'Adicionado: {nome} - {valor}')

        # Limpa os campos e devolve o foco para o próximo cadastro.
        self.txt_pessoa.set_text('')
        self.txt_consumo.set_text('')
        self.txt_pessoa.grab_focus()

        self._atualizar_tela()

    def ao_nova_conta(self, widget):
        # Handler do botão "Nova conta": esvazia o modelo e a tela.
        self.conta.limpar()
        self.txt_pessoa.set_text('')
        self.txt_consumo.set_text('')
        self._atualizar_tela()

    def ao_destruir(self, widget):
        # Handler do sinal destroy da janela principal: encerra o programa.
        Gtk.main_quit()

    def _atualizar_tela(self):
        # Monta o texto da lista de pessoas (uma por linha).
        linhas = [
            f'{nome} — R$ {valor:.2f}'.replace('.', ',')
            for nome, valor in self.conta.listar()
        ]
        self.lbl_lista.set_text('\n'.join(linhas))

        # Monta o texto dos resultados, formatando os valores em R$.
        subtotal = self._formatar_moeda(self.conta.subtotal())
        servico = self._formatar_moeda(self.conta.valor_servico())
        total = self._formatar_moeda(self.conta.total())
        por_pessoa = self._formatar_moeda(self.conta.valor_por_pessoa())
        quem_mais = self.conta.quem_consumiu_mais()

        resultado = (
            f'Subtotal: {subtotal}\n'
            f'Serviço (10%): {servico}\n'
            f'Total: {total}\n'
            f'Cada um paga: {por_pessoa}\n'
            f'Consumiu mais: {quem_mais}'
        )
        self.lbl_resultado.set_text(resultado)

        # Atualiza o contador de pessoas no rodapé.
        total_pessoas = self.conta.total_pessoas()
        self.lbl_rodape.set_text(f'{total_pessoas} pessoa(s) na conta')

    @staticmethod
    def _formatar_moeda(valor):
        # Formata um float como moeda no padrão brasileiro: R$ 1234,56
        return f'R$ {valor:.2f}'.replace('.', ',')


if __name__ == '__main__':
    Controlador()
    Gtk.main()
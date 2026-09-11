#Maria Clara e Leonardo


class Conta:
    """Representa a conta de um grupo de pessoas em um restaurante."""

    TAXA_SERVICO = 0.10

    def __init__(self):
        self._pessoas = []

    def adicionar(self, nome, valor):
        self._pessoas.append((nome, valor))

    def total_pessoas(self):
        return len(self._pessoas)

    def subtotal(self):
        return sum(valor for _, valor in self._pessoas)

    def valor_servico(self):
        return self.subtotal() * self.TAXA_SERVICO

    def total(self):
        return self.subtotal() + self.valor_servico()

    def valor_por_pessoa(self):
        if self.total_pessoas() == 0:
            return 0.0
        return self.total() / self.total_pessoas()

    def quem_consumiu_mais(self):
        if not self._pessoas:
            return '-'
        nome_maior, _ = max(self._pessoas, key=lambda pessoa: pessoa[1])
        return nome_maior

    def listar(self):
        return list(self._pessoas)

    def limpar(self):
        self._pessoas = []
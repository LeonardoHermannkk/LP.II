#Leonardo Hermann e Maria Urbano

from abc import ABC, abstractmethod


class Forma(ABC):
    def __init__(self, cor):
        self.__cor = cor
        
    def get_cor(self):
        return self.__cor

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(Forma):
    def __init__(self, cor, lado):
        super().__init__(cor)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

class Retangulo(Forma):
    def __init__(self, cor, base, altura):
        super().__init__(cor)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Forma):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.raio

class Triangulo(Forma):
    def __init__(self, cor, base, altura, lado1, lado2, lado3):
        super().__init__(cor)
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

class Losango(Forma):
    def __init__(self, cor, diagonal_maior, diagonal_menor, lado):
        super().__init__(cor)
        self.diagonal_maior = diagonal_maior
        self.diagonal_menor = diagonal_menor
        self.lado = lado

    def area(self):
        return (self.diagonal_maior * self.diagonal_menor) / 2

    def perimetro(self):
        return 4 * self.lado

formas = [
    Quadrado("Vermelho", 4),
    Retangulo("Azul", 5, 3),
    Circulo("Verde", 2),
    Triangulo("Amarelo", 4, 3, 3, 4, 5),
    Losango("Roxo", 6, 4, 5)
]

for forma in formas:
    print(f"Cor: {forma.get_cor()} - Área: {forma.area()} - Perímetro: {forma.perimetro()}")

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
## 1. O que aconteceu quando você tentou criar um objeto diretamente da classe Forma?
# R: O Python não deixa e dá um erro. Isso acontece porque a classe Forma é "abstrata", ou seja, ela serve só como um molde para as outras. Como ela não tem as fórmulas de cálculo prontas, não faz sentido criar uma forma que não sabe calcular nada.

# 2. Se você tentar alterar a cor da forma diretamente (ex: forma.__cor = "Azul"), o que acontece? Por que usamos métodos Getters e Setters?
# R: Na verdade, você não consegue mudar a cor original assim. O Python "esconde" variáveis que começam com dois underlines. Se você tentar mudar direto, ele acaba criando uma variável nova com o mesmo nome por fora, mas a cor de verdade lá dentro continua igual. Usamos Getters e Setters para ter mais controle e segurança sobre os dados, evitando que alguém mude algo importante de qualquer jeito.

# 3. Quais códigos você não precisou repetir nas classes filhas por causa da classe Forma?
# R: Eu não precisei criar o atributo da cor nem o método para ler essa cor (get_cor) em cada uma das 5 classes. A classe mãe já resolveu isso para todo mundo, então foi só herdar.

# 4. Como o Python soube qual fórmula de área usar se, dentro do for, chamamos apenas o método .area()?
# R: Isso é por causa do Polimorfismo. Como cada classe (Quadrado, Círculo, etc.) tem sua própria versão do método area(), o Python é esperto o suficiente para olhar o tipo do objeto na hora do loop e usar a fórmula certa para ele.

# 5. Caso você precisasse adicionar os cálculos para área e perímetro de Triângulo Equilátero, o que precisaria fazer?
# R: Seria só criar uma classe nova chamada TrianguloEquilatero, herdar da classe Forma e escrever as fórmulas específicas dele nos métodos de área e perímetro. O resto do código continuaria funcionando igual.

# 6. Explique o que é o princípio de aberto/fechado dentro do SOLID. Como este princípio pode ser visto nesta estrutura que vocês montaram?
# R: Esse princípio diz que o código deve ser fácil de aumentar (aberto para extensão), mas que não devemos precisar mexer no que já está pronto (fechado para modificação). No nosso projeto, se eu quiser colocar mais 20 formas diferentes, eu só crio as classes novas. Não preciso mudar nada na classe Forma nem no loop que imprime os resultados, o que evita criar erros novos no que já estava funcionando.
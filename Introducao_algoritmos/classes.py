"""
Em Python, as classes são uma parte fundamental da programação orientada a objetos (POO). 
Uma classe é um modelo ou uma planta para criar objetos, que são instâncias dessa classe. 
As classes definem atributos e métodos que os objetos podem ter.
"""  
# Definindo uma Classe:
"""
Para criar uma classe em Python, você usa a palavra-chave class, seguida pelo nome da classe. 
Por convenção, os nomes de classe em Python geralmente começam com uma letra maiúscula. 
A estrutura básica de uma classe é a seguinte:


class MinhaClasse:
    # Atributos e métodos da classe

"""    

# Atributos da Classe:
"""
Os atributos são variáveis que armazenam informações sobre o objeto da classe. 
Eles são definidos dentro da classe e têm um valor padrão. 
Você pode acessar os atributos usando a notação de ponto.
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("Bruno", 38)
print(pessoa1.nome)  # Isso imprimirá "Bruno"
print(pessoa1.idade)  # Isso imprimirá 38

pessoa2 = Pessoa("Felipe", 20)
print(pessoa2.nome)
print(pessoa2.idade)

# Métodos da Classe:
"""
Métodos são funções definidas dentro da classe que realizam operações relacionadas a objetos dessa classe. 
Métodos podem acessar e modificar atributos da classe. O método __init__() 
é especial e é chamado de construtor. Ele é usado para inicializar os 
atributos do objeto quando um objeto é criado.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

pessoa1 = Pessoa("Bruno", 38)
mensagem = pessoa1.saudacao()
print(mensagem)  # Isso imprimirá "Olá, meu nome é Bruno e tenho 38 anos."


# Método self:
"""
O primeiro parâmetro de todos os métodos de classe em Python é self, que é uma referência ao 
próprio objeto. Você usa self para acessar os atributos e métodos do objeto dentro da classe.
"""

# Herança:
"""
Python suporta herança, que permite que você crie uma nova classe que é uma versão 
modificada de uma classe existente. A nova classe herda os atributos e métodos da classe pai.
"""
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Latir"

cachorro = Cachorro("Toko")
print(cachorro.fazer_som())  # Isso imprimirá "Latir"

# Encapsulamento:
"""
Python não tem modificadores de acesso como algumas outras linguagens de programação, mas usa 
convenções para indicar a visibilidade de um atributo ou método. Um atributo ou método com um 
único sublinhado (por exemplo, _atributo) é considerado como "protegido" e deve ser acessado
apenas dentro da classe ou subclasse. Um atributo ou método com dois sublinhados (por exemplo, __atributo) 
é considerado "privado" e deve ser acessado apenas dentro da classe.

Esses são os conceitos básicos relacionados a classes em Python. As classes são uma parte 
central da programação orientada a objetos e permitem a modelagem de objetos e a criação 
de estruturas de código reutilizáveis e organizadas.
"""
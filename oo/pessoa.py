class Pessoa:
    olhos=2
    def __init__(self, *filhos, nome=None, idade=42):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def method_statico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    reginaldo = Pessoa(nome='Reginaldo')
    pedro = Pessoa(reginaldo, nome='Pedro')
    print(Pessoa.cumprimentar(pedro))
    print(id(pedro))
    print(pedro.cumprimentar())
    print(pedro.nome)
    print(pedro.idade)
    print(pedro.filhos)
    for filho in pedro.filhos:
        print(filho.nome)
    pedro.sobrenome = 'Silva'
    del pedro.filhos
    pedro.olhos=1
    del pedro.olhos
    print(pedro.__dict__)
    print(reginaldo.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(pedro.olhos)
    print(reginaldo.olhos)
    print(id(Pessoa.olhos), id(pedro.olhos), id(reginaldo.olhos))
    print(Pessoa.method_statico(), pedro.method_statico())
    print(Pessoa.nome_e_atributos_de_classe(), pedro.nome_e_atributos_de_classe())


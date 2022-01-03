class DomainsChecked:
    def __init__(self, nome, resultado):
        self.nome = nome
        self.resultado = resultado

domain = DomainsChecked('domínio 1', 'muitas outras coisas')
resultado = (f' Domínio: {domain.nome}\n Resultado: {domain.resultado}')

print(resultado)
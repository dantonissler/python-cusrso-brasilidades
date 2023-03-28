from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def criar_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta!!")

class DocCpf:
    def __init__(self, cpf):
        if self.valida(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.formata()

    def valida(self, cpf):
        return CPF().validate(cpf)

    def formata(self):
        return CPF().mask(self.cpf)

class DocCnpj:
    def __init__(self, cnpj):
        if self.valida(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ inválido!")

    def valida(self, cnpj):
        return CNPJ().validate(cnpj)

    def formata(self):
        return CNPJ().mask(self.cnpj)

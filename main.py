from cpf_cnpj import Documento
from datas_br import DatasBr
from telefone import TelefonesBr
from acesso_cep import BuscaEndereco
import re
import PyPDF2

if __name__ == '__main__':
    objeto_cpf = Documento.criar_documento("12354367996")
    print(objeto_cpf)

    telefone_objeto = TelefonesBr("552126481234")
    print(telefone_objeto)

    datas_objeto = DatasBr()
    print(datas_objeto.dia_semana())
    print(datas_objeto.mes_cadastro())

    objeto_cep = BuscaEndereco("79070295")
    bairro, cidade, uf = objeto_cep.acessa_via_cep()
    print(bairro, cidade, uf)

    # TESTES de leitura de documentos.
    pdf = open('pdf/Incorporacao, Cisao ou Fusao da Companhia.pdf', 'rb')
    reader = PyPDF2.PdfFileReader(pdf)
    pagina = reader.getPage(0)
    texto = pagina.extractText()
    print(texto)
    padrao = "([0-9]{2})([.])([0-9]{3})([.])([0-9]{3})([/])([0-9]{4})([ ])?([-])([0-9]{2})"
    respostas = re.findall(padrao, texto)
    print(respostas)
    print(len(respostas))
    print(respostas[0][0])

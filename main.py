from CPF_CNPJ import Documento
#from validate_docbr import CNPJ
# cpf_um = Cpf("01234567890")
# print(cpf_um)

exemplo_cnpj = "81994337000163"
exemplo_cpf = "43473283037"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
documentoCPF = Documento.cria_documento(exemplo_cpf)
documentoCNPJ = Documento.cria_documento(exemplo_cnpj)

print(documentoCPF, documentoCNPJ)

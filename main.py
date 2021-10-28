from CPF_CNPJ import CpfCnpj
#from validate_docbr import CNPJ
# cpf_um = Cpf("01234567890")
# print(cpf_um)

exemplo_cnpj = "81994337000163"
exemplo_cpf = "43473283035"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
documento = CpfCnpj(exemplo_cpf, 'cpf')

print(documento)
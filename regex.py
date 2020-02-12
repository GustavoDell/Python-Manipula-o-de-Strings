#EXPRESSÕES REGULARES (regex)
import re #biblioteca que lida com expressões regulares no python

email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"

padrao = "[0-9]{4,5}-?[0-9]{4}"

search = re.search(padrao, email2)
findall = re.findall(padrao, email2)

print("Testando com SEARCH", search.group())
print("Testando com FINDALL", findall)

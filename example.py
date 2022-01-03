# import os
import subprocess
import threading

#arquivo com domínios
file = open('urlsScripts.txt', 'r+')
#arquivo onde será salvo o resultado
checkedDomain = open('myfile.txt', 'w')
#lendo linha por linha do arquivo
domains = file.readlines()

class DomainsChecked:
    def __init__(self, nome, resultado):
        self.nome = nome
        self.resultado = resultado


#função responsável fazer o whois dos domínios 
def getDomain(domainName):
    #string remove \n entre os valores de entrada
    domainFormated = domainName.strip()
    
    command = (f'whois {domainFormated} | grep -F -e"expires" -e "Registry Expiry Date" -e"e-mail" -e "Registry Admin ID" ')
    # command = (f'whois {domainFormated} | grep -F -e "expires" -e "e-mail" -e "owner-c"')
    #Executa o comando do sistema - saída devolvida em bytes 
    executedCommand = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    #lê resultado do comando - dados em buffer
    bufferedResult = executedCommand.read()
    #parsea os dados do buffer para string
    result = bufferedResult.decode()

    domain = DomainsChecked(domainFormated, result)
    resultadoFinal = (f'Domínio: {domain.nome}\n{domain.resultado}')

    #printa na tela
    print(resultadoFinal)

    #salva domínio verificado 
    checkedDomain.writelines(resultadoFinal)
     
    
class minhaThread(threading.Thread):
    def __init__(self, meuId, mutex, domainName):
        self.meudId = meuId 
        self.mutex = mutex
        self.domainName = domainName
        threading.Thread.__init__(self)
    def run(self):
            with self.mutex:
                getDomain(self.domainName)

#mutex para thread
stdoutmutex = threading.Lock()
threads = []

for domain in domains:
    thread = minhaThread(domain, stdoutmutex, domain)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    

checkedDomain.close()



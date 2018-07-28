from datetime import datetime

def funcao1(File):
    arquivo = open(File)
    
    for line in arquivo:
        nome = line[0:6]    
        tamanho = line[8:12]
        data = line[13:24]
        
        datatotal = datetime.strptime(data, '%d %b %Y')
        datamax = datetime.strptime('28 Feb 2000', '%d %b %Y')
        
        try:
            tamanho = int (tamanho)
            print (tamanho, 'Bytes')
        except:
            t = line[11:12]
            t2 = line[8:11]
            if t == 'K':
               
                tamanho = t2 * 2
                print (t2, tamanho, 'k')
            else:
                if t == 'M':
                    print (t2, 'm')
        
        if datatotal < datamax:
            print (nome)
            
        else:
            print ('Data de criação do arquivo posterior à 28 de Fevereiro de 2000.')


funcao1 ('files.txt')

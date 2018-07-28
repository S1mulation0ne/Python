from array import *
import json


def createJsonFile(jsonContent, totalIncident):
    print('Total Incident', totalIncident)
    estatistics = []
    
    #criando o conteudo para o arquivo JSON
    for item in jsonContent:
        estatistics.append({
            'fase_operacao':item[0],
            'ocorrencias': item[1],
            "percentual": str(round((int(item[1])*100)/int(totalIncident), 3)) +'%'
        })
    print(estatistics)
    
    #Salvando estatisticas no arquivo JSON
    with open('data.json', 'w') as outfile:
        json.dump(estatistics, outfile,indent=4,)
        
        def createJsonContent(tableArray):
    aeronave_fase_operacao = [] #crio array pra guardar todas das fases da operação
    for line in tableArray:
        aeronaveFaseOperacaoCell = line[20] #pegando cada fase de cada linha do arquivo
        
        # try para verificar se o valor da celula do arquivo ja foi incluido no array aeronave_fase_operacao
        x=[] 
        try:
            x = [x for x in aeronave_fase_operacao if aeronaveFaseOperacaoCell in x][0] # localizando o item no array bidimensional
        except:
            print()
        
        
        if len(x) == 0:
            # Se a fase operação nao foi ele localizado inclui a fase operação no array
            aeronave_fase_operacao.insert(len(aeronave_fase_operacao)+1 , [aeronaveFaseOperacaoCell, 0])
        else:
            #se foi localizado
            indexAFO = aeronave_fase_operacao.index(x) #Acha a posição da fase operação no array
            updateAFO = aeronave_fase_operacao[indexAFO][1] #pega o valor antigo do total daquela fase de operaçao
            aeronave_fase_operacao[indexAFO][1] = updateAFO + 1  # soma mais 1 no total daquela fase de operação

    return aeronave_fase_operacao
  
  def readFile(fileName):
    f = open (fileName).readlines() #lendo o arquivo
    header = f.pop(0) #guardando o cabeçalho e removendo ele da lista
    lineArray = [] #Array pra guardar linha
    tableArray = [] #array pra guardar tabela toda
    for line in f:
        splitLine = line.split('~') #separando as celulas por split ~
        for item in splitLine:
            item = item.replace("\"", "") #removendo o aspas
            lineArray.append(item) #adicionando a celula no array da linha
        tableArray.append(lineArray) #adicionando a linha na tabela
        lineArray=[] #limpando o array da linha para ser usado na proxima interação
    return tableArray
  
  tableArray = readFile('anv.csv');
  
  jsonContent = createJsonContent(tableArray)

import time
import os

class ListClass:

    def __init__(self):
        self.currentList = []

    def add(self, data):
        if data:
            self.currentList.append({"data": data, "isChecked": False})
            print("\nTarefa adicionada com sucesso!\n")
            return True
        else:
            print("\nErro: A tarefa não pode ser vazia.\n")
            return False

    def get(self):
        if self.currentList:
            print("------------------------------")
            print("\nTarefas:")
            for index, task in enumerate(self.currentList):
                checked = "✔" if task["isChecked"] else "✘"
                print(f"{index}: {task['data']} [{checked}]")
            print("\n------------------------------\n")
        else:
            print("\nNenhuma tarefa na lista.\n")
            print("------------------------------\n")

    def edit(self, index, data):
        if index is not None and 0 <= index < len(self.currentList) and data:
            self.currentList[index]["data"] = data
            print("\nTarefa editada com sucesso!\n")
            return True
        else:
            print("\nErro: Índice inválido ou dados vazios.\n")
            return False

    def remove(self, index):
        if index is not None and 0 <= index < len(self.currentList):
            self.currentList.pop(index)
            print("\nTarefa excluída com sucesso!\n")
            return True
        else:
            print("\nErro: Índice inválido.\n")
            return False

    def check(self, index):
        if index is not None and 0 <= index < len(self.currentList):
            self.currentList[index]["isChecked"] = True
            print("\nTarefa marcada como concluída!\n")
            return True
        else:
            print("\nErro: Índice inválido.\n")
            return False

def showMenu():
    print("\n--------Iniciando Sistema--------\n")
    print("1-Adicionar Tarefa")
    print("2-Listar tarefas")
    print("3-Editar tarefa")
    print("4-Checar tarefa")
    print("5-Excluir tarefa")
    print("6-Sair")
    print("\n------------------------------\n")

def exitMenu():
    print("\n--------Desligando Sistema--------\n")

def clearTerminal():
  os.system("cls")

currentList = ListClass()

while True:
    clearTerminal()
    showMenu()
    answer = input("Escolha uma opção: ")
    clearTerminal()
    
    match answer:
        case "1":
            case1Value = input("Digite a informação que você quer adicionar: ")
            currentList.add(case1Value)
            clearTerminal()
            currentList.get()
            time.sleep(3)
            
        case "2":
            currentList.get() 
            input("\nPressione Enter para voltar ao menu.\n")

        case "3":
            currentList.get()
            case3IndexValue = int(input("Digite o índice da tarefa que você quer modificar: "))
            case3AnswerValue = input("Digite a nova informação: ")
            returnedValue = currentList.edit(case3IndexValue, case3AnswerValue)
            if returnedValue:
              clearTerminal()
              currentList.get()  
              time.sleep(2)
            else:
              time.sleep(2)
              continue
              
            
        case "4":
            currentList.get()
            case4CheckValue = int(input("Digite o índice da tarefa que você quer checar: "))
            returnedValue =currentList.check(case4CheckValue)
            if returnedValue:
              clearTerminal()
              currentList.get()  
              time.sleep(2)
            else:
              time.sleep(2)
              continue
           
        case "5":
            currentList.get()
            case5RemoveIndex = int(input("Digite o índice da tarefa que você quer excluir: "))
            returnedValue = currentList.remove(case5RemoveIndex)
            if returnedValue:
              clearTerminal()
              currentList.get()  
              time.sleep(2)
            else:
              time.sleep(2)
              continue

        case "6":
            exitMenu()
            break
        case _:
            continue

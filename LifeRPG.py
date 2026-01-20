import os

# --- TÓPICO: CLASSES ---
class Missao:
    def __init__(self, titulo, dificuldade):
        self.titulo = titulo
        self.dificuldade = dificuldade
        self.concluida = False
        
        # TÓPICO: CONDICIONAIS (Definindo XP baseado na dificuldade)
        if self.dificuldade == 'facil':
            self.xp_recompensa = 10
        elif self.dificuldade == 'medio':
            self.xp_recompensa = 20
        else:
            self.xp_recompensa = 50

    def __str__(self):
        # Formata como a missão aparece na tela
        status = "[X]" if self.concluida else "[ ]"
        return f"{status} {self.titulo} (XP: {self.xp_recompensa})"

class Heroi:
    def __init__(self, nome):
        self.nome = nome
        self.xp = 0
        self.nivel = 1

    # TÓPICO: FUNCTIONS (Métodos da classe)
    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        print(f"\n✨ Você ganhou {quantidade} XP!")
        self.verificar_nivel()

    def verificar_nivel(self):
        # Regra simples: A cada 100 XP sobe de nível
        xp_necessario = self.nivel * 100 
        if self.xp >= xp_necessario:
            self.nivel += 1
            print(f"🎉 PARABÉNS! Você subiu para o Nível {self.nivel}!")

    def mostrar_status(self):
        print(f"\n--- HERÓI: {self.nome} ---")
        print(f"Nível: {self.nivel} | XP Atual: {self.xp}")
        print("-" * 20)

# --- FUNÇÕES AUXILIARES ---
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- PROGRAMA PRINCIPAL ---
def main():
    print("⚔️ Bem-vindo ao LifeRPG ⚔️")
    nome_heroi = input("Qual o nome do seu herói? ")
    
    # Instanciando o objeto Heroi
    jogador = Heroi(nome_heroi)
    
    # TÓPICO: DATA STRUCTURES (Lista para guardar as missões)
    lista_de_missoes = []

    # TÓPICO: LOOPS (Loop infinito do menu)
    while True:
        jogador.mostrar_status()
        print("\n1. Adicionar Nova Missão")
        print("2. Ver Missões")
        print("3. Completar Missão")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            titulo = input("Nome da tarefa/missão: ")
            dificuldade = input("Dificuldade (facil/medio/dificil): ").lower()
            nova_missao = Missao(titulo, dificuldade)
            lista_de_missoes.append(nova_missao)
            print("Missão adicionada!")

        elif opcao == '2':
            print("\n--- QUADRO DE MISSÕES ---")
            
            if not lista_de_missoes:
                print("📭 Nenhuma missão encontrada. Adicione uma na opção 1!")
            else:
                for index, missao in enumerate(lista_de_missoes):
                    print(f"{index}. {missao}")
        
        elif opcao == '3':
            # TÓPICO: VARIABLES & INPUT
            try:
                id_missao = int(input("Digite o número da missão para completar: "))
                missao_escolhida = lista_de_missoes[id_missao]
                
                if not missao_escolhida.concluida:
                    missao_escolhida.concluida = True
                    jogador.ganhar_xp(missao_escolhida.xp_recompensa)
                    # Opcional: Remover a missão da lista após completar
                    # lista_de_missoes.pop(id_missao)
                else:
                    print("Essa missão já foi completada!")
            except:
                print("Número inválido!")

        elif opcao == '4':
            print("Até a próxima aventura!")
            break
        
        else:
            print("Opção inválida.")

# Executar o programa
if __name__ == "__main__":
    main()
class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, name, description, options):
        self.states[name] = GameState(description, options)

    def set_start(self, name):
        self.current_state = name

    def transition(self, choice):
        if choice in self.states[self.current_state].options:
            self.current_state = self.states[self.current_state].options[choice]
        else:
            print("Escolha inválida. Tente novamente.")

    def play(self):
        while True:
            state = self.states[self.current_state]
            print(state.description)
            for option in state.options:
                print(f"- {option}")
            choice = input("O que você quer fazer? ").lower()
            self.transition(choice)

class GameState:
    def __init__(self, description, options):
        self.description = description
        self.options = options

# Configuração do jogo
game = StateMachine()
game.add_state("start", "Você está em uma floresta. Pode ir para o norte ou para o sul.", {"norte": "norte", "sul": "sul"})
game.add_state("norte", "Você está diante de um rio. Pode nadar ou voltar.", {"nadar": "start", "voltar": "start"})
game.add_state("sul", "Você está na entrada de uma caverna. Pode entrar ou voltar.", {"entrar": "start", "voltar": "start"})
game.set_start("start")

# Início do jogo
game.play()

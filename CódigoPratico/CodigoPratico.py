class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states                # Conjunto de estados (ex: {'q0', 'q1'})
        self.alphabet = alphabet            # Alfabeto aceito (ex: {'a', 'b'})
        self.transitions = transitions      # Dicionário de transições: {(estado, símbolo): próximo_estado}
        self.start_state = start_state      # Estado inicial (ex: 'q0')
        self.accept_states = accept_states  # Conjunto de estados de aceitação (ex: {'q0'})

    def process_string(self, input_string):
        """Simula o autômato para uma dada string de entrada."""
        current_state = self.start_state
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False  # Símbolo fora do alfabeto
            
            # Busca a próxima transição
            next_state = self.transitions.get((current_state, symbol))
            if next_state is None:
                return False  # Não há transição definida (estado morto)
                
            current_state = next_state
            
        # Retorna verdadeiro se o estado final for de aceitação
        return current_state in self.accept_states


# --- Exemplo de Uso ---
# Autômato que aceita strings com um número par de 'a's
states = {'q0', 'q1'}
alphabet = {'a', 'b'}
transitions = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q1'
}
start_state = 'q0'
accept_states = {'q0'}

# Instanciando o autômato
automaton = DFA(states, alphabet, transitions, start_state, accept_states)

# Testando algumas palavras
test_strings = ["aab", "abba", "bba", "aaaa"]
for s in test_strings:
    resultado = "Aceita" if automaton.process_string(s) else "Rejeitada"
    print(f"String '{s}': {resultado}")
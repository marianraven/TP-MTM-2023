from sys import stdin, argv
from automata.tm.dtm import DTM
from automata.base.exceptions import AutomatonException


transiciones={
    'q0': {
    'a': ('q1', 'x', 'R'),
    'b': ('q5', 'x', 'R'),
    'x': ('q4', 'x', 'R'),
    },
    'q1': {
    'a': ('q1', 'a', 'R'),
    'b': ('q1', 'b', 'R'),
    'c': ('q2', 'x', 'L'),
    'x': ('q3', 'x', 'R'),
    },
    'q2': {
    'a': ('q2', 'a', 'L'),
    'b': ('q2', 'b', 'L'),
    'x': ('q2', 'x', 'L'),
    '~': ('q2', '~', 'R'),
    },
    'q3': {
    'c': ('q2', 'x', 'L'),
    'x': ('q3', 'x', 'R'),
    },
    'q4': {
    'a': ('q1', 'x', 'R'),
    'b': ('q5', 'x', 'R'),
    'x': ('q4', 'x', 'R'),
    '~': ('qaccept', '~', 'R'),
    '~': ('qreject', 'x', 'S'),
    },
    'q5': {
    'b': ('q5', 'b', 'R'),
    'c': ('q5', 'x', 'L'),
    'x': ('q3', 'x', 'R'),
    }
}

maquina = DTM(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'qaccept', 'qreject'},
    input_symbols={'a', 'b','c'},
    tape_symbols={'a', 'b', 'c', 'x', '~'},
    transitions=transiciones,
    initial_state='q0',
    final_states={'qaccept', 'qreject'},
    blank_symbol='~'
)

def evaluar(w, debug=True):
    if debug:
        for c in maquina.read_input_stepwise(w):
            c.print()
        return True
    return maquina.accepts_input(w)


if __name__ == '__main__':
    for w in stdin:
        res = False
        try:
            res = evaluar(w.strip(), '--debug' in argv) 
        except AutomatonException as ex:
            print(ex.args)
        if (res):
            print('ACEPTA')
        else:
            print('RECHAZA')

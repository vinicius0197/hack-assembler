class SymbolTable:
    '''
    Implements a Symbol Table using a dictionary. The symbol
    table contains pre-defined values from the Hack machine specification
    and enables adding new keys for variables and label declarations.
    '''

    def __init__(self):
        self.symbol_table = dict()
        self.initialize()

    def add_entry(self, symbol, addr):
        '''
        Adds a new entry to the symbol table
        '''
        self.symbol_table[symbol] = addr

    def contains(self, symbol):
        '''
        Checks if symbol table contains a given symbol
        '''
        if symbol in self.symbol_table:
            return True
        else:
            return False

    def get_addr(self, symbol):
        '''
        Gets memory address for a given symbol
        '''
        if self.contains(symbol):
            return self.symbol_table[symbol]
        else:
            return None

    def initialize(self):
        '''
        Initialize symbol table with pre-defined values
        '''
        self.symbol_table['SP'] = 0
        self.symbol_table['LCL'] = 1
        self.symbol_table['ARG'] = 2
        self.symbol_table['THIS'] = 3
        self.symbol_table['THAT'] = 4
        self.symbol_table['R0'] = 0
        self.symbol_table['R1'] = 1
        self.symbol_table['R2'] = 2
        self.symbol_table['R3'] = 3
        self.symbol_table['R4'] = 4
        self.symbol_table['R5'] = 5
        self.symbol_table['R6'] = 6
        self.symbol_table['R7'] = 7
        self.symbol_table['R8'] = 8
        self.symbol_table['R9'] = 9
        self.symbol_table['R10'] = 10
        self.symbol_table['R11'] = 11
        self.symbol_table['R12'] = 12
        self.symbol_table['R13'] = 13
        self.symbol_table['R14'] = 14
        self.symbol_table['R15'] = 15
        self.symbol_table['SCREEN'] = 16384
        self.symbol_table['KBD'] = 24576

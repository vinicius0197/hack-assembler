import os


class Code:
    '''
    This module receives the parsed source file and a symbol table and iterates
    the parsed source file twice.

    During the first iteration, the symbol table is updated with label declarations.

    During the second iteration, machine code is generated from the parsed instructions
    and labels and variables are substituted by their respective memory locations.
    '''

    def __init__(self, parser, symbol_table):
        self.parser = parser
        self.symbol_table = symbol_table
        self.n = 16

    def assemble(self):
        self.__build_symbol_table()  # First pass
        output_file_name = os.path.splitext(os.path.normpath(
            self.parser.src).split(os.path.sep)[-1])[0] + '.hack'
        f = open(output_file_name, 'w')

        for command in self.parser.commands:  # Second pass
            if command['type'] == 'A_COMMAND':
                if self.__is_int(command['addr']):
                    output = '0' + '{0:015b}'.format(int(command['addr']))
                elif command['addr'] in self.symbol_table.symbol_table:
                    symbol = command['addr']
                    output = '0' + \
                        '{0:015b}'.format(
                            self.symbol_table.symbol_table[symbol])
                else:
                    self.symbol_table.add_entry(command['addr'], self.n)
                    output = '0' + '{0:015b}'.format(self.n)
                    self.n += 1
            elif command['type'] == 'C_COMMAND':
                output = '111' + self.__get_comp(command['comp']) + self.__get_dest(
                    command['dest']) + self.__get_jump(command['jump'])
            elif command['type'] == 'L_COMMAND':
                output = ''

            if output:
                f.write(output + '\n')
        f.close()

    def __is_int(self, value):
        '''
        Returns true if value is int
        '''
        try:
            int(value)
            return True
        except ValueError:
            return False

    def __build_symbol_table(self):
        '''
        Adds label declarations to symbol table
        '''
        for command in self.parser.commands:
            if command['type'] == 'L_COMMAND':
                self.symbol_table.add_entry(
                    command['addr'], command['line'])

    def __get_dest(self, dest):
        '''
        Get destination field from parsed command
        '''
        if dest == '':
            return '000'
        elif dest == 'M':
            return '001'
        elif dest == 'D':
            return '010'
        elif dest == 'MD':
            return '011'
        elif dest == 'A':
            return '100'
        elif dest == 'AM':
            return '101'
        elif dest == 'AD':
            return '110'
        elif dest == 'AMD':
            return '111'

    def __get_comp(self, comp):
        '''
        Gets computation field from parsed command
        '''
        if comp == '0':
            return '0101010'
        elif comp == '1':
            return '0111111'
        elif comp == '-1':
            return '0111010'
        elif comp == 'D':
            return '0001100'
        elif comp == 'A':
            return '0110000'
        elif comp == '!D':
            return '0001101'
        elif comp == '!A':
            return '0110001'
        elif comp == '-D':
            return '0001111'
        elif comp == '-A':
            return '0110011'
        elif comp == 'D+1':
            return '0011111'
        elif comp == 'A+1':
            return '0110111'
        elif comp == 'D-1':
            return '0001110'
        elif comp == 'A-1':
            return '0110010'
        elif comp == 'D+A':
            return '0000010'
        elif comp == 'D-A':
            return '0010011'
        elif comp == 'A-D':
            return '0000111'
        elif comp == 'D&A':
            return '0000000'
        elif comp == 'D|A':
            return '0010101'
        elif comp == 'M':
            return '1110000'
        elif comp == '!M':
            return '1110001'
        elif comp == '-M':
            return '1110011'
        elif comp == 'M+1':
            return '1110111'
        elif comp == 'M-1':
            return '1110010'
        elif comp == 'D+M':
            return '1000010'
        elif comp == 'D-M':
            return '1010011'
        elif comp == 'M-D':
            return '1000111'
        elif comp == 'D&M':
            return '1000000'
        elif comp == 'D|M':
            return '1010101'

    def __get_jump(self, jump):
        '''
        Gets jump field from parsed command
        '''
        if jump == '':
            return '000'
        elif jump == 'JGT':
            return '001'
        elif jump == 'JEQ':
            return '010'
        elif jump == 'JGE':
            return '011'
        elif jump == 'JLT':
            return '100'
        elif jump == 'JNE':
            return '101'
        elif jump == 'JLE':
            return '110'
        elif jump == 'JMP':
            return '111'

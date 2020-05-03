class Parser:
    '''
    A Parser for the Hack Machine Language.
    '''

    def __init__(self, src):
        self.src = src
        self.commands = []
        self.lines = 0

    def parse(self):
        '''
        Main parsing function. Populates self.commands attribute
        with Hack machine code fields.
        '''
        lines = self.__read_file()
        for line in lines:
            line = self.__remove_comments(line)
            if line.strip():
                command = dict()
                command['type'] = self.__command_type(line.strip())
                if command['type'] == 'A_COMMAND':
                    command['addr'] = self.symbol(line.strip())
                    command['line'] = self.lines
                    self.lines += 1
                elif command['type'] == 'C_COMMAND':
                    command['dest'], command['comp'], command['jump'] = self.__parse_c_command(
                        line.strip())
                    command['line'] = self.lines
                    self.lines += 1
                elif command['type'] == 'L_COMMAND':
                    command['addr'] = self.__get_label(line.strip())
                    command['line'] = self.lines

                self.commands.append(command)

    def symbol(self, command):
        '''
        Returns symbol for a given A-type command
        '''
        head, sep, symbol = command.partition('@')
        return symbol

    def __get_label(self, command):
        '''
        Returns label for label declaration
        '''
        return command[command.find("(")+1:command.find(")")]

    def __read_file(self):
        '''
        Read lines from source .asm file
        '''
        f = open(self.src, "r")
        lines = f.readlines()
        return lines

    def __remove_comments(self, line):
        '''
        Remove comments from source file
        '''
        head, sep, tail = line.partition('//')
        return head

    def __command_type(self, command):
        '''
        Returns command type (A, L, C) according to Hack
        specification
        '''
        if command.startswith('@'):
            return 'A_COMMAND'
        elif command.startswith('('):
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def __parse_c_command(self, command):
        '''
        Parses a C-type command
        '''
        dest, equal_sep, tail = command.partition('=')
        if tail:
            comp, sep, jump = tail.partition(';')
            return dest, comp, jump
        else:
            comp, sep, jump = dest.partition(';')
            dest = ''
            return dest, comp, jump

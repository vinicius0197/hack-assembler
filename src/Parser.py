class Parser:
    def __init__(self, src):
        self.src = src
        self.commands = []

    def parse(self):
        lines = self.__read_file()
        for line in lines:
            line = self.__remove_comments(line)
            if line.strip():
                command = dict()
                command['type'] = self.__command_type(line.strip())
                if command['type'] == 'A_COMMAND':
                    command['addr'] = self.symbol(line.strip())
                elif command['type'] == 'C_COMMAND':
                    command['dest'], command['comp'], command['jump'] = self.__parse_c_command(
                        line.strip())
                elif command['type'] == 'L_COMMAND':
                    command['addr'] = self.__get_label(line.strip())

                self.commands.append(command)

    def symbol(self, command):
        head, sep, symbol = command.partition('@')
        return symbol

    def __get_label(self, command):
        return command[command.find("(")+1:command.find(")")]

    def __read_file(self):
        f = open(self.src, "r")
        lines = f.readlines()
        return lines

    def __remove_comments(self, line):
        head, sep, tail = line.partition('//')
        return head

    def __command_type(self, command):
        if command.startswith('@'):
            return 'A_COMMAND'
        elif command.startswith('('):
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def __parse_c_command(self, command):
        dest, equal_sep, tail = command.partition('=')
        if tail:
            comp, sep, jump = tail.partition(';')
            return dest, comp, jump
        else:
            comp, sep, jump = dest.partition(';')
            dest = ''
            return dest, comp, jump

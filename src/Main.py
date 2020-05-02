import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Name of the input ASM file')
    parser.add_argument('--source', action='store', required=True,
                        dest='input_file', help='a source assembly file for the assembler')

    args = parser.parse_args()
    return args.input_file


def main():
    input_file = parse_arguments()
    print(input_file)


if __name__ == "__main__":
    main()

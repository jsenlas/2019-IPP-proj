import argparse
import sys
from errors import *
from framestack import FrameStack
from xmlparser import XMLParser


class ArgumentType:
    VAR = 1
    LABEL = 2
    STR = 3
    INT = 4
    FLOAT = 5
    TYPE = 6
    NIL = 7


class IPStack():
    def __init__(self):
        self.stack = list()
        self.ip = 0

    def get_ip(self):
        return self.stack[self.ip]

    def pop_ip(self):
        if self.stack:
            return self.stack.pop()
        else:
            pass  # $#$

    def push_ip(self, new_ip):
        self.stack.append(new_ip)


class DataStack():
    def __init__(self):
        self.data_stack = []

    def pushs(self, data):
        self.data_stack.append(data)

    def pops(self):
        if self.data_stack:
            return self.data_stack.pop()


class Interpret:
    def __init__(self, ins):
        self.framestack = FrameStack()
        self.instructions_list = ins
        self.ip_stack = IPStack()
        self.labels = dict()
        self.data_stack = DataStack()
        pass

    def print_stack(self, d_stack):
        for i in d_stack:
            print(i)
        print("GF", self.framestack.GlobalFrame)

    def run_interpret(self):
        if self.instructions_list is not None:
            for self.ip_stack.ip in range(0, len(self.instructions_list)):
                print(self.instructions_list[self.ip_stack.ip].order)
                # self.print_stack(self.data_stack.data_stack)
                self.instructions_list[self.ip_stack.ip].run_instruction(self.framestack, self.ip_stack, self.labels, self.data_stack)

        print("GF", self.framestack.GlobalFrame)
        print("TF", self.framestack.TmpFrame)
        print("FStack", self.framestack.frameStack)
        print("IPS", self.ip_stack.stack)
        print("labels", self.labels)


def main():
    file_flag = 1
    string_flag = 2

    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--source", nargs=1, required=False)
    argument_parser.add_argument("--input", nargs=1, required=False)
    args = argument_parser.parse_args()

    if args.input is not None:
        input_file_name = args.input[0]
        try:
            input_file = open(input_file_name, "r")
        except IOError:
            print("Couldn't open the file", input_file_name, "\n")
            raise OpenInputFileException()
    else:
        """Here should be some flag to change where the input should come from"""
        pass

    if args.source is not None:
        source_file_name = args.source[0]
        try:
            source_file = open(source_file_name, "r")
            reading_from = file_flag
        except IOError:
            print("Couldn't open the file", source_file_name, "\n")
            raise OpenSourceFileException()
    else:
        source_file = sys.stdin.read()
        reading_from = string_flag

    xml_parser = XMLParser()
    instructions = xml_parser.ParseXml(source_file, reading_from)
    """
    for idx in range(0, len(instructions)):
        print(instructions[idx].order, instructions[idx].name, instructions[idx].arguments)
        pass
    exit(0)
    """
    interpret = Interpret(instructions)
    interpret.run_interpret()


if __name__ == "__main__":
    error = Errors()
    try:
        main()
    except MissingParamException:
        sys.exit(error.missing_param)
    except OpenInputFileException:
        sys.exit(error.open_input_file_failed)
    except OpenSourceFileException:
        sys.exit(error.open_source_file_failed)
    except XMLFormatException:
        sys.exit(error.xml_wrong_format)
    except XMLStructureException:
        sys.exit(error.xml_lex_or_sem_err)
    except InternalErrorException:
        sys.exit(error.internal_error)
    except SemanticErrorLabel:
        sys.exit(error.semantic_error_nondefined_label)
    except OperandTypeException:
        sys.exit(error.wrong_operand_type)
    except NonExistingVariableException:
        sys.exit(error.non_existing_variable)
    except FrameNotDefinedException:  # NonExistingFrameException:
        sys.exit(error.frame_not_defined)
    except MissingValueException:
        sys.exit(error.missing_value)
    except ValueOperandException:
        sys.exit(error.value_operand)
    except StringException:
        sys.exit(error.working_with_string)
    except SystemExit as ex:
        # if ex.code != 0:
        #    raise MissingParamException()
        sys.exit(ex.code)
    except BaseException:
        raise InternalErrorException()
    sys.exit(0)
    # ^^^ Go ^up^, just go ^up^, don't be so low. ^^^

import argparse

# The Universal Turing Machine
class UTM:

    def __init__(self, simulated_machine_description, simulated_machine_tape, simulated_machine_condition, infinity_buffer_size=2, t_buffer_size=3, implicit_quintuples=True, dangerous_quintuples=False, max_steps=float("inf"), verbosity=1):
        self.max_steps = max_steps
        self.verbosity = verbosity
        
        # Defining the UTM as presented in Minsky, Computation: Finite and infinite machines, 1967, Chapter 7.
        # Defining the UTMs states.
        self.states = []
        self.states.append(None)
        self.states.append(State(1, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(2, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(3, "L", implicit_quintuples=implicit_quintuples))
        self.states.append(State(4, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(5, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(6, "L", implicit_quintuples=implicit_quintuples))
        self.states.append(State(7, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(8, "L", implicit_quintuples=implicit_quintuples))
        self.states.append(State(9, "L", implicit_quintuples=implicit_quintuples))
        self.states.append(State(10, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(11, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(12, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(13, "L", implicit_quintuples=implicit_quintuples))
        self.states.append(State(14, "L", implicit_quintuples=implicit_quintuples))
        self.states.append(State(15, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(16, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(17, "L", implicit_quintuples=implicit_quintuples))
        self.states.append(State(18, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(19, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(20, "R", implicit_quintuples=implicit_quintuples))
        self.states.append(State(21, "L", implicit_quintuples=implicit_quintuples))
        self.states.append(State(22, "L", implicit_quintuples=implicit_quintuples))
        self.states.append(State(23, "L", implicit_quintuples=implicit_quintuples))

        # Defining the UTMs operations.
        self.states[1].define_operation('0', 'A', self.states[3], 4)
        self.states[1].define_operation('1', 'B', self.states[4], 4)
        self.states[2].define_operation('A', '0', self.states[1], 4)
        self.states[2].define_operation('B', '1', self.states[5], 4)
        self.states[2].define_operation('X', 'X', self.states[7], 2)
        self.states[3].define_operation('Y', 'Y', self.states[2], 4)
        self.states[4].define_operation('X', 'X', self.states[6], 4)
        self.states[4].define_operation('Y', 'Y', self.states[0], 4)
        self.states[5].define_operation('0', 'A', self.states[4], 4)
        self.states[5].define_operation('1', 'B', self.states[3], 4)
        self.states[6].define_operation('0', 'A', self.states[6], 4)
        self.states[6].define_operation('1', 'B', self.states[6], 4)
        self.states[6].define_operation('Y', 'Y', self.states[2], 3)
        self.states[7].define_operation('0', 'A', self.states[9], 4)
        self.states[7].define_operation('1', 'B', self.states[8], 4)
        self.states[8].define_operation('Y', 'Y', self.states[10], 4)
        self.states[9].define_operation('Y', 'Y', self.states[11], 4)
        self.states[10].define_operation('0', 'B', self.states[12], 4)
        self.states[10].define_operation('1', 'B', self.states[12], 4)
        self.states[10].define_operation('X', 'X', self.states[13], 2)
        self.states[11].define_operation('0', 'A', self.states[12], 4)
        self.states[11].define_operation('1', 'A', self.states[12], 4)
        self.states[11].define_operation('X', 'X', self.states[14], 2)
        self.states[12].define_operation('X', 'X', self.states[7], 4)
        self.states[13].define_operation('M', 'B', self.states[15], 4)
        self.states[14].define_operation('M', 'A', self.states[15], 4)
        self.states[15].define_operation('A', '0', self.states[15], 4)
        self.states[15].define_operation('B', '1', self.states[15], 4)
        self.states[15].define_operation('X', 'X', self.states[16], 3)
        self.states[16].define_operation('0', '0', self.states[17], 3)
        self.states[16].define_operation('1', '1', self.states[17], 3)
        self.states[17].define_operation('0', 'S', self.states[22], 2)
        self.states[17].define_operation('1', 'S', self.states[23], 2)
        self.states[17].define_operation('A', '0', self.states[17], 4)
        self.states[17].define_operation('B', '1', self.states[17], 4)
        self.states[18].define_operation('S', 'A', self.states[6], 1)
        self.states[19].define_operation('S', 'B', self.states[6], 1)
        self.states[20].define_operation('0', 'M', self.states[18], 3)
        self.states[20].define_operation('1', 'M', self.states[19], 3)
        self.states[21].define_operation('0', 'M', self.states[18], 3)
        self.states[21].define_operation('1', 'M', self.states[19], 3)
        self.states[22].define_operation('A', '0', self.states[21], 3)
        self.states[22].define_operation('B', '0', self.states[20], 3)
        self.states[23].define_operation('A', '1', self.states[21], 3)
        self.states[23].define_operation('B', '1', self.states[20], 3)

        # Explicit quintuples
        self.states[1].define_operation('A', 'A', self.states[1], 4)
        self.states[1].define_operation('B', 'B', self.states[1], 4)
        self.states[1].define_operation('X', 'X', self.states[1], 4)
        self.states[2].define_operation('0', '0', self.states[2], 4)
        self.states[2].define_operation('1', '1', self.states[2], 4)
        self.states[3].define_operation('0', '0', self.states[3], 4)
        self.states[3].define_operation('1', '1', self.states[3], 4)
        self.states[3].define_operation('A', 'A', self.states[3], 4)
        self.states[3].define_operation('B', 'B', self.states[3], 4)
        self.states[3].define_operation('X', 'X', self.states[3], 4)
        self.states[4].define_operation('0', '0', self.states[4], 4)
        self.states[4].define_operation('1', '1', self.states[4], 4)
        self.states[5].define_operation('A', 'A', self.states[5], 4)
        self.states[5].define_operation('B', 'B', self.states[5], 4)
        self.states[5].define_operation('X', 'X', self.states[5], 4)
        self.states[6].define_operation('A', 'A', self.states[6], 4)
        self.states[6].define_operation('B', 'B', self.states[6], 4)
        self.states[6].define_operation('X', 'X', self.states[6], 4)
        self.states[7].define_operation('A', 'A', self.states[7], 4)
        self.states[7].define_operation('B', 'B', self.states[7], 4)
        self.states[7].define_operation('X', 'X', self.states[7], 4)
        self.states[8].define_operation('0', '0', self.states[8], 4)
        self.states[8].define_operation('1', '1', self.states[8], 4)
        self.states[8].define_operation('A', 'A', self.states[8], 4)
        self.states[8].define_operation('B', 'B', self.states[8], 4)
        self.states[8].define_operation('X', 'X', self.states[8], 4)
        self.states[9].define_operation('0', '0', self.states[9], 4)
        self.states[9].define_operation('1', '1', self.states[9], 4)
        self.states[9].define_operation('A', 'A', self.states[9], 4)
        self.states[9].define_operation('B', 'B', self.states[9], 4)
        self.states[9].define_operation('X', 'X', self.states[9], 4)
        self.states[10].define_operation('A', 'A', self.states[10], 4)
        self.states[10].define_operation('B', 'B', self.states[10], 4)
        self.states[11].define_operation('A', 'A', self.states[11], 4)
        self.states[11].define_operation('B', 'B', self.states[11], 4)
        self.states[12].define_operation('0', '0', self.states[12], 4)
        self.states[12].define_operation('1', '1', self.states[12], 4)
        self.states[13].define_operation('0', '0', self.states[13], 4)
        self.states[13].define_operation('1', '1', self.states[13], 4)
        self.states[13].define_operation('A', 'A', self.states[13], 4)
        self.states[13].define_operation('B', 'B', self.states[13], 4)
        self.states[13].define_operation('Y', 'Y', self.states[13], 4)
        self.states[14].define_operation('0', '0', self.states[14], 4)
        self.states[14].define_operation('1', '1', self.states[14], 4)
        self.states[14].define_operation('A', 'A', self.states[14], 4)
        self.states[14].define_operation('B', 'B', self.states[14], 4)
        self.states[14].define_operation('Y', 'Y', self.states[14], 4)
        self.states[15].define_operation('0', '0', self.states[15], 4)
        self.states[15].define_operation('1', '1', self.states[15], 4)
        self.states[15].define_operation('Y', 'Y', self.states[15], 4)
        self.states[16].define_operation('A', 'A', self.states[16], 4)
        self.states[16].define_operation('B', 'B', self.states[16], 4)
        self.states[16].define_operation('X', 'X', self.states[16], 4)
        self.states[16].define_operation('Y', 'Y', self.states[16], 4)
        self.states[17].define_operation('X', 'X', self.states[17], 4)
        self.states[17].define_operation('Y', 'Y', self.states[17], 4)
        self.states[18].define_operation('0', '0', self.states[18], 4)
        self.states[18].define_operation('1', '1', self.states[18], 4)
        self.states[18].define_operation('Y', 'Y', self.states[18], 4)
        self.states[19].define_operation('0', '0', self.states[19], 4)
        self.states[19].define_operation('1', '1', self.states[19], 4)
        self.states[19].define_operation('Y', 'Y', self.states[19], 4)
        self.states[22].define_operation('0', '0', self.states[22], 4)
        self.states[22].define_operation('1', '1', self.states[22], 4)
        self.states[22].define_operation('Y', 'Y', self.states[22], 4)
        self.states[23].define_operation('0', '0', self.states[23], 4)
        self.states[23].define_operation('1', '1', self.states[23], 4)
        self.states[23].define_operation('Y', 'Y', self.states[23], 4)

        # Dangerous quintuples. These are accepted implicitly in Minsky's machine, but if disabled will all mitigate exploitation.
        if dangerous_quintuples:
            self.states[7].define_operation('Y', 'Y', self.states[7], 4)
            self.states[8].define_operation('S', 'S', self.states[8], 4)
            self.states[9].define_operation('S', 'S', self.states[9], 4)
            self.states[10].define_operation('S', 'S', self.states[10], 4)
            self.states[11].define_operation('S', 'S', self.states[11], 4)
            self.states[12].define_operation('S', 'S', self.states[12], 4)
            self.states[13].define_operation('S', 'S', self.states[13], 4)
            self.states[14].define_operation('X', 'X', self.states[14], 4)
            self.states[14].define_operation('S', 'S', self.states[14], 4)
            self.states[16].define_operation('S', 'S', self.states[16], 4)
            self.states[17].define_operation('S', 'S', self.states[17], 4)
            self.states[18].define_operation('A', 'A', self.states[18], 4)
            self.states[18].define_operation('B', 'B', self.states[18], 4)
            self.states[18].define_operation('X', 'X', self.states[18], 4)
            self.states[19].define_operation('A', 'A', self.states[19], 4)
            self.states[19].define_operation('B', 'B', self.states[19], 4)
            self.states[19].define_operation('X', 'X', self.states[19], 4)
            self.states[20].define_operation('A', 'A', self.states[20], 4)
            self.states[20].define_operation('B', 'B', self.states[20], 4)
            self.states[20].define_operation('S', 'S', self.states[20], 4)
            self.states[20].define_operation('X', 'X', self.states[20], 4)
            self.states[20].define_operation('Y', 'Y', self.states[20], 4)
            self.states[21].define_operation('A', 'A', self.states[21], 4)
            self.states[21].define_operation('S', 'S', self.states[21], 4)
            self.states[21].define_operation('B', 'B', self.states[21], 4)
            self.states[21].define_operation('X', 'X', self.states[21], 4)
            self.states[21].define_operation('Y', 'Y', self.states[21], 4)


        self.step = 0
        # This is the initial state
        self.state = self.states[6]
        # The tape is composed of a buffer to represent the infinite number of zeros of the UTM, the simulated machine's tape. it's internal machine condition, and the actual program describing that simulated machine.
        self.tape = Tape(list("0"*infinity_buffer_size + simulated_machine_tape + "M" + "0"*t_buffer_size + "Y" + simulated_machine_condition + simulated_machine_description + "Y" + "0"*infinity_buffer_size), \
            infinity_buffer_size + len(simulated_machine_tape) + 1 + t_buffer_size + 1 + len(simulated_machine_condition))

    # Run the UTM
    def execute(self):
        self.print_all(ignore_verbosity=True)
        while self.step < self.max_steps:
            self.step += 1
            symbol = self.tape.scan()
            self.print_before_operation()
            operation = self.state.get_operation(symbol)
            try:
                self.state = operation.execute(self.tape)
            except EndOfTapeException:
                if self.verbosity >= 0:
                    print('Reached the end of the infinite tape. Increase buffer size to proceed further.')
                    break
                break
            except HaltException:
                if self.verbosity >= 0:
                    print("Found halting state. Halting.")
                    break
                break
            self.print_after_operation()
        self.print_all(ignore_verbosity=True)
        return self.step

    def print_all(self, ignore_verbosity=False):
        self.print_before_operation(ignore_verbosity)
        self.print_after_operation(ignore_verbosity)

    # Printing the output
    def print_before_operation(self, ignore_verbosity=False):
        if self.verbosity >= 0:
            operation = self.state.get_operation(self.tape.scan())
            self.current_verbosity = operation.verbosity
            if self.current_verbosity <= self.verbosity or ignore_verbosity:
                print("State " + self.state.id_string(), end = ' ')
                print("reading " + self.tape.scan(), end = ' ')
                print("writing " + operation.print_symbol, end = ' ')
                if operation.target_state:
                    if operation.target_state.direction == "R":
                        print("shifting right", end = ' ')
                    if operation.target_state.direction == "L":
                        print("shifting left ", end = ' ')
                else:
                    print("stopping      ", end = ' ')
                

    def print_after_operation(self, ignore_verbosity=False):
        if self.verbosity >= 0:
            if self.current_verbosity <= self.verbosity or ignore_verbosity:
                print("resulting in:  " + "".join(self.tape.tape), end = ' ')
                print("Step " + str(self.step))
                print(" "*59 + " "*self.tape.head_location + "A")


# The tape of the UTM
class Tape:
    def __init__(self, initial_tape, head_location):
        self.tape = initial_tape
        self.head_location = head_location

    def scan(self):
        return self.tape[self.head_location]

    def shift_left(self):
        self.head_location -= 1
        if self.head_location < 0:
            raise EndOfTapeException()

    def shift_right(self):
        self.head_location += 1
        if self.head_location >= len(self.tape):
            raise EndOfTapeException()

    def write(self, print_symbol):
        self.tape[self.head_location] = print_symbol


class EndOfTapeException(Exception):
    pass


class HaltException(Exception):
    pass


# An operation of the UTM
class Operation:

    def __init__(self, print_symbol, target_state, verbosity):
        self.print_symbol = print_symbol
        self.target_state = target_state
        self.verbosity = verbosity

    def execute(self, tape):
        tape.write(self.print_symbol)
        r = False
        if self.target_state:
            if self.target_state.direction == "R":
                tape.shift_right()
            if self.target_state.direction == "L":
                tape.shift_left()
            return self.target_state
        else:
            raise HaltException()

# A state of the UTM
class State:

    def __init__(self, id_num, direction, implicit_quintuples=True):
        self.id = id_num
        self.direction = direction
        self.operations = dict()
        self.implicit_quintuples = implicit_quintuples

    def id_string(self):
        if self.id < 10:
            return "0" + str(self.id)
        else:
            return str(self.id)

    def define_operation(self, scan_symbol, print_symbol, target_state, verbosity):
        self.operations[scan_symbol] = Operation(print_symbol, target_state, verbosity)

    def get_operation(self, scan_symbol):
        try:
            return self.operations[scan_symbol]
        except KeyError:
            if self.implicit_quintuples:
                # As specified on page 123 of the Minsky book, the most common quintuples, of the form (qi, sj, qi, sj, dij) are implicit.
                return Operation(scan_symbol, self, 4)
            else:
                # In order to make exploitation harder, we may restrict input to valid symbols.
                raise HaltException()

import argparse
from minskys_turing_machine_lib import UTM

# Verbosity
parser = argparse.ArgumentParser(description='A Universal Turing Machine as described in Minsky, Computation: Finite and infinite machines, 1967, Chapter 7.')
parser.add_argument('--verbosity', type=int, default=1, help='Degree of vebosity, -1 to 4.')

args = parser.parse_args()

# The original program cannot be manipulated by the attacker, so the exploit must be able to handle all original programs. Because the first quintuple is all that the machine ever needs to come into contact with, we need not concern ourselves with larger programs; if it works for any single quintuple, then it will work for all programs.
for quintuple_1_machine_state in ['00', '01', '10', '11']:
    for quintuple_1_scanned_symbol in ['0', '1']:
        for quintuple_1_target_state in ['00', '01', '10', '11']:
            for quintuple_1_printed_symbol in ['0', '1']:
                # We do not explore the option of shifting the machine head right, as this will bring it to its end rather than onto the user input. Arguably, programs that do not consider the user input may be ignored as a degenerated special case.
                for quintuple_1_direction in ['0']:
                    machine_description="X" + quintuple_1_machine_state + quintuple_1_scanned_symbol + quintuple_1_target_state + quintuple_1_printed_symbol + quintuple_1_direction 
                    # For any valid program, the first machine state and scanned symbol must point to a quintuple in the original program.
                    initial_utm_state = quintuple_1_machine_state
                    initial_utm_symbol = quintuple_1_scanned_symbol
                    utm_condition = initial_utm_state + initial_utm_symbol
                    # This can be anything that the malicious code is to operate on.
                    initial_fake_input = "1111"
                    # This can be any malicious code of the attacker's choosing.
                    malicious_code = "XAAAAAAAXAABAAAA"
                    # It happens that the symbol printed by the first quintuple will be interpreted as the first symbol in the next state to look for. This condition is satisfied by providing a matching fake state, thus tricking the machine into executing a crafted quintuple in the user data. The second symbol in the state needs to be an 'A'.
                    if quintuple_1_printed_symbol == '0':
                        initial_fake_state = 'AA'
                    else:
                        initial_fake_state = 'BA'
                    # The initial fake symbol needs to be an 'A'.
                    for initial_fake_symbol in ['A']:
                        initial_fake_condition = initial_fake_state + initial_fake_symbol
                        machine_tape= initial_fake_input + "Y" + initial_fake_condition + malicious_code + "S"
                        utm = UTM(machine_description, machine_tape, utm_condition, 2, args.verbosity)
                        steps = utm.execute()
                        print("--machine_tape=\"" + machine_tape + "\" --machine_condition=\"" + utm_condition + "\" --machine_description=\"" + machine_description + "\"")
                        if (steps == 1902) or (steps == 2334):
                            print("Success")
                        else:
                            print("Failure")
                            print(steps)

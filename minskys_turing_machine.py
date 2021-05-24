import argparse
from minskys_turing_machine_lib import UTM

parser = argparse.ArgumentParser(description='A Universal Turing Machine as described in Minsky, Computation: Finite and infinite machines, 1967, Chapter 7.')
parser.add_argument('--machine_condition', type=str, default="001", help="The internal state and the currently read symbol. The default starts in state 00 and the head is scanning a 1.")
parser.add_argument('--machine_description', type=str, default="X0000001X0010110X0100011X0110100", help="The program of the Turing machine to be simulated.")
parser.add_argument('--machine_tape', type=str, default="1111YBAAXAAAAAAAXAABAAAAS", help="The simulated Turing machine's initial tape. The default is an exploit that achieves arbitrary code execution.")
parser.add_argument('--infinity_buffer_size', type=int, default=2, help='Number of zeros to the left and right of the UTM tape,')
parser.add_argument('--t_buffer_size', type=int, default=6, help='Number of zeros to the right of the simulated machine\'s tape,')
parser.add_argument('--max_steps', type=int, default=float("inf"), help='Maximum number of steps to execute before terminating the program.')
parser.add_argument('--verbosity', type=int, default=1, help='Degree of vebosity, -1 to 4.')
parser.add_argument('--explicit_quintuples', action='store_true', help='In Minsky\'s original machine the most common quintuples, of the form (qi, sj, qi, sj, dij) are implicit. We can require explicit ones instead, though.')
parser.add_argument('--dangerous_quintuples', action='store_true', help='If explicit quintuples are enabled, we can add the specific set of quintuples that make exploitation possible. The results will be the same is when disabling explicit quintuples, though.')
args = parser.parse_args()

utm = UTM(args.machine_description, args.machine_tape, args.machine_condition, infinity_buffer_size=args.infinity_buffer_size, t_buffer_size=args.t_buffer_size, max_steps=args.max_steps, verbosity=args.verbosity, implicit_quintuples=(not args.explicit_quintuples), dangerous_quintuples=args.dangerous_quintuples)
utm.execute()

# turing
Exploiting the UTM

This is an implementation of the Universal Turing Machine as presented in Minsky, Computation: Finite and infinite machines, 1967, Chapter 7.

The default input to the simulated machine is an exploit that achieves arbitrary code execution.


Run the program with

```console
$ python3.7 minskys_turing_machine.py 
State 19 reading S writing B shifting left  resulting in:  00111MYBAAXAAAAAAAXAABAAAAB1000Y01SX0000001X0010110X0100011X0110100Y00 Step 380
                                                                                    A
State 19 reading S writing B shifting left  resulting in:  0011M0Y00BX0000000X001000011000Y00SX0000001X0010110X0100011X0110100Y00 Step 721
                                                                   A
State 19 reading S writing B shifting left  resulting in:  001M00Y00BX0000000X001000011000Y00SX0000001X0010110X0100011X0110100Y00 Step 1055
                                                                   A
State 19 reading S writing B shifting left  resulting in:  00M000Y00BX0000000X001000011000Y00SX0000001X0010110X0100011X0110100Y00 Step 1393
                                                                   A
State 18 reading S writing A shifting left  resulting in:  0M0000Y00AX0000000X001000011000Y00SX0000001X0010110X0100011X0110100Y00 Step 1735
                                                                   A
State 18 reading S writing A shifting left  resulting in:  M00000Y00AX0000000X001000011000Y00SX0000001X0010110X0100011X0110100Y00 Step 1909
                                                                   A
Ran out of tape!

```

Help is provided with 

```console
$ python3.7 minskys_turing_machine.py -h
usage: minskys_turing_machine.py [-h] [--machine_condition MACHINE_CONDITION]
                                 [--machine_description MACHINE_DESCRIPTION]
                                 [--machine_tape MACHINE_TAPE]
                                 [--verbosity VERBOSITY]

A Universal Turing Machine as described in Minsky, Computation: Finite and
infinite machines, 1967, Chapter 7.

optional arguments:
  -h, --help            show this help message and exit
  --machine_condition MACHINE_CONDITION
                        The internal state and the currently read symbol. The
                        default starts in state 00 and the head is scanning a
                        1.
  --machine_description MACHINE_DESCRIPTION
                        The program of the Turing machine to be simulated.
  --machine_tape MACHINE_TAPE
                        The simulated Turing machine's initial tape. The
                        default is an exploit that achieves arbitrary code
                        execution.
  --verbosity VERBOSITY
                        Degree of vebosity, 1-4.

```

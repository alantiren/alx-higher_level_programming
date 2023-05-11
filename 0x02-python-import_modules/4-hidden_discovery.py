#!/usr/bin/python3

import dis
import types
import sys

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as f:
        code = f.read()

    # Load the compiled code as a module
    mod = types.ModuleType("hidden_4")
    mod.__file__ = "hidden_4.pyc"
    sys.modules["hidden_4"] = mod
    code = mod.__loader__.code_from_bytes(code)
    mod.__dict__.update(vars(dis))

    # Disassemble the module and extract the names of the variables
    names = set()
    for instr in dis.get_instructions(code):
        if instr.opname == "LOAD_NAME" and instr.argval[:2] != "__":
            names.add(instr.argval)

    # Print the names in alphabetical order
    for name in sorted(names):
        print(name)

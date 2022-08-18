# %%
from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator
# %%
# !!! Function taken from the
# Grover's Search Algorithm portion of the textbook
def display_unitary(qc, prefix=""):
    """Simulates a simple circuit and display its matrix representation.
    Args:
        qc (QuantumCircuit): The circuit to compile to a unitary matrix
        prefix (str): Optional LaTeX to be displayed before the matrix
    Returns:
        None (displays matrix as side effect)
    """
    from qiskit.visualization import array_to_latex
    sim = AerSimulator()
    # Next, we'll create a copy of the circuit and work on
    # that so we don't change anything as a side effect
    qc = qc.copy()
    # Tell the simulator to save the unitary matrix of this circuit
    qc.save_unitary()
    unitary = sim.run(qc).result().get_unitary()
    display(array_to_latex(unitary, prefix=prefix))
# %%
# !!! My original code
# Set up the string
STRING = "000"
LENGTH = len(STRING)
# %%
# Create the oracle circuit
oracle = QuantumCircuit(LENGTH)
# %%
# 
if STRING[-1] == "0":
    oracle.x(0)
for i in range(1, LENGTH):
    if (STRING[-i - 1] == "1"):
        oracle.x(i)
    oracle.cx(i-1, i)
oracle.cz(LENGTH - 1, 0)
for i in range(LENGTH - 1, 0, -1):
    oracle.cx(i-1, i)
    if (STRING[-i - 1] == "1"):
        oracle.x(i)
if STRING[-1] == "0":
    oracle.x(0)
oracle.draw()
# %%
# !!!! All following code to run the oracle circuit
display_unitary(oracle, "U_\\text{oracle}=")

# %%

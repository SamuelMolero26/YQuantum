
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from math import gcd
from qiskit import transpile



from math import gcd


def order_finding(a, N):
    n_qubits = int(np.ceil(np.log(N))) + 1
    
    qc = QuantumCircuit(n_qubits)
    
    #hadamard gates
    qc.h(range(n_qubits))
    
    qc.measure_all()
    
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator, optimization_level  = 3)
    result = simulator.run(compiled_circuit, shots=1024).result()
    counts = result.get_counts()

    # Extract the most frequent measurement result
    measured_value = max(counts, key=counts.get)
    return int(measured_value, 2)
    

def shor_factor(N):
    while True:  # to avoid None and get a factorization
        a = np.random.randint(2, N)


        factor = gcd(a, N)
        if factor > 1:
            return factor, N // factor  # Found a factor


        r = order_finding(a, N)

        # Step 4: Check if r is valid
        if r is None or r % 2 != 0 or pow(a, r // 2, N) == N - 1:
            return None  # Retry with a different 'a'


        factor1 = gcd(pow(a, r // 2) - 1, N)
        factor2 = gcd(pow(a, r // 2) + 1, N)
        
        if factor1 * factor2 == N and (factor1 > 1 and factor2 > 1):
            return factor1, factor2

N = 35
print(f"Factoring {N}:", shor_factor(N))
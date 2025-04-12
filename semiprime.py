
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from math import gcd
from qiskit import transpile
import QuantumRingsLib
from QuantumRingsLib import QuantumRingsProvider
from quantumrings.toolkit.qiskit import QrBackendV2



from math import gcd


def order_finding(a, N, backend):
    n_qubits = int(np.ceil(np.log(N))) + 1
    
    qc = QuantumCircuit(n_qubits)
    
    #hadamard gates
    qc.h(range(n_qubits))
    
    qc.measure_all()
    
    
    transpiled_qc = transpile(qc, backend)
    
    
    job = backend.run(transpiled_qc, shots = 1024)
    result = job.result()
    counts = result.get_counts()

    # Extract the most frequent measurement result
    measured_value = max(counts, key=counts.get)
    return int(measured_value, 2)
    

def shor_factor(N, backend):
    for iteration in range(20): # to avoid None and get a factorization
        a = np.random.randint(2, N)


        factor = gcd(a, N)
        if factor > 1:
            return factor, N // factor  # Found a factor


        r = order_finding(a, N, backend)

       # Check if r is valid
        if r is None or r % 2 != 0 or pow(a, r // 2, N) == N - 1:
            continue  


        factor1 = gcd(pow(a, r // 2) - 1, N)
        factor2 = gcd(pow(a, r // 2) + 1, N)
        
        if factor1 * factor2 == N and (factor1 > 1 and factor2 > 1):
            return factor1, factor2
        
    return None

provider  = QuantumRingsProvider(token='rings-200.zQqULWzwsK1dEEYiumxQ1i6fedLpIJZi',
    name='samueljosemolero@tamu.edu')
backend = QrBackendV2(provider, num_qubits = 8)
provider.active_account()


print(shor_factor(143, backend))
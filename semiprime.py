
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from math import gcd
from qiskit import transpile
import QuantumRingsLib
from QuantumRingsLib import (
    QuantumRegister, ClassicalRegister, QuantumCircuit,
    QuantumRingsProvider, OptimizeQuantumCircuit, job_monitor
)
from quantumrings.toolkit.qiskit import QrBackendV2



from math import gcd




def order_finding(a, N, backend):
    #n_qubits = int(np.ceil(np.log(N))) + 1
    #n_qubits = N.bit_length() // 2
    n_qubits = int(np.ceil(np.log2(N)))  # OR set a max limit like 10–15
    n_qubits = min(n_qubits, 12)
    #print(n_qubits)
    
    q = QuantumRegister(n_qubits)
    c = ClassicalRegister(n_qubits)
    qc = QuantumCircuit(q, c)
    
    #hadamard gates
    qc.h(q)
    
    for i in range(n_qubits - 1):
        qc.cx(q[i], q[i + 1])
    qc.measure_all()
    
    
    
    transpiled_qc = transpile(qc, backend, optimization_level= 3)
    
    
    job = backend.run(transpiled_qc, shots = 512)
    job_monitor(job, quiet = True)
    result = job.result()
    counts = result.get_counts()

    # Extract the most frequent measurement result
    measured_value = max(counts, key=counts.get)
    return int(measured_value, 2)
    

def shor_factor(N, backend):
    count = 0
    while True:
        print(count)
        count += 1
        
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
        
        if factor1 * factor2 == N and factor1 > 1 and factor2 > 1:
           
            return factor1, factor2
        
    return None
from dotenv import load_dotenv
import os
load_dotenv()

token = os.getenv("QUANTUM_RINGS_TOKEN")
name = os.getenv("QUANTUM_RINGS_NAME")
provider  = QuantumRingsProvider(token= token,
    name= name)
backend = provider.get_backend("scarlet_quantum_rings")

provider.active_account()


print(shor_factor(899, backend))
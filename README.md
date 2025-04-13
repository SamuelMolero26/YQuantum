# YQuantum Team: The Dirac Attack

## Our implementation

Our code runs through Quantum Rings' list of semiprimes and utilizes Shor's algorithm to factor them in order. 

The code by be run with a Quantum Rings account. In the qr_provider variable, replace the fillers with your token from Quantum Rings' website and your username (email from signup). 

1. **Python 3.11+** 
2. **Jupyter Notebook**
3. **QuantumRings API Token** (Register at [quantumrings.com](https://quantumrings.com))

## Configuration

1. **API Token Setup**  
   Replace in Notebook.

2. **Semiprimes File**  
Ensure `semiprimes.py` exists in your working directory with this structure:
semiprimes = {
8: 143,
10: 899,
 ... (keep original structure from Quantum Rings repo)
}

## Key Features

- **Hybrid Architecture**  
Combines Qiskit simulators with QuantumRings' 128-qubit hardware.
- **Optimized Circuits**  
Implements approximate QFT and parallel runs for faster factorization. Additional testing may be done with the full Inverse QFT.
- **Automatic GCD Filtering**  
Skips trivial factors before quantum simulations performed.

## References

- [Qiskit Textbook: Shor's Algorithm](https://qiskit.org/textbook/ch-algorithms/shor.html)
- [QuantumRings Documentation](https://quantumrings.com/docs)

**Note:** Actual factorization times depend on quantum hardware availability. Larger numbers (50+ bits) require distributed quantum simulator resources and significantly longer runtimes. 

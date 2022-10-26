# Quantum-safe-cryptograph-Quantum-random-number-generator

Quantum computers will eventually become more readily available and by the end of the 2020- decade 
they would be able to break through most classical cryptography. Random number generators are at the 
core of such a cryptographic system, there is an effort to build new quantum-resistant cryptography that 
would be resilient to both classical and quantum computers. This project aims to implement and perform a 
comparative analysis of classical and quantum algorithms for random number generators for use in quantum-resistant cryptography.

## Getting Started

### Prerequisite:
You need the following software and packages for this application:
1. Python 3.8 and above 
2. Qiskit,Numpy,Scipy,Matplotlib,PySimpleGUI
```
pip3 install qiskit, numpy, scipy ,matplotlib,PySimpleGUI
```

### How to use:
* You can start the program using your IDE feature (like run) to run main.py or 
```
    python3 main.py in terminal 
```
* User Interface
![User Interface Screenshot](https://github.com/CS-UWC/Quantum-safe-cryptograph-Quantum-random-number-generator-/blob/main/UI.PNG)

    * Text Box - Input text to this data block for the appication to encrypt
    * Add Button - Add the text so it can be used to encrypt
    * Browse Button - Browse through local computer for a text file that contains data to encrypt
    * Submit - Reads the data in so it can be encrypted
    * PRNG Button - Encrypt data using the pseudo-random number generator 
    * 1 - 7 Button - Encrypt data using the quantum-random number generator ( The number implies how much Hardman gates should be applied)  
    * Decrypt Button - Decrypts the encrypted data
    * NIST test suite Checkbox - Applies the NIST test suite which can be found here (https://github.com/stevenang/randomness_testsuite)
				Industry standard testing for random number generator     
    * Key Box - Displays Key generated to decrypt the data
    * clear Button - Button that clears Graphs

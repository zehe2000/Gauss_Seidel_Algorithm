# Gauss-Seidel Project

This part of the project implements and tests the Gauss-Seidel algorithm, a method for solving linear systems of equations iteratively. It includes tools for equation processing, tests to ensure reliability, and automated pre-commit hooks to enforce code quality.

---

## **Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Pre-commit Hook](#pre-commit-hook)
- [License](#license)

---

## **Overview**

The Gauss-Seidel project solves linear systems of equations of the form:

**Ax = b**

Where:
- `A` is a square matrix of coefficients.
- `b` is a vector of constants.
- `x` is the vector of unknowns.

This implementation also validates the input matrices and provides a robust set of tests for edge cases like:
- Overdetermined or underdetermined systems.
- Matrices with missing or invalid values.

---

## **Features**

- **Implementation of the Gauss-Seidel algorithm** (`gauss_seidel_algorithm.py`).
- **Equation processing utilities** (`read_equation.py`):
  - Reads input matrices and vectors from files.
  - Validates inputs for correctness.
- **Unit tests** to ensure algorithm reliability and input validation:
  - `test_gauss.py` tests the Gauss-Seidel algorithm.
  - `test_read_equation.py` tests equation file parsing and validation.
- **Pre-commit hook** to enforce code quality by running tests before committing.

---

## **Requirements**

- **Python 3.8 or higher**
- **Required Python packages**:
  - `numpy`
  - `pytest`

To install dependencies, run:
```bash
pip install -r requirements.txt
```

---

## **Installation**

1. Clone the repository and navigate to the `gauss_seidel` directory:
   ```bash
   git clone https://github.com/freiburg-missing-semester-course/13-Project-Zehe2000.git
   cd 13-Project-Zehe2000/gauss_seidel
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set the `PYTHONPATH` environment variable to include the `gauss_seidel` directory:
   ```bash
   export PYTHONPATH=$(pwd)
   ```

To make this permanent, add it to your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`):
```bash
echo 'export PYTHONPATH=$(pwd)/gauss_seidel' >> ~/.bashrc
source ~/.bashrc
```

---

## **Usage**

1. **Solve a System of Equations**
   - Use the `main.py` script to solve systems of equations:
     ```bash
     python main.py
     ```
   - The script reads input matrices and vectors from the `matrices_as_txt` directory.

2. **Run Tests Manually**
   - Run all tests using:
     ```bash
     pytest tests/
     ```

---

## **Tests**

The `tests/` directory includes unit tests for key components:
1. **`test_gauss.py`**: Validates the Gauss-Seidel algorithm.
2. **`test_read_equation.py`**: Validates input parsing and matrix/vector validation.

To run the tests:
```bash
pytest tests/
```

---

## **Pre-commit Hook**

The `gauss_seidel/.githooks/pre-commit` script ensures code quality by running all tests before allowing a commit.

### Setting Up the Pre-commit Hook

1. Configure Git to use the custom hooks directory:
   ```bash
   git config core.hooksPath gauss_seidel/.githooks
   ```

2. Ensure the pre-commit hook script is executable:
   ```bash
   chmod +x gauss_seidel/.githooks/pre-commit
   ```

3. Now, every commit will run all tests in the `tests/` directory. If any test fails, the commit will be blocked until the issue is resolved.

---

## **Directory Structure**

```
gauss_seidel/
├── .githooks/
│   └── pre-commit           # Pre-commit hook script
├── matrices_as_txt/         # Input files for matrices and vectors
├── tests/                   # Unit tests
│   ├── test_gauss.py
│   ├── test_read_equation.py
│   └── broken_txt/          # Malformed input files for testing
├── gauss_seidel_algorithm.py # Implementation of the Gauss-Seidel algorithm
├── main.py                  # Main script to run the program
├── read_equation.py         # Input parsing and validation
└── readme.md                # Documentation
```

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

---

## **Contributing**

Contributions are welcome! If you would like to contribute, please:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.


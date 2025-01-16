# Beer Brewing Process Simulation - README

## **Project Overview**
This project models the beer brewing process, including seven stages: milling, mashing, grain washing, boiling, cooling, fermentation, and conditioning. The project uses mathematical models (ODEs) to simulate mass and energy balances for each stage. The goal is to optimize the process for efficiency, quality, and control, integrating advanced techniques like Model Predictive Control (MPC) or NSGA-II optimization.

---

## **Features**
- Modular design for each brewing stage.
- Simulation of key variables such as temperature, sugar concentration, ethanol production, CO\(_2\) release, and pH.
- Integration-ready for coupling stages and incorporating real-world data.
- Support for optimization using NSGA-II and testing frameworks like `pytest`.

---

## **Environment Setup**
### **Requirements**
- Python >= 3.8
- Anaconda environment (recommended)

### **Required Libraries**
Install the following Python libraries:
```bash
pip install numpy scipy matplotlib pandas sympy pytest pymoo
```

### **Optional Libraries**
For enhanced testing and visualization:
```bash
pip install pytest-benchmark seaborn
```

### **Setting Up the Environment**
1. Create a new Anaconda environment:
   ```bash
   conda create -n brewing_env python=3.8
   conda activate brewing_env
   ```
2. Install the required libraries:
   ```bash
   pip install numpy scipy matplotlib pandas sympy pytest pymoo
   ```

---

## **Project Structure**
```
.
├── src/
│   ├── milling.py
│   ├── mashing.py
│   ├── grain_washing.py
│   ├── boiling.py
│   ├── cooling.py
│   ├── fermentation.py
│   ├── conditioning.py
│   └── utils/   # Shared utility functions
├── tests/
│   ├── test_milling.py
│   ├── test_fermentation.py
│   └── ...
├── data/
│   ├── input_parameters.json  # Default parameters for each stage
│   └── simulation_results.csv # Outputs
├── README.md
└── environment.yml  # Conda environment setup
```

---

## **Running the Project**
### **Simulating Individual Stages**
Each module is independent and can be tested individually. For example:
```bash
python src/fermentation.py
```

### **Testing**
Unit and integration tests are available for all modules using `pytest`. Run tests with:
```bash
pytest tests/
```

---

## **Integration and Optimization**
### **Connecting Modules**
The output of one stage (e.g., cooling) feeds into the input of the next (e.g., fermentation). This ensures smooth integration and modularity.

### **Optimization**
Use the `pymoo` library to apply NSGA-II for optimizing process parameters. Example optimizations include:
- Maximizing ethanol yield.
- Minimizing energy usage during cooling.

---

## **Contributing**
1. Fork the repository and create a new branch.
2. Write clear and concise code following the modular structure.
3. Add tests for new modules or modifications.
4. Submit a pull request with a detailed explanation.

---

## **References**
- Brewer’s Handbook
- ODE models for chemical processes
- Libraries: `scipy`, `numpy`, `pymoo`, `matplotlib`

---

Let me know if you'd like any changes or additions!
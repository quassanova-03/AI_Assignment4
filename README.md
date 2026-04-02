# AI Assignment 4

## Overview
This assignment explores multiple problems modeled using Constraint Satisfaction Problems (CSP). Each problem is solved using backtracking search, where variables are assigned values such that all constraints are satisfied.

Here, it has been demonstrated how CSP can be applied across different domains including:
- Map Colouring
- Sudoku Solving
- Crypt-Arithmetic

## What is CSP?
A Constraint Satisfaction Problem (CSP) consists of:

- Variables : Elements that need values  
- Domains : Possible values each variable can take  
- Constraints : Rules restricting valid combinations  

The goal is to:
Assign values to all variables such that all constraints are satisfied.

## Problems

### 1. Australia Map Colouring
Assign colors to Australian regions such that no two adjacent regions share the same color.

**CSP Formulation :**
- Variables: Regions
- Domain: Colours (Red, Green, Blue)
- Constraints: Neighbouring regions must have different colours

**Features :**
- Finds all valid solutions
- Interactive solution selection
- Graph visualization

### 2. Telangana Map Colouring
A larger map coloring problem involving 33 districts.

**CSP Formulation :**
- Variables: Districts
- Domain: Colours (Red, Green, Blue, Yellow)
- Constraints: Adjacent districts must have different colours

**Features :**
- Optimized to find one solution
- Constraint validation
- Improved graph visualization

### 3. Sudoku Solver
Solves a 9×9 Sudoku puzzle using CSP.

**CSP Formulation :**
- Variables: 81 cells
- Domain: {1, 2, 3, 4, 5, 6, 7, 8, 9}
- Constraints:
  - Row uniqueness
  - Column uniqueness
  - 3 x 3 grid uniqueness

**Features :**
- Backtracking solver
- Step count tracker
- GUI display using tinker
- Clean sudoku grid visualization

### 4. Crypt-Arithmetic Puzzle
Solves a letter-based arithmetic puzzle using digit assignments.
(TWO + TWO = FOUR)

**CSP Formulation :**
- Variables: Letters  
- Domain: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} 
- Constraints:
  - Unique digits 
  - Leading digit should not be 0  
  - Arithmetic equation holds  

**Features :**
- Backtracking-based solution  
- Finds all valid solutions  
- Interactive solution selection  
- Step count tracking

## Project Structure
```
AI_Assignment4/
│
├── CSP_Australia/
│ └── CSP_Australia.py
│
├── CSP_Telangana/
│ └── CSP_Telangana.py
│
├── CSP_Sudoku/
│ └── CSP_Sudoku.py
|
├── CSP_Crypt/
│ └── CSP_Crypt.py
|
└── README.md
```
- Language : Python

## How to run the code
1. Navigate to the directory
   ```
   cd AI_Assignment4/CSP_Australia
   ```
2. Run the python file
   ```
   python CSP_Australia.py
   ```
   or
   ```
   py CSP_Australia.py
   ```
Application is similar for all of the files

## Concepts Used
- Backtracking Search
- Constraint Checking
- Recursive Problem Solving

## Applications
- Map Coloring (Geography, Scheduling)
- Puzzle Solving (Sudoku, Logic games)
- Cryptography and Code Breaking
- Resource Allocation
- AI Planning Systems

## Conclusion
This assignment demonstrates how diverse problems can be modeled using a single framework: Constraint Satisfaction Problems.
By applying backtracking and constraint checking, we solve problems across different domains efficiently and systematically.


# cmpsc-463-project-2

## Overview
This project is a web-based tool designed to help allocate emergency resources during severe weather crises. The system uses Greedy selection, Knapsack optimization, Minimum Spanning Tree planning, and Maximum Flow routing.
The application is built with Python (Flask) on the backend and a simple HTML/JavaScript frontend.

## Features
**Greedy Allocation**

Selects regions based on urgency and distributes resources as efficiently as possible.

**Knapsack Optimization**

Uses dynamic programming to maximize total urgency while staying under supply constraints.

**Maximum Flow Routing**

Models transportation networks as directed graphs to calculate the maximum possible resource flow from a depot to regions.

**HTML User Interface for Algorithm Testing**

Users can enter region data, supply limits, and even build a max-flow capacity matrix directly in the browser.

## Repository Structure

```
weather-crisis-resource-allocation/
│
├── backend/
│   ├── algorithms/
│   │   ├── greedy.py
│   │   ├── knapsack.py
│   │   ├── maxflow.py
│   │   ├── mst.py
│   ├── models/
│   │   └── data_models.py
│   └── app.py
│
├── web/
│   └── index.html
│
└── README.md
```

## Installation & Setup

### 1. Clone the repository
```
git clone https://github.com/YourUsername/weather-crisis-resource-allocation.git
cd weather-crisis-resource-allocation/backend
```
### 2. Install Python dependencies
Make sure you have Python 3.9+ installed.
```
pip install flask flask-cors
```
### 3. Run the server
```
python ./weather-crisis-resource-allocation/app.py
```
### 4. Open the web interface


## Team Members / Creators
Ian Grinarml & Faviana Troshani

# Car Wash Operation Stochastic Simulation

A modular, event-driven simulation engine designed to model the daily operations of a service business (car wash) using probabilistic models. It calculates resource utilization metrics and serves as an HR Decision Support System (DSS).

## 🏗️ Project Architecture
The project is built using a highly structured, modular architecture:
* **`app.py`:** The main user interface and entry point for running simulation scenarios.
* **`engine.py`:** The core simulation engine that processes time steps, queues, and tracks staff utilization metrics.
* **`decision.py`:** A rule-based Decision Support Module that analyzes simulation outcomes to recommend hiring or capacity adjustments.
* **`distributions.py`:** Generates stochastic models for dynamic customer arrivals and varied service times using random distributions.

## 📈 Core Capabilities
* Simulates a standard shift (e.g., 600 minutes) with random operational variables.
* Measures dynamic capacity utilization rates for the staff.
* Evaluates bottleneck points in customer queues.
* Provides rule-based recommendations on whether the business needs more staff or if the current capacity is optimized.

## 🛠️ Tech Stack
* Python 3
* Modular Software Design (`Separation of Concerns`)

# Cosmological Parameter Estimation: Bayesian Inference with cpnest

[![Python Version](https://img.shields.io/badge/Python-3.7-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](../../LICENSE) ## Description

## Project Goal
This project applies advanced statistical inference techniques to estimate key **cosmological parameters** ($\Omega_{\Lambda}, \Omega_{M}$) that govern the expansion and destiny of the Universe. It uses observational data from **Type Ia Supernovae (SN Ia)** surveys (specifically, data derived from Perlmutter et al. 1999, [1]) to test and quantify uncertainties across different cosmological models (Flat, Closed, and Open Universes).

## Core Methodology: Nested Sampling

The analysis utilizes the **`cpnest` library**, a powerful and efficient Python package implementing the **Nested Sampling** algorithm.

The current report uses **Supernovae Ia (SN Ia) data** presented in **Perlmutter et al. 1999, "Measurements of Omega and Lambda from 42 High-Redshift Supernovae"** (Reference: [1]) to estimate the cosmological parameters, $\Omega_{\Lambda}$ and $\Omega_{M}$. This advanced Bayesian technique is superior to traditional Markov Chain Monte Carlo (MCMC) methods for complex, high-dimensional likelihood spaces, enabling:

* **Robust Parameter Estimation:** Accurately calculating the probability distributions (posteriors) for parameters like the dark energy density, $\Omega_{\Lambda}$.
* **Bayesian Model Comparison:** Computing the **Bayesian evidence** (or model likelihood), which is essential for comparing the fit of competing cosmological models.

## Project Structure
```
.
├── README.md               <- This file
├── ObsCosNest_flat.py           <- Python script for fitting a Flat Universe model (Ω_m + Ω_Λ = 1)
├── ObsCosNest_closed.py         <- Python script for fitting a Closed Universe model (Ω_m + Ω_Λ > 1)
├── ObsCosNest_open.py           <- Python script for fitting an Open Universe model (Ω_m + Ω_Λ < 1)
├── Cornerplot_flat.py           <- Python script to generate corner plots from cpnest posterior samples
├── Cornerplot_closed.py         <- Python script to generate corner plots from cpnest posterior samples
├── Cornerplot_open.py           <- Python script to generate corner plots from cpnest posterior samples
├── supernovae_data.dat          <- Input observational data for cosmological analysis (e.g., Supernovae data)
├── Run_files_flat/         <- Output directory for results from Flat Model (cpnest output files)
├── Run_files_closed/       <- Output directory for results from Closed Model (cpnest output files)
├── Run_files_open/         <- Output directory for results from Open Model (cpnest output files)
├── Corner_plots/           <- Output directory for generated corner plots (PNG images)
└── requirements.txt        <- Python dependencies specific to this project
```

## Data Analysis Workflow

This section outlines the logical steps the Python scripts execute to go from raw observational data to final cosmological parameter posteriors.

### 1. Likelihood Definition
A **log-likelihood function** is defined to quantify the **goodness-of-fit**. This calculation compares the **observed distance modulus** data ($\mu$, stored in `self._data`) against the theoretical **distance modulus** predicted by the `CosmologyModel` function (`self._model`), weighted by the observed uncertainty ($\sigma$). This is the core step that constrains the cosmological parameters ($\Omega_{\Lambda}, \Omega_{M}$).

### 2. Model Definition
The project defines and tests three distinct cosmological models, each with a specific constraint on the density parameters ($\Omega_{M}$ and $\Omega_{\Lambda}$):
* **Flat Universe:** $\Omega_{M} + \Omega_{\Lambda} = 1$
* **Closed Universe:** $\Omega_{M} + \Omega_{\Lambda} > 1$
* **Open Universe:** $\Omega_{M} + \Omega_{\Lambda} < 1$

### 3. Nested Sampling Execution
The dedicated Python scripts (`ObsCosNest_*.py`) invoke the `cpnest` sampler, defining the parameter priors and the complex **log-likelihood function** (which quantifies the goodness-of-fit). The sampler runs iteratively, exploring the high-dimensional parameter space to generate thousands of weighted samples.

### 4. Results Generation and Visualization
The final samples are saved to the respective `Run_files_*` directories. Separate scripts (`Cornerplot_*.py`) then process these samples to generate **corner plots**  which graphically display the marginalized 1D and 2D posterior probability distributions, including the final **confidence intervals** for the estimated parameters.

## Features / Highlights

* **Advanced Bayesian Inference:** Application of Bayes' theorem for robust parameter estimation, providing full posterior probability distributions.
* **Nested Sampling with `cpnest`:** Efficient computation of Bayesian evidences and accurate posterior distributions for complex likelihoods, particularly effective for high-dimensional parameter spaces.
* **Cosmological Model Exploration:** Implements and compares three different cosmological models (Flat, Closed, and Open Universes) by fitting key parameters (e.g., absolute magnitude `M`, matter density `Ω_M`, dark energy density `Ω_Λ`).
* **Numerical Integration of Cosmology:** Uses numerical methods (e.g., `np.trapz`) to solve the luminosity distance integral for different cosmological scenarios.
* **Uncertainty Quantification:** Robust estimation of parameter uncertainties, correlations, and credible intervals through analysis of posterior samples.
* **Scientific Computing & Domain Expertise:** Demonstrates proficiency in handling specialized scientific datasets and applying advanced computational tools within the field of observational cosmology.
* **Reproducible Analysis:** Code is provided in standalone Python scripts, designed for clear execution and analysis.

## Installation and Setup

This project requires a specific Python environment due to library compatibility, particularly with `cpnest`.

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone [https://github.com/vfgalabo/Coding_portfolio.git](https://github.com/vfgalabo/Coding_portfolio.git)
    cd Observational_cosmology
    ```
    
2. **Install LaTeX Distribution (for plot rendering):**
    This project uses LaTeX for high-quality text rendering in plots (`matplotlib.rc('text', usetex=True)`). You will need a LaTeX distribution installed on your system.
    * **macOS:** Install [MacTeX](https://tug.org/mactex/).
    * **Linux:** Install [TeX Live](https://www.tug.org/texlive/) (e.g., `sudo apt-get install texlive-full` or `texlive-latex-extra`).
    * **Windows:** Install [MikTeX](https://miktex.org/download) or [TeX Live](https://www.tug.org/texlive/).

    After installation, ensure LaTeX commands are available in your system's PATH.
    
3.  **Create and activate a dedicated Python 3.7 virtual environment (highly recommended for `cpnest` compatibility):**
    * **Using `conda` (recommended for easier environment management):**
        ```bash
        conda create -n cpnest_env python=3.7
        conda activate cpnest_env
        ```
    * **Using `venv` (standard Python virtual environment):**
        ```bash
        python3.7 -m venv venv_cpnest
        source venv_cpnest/bin/activate
        ```

4.  **Install Python dependencies:**
    * First, ensure `pip` is updated within your new environment:
        ```bash
        python -m pip install --upgrade pip
        ```
    * Then, install project-specific requirements:
        ```bash
        pip install -r requirements.txt
        ```
# --- ENVIRONMENT NOTE ---
"""
OS DEPENDENCY: This code relies on the standard Unix 'signal' module. 
It is intended to be run on **Linux** or **macOS**. 
Execution on Windows operating systems (even within Anaconda) may fail 
with an AttributeError (SIGALRM) due to platform incompatibility with 
native system signals.
"""
# ------------------------
## Usage

To run the cosmological parameter estimation analysis for each model and generate plots:

1.  Ensure you have followed the [Installation and Setup](#installation-and-setup) steps.
2.  Activate your virtual environment (e.g., `conda activate cpnest_env`).
3.  **Run the cosmological model scripts:**
    Execute each model script from your terminal. This will run the `cpnest` sampling and save the posterior samples in their respective `Run_files_...` folders.
    ```bash
    python ObsCosNest_flat.py
    python ObsCosNest_open.py
    python ObsCosNest_closed.py
    ```
4.  **Generate Corner Plots:**
    After running the model scripts, execute the plotting script. This will load the posterior samples and save the corner plots to the `Corner_plots/` directory.
    ```bash
    python Cornerplot_flat.py
    python Cornerplot_open.py
    python Cornerplot_closed.py
    ```

## Results and Insights

This project successfully implemented Bayesian inference using `cpnest` to estimate cosmological parameters across three distinct cosmological models: Flat, Closed, and Open Universes. For each model, the `cpnest` sampler demonstrated effective exploration of the parameter space, with all runs showing good convergence to well-defined posterior distributions and generating posterior samples.

### 1. Flat Universe Model ($\mathbf{\Omega_m + \Omega_{\Lambda} = 1}$)

| Parameter | Result | Interpretation |
| :--- | :--- | :--- |
| $\mathbf{\Omega_M}$ (Matter Density) | Well-constrained around $\approx 1.11$ | The model converged successfully to a sharp posterior, confirming the sampler's robustness. (Note: Value is higher than current consensus but reflects model bias for this specific dataset.) |
| **Parameter Correlation** | **Strong Positive Correlation** | The $M$ vs. $\Omega_M$ 2D plot shows clear positive covariance, demonstrating the inherent **degeneracy** between the nuisance parameter ($M$) and matter density. |

### 2. Closed Universe Model ($\mathbf{\Omega_m + \Omega_{\Lambda} > 1}$)

| Parameter | Result | Interpretation |
| :--- | :--- | :--- |
| **$\mathbf{\Omega_M}$ and $\mathbf{\Omega_{\Lambda}}$** | Well-constrained around $\mathbf{\Omega_M \approx 1.11}$ and $\mathbf{\Omega_{\Lambda} \approx 1.00}$ | Both parameters show excellent convergence and Gaussian-like marginalized distributions. |
| **Parameter Correlation** | **Strong Negative Correlation** | The $\mathbf{\Omega_M}$ vs. $\mathbf{\Omega_{\Lambda}}$ 2D plot reveals a classical **anti-correlation** (negative covariance). This is the expected degeneracy when exploring the closed region of parameter space. |

### 3. Open Universe Model ($\mathbf{\Omega_m + \Omega_{\Lambda} < 1}$)

| Parameter | Result | Interpretation |
| :--- | :--- | :--- |
| **Constraint Quality** | **Poorly Constrained / Wide Posteriors** | The marginalized posterior distributions for $\mathbf{\Omega_M}$ and $\mathbf{\Omega_{\Lambda}}$ are wide and less tightly peaked. |
| **Degeneracy Pattern** | **Extreme Anti-Correlation** | The 2D plot shows an extremely elongated, narrow anti-correlation contour. This indicates the model struggles to find a strong best-fit, but successfully maps the region of acceptable solutions (the parameter degeneracy). |

***

### Key Scientific Takeaway

The CPNest routine successfully validates that **the cosmological parameters are strongly degenerate** in the SNe Ia distance measurements, and the sampler is robust enough to map these complex likelihood surfaces and parameter covariances in non-flat geometries.


## Future Work

* Explore more complex cosmological models or alternative likelihood functions (e.g., including neutrino mass, early dark energy).
* Integrate with larger datasets or actual observational data from ongoing surveys.
* Investigate different sampling algorithms within `cpnest` or other packages for comparison (e.g., `emcee`, `dynesty`).
* Implement custom plotting scripts for more specialized visualizations.


## Author

[Vanya Fernandez Galabo]

## References

[1] Perlmutter et al. 1999, “Measurements of Omega and Lambda from 42 High-Redshift Supernovae”
arXiv:astro-ph/9812133
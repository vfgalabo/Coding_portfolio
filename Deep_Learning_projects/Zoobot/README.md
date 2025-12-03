# Zoobot Fine-Tuning: Galaxy Morphology Classification

The goal of this project was to demonstrate proficiency in **Transfer Learning** by fine-tuning the pre-trained **Zoobot convolutional neural network (CNN) backbone** to classify galaxies from the **GalaxyMNIST dataset** into four distinct morphological classes.

The analysis confirms **high accuracy** and provides deep insight into model certainty and systematic errors.

---

## 🧠 Methodology and Architecture

### 1. Project Setup

* **Accelerator:** NVIDIA GPU (CUDA/Google Colab).
* **Base Model:** Zoobot's **ConvNeXt Nano backbone**.
* **Fine-Tuning Type:** **End-to-end fine-tuning**, training the entire $\approx 15 \text{ Million}$ parameter model simultaneously.
* **Data:** **GalaxyMNIST** (10,000 images) [1], split internally by the `CatalogDataModule` into Training, Validation, and Test sets.

### 2. The Fine-Tuning Mechanism

The process involved two key steps, demonstrating an understanding of model adaptation:

1.  The massive pre-trained **encoder (backbone)** was loaded with weights learned from millions of galaxies.
2.  The original output layer was replaced with a **new head layer** specifically sized for the **4** distinct classes (`num_classes=4`), which was trained along with the backbone using a very low learning rate ($\mathbf{10^{-5}}$).

---

## 📈 Key Results & Analytical Findings

### 1. Overall Performance and Efficiency

| Metric | Result | Analytical Insight |
| :--- | :--- | :--- |
| **Overall Accuracy** | **$88.85\%$** | Achieved a highly robust result, confirming successful transfer learning. |
| **Training Time** | **$< 30 \text{ minutes}$** (GPU) | Validated the necessity of GPU acceleration for practical deep learning research (reducing the task from an estimated $\approx 36$ hours on CPU). |
| **Total Parameters** | **$\approx 15.0 \text{ Million}$** | Confirmed the model was fully trained (fine-tuned) end-to-end. |

### 2. Systematic Error Analysis (Confusion Matrix)

The Confusion Matrix (see `zoobot.png`) revealed a **systematic pattern of confusion**, which is typical in early-stage galaxy classification due to structural ambiguities:

* **Highest Error Rate:** The largest single systematic confusion occurred between the **`smooth_cigar`** and **`edge_on_disk`** classes.
* **Cause:** This error is likely due to **structural ambiguity**, where the model struggles to differentiate between a non-edge-on, elongated smooth galaxy (`smooth_cigar`) and an edge-on view of another smooth galaxy (`edge_on_disk`). This suggests a reliance on orientation cues.


### 3. Model Confidence Profile

The Residual Distribution by True Galaxy Class plot (residual_distribution.png) demonstrated the model's reliability:

* The residual histograms for highly successful classes (**`smooth_round`**) are heavily peaked near **$0.0$ (zero error)**, meaning the model is highly certain of its correct predictions.
* The residual distribution for the weakest class, **`smooth_cigar`** (highlighted in the Per-Class Accuracy chart), is noticeably **flatter** and spread out towards **$1.0$**. This confirms that the model's **uncertainty** is directly correlated with its misclassification errors.

---

## Reproduction Instructions

### Prerequisites

* Google Colab (with **GPU runtime selected**).
* `git` must be installed.

### Execution Steps

1.  **Run Cell 1 (Installs & Path Fixes):** Installs `Zoobot` and `galaxy-datasets`, and runs the necessary `sys.path.append` commands to enable successful imports in the Colab environment.
2.  **Run Cell 2 (Data Setup):** Downloads the data and initializes the `CatalogDataModule`.
3.  **Run Cell 3 (Training):** Defines the `FinetuneableZoobotClassifier` and runs the **30-epoch** GPU fine-tuning process.
4.  **Run Final Cells:** Executes the `predict_on_catalog` utility and generates all analytical plots (Confusion Matrix, Per-Class Accuracy, and Residual Distribution).

## References
[1] Walmsley, M., Lintott, C., Géron, T., Kruk, S., Krawczyk, C., Willett, K. W., Bamford, S., Kelvin, L. S., Fortson, L., Gal, Y., Keel, W., Masters, K. L., Mehta, V., Simmons, B. D., Smethurst, R., Smith, L., Baeten, E. M., & Macmillan, C. (2022). Galaxy Zoo DECaLS: Detailed visual morphology measurements from volunteers and deep learning for 314 000 galaxies. *Monthly Notices of the Royal Astronomical Society*, *509*(3), 3966–3985. https://ui.adsabs.harvard.edu/abs/2022MNRAS.509.3966W/abstract


## Acknowledgements and Codebase

This project is built upon the robust **Zoobot** framework, developed for galaxy morphology classification. I am grateful to the authors for making the codebase and pre-trained models publicly available.

### 1. Zoobot Framework and Repository

* **Repository:** The core architecture and pre-trained weights (ConvNeXt Nano backbone) were sourced from the official Zoobot repository.
* **Link:** [https://github.com/mwalmsley/zoobot](https://github.com/mwalmsley/zoobot)

### 2. Implementation Inspiration

This project's methodology, particularly the setup for end-to-end fine-tuning and the use of the `CatalogDataModule`, was inspired by the following tutorial notebook:

* **Inspiration Source:** A Google Colab notebook demonstrating Zoobot fine-tuning for regression
* **Link:** [https://colab.research.google.com/drive/1A_-M3Sz5maQmyfW2A7rEu-g_Zi0RMGz5?usp=sharing](https://colab.research.google.com/drive/1A_-M3Sz5maQmyfW2A7rEu-g_Zi0RMGz5?usp=sharing)

> **Note on Adaptation:** While the inspiration notebook performed a **regression** task (predicting continuous properties), this project adapted the method to perform **classification** (predicting discrete morphological classes).

## Author
[Vanya Fernandez Galabo]
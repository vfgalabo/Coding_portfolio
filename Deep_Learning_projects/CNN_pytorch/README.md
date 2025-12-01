# CIFAR-10 Image Classifier (PyTorch CNN Foundation)

## Project Goal
This project establishes a foundational **Convolutional Neural Network (CNN)** for image classification using the standard CIFAR-10 dataset (10 classes of small images).

---

---
## Theoretical Background: The CNN Process

The architecture is built on two core principles of image recognition:

1.  **Feature Extraction:** The network uses **`nn.Conv2d`** layers (filters) to automatically learn patterns (edges, shapes, textures) across the input image. The repeated application of **ReLU activation** (introducing non-linearity) and **`nn.MaxPool2d`** (reducing dimension while retaining key information) creates a robust hierarchy of learned features.
2.  **Classification Head:** After features are extracted, the tensor is **flattened** into a one-dimensional vector and fed into the **Fully Connected (FC) layers**. These layers map the high-level features learned by the convolutions to the final output, which are 10 logits (scores) corresponding to the 10 possible CIFAR classes.

---

## Key Technical Highlights

* **Deep Learning Framework:** The entire pipeline, from data preparation to model training, is built using the **PyTorch framework** which includes `nn.Module` classes and managing the tensor flow.
* **Convolutional Architecture:** Implements a standard, multi-layered CNN featuring **`nn.Conv2d`** layers for hierarchical feature extraction and **`nn.MaxPool2d`** for dimension reduction.
* **Data Pipelining with `torchvision`:** Uses `torchvision.datasets` and `torch.utils.data.DataLoader` for efficient, parallel loading and batching of the CIFAR-10 dataset, including necessary **data normalization** and tensor conversion.
* **Core Training Loop:** Implements the canonical five-step PyTorch optimization process: **Forward Pass $\rightarrow$ Loss $\rightarrow$ Zero Gradients $\rightarrow$ Backward Pass $\rightarrow$ Optimizer Step**.

## Setup and Execution

### 1. Requirements

This project requires `torch`, `torchvision`, and `numpy`.

```bash
# requirements.txt
torch
torchvision
numpy
```

### 2. Running the Model

The script is executed as a Jupyter notebook and includes comprehensive logging to track the training progress across batches.

```bash
jupyter notebook cnn_pytorch.ipynb
```
## Evaluation and Qualitative Analysis

After training is complete, the model's performance is assessed using the reserved test set. This confirms the network's ability to generalize to unseen data.

### 1. Model Accuracy on Test Set

The script calculates the **overall accuracy** of the model across the entire 10,000-image test set.

### 2. Per-Class Accuracy Report

Beyond overall accuracy, the evaluation includes a detailed **per-class accuracy report**. This crucial step isolates the model's performance on *each* of the 10 CIFAR categories (e.g., 'dog', 'car', 'plane'), identifying specific strengths and weaknesses of the classifier.

### 3. Qualitative Prediction Analysis

A final check is performed by visualizing a single batch of test images and comparing the model's **predicted label** against the **true ground truth label**, providing an intuitive confirmation of the classification results.

## Performance Note: 
This model is trained using CPU. Due to the size of the dataset (50,000 training images), training can be slow (roughly 25 minutes). If high-speed training or deployment is preferred, the pipeline can be migrated to a GPU environment (e.g., using CUDA).

## Author

[Vanya Fernandez Galabo]
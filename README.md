### RAPID: Road Assistance and Prioritized Intervention for Damage

This repository contains the source code for the **RAPID** system, a two-phase framework designed for intelligent road maintenance. RAPID addresses the inefficiencies of traditional, manual road inspection by providing an automated and data-driven approach to detect damage and prioritize repairs.

-----

### Project Overview

The RAPID system is a novel solution that bridges the gap between raw data collection and actionable maintenance planning. Its two phases are:

  * **Phase I: Automated Damage Detection:** This phase utilizes an ensemble of deep learning models to perform pixel-level, semantic segmentation of road surfaces. The models are trained to accurately classify and delineate road features into three categories: background, cracks, and potholes.
  * **Phase II: Data-Driven Repair Prioritization:** The system moves beyond simple detection by integrating the quantified damage data from Phase I with a calculated **Repair Priority Score (RPS)**. This score is derived from a combination of the damage severity and socio-economic factors to generate a ranked list of road segments for repair.

-----

### Key Features

  * **Ensemble Semantic Segmentation:** RAPID employs an ensemble of three advanced deep learning models—**UNet-MobileNetV2**, **UNet-ResNet34**, and **SegFormer B2**—to achieve high-performance and robust damage detection. This approach leverages the strengths of each model to improve overall accuracy.
  * **Multi-Factor Prioritization:** The Repair Priority Score (RPS) is calculated based on a comprehensive set of factors, including the precise area of damage, number of lanes, speed limits, and regional data on urbanization and population density. This ensures that maintenance decisions are not only based on damage but also on the societal impact of a road's condition.
  * **Scalable and Practical:** The framework is designed to be highly scalable, providing a practical solution for road maintenance planning that can be adopted by government agencies to optimize resource allocation and enhance public safety.
  * **Interactive Frontend:** A user-friendly interface allows maintenance officers to visualize the detected damage and interact with the prioritized repair list, enabling informed decision-making.

-----

### Getting Started

To get a local copy of this project up and running, follow these steps to recreate the Conda environment.

#### Prerequisites

  * Anaconda or Miniconda
  * Git

#### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/your-username/RAPID.git
    ```
2.  Navigate to the project directory:
    ```sh
    cd RAPID
    ```
3.  Recreate the Conda environment using the provided `environment.yml` file:
    ```sh
    conda env create -f environment.yml
    ```
4.  Activate the newly created environment:
    ```sh
    conda activate rapid
    ```

-----

### Dataset

The model in this project was trained and validated on the publicly available **"Cracks and Potholes in Road Images"** dataset. This dataset provides a collection of road images with pixel-level annotations for cracks and potholes, which is essential for training the semantic segmentation models.

Passos, Bianka T.; Cassaniga, Mateus J.; Fernandes, Anita M. R. ; Medeiros, Kátya B. ; Comunello, Eros (2020), “Cracks and Potholes in Road Images”, Mendeley Data, V4, doi:10.17632/t576ydh9v8.4

-----


### Acknowledgements

This project was developed with the support of the IT Department of Government of National Capital Territory of Delhi and would not have been possible without their continued guidance and mentorship.

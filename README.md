# Quality of AI-Generated vs. Human-Generated Code

# 1: Literature Survey

This folder contains materials and resources related to the literature review phase of the project. It includes a detailed exploration of existing research on AI-generated and human-generated code quality, identifying gaps in the literature and laying the foundation for the comparative analysis.

## Folder Components

- **Literature Survey.xlsx**: This Excel file contains a comprehensive summary of key research studies, including:
  - Title of the paper
  - Year of publication
  - Authors
  - Key findings
  - Methodologies used
  - Identified research gaps
  - Relevance to our project objectives

## Purpose

The literature survey serves as the initial phase of the project, where we systematically review previous studies to understand the current state of research on AI-generated and human-generated code quality. The results from this phase provide essential context and support for our own analysis in later stages of the project.

## Structure of the Excel File

The **Literature Survey.xlsx** is organized as follows:
- **Title**: Name of the research paper or source.
- **Year**: The year the study was published.
- **Authors**: Names of the researchers or contributors.
- **Key Findings**: A brief summary of the most relevant findings related to AI and human code quality.
- **Methodology**: Descriptions of the techniques or approaches used in the research.
- **Limitations/Gaps**: Gaps identified in the research that our project aims to address.
- **Relevance**: The relationship of each study to our project's goals, including any insights that inform our comparative analysis.

## How to Use the Literature Survey

1. **Explore Existing Research**: Use the Excel file to understand the major findings from previous studies on AI and human code quality. This can help guide your analysis and provide references for academic writing.
   
2. **Identify Gaps**: The survey identifies key gaps in current research, helping you to position your work within the broader academic and technical context.

3. **Plan Your Work**: The summarized studies offer insight into different methodologies used to analyze code quality. This can help inform the methodologies used in the later phases of this project.

## Future Updates

The **Literature Survey.xlsx** file will be updated as new research becomes available. As the project progresses, we may add new references, studies, or other literature that further informs our work.

For any questions regarding the literature survey or the Excel file, feel free to contact the project maintainers.

# 2: DataCollecting_Human

This folder contains resources and scripts related to the collection of human-generated code for our comparative analysis. It involves scraping, cleaning, and curating datasets from popular coding platforms. The data collected here forms the human code dataset that is used in later stages of the project.

## Folder Components

### 1. **human-eval-master**
This folder contains the **HumanEval** dataset, which consists of human-written code solutions for a wide range of coding problems.

- **Dataset Description**: The HumanEval dataset includes Python-based coding problems along with human-written solutions, typically used as a baseline for comparing human code against AI-generated code.
  
- **Purpose**: The dataset helps compare human-written code with AI-generated solutions, providing a baseline for analysis.

### 2. **leetcode-main**
This folder contains scripts used for scraping **LeetCode**, a popular platform for coding challenges, to gather human-generated code solutions. The main focus is to extract pre-2014 code from LeetCode to ensure it is purely human-written without AI assistance.

- **Scraping Process**: Python-based web scrapers were developed to extract human-written solutions from LeetCode archives.
- **Purpose**: These solutions provide human code data for the same types of problems being analyzed with AI-generated code.

### 3. **PythonCleaning**
The **PythonCleaning** folder contains the cleaned and finalized dataset of human-generated code that was used for analysis.

- **Source**: The dataset was obtained from a Kaggle dataset titled [Coding Problems and Solution - Python Code](https://www.kaggle.com/datasets/linkanjarad/coding-problems-and-solution-python-code).
- **Data Cleaning**: Scripts in this folder ensure that the data is clean, validated, and free of errors before being used in our comparative analysis.

### 4. **Web Scraping**
This folder contains scripts for scraping code from the **Wayback Machine** to collect pre-2014 data from coding platforms such as **Codeforces**, **HackerRank**, and **LeetCode**.

- **Scraping Scope**: The goal is to collect human-written code samples before AI-assisted coding became common, ensuring that the dataset is purely human-generated.
- **Tools**: Python scripts with libraries like BeautifulSoup and requests were used to scrape archived content from the Wayback Machine.

## Workflow

### Step 1: HumanEval Dataset
1. **Download** the HumanEval dataset from the `human-eval-master` folder.
2. **Organize** the dataset for comparison with AI-generated code.

### Step 2: LeetCode Scraping
1. **Navigate to `leetcode-main`** to find scripts that scrape human-written solutions from LeetCode.
2. **Run the scraper** to gather pre-2014 solutions from LeetCode archives.

### Step 3: Web Scraping (Wayback Machine)
1. **Navigate to `Web Scraping`** to find scripts that scrape coding platforms like Codeforces and HackerRank via the Wayback Machine.
2. **Run the scripts** to extract data from before 2014, ensuring that the dataset is composed of human-written code.

### Step 4: Data Cleaning
1. **Use the PythonCleaning folder** for scripts that clean and validate the collected data.
2. **Finalize the cleaned dataset** available on Kaggle, ensuring the code samples are free of errors and ready for analysis.

## How to Use

1. **Explore the subfolders**: Each folder has its purpose, from data scraping to cleaning. Start with the scraping scripts to gather raw data, then proceed to the cleaning process.
   
2. **Leverage the cleaned dataset** in the `PythonCleaning` folder for analysis. The final human-generated code data is available for direct comparison with AI-generated code.

## Dependencies

Make sure you have the following Python libraries installed for scraping and data processing:
- **pandas**
- **BeautifulSoup4**
- **requests**

You can install these dependencies using:
```bash
pip install pandas beautifulsoup4 requests
 
```

#  3: AI-Generated Code

This folder contains scripts and datasets related to AI-generated code, specifically solutions generated by GPT-4. The data is used for further analysis and processing in other parts of the project.

## Project Components

- **Cleaned_ProblemSolutionPythonV3.csv**: A CSV file containing cleaned AI-generated code solutions for various problems.
- **output_with_solutions_GPT4.csv**: A CSV file with raw GPT-4-generated code solutions, which may include uncleaned and preprocessed code snippets.
- **main.py**: The main Python script to process and manage AI-generated code, which can perform operations like cleaning or transforming the data for subsequent stages.

## Workflow

### Step 1: Data Processing

1. **Input**:
   - The `Cleaned_ProblemSolutionPythonV3.csv` file contains AI-generated solutions that have been cleaned.
   - The `output_with_solutions_GPT4.csv` contains the raw GPT-4 code output.

2. **Process**:
   - Before running the `main.py` script, ensure the following imports and OpenAI client initialization are included in the script:
   
   ```python
         $env:OPENAI_API_KEY="your-actual-api-key-here"
     ```
## How to Run

1. **Navigate to the folder** `3. AI-Generated Code`.
2. Ensure that the input CSV files (`Cleaned_ProblemSolutionPythonV3.csv` and `output_with_solutions_GPT4.csv`) are correctly placed in the folder.
3. Add the required imports and initialize the OpenAI client in `main.py`.
4. Run the `main.py` script to process the AI-generated code for further use.

### Dependencies

Ensure the following libraries are installed before running the scripts:

- **Python 3.x**
- **pandas**
- **openai**

You can install external dependencies using the following command:

```bash
pip install pandas openai
```
   

#  4: Matrices Generation

This folder contains scripts to generate matrices for AI (GPT-4) solutions and human solutions. The process involves separating code snippets into individual Python files and then generating feature matrices from those files. 

## Folder Structure

- **4.1 Generate GPT-4 Solution's Matrix Files**: Contains scripts to process GPT-4 generated code solutions and generate corresponding feature matrices.
- **4.2 Generate Human Solution's Matrix Files**: Contains scripts to process human-generated code solutions and generate corresponding feature matrices.

## Project Components

### Common Scripts in Both Folders (4.1 & 4.2)

- **separated-files.py**: This script extracts individual code snippets from a dataset (CSV file) and saves them as separate Python files. It is used to process both AI-generated and human-generated solutions.
- **MatrixGenration.py**: This script generates feature matrices from the Python files created by `separated-files.py`. The matrices represent various code metrics such as cyclomatic complexity, maintainability index, etc.
  
Each folder has its own dataset and output files:

### 4.1: Generate GPT-4 Solution's Matrix Files

- **Input Dataset**: Contains AI (GPT-4) generated code solutions.
- **separated-files.py**: Processes the GPT-4 code snippets from the dataset and creates separate Python files.
- **MatrixGenration.py**: Processes the separated Python files and generates a matrix with various metrics.

### 4.2: Generate Human Solution's Matrix Files

- **Input Dataset**: Contains human-generated code solutions.
- **separated-files.py**: Processes the human code snippets from the dataset and creates separate Python files.
- **MatrixGenration.py**: Processes the separated Python files and generates a matrix with various metrics.

## Workflow

### Step 1: Generate Python Files from Code Snippets

1. **Input**:
   - **4.1** uses a CSV dataset containing GPT-4 code solutions.
   - **4.2** uses a CSV dataset containing human-generated code solutions.

2. **Process**:
   - The `separated-files.py` script reads the dataset, extracts the code snippets, and writes each snippet into an individual Python file.

3. **Execution**:
   ```bash
   python separated-files.py
   ```
### Step 2: Generate Feature Matrices

#### Input:

- The individual Python files generated from the previous step.

#### Process:

- The `MatrixGenration.py` script computes various code metrics for each Python file and constructs a feature matrix for further analysis.

#### Execution:

```bash
python MatrixGenration.py
```

## How to Run

1. **Navigate to the respective folder** (`4.1 Generate GPT-4 Solution's Matrix Files` or `4.2 Generate Human Solution's Matrix Files`).
2. Run the `separated-files.py` script to generate individual Python files from the dataset.
3. Run the `MatrixGenration.py` script to generate the feature matrix.

### Dependencies

Ensure the following libraries are installed before running the scripts:

- **Python 3.x**
- **pandas**
- **os** (built-in library)
- **ast** (built-in library)

You can install external dependencies using the following command:

```bash
pip install pandas
```


# 5: Machine Learning Model

This folder contains the implementation of a machine learning model to classify code segments as either human-written or AI-generated. The model leverages various code metrics, and its performance is analyzed through several visualizations and metric evaluations.

## Project Components

This folder includes the following key components:

- **Model.ipynb**: A Jupyter Notebook that contains the full pipeline for training, evaluating, and analyzing the machine learning model. The notebook includes data loading, feature engineering, model training, and performance evaluation.
- **main-dataset.xlsx**: The dataset used to train and test the machine learning model. This Excel file includes various code metrics.
- **Images and Visualizations**: A set of visualizations generated from the model's performance and data analysis.

## Model Overview

The goal of this model is to classify whether a given code snippet is AI-generated or human-written based on the following code metrics:

- **Cyclomatic Complexity**
- **Maintainability Index**
- **Source Lines of Code (SLOC)**
- **Comments Ratio**
- **Number of Parameters**
- **Afferent and Efferent Coupling**

### Key Features

- **Supervised Learning**: The model uses supervised learning to classify code snippets.
- **Confusion Matrix**: Evaluates the performance of the model.
- **Principal Component Analysis (PCA)**: Used for dimensionality reduction and to visualize the separation between AI and human code.
- **Feature Importance**: Shows which features contribute most to classification.

## Visualizations

### Confusion Matrix
The confusion matrix shows the classification performance of the model:
![Confusion Matrix](confusion_matrix.png)

- **547** human-written code samples were correctly classified.
- **510** AI-generated code samples were correctly classified.
- The model produced **4 false positives** and **2 false negatives**.

### Correlation Heatmap
The heatmap below displays the correlation between different code metrics used in the model:
![Correlation Heatmap](correlation_heatmap.png)

### Distribution Comparison
This figure compares the distributions of key code metrics between human and AI-generated code:
![Distribution Comparison](distribution_comparison.png)

### Feature Distributions
The following boxplots show the distributions of important features between human and AI-generated code:
![Feature Distributions](feature_distributions.png)

### Feature Importance
This bar plot shows the importance of various features in the model:
![Feature Importance](feature_importance.png)

### PCA Visualization
A 2D PCA plot that visualizes the separation between human-written and AI-generated code:
![PCA Visualization](pca_visualization.png)

## How to Run

To execute the machine learning model, follow these steps:

### Install Dependencies

Ensure you have Python 3 installed. Use the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt
```
### Run the model 
```bash
jupyter notebook Model.ipynb
```

# Project Directory Structure

This repository contains all materials and scripts for the analysis of AI-generated code vs. human-generated code quality. Below is a complete directory hierarchy for the project:

```bash
Internship-Quality-of-AI-Generated-vs.-Human-Generated-Code/
│
├── DataCollecting_Human/
│   ├── human-eval-master/
│   │   └── # Contains the HumanEval dataset (human-written Python code)
│   ├── leetcode-main/
│   │   └── # Scripts for scraping LeetCode (pre-2014 data)
│   ├── PythonCleaning/
│   │   └── # Cleaned dataset from Kaggle ("Coding Problems and Solutions - Python Code")
│   └── Web Scraping/
│       └── # Scripts to scrape code from Wayback Machine for platforms like Codeforces and HackerRank
│
├── LiteratureSurvey/
│   ├── Literature Survey.xlsx
│   └── # Contains materials related to the literature review phase, including research papers and findings
│
├── AI-Generated Code/
│   ├── Cleaned_ProblemSolutionPythonV3.csv
│   ├── output_with_solutions_GPT4.csv
│   └── main.py
│       └── # Script for processing AI-generated code (cleaning and transformations)
│
├── Matrices Generation/
│   ├── 4.1 Generate GPT-4 Solution's Matrix Files/
│   │   ├── separated-files.py
│   │   ├── MatrixGeneration.py
│   │   └── # Processes AI-generated solutions into feature matrices
│   └── 4.2 Generate Human Solution's Matrix Files/
│       ├── separated-files.py
│       ├── MatrixGeneration.py
│       └── # Processes human-generated solutions into feature matrices
│
├── Machine Learning Model/
│   ├── Model.ipynb
│   ├── main-dataset.xlsx
│   └── Images and Visualizations/
│       └── # Contains images generated from model evaluations
│
├── README.md
└── LICENSE
```

## License:
This project is licensed under the MIT License. See the LICENSE file for more information.

---
Please don't hesitate to reach out if you require any further assistance.

- s-tasneem.attia@zewailcity.edu.eg
- s-rghda.ahmed@zewailcity.edu.eg
- s-nada.soudi@zewailcity.edu.eg
- s-nourhan.mahgoub@zewailcity.edu.eg
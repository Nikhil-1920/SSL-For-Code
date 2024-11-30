# SSL-For-Code: Learning a Code Language Model for Code

This project demonstrates how deep learning can be used to autocomplete Python code, providing a productivity boost by saving keystrokes during coding. The project uses **LSTM** and **Transformer** models to predict Python code completions and integrates with a **VSCode extension** for easy interaction.

## Key Features
- Train deep learning models for Python code autocompletion.
- Use a character-level model for simplicity and effectiveness.
- Save up to **50%** in keystrokes for Python developers.
- **VSCode Extension**: Integrate the trained model to get autocompletion suggestions directly in VSCode.
- Model training and evaluation are made simple with easy-to-use Python scripts.

## How to Start Working with SSL-For-Code

### 1. Clone the Repository & Navigate

Clone the repository to your local machine:

```bash
git clone https://github.com/Nikhil-1920/SSL-For-Code.git
cd SSL-For-Code/final-submit/python_autocomplete/
```

### 2. Install Requirements

Install necessary requirements:

```bash
pip install -r requirements.txt
```

### 3. Create the Dataset

The dataset used to train the model consists of Python code from various repositories listed in the Awesome-pytorch-list. To prepare the dataset, run the following script:

```bash
python3 python_autocomplete/create_dataset.py
```

### 4. Train the Model

Once the dataset is prepared, you can train the model. The training script is available in the python_autocomplete directory:

```bash
python3 train.py
```

### 5. Use the VSCode Extension for Code Autocompletion

To use the trained model within VSCode, follow these steps:

Install Node.js: Make sure you have Node.js installed on your system to run the extension.

Install npm dependencies:

```bash
cd frontend
npm install
```

### 6. Start the Python Server:

The VSCode extension communicates with a Python server. Start the server with:

```bash
python3 python_autocomplete/server.py
```

### 7. Open the VSCode Extension:

Open the frontend/ folder in VSCode:

```bash
cd frontend/
code .
```

### 8. Run the Extension:

In VSCode, go to Run > Start Debugging. This will launch the extension in a new VSCode window.


### 9. Start Coding:

Open or create a Python file in VSCode. As you type, the extension will suggest code completions based on the trained model.


### 10. Experiment with Hyperparameters

Feel free to experiment with the model architecture and hyperparameters:

Modify the number of layers or dimensions of the LSTM/Transformer model in the training script (train.py). Explore the impact of different hyperparameters like learning rate, batch size, and training epochs.

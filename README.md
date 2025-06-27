# Project: Cleaning Bank Marketing Campaign Data 💰

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

This is a simple data cleaning project that I completed on DataCamp and decided to host on GitHub.

It is a bonus coursework module for the **[Data Engineer in Python](https://app.datacamp.com/learn/career-tracks/data-engineer-in-python)** career track. I saw it as an opportunity to practice some fundamentals with `pandas`, as well as practice for hosting projects on GitHub and writing articles for LinkedIn.

### Project structure

```
└── 📁cleaning-bank-marketing-campaign-data
    └── 📁assets
    └── 📁code
        └── 📁assets
            ├── piggy_bank.jpg
        └── 📁utilities
            ├── __init__.py
            └── config.py
        ├── notebook.ipynb
    └── 📁data
        ├── bank_marketing.csv
        ├── campaign.csv
        ├── client.csv
        ├── economic.csv
        └── economics.csv
    ├── .gitignore
    ├── README.md
    └── requirements.txt
```

## Getting Started <a name = "getting_started"></a>

These instructions will get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.11.5.
- pandas 2.3.0
- Jupyter Notebooks (IPython)

The `requirements.txt` file has many more packages listed but these are for my data project development environment and some of them may not be explicitly necessary here.

If you want to replicate my work, you only need the listed items. I do my programming in Visual Studio Code (VS Code), so if you want to follow along in my environment, continue reading. Otherwise, you can skip to [Usage](#usage) or take a look at the [notebook](code/notebook.ipynb).

### On your computer

1. Download VS Code and install it. You can get help with that [at their website](https://code.visualstudio.com/download).
2. Download and install Python. I recommend [version 3.11](https://www.python.org/downloads/release/python-3119/), at least.
3. Download the files from this repository and place them somewhere you have appropriate permissions to access.
4. Start up VS Code.

### In VS Code

#### Install extensions

Go to the "Extensions" tab and install the following:
- the official Python extension
- the Jupyter extension

#### Create a virtual environment (optional but recommended)

##### Method 1 (command palette)

1. Type "interpreter" into the "command palette" (`Ctrl+Shift+P` on Windows) to select "Python: Select Interpreter"

    > If you do not see an interpreter matching the version of Python you are using, browse to it using the "Enter interpreter path..." option.

2. Select "Create Virtual Enviroment".
3. Select "Venv"

    > This uses Python's `venv` package to create a virtual environment.

##### Method 2 (terminal)

1. Open a terminal. The easiest way to do this is to open the lower panel and navigate to the "Terminal" tab, if the application does not do it for you.

    > You should see a prompt that contains the name of the folder you are currently working in.

2. Type the following: `python -m venv .venv`. Press "enter".

    > This calls the Python package `venv` as a module and runs it to create a virtual environment in your current working directory; the files for this environment are in a directory called `.venv`.

#### Install `pandas`

1. Open a terminal, if you have not already. *See the first step of [this section](#method-2-terminal) for instructions, if necessary.*
2. Type `pip install pandas`. Press "enter".

   > `pip` will install all the dependencies that are needed for `pandas`.

#### Finishing

If you set up a virtual environment using [the first method](#method-1-command-palette), you can stop here. Otherwise, read on.

##### Set up interpreter and kernel

1. Type "interpreter" into the "command palette" (`Ctrl+Shift+P` on Windows) to select your interpreter.

    > If you do not see an interpreter matching the version of Python you are using, browse to it using the "Enter interpreter path..." option.

2. If VS Code does not automatically select a kernel for you--as indicated by a button near the upper right corner of the application window--you can either press that button or use the command palette to select a kernel using the option "Notebook: Select Notebook Kernel".

    > This step must be performed with the window focused on the Jupyter notebook file (`notebook.ipynb`).

## Usage <a name = "usage"></a>

If you made it through the wilderness of [Getting Started](#getting-started), you can now edit the notebook and run it using VS Code.

As it is right now, the code in the notebook performs some (very simple) data manipulations, and saves the cleaned data into some files.

I plan to add some analysis, later. For now, you can add you own, provided you downloaded this repo and placed it in a development environment.

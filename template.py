import os
from pathlib import Path

list_of_files=[
    ".github/mlop_project1/.gitkeep",           # For github workflows
    "src/__init__.py",                         # Python package initialization
    "src/components/__init__.py",              # Component package initialization
    "src/components/data_ingestion.py",         
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",                 # Pipeline package initialization
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",                     # Utility package initialization
    "src/utils/utils.py",                       # Utility functions
    "src/logger/logging.py",                    # Logging functionality
    "src/exception/exception",                  # Exception handling
    "tests/unit/__init__.py",                   # Unit tests initialization
    "tests/integration/__init__.py",            # Intigration tests intialization
    "init_setup.sh",                            # Shell script for intial setup
    "requirements.txt",                         # Production requirements
    "requirements_dev.txt",                     # Development requirements
    "setup.py",                                 # Package setup file
    "setup.cfg",                                # Setup configuration file
    "pyproject.toml",                           # Project configuration (e.g. Poetry, Flit)
    "tox.ini",                                  # Tox configuration for testing
    "experiment/experiments.ipynb"              # Jupyter Notebook for experiments
]

for filepath in list_of_files:
    filepath = Path(filepath)   # Convert string path to a Path object for OS compatibility
    filedir, filename = os.path.split(filepath)     # Separate directory and file name
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)    # Create directory if it doesn't exist

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:      
            pass # create an empty file
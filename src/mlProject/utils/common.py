# Importing necessary libraries and modules
import os  # For file and directory operations
from box.exceptions import BoxValueError  # To handle specific exceptions from the Box library
import yaml  # For reading and writing YAML files
from mlProject import logger  # Custom logger for logging messages
import json  # For reading and writing JSON files
import joblib  # For saving and loading binary files
from ensure import ensure_annotations  # For ensuring type annotations
from box import ConfigBox  # A utility to work with dict-like objects
from pathlib import Path  # For working with file paths
from typing import Any  # For type hints with flexible types

# Function to read a YAML file and return its content as a ConfigBox
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content wrapped in a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For other unexpected errors.

    Returns:
        ConfigBox: Parsed YAML content as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # Load the YAML content
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)  # Return as ConfigBox for enhanced usability
    except BoxValueError:
        raise ValueError("YAML file is empty")  # Handle empty YAML file
    except Exception as e:
        raise e  # Re-raise unexpected exceptions

# Function to create a list of directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories from a list of paths.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): If True, log the creation of each directory. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Create directories, ignore if they already exist
        if verbose:
            logger.info(f"Created directory at: {path}")

# Function to save data as a JSON file
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves data as a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in JSON format.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)  # Write JSON data with indentation
    logger.info(f"JSON file saved at: {path}")

# Function to load data from a JSON file
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as a ConfigBox object for attribute-like access.
    """
    with open(path) as f:
        content = json.load(f)  # Load JSON content
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)  # Return as ConfigBox for usability

# Function to save data in binary format
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data to a binary file.

    Args:
        data (Any): Data to be saved in binary format.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)  # Save data in binary format
    logger.info(f"Binary file saved at: {path}")

# Function to load data from a binary file
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: The data object stored in the binary file.
    """
    data = joblib.load(path)  # Load binary data
    logger.info(f"Binary file loaded from: {path}")
    return data

# Function to get the size of a file in kilobytes
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of a file in kilobytes.

    Args:
        path (Path): Path of the file.

    Returns:
        str: File size in kilobytes as a string.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Calculate size in KB
    return f"~ {size_in_kb} KB"

import os  # Provides functions to interact with the operating system.
import sys  # Provides access to system-specific parameters and functions.
import logging  # Provides a flexible framework for emitting log messages.

# Define the format for logging messages
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Directory to store log files
log_dir = "logs"

# Complete file path for the log file
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't already exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO (logs INFO and above).
    format=logging_str,  # Use the custom logging format defined above.
    handlers=[
        logging.FileHandler(log_filepath),  # Log messages to the specified file.
        logging.StreamHandler(sys.stdout)  # Also log messages to the console.
    ]
)

# Create a logger instance with a custom name
logger = logging.getLogger("mlProjectLogger")

# Example usage:
# logger.info("This is an INFO log message.")
# logger.error("This is an ERROR log message.")

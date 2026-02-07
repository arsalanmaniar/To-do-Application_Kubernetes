import logging
import sys
from datetime import datetime
from typing import Optional, Any, Dict


def setup_logging(log_level: Optional[str] = "INFO"):
    """
    Setup logging configuration for the application
    """
    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Create handler for stdout
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Create file handler
    file_handler = logging.FileHandler('app.log', mode='a')
    file_handler.setFormatter(formatter)

    # Get the root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, log_level.upper()))

    # Add handlers if they don't already exist
    if not root_logger.handlers:
        root_logger.addHandler(console_handler)
        root_logger.addHandler(file_handler)

    # Get the logger for this application
    logger = logging.getLogger(__name__)
    return logger


def log_api_call(endpoint: str, method: str, user_id: str = None, status_code: int = None):
    """
    Log an API call with relevant information
    """
    user_info = f"User: {user_id}" if user_id else "Anonymous User"
    status_info = f"Status: {status_code}" if status_code else "Status: Pending"

    logger = setup_logging()
    logger.info(f"API Call - {method} {endpoint} | {user_info} | {status_info}")


def log_error(error: Exception, context: str = ""):
    """
    Log an error with context information
    """
    logger = setup_logging()
    logger.error(f"Error in {context}: {str(error)}", exc_info=True)


def log_service_operation(service_name: str, operation: str, user_id: str = None, success: bool = True):
    """
    Log a service operation
    """
    user_info = f"User: {user_id}" if user_id else "Unknown User"
    status = "SUCCESS" if success else "FAILED"

    logger = setup_logging()
    logger.info(f"Service Operation - {service_name}.{operation} | {user_info} | {status}")


def log_database_operation(operation: str, table: str, record_id: str = None, success: bool = True):
    """
    Log a database operation
    """
    record_info = f"Record: {record_id}" if record_id else "New Record"
    status = "SUCCESS" if success else "FAILED"

    logger = setup_logging()
    logger.info(f"DB Operation - {operation} on {table} | {record_info} | {status}")


# Create a default logger instance
logger = setup_logging()
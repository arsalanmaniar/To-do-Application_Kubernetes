"""
Debug server with detailed error logging
"""
import sys
import os

# Add the project root to Python path so 'backend' package can be found
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)  # This is the project root
sys.path.insert(0, parent_dir)

import logging
import traceback
from fastapi import Request
from fastapi.logger import logger as fastapi_logger

# Set up detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import and create the app
from app.main import create_app
app = create_app()

# Add middleware to log errors in detail
@app.middleware("http")
async def log_errors(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logger.error(f"Error processing request {request.method} {request.url}")
        logger.error(f"Headers: {request.headers}")
        logger.error(f"Exception: {e}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        raise

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False, log_level="debug")
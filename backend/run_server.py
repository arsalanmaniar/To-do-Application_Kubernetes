import sys
import os

# Add the project root to Python path so 'backend' package can be found
# Get the directory containing this file (backend directory), then go up one level to project root
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Change to the backend directory so uvicorn can find the modules
os.chdir(current_dir)

# Now run the uvicorn server
import uvicorn

if __name__ == "__main__":
    print("Starting server...")
    # Run with string import to support reload
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
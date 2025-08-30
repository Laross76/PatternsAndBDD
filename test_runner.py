import subprocess
import time
from pages.note_page import NotePage


def start_server():
    """Start the FastAPI server"""
    return subprocess.Popen(["uvicorn", "main:app", "--reload"])


def run_tests():
    """Run behave tests"""
    return subprocess.run(["behave"], check=True)


if __name__ == "__main__":
    # Start server
    server_process = start_server()
    time.sleep(3)  # Wait for server to start

    try:
        # Run tests
        run_tests()
    finally:
        # Stop server
        server_process.terminate()

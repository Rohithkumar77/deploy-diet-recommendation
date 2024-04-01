import subprocess

def run_streamlit(file_path):
    command = ["streamlit", "run", file_path]
    subprocess.Popen(command)

def run_backend():
    # Replace 'backend/main.py' with the actual path to your backend script
    backend_command = ["python", "backend/main.py"]
    subprocess.Popen(backend_command)

def main():
    # Run frontend/Home.py using Streamlit
    run_streamlit("frontend/Home.py")

    # Run backend/main.py as a separate process
    run_backend()

if __name__ == "__main__":
    main()

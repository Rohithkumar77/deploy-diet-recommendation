import streamlit as st
import subprocess
import frontend.Home as home

def run_streamlit(file_path):
    command = ["streamlit", "run", file_path]
    subprocess.Popen(command)

def main():
    # Run main.py from the backend folder in a separate Streamlit process
    run_streamlit("backend/main.py")

    # Run home.py from the frontend folder in the current Streamlit process
    import frontend.Home as home

    home.main()

if __name__ == "__main__":
    main()

import subprocess

def run_docker_compose():
    command = ["docker-compose", "up", "-d", "--build"]
    subprocess.run(command)

# Call the function to run the command
run_docker_compose()

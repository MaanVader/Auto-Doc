import subprocess
import os

# Function to read the file and get Dockerfile, container name, and port
def read_paths(file_path):
    paths = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:  # Ensure the line has exactly three elements
                paths.append(parts)
            else:
                print(f"Skipping invalid line: {line.strip()}")
    return paths


# Function to build Docker images
def build_image(dockerfile_path, tag):
    dockerfile_dir = os.path.dirname(dockerfile_path)
    try:
        subprocess.run(["docker", "build", "-t", tag, dockerfile_dir], check=True)
        print(f"Successfully built image for {tag}")
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to build image for {tag}")
        return False

# Function to run Docker container with port mapping
def run_container(image_tag, port_mapping):
    try:
        subprocess.run(["docker", "run", "-d", "-p", port_mapping, "--name", image_tag, image_tag], check=True)
        print(f"Successfully running container {image_tag}")
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to run container {image_tag}")
        return False

def main(file_path):
    paths = read_paths(file_path)

    # First, build all the images
    for dockerfile_path, image_tag, _ in paths:
        if not build_image(dockerfile_path, image_tag):
            print(f"Skipping running container {image_tag} due to build failure.")

    # Then, run all the containers
    for _, image_tag, port_mapping in paths:
        run_container(image_tag, port_mapping)

if __name__ == "__main__":
    file_path = "./docker.txt"  # Replace with your text file path
    main(file_path)


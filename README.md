
---

# Auto-Doc 🚀

## Description
Auto-Doc is an innovative tool designed to streamline the process of managing and deploying multiple Docker containers 🐳. It's perfect for running multiple CTF challenges at one go.

## Installation 🛠️
1. Ensure Docker is installed on your system. You can download it from [Docker's official website](https://www.docker.com/get-started).
2. Clone the Auto-Doc repository:
   ```
   git clone https://github.com/MaanVader/Auto-Doc
   ```
3. Navigate to the Auto-Doc directory:
   ```
   cd auto-doc
   ```

## Setting Up Docker 🐳
1. Prepare your Docker environment as per the instructions in 'docker.txt'.
2. The 'docker.txt' file should contain paths to Dockerfiles, container names, and port mappings. For example:
   ```
   /path/to/Dockerfile,container_name,port_mapping
   ```

## Usage 🌟
1. Run the 'upload.py' script to initiate the setup:
   ```
   python upload.py
   ```
2. This script will read 'docker.txt', build Docker images, and spin up containers based on the configurations provided.

---

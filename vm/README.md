VM Walkthrough (VirtualBox)

Goal: Run the project in a small Ubuntu VM to show an isolated environment.

Steps (high-level):
1) Install VirtualBox and the Extension Pack.
2) Create an Ubuntu VM (2 vCPU, 4 GB RAM, 20+ GB disk).
3) Install Ubuntu inside the VM.
4) Inside the VM, install Docker and Nomad.
5) Clone this repo and run the same steps as in the main README.

Inside the VM (example commands):
  sudo apt update
  sudo apt install -y git curl gnupg software-properties-common

  # Docker
  curl -fsSL https://get.docker.com | sudo sh
  sudo usermod -aG docker $USER
  newgrp docker

  # Nomad (HashiCorp repo)
  curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
  echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
  sudo apt update
  sudo apt install -y nomad

  # Clone and run
  git clone https://github.com/aalok-akarsh/devops-intern-final.git
  cd devops-intern-final
  python3 hello.py
  docker build -t hello-devops:latest .
  docker run --rm hello-devops:latest
  nomad agent -dev

Notes:
- If you want Loki/Grafana in the VM, follow `monitoring/loki_setup.txt`.

# DevOps Intern Final Project

Name: Alok Pandey
Date: March 2026

This project is a simple DevOps workflow using GitHub, Linux scripting, Docker, CI/CD, Nomad, and monitoring.

## Project Steps

### 1. Git & GitHub Setup
- Repo initialized with README and `hello.py`.
- `hello.py` prints "Hello, DevOps!".

### 2. Linux & Scripting Basics
Script: `scripts/sysinfo.sh`

Run:
```bash
chmod +x scripts/sysinfo.sh
./scripts/sysinfo.sh
```

### 3. Docker Basics
Dockerfile: `Dockerfile`

Build and run:
```bash
docker build -t hello-devops:latest .
docker run --rm hello-devops:latest
```

### 4. CI/CD with GitHub Actions
Workflow: `.github/workflows/ci.yml`

On every push, GitHub Actions runs `python hello.py`.

Status badge:
![CI](https://github.com/aalok-akarsh/devops-intern-final/actions/workflows/ci.yml/badge.svg)

### 5. Job Deployment with Nomad
Nomad job file: `nomad/hello.nomad`

Run:
```bash
nomad job run nomad/hello.nomad
```

### 6. Monitoring with Grafana Loki
Setup notes: `monitoring/loki_setup.txt`

Example commands:
```bash
docker run -d --name loki -p 3100:3100 grafana/loki:2.9.8 -config.file=/etc/loki/local-config.yaml
curl "http://localhost:3100/loki/api/v1/query?query={job=\"hello\"}"
```
Log forwarding (simple option):
- Use the Docker Loki logging driver for container logs (see `monitoring/loki_setup.txt`).

## Run Notes
- Tested locally in WSL (Ubuntu) on March 24, 2026: Python, the script, Docker build/run, Nomad job, and Loki/Grafana.
- Used a local registry (`localhost:5000`) for Nomad to avoid Docker Hub.
- Loki test push/query worked locally (test log `hello-from-loki-test`).

## Files Included
- `hello.py`
- `scripts/sysinfo.sh`
- `Dockerfile`
- `.github/workflows/ci.yml`
- `nomad/hello.nomad`
- `monitoring/loki_setup.txt`

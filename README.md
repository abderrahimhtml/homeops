![Deploy](https://github.com/abderrahimhtml/homeops/actions/workflows/deploy.yml/badge.svg)

# HomeOps - Self-Hosted Server Infrastructure

Personal homelab infrastructure project demonstrating real-world sysadmin and DevOps skills.
Provisioned with Ansible, containerized with Docker, served via Nginx, and deployed automatically with GitHub Actions CI/CD.

## Stack

| Layer | Technology |
|---|---|
| Virtualization | Hyper-V (Windows 11) |
| OS | Ubuntu Server 24.04 LTS |
| Provisioning | Ansible |
| Containerization | Docker + Docker Compose |
| Reverse Proxy | Nginx + self-signed SSL |
| API | FastAPI (Python) |
| CI/CD | GitHub Actions (self-hosted runner) |
| Firewall | UFW |

## How it works

1. Ansible provisions the server automatically - installs Docker, Nginx, configures UFW firewall
2. Docker Compose runs the FastAPI app as a container with restart always
3. Nginx acts as a reverse proxy, terminating SSL and forwarding traffic to the container
4. GitHub Actions triggers on every push to main, rebuilds and restarts the container, and verifies the /health endpoint

## API Endpoints

| Endpoint | Description |
|---|---|
| GET / | Server status, hostname and timestamp |
| GET /health | Health check for CI/CD verification |
| GET /docs | Auto-generated Swagger UI |

## Skills demonstrated

- Linux server administration (Ubuntu Server 24.04)
- Infrastructure as Code with Ansible
- Docker containerization and Docker Compose
- Nginx reverse proxy configuration with SSL
- CI/CD pipeline design with GitHub Actions
- Network security with UFW firewall rules
- Self-hosted runner setup and management

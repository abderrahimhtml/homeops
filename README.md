# HomeOps - Self-Hosted Server Infrastructure

![Deploy](https://github.com/abderrahimhtml/homeops/actions/workflows/deploy.yml/badge.svg)

Personal homelab infrastructure project demonstrating real-world sysadmin and DevOps skills.
Provisioned with Ansible, containerized with Docker, served via Nginx with SSL, and deployed automatically with GitHub Actions CI/CD.

---

## Architecture
Windows 11 (Hyper-V)
└── Ubuntu Server 24.04 VM
├── Nginx (reverse proxy, SSL :443)
│   └── FastAPI container (:8000)
│       └── PostgreSQL container (:5432)
└── GitHub Actions self-hosted runner

---

## Stack

| Layer | Technology |
|---|---|
| Virtualization | Hyper-V (Windows 11) |
| OS | Ubuntu Server 24.04 LTS |
| Provisioning | Ansible |
| Containerization | Docker + Docker Compose |
| Reverse Proxy | Nginx + self-signed SSL |
| API | FastAPI (Python) |
| Database | PostgreSQL 16 |
| CI/CD | GitHub Actions (self-hosted runner) |
| Firewall | UFW |

---

## API Endpoints

| Endpoint | Description |
|---|---|
| GET / | Server status, hostname and timestamp |
| GET /health | Health check for CI/CD pipeline |
| GET /metrics | Live CPU, RAM, disk and uptime stats |
| GET /docs | Auto-generated Swagger UI |

---

## How it works

1. Ansible provisions the server from scratch - installs Docker, Nginx, configures UFW firewall rules
2. Docker Compose orchestrates two services: FastAPI app and PostgreSQL database
3. Nginx acts as reverse proxy with SSL termination, forwarding traffic to the API container
4. Every git push to main triggers the GitHub Actions pipeline which rebuilds and redeploys automatically
5. The self-hosted runner runs inside the VM itself, no external infrastructure needed

---

## Quick Start
```bash
git clone https://github.com/abderrahimhtml/homeops.git
cp inventory_example.ini inventory/hosts.ini
# Edit hosts.ini with your server IP and SSH key path
ansible-playbook -i inventory/hosts.ini playbook.yml
cd app && docker compose up -d --build
curl -k https://YOUR_SERVER_IP/health
```

---

## Skills demonstrated

- Linux server administration (Ubuntu Server 24.04)
- Infrastructure as Code with Ansible playbooks and roles
- Docker containerization and multi-service Docker Compose orchestration
- Nginx reverse proxy configuration with SSL
- CI/CD pipeline design with GitHub Actions and self-hosted runners
- Network security with UFW firewall rules
- REST API development with FastAPI and system metrics collection
- PostgreSQL database integration

# Python Playground 🐍

A repository to learn Python by building real-world applications, following the **Udemy course: "Python Mega Course: Build 20 Real-World Apps and AI Agents"**.

## 🎯 Goals

- Practice Python syntax and fundamentals
- Build 20 real-world apps as part of the Udemy course
- Use GitHub Copilot and AI agents to assist development
- Containerize apps with **Docker** and orchestrate with **Kubernetes**

## 📁 Project Structure

```
python-playground/
├── apps/                  # Course apps (one folder per app)
│   ├── 01-weather-app/
│   ├── 02-todo-app/
│   └── ...
├── basics/                # Python syntax and fundamentals practice
│   ├── variables.py
│   ├── control_flow.py
│   ├── functions.py
│   ├── oop.py
│   └── ...
├── k8s/                   # Kubernetes manifests
│   ├── deployment.yaml
│   └── service.yaml
├── Dockerfile             # Docker image for running Python apps
├── docker-compose.yml     # Docker Compose for multi-container setup
├── requirements.txt       # Python dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- kubectl (for Kubernetes deployments)

### Run locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run a specific app
python apps/01-weather-app/app.py
```

### Run with Docker

```bash
# Build the image
docker build -t python-playground .

# Run a container
docker run --rm python-playground

# Or use Docker Compose
docker-compose up
```

### Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

## 📚 Course Apps Progress

| # | App | Status |
|---|-----|--------|
| 01 | Weather App | 🚧 In Progress |
| 02 | Todo App | ⬜ Planned |
| 03 | Portfolio Website | ⬜ Planned |
| 04 | Web Scraper | ⬜ Planned |
| 05 | Data Analysis Dashboard | ⬜ Planned |
| 06 | Database App | ⬜ Planned |
| 07 | PDF Generator | ⬜ Planned |
| 08 | Webcam App | ⬜ Planned |
| 09 | News Aggregator | ⬜ Planned |
| 10 | Email Sender | ⬜ Planned |
| 11 | Chat App | ⬜ Planned |
| 12 | Face Detection App | ⬜ Planned |
| 13 | Map App | ⬜ Planned |
| 14 | File Organizer | ⬜ Planned |
| 15 | Vocabulary App | ⬜ Planned |
| 16 | Web App with Flask | ⬜ Planned |
| 17 | REST API | ⬜ Planned |
| 18 | AI Agent | ⬜ Planned |
| 19 | Image Processor | ⬜ Planned |
| 20 | Student Management System | ⬜ Planned |

## 🐳 Docker & Kubernetes

This repo uses Docker and Kubernetes to containerize and deploy the applications.  
See the `Dockerfile`, `docker-compose.yml`, and `k8s/` directory for details.

## 🤖 AI-Assisted Development

GitHub Copilot and AI agents are used throughout this project to accelerate development and explore best practices.

## 📝 License

MIT

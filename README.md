# 🚀 CI/CD Pipeline with GitHub Actions, Docker & Kubernetes (Minikube)

This project demonstrates a **complete CI/CD workflow** for a simple Python web application using:
- **GitHub Actions** for CI/CD automation  
- **Docker** for containerization  
- **Kubernetes (Minikube)** for deployment and local testing  

---

## 📁 Project Structure

CICD/
│
├── app.py # Simple Python Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Defines Docker image
├── deployment.yaml # Kubernetes Deployment manifest
├── service.yaml # Kubernetes Service manifest
└── .github/
└── workflows/
└── docker-build.yml # GitHub Actions pipeline

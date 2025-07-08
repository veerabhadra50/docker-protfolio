# 🚀 Veera's Docker Portfolio

A simple, lightweight Flask-based portfolio website, containerized using Docker.  
Perfect for deploying your personal site anywhere with a single `docker run` command.

---

## 🌐 Demo

> You can run it locally or deploy to any server (EC2, VPS, etc.)

```bash
docker pull veerabhadra50/docker-portfolio
docker run -d -p 5000:5000 veerabhadra50/docker-portfolio

🛠 Tech Stack
Python 3.11

Flask 3.1

HTML + CSS

Docker (Slim Image)


📁 Project Structure

docker-portfolio/
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css

 📦 Build Your Own Image 
 # Build image
docker build -t veerabhadra50/docker-portfolio .

# Push to Docker Hub
docker push veerabhadra50/docker-portfolio
  

👨‍💻 Author
VeerabhadraSwamy
🔗 GitHub
🐳 Docker Hub  



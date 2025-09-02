# Docker-Projects

This repository contains two Docker-based projects.

## 🚀 Project 1 – SSH Connection Between Two Ubuntu Containers
This project demonstrates setting up an SSH connection between two Ubuntu containers using Docker.
[https://github.com/Sathvikmm18/Docker-Projects/blob/main/p1.png](https://github.com/Sathvikmm18/Docker-Projects/blob/84ed045cf7c8d7703b5a709de6e437be6e0da088/p1.png)

- The **first container** is configured as an **OpenSSH Server**.
- The **second container** is configured as an **OpenSSH Client**.
- Together, they enable secure SSH communication between containers, which is useful for testing container networking and security setups.
  

## 🌐 Project 2 – Dockerized Apache Web Server
This project demonstrates how to containerize and run an Apache web server using Docker.

### Steps to Run:
1. Open VS Code (or your terminal) inside the `project2/` directory.
2. Build the Docker image:
   ```bash
   docker build -t my-apache-image .
   docker run -p 80:80 my-apache-image
 Now ,run localhost in browser   


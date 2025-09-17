# FoodTech Scraper

A **full-stack** project to showcase skills in **Python, Flask, MySQL, Docker, and React**.  
The system extracts public data using a **web scraper** and displays it on a web interface.  

This project is designed for internships/portfolio and includes:
- **Python Scraper** to collect data.
- **Flask REST API** to expose the data.
- **MySQL Database** running in a Docker container.
- **React Frontend** to visualize the data in a table..

---

## 🚀 Project Structure
```
foodtech_scraper
├── backend # Flask API with basic CRUD
├── frontend # React app to display data
├── scraper # Web scraper with Python
├── docker # Docker configuration for MySQL
└── README.md # This file
```

---

## 🛠 Technologies

- **Python 3** (Scraper + Flask API)
- **MySQL** (Database)
- **Docker** (MySQL and easy deployment)
- **React** (Frontend)
- **Git** for version control

---

## ⚙️ Setup and Execution

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SofiaGracia/foodtech_scraper.git
cd foodtech_scraper
```

### 2️⃣ Start MySQL with Docker
```bash
cd docker
docker-compose up -d
```
This will create a foodtech database at 127.0.0.1:3307.
User: fooduser.
Password: password123

### 3️⃣ Backend (Flask)
```bash
cd backend
python3 -m venv env
source env/bin/activate  # Linux/Mac
# .\env\Scripts\activate  # Windows

pip install -r requirements.txt
python app.py
```
The backend will run at http://127.0.0.1:5000.

### 4️⃣ Frontend (React)
```bash
cd frontend
npm install
npm start
```
The frontend will run at http://localhost:3000.

### 📊 Available Routes (Backend)
| Method | Route   | Description               |
|--------|---------|----------------------------|
| GET    | `/`     | Connection test            |
| GET    | `/data` | Returns data from scraper   |
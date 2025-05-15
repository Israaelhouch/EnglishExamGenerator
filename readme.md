# 📝 English Exam Generator

This project is a backend application for generating exams using Python. It includes route handling, utilities for formatting and modifying outputs, and is built with FastAPI.

---

## 📁 Project Structure

```
EXAM_GENERATOR/
├── backend/                # Contains data and DB-related files
│   ├── data/               # Raw or intermediate data
├── src/routes/            # Route logic for the FastAPI app
│   ├── db_store/          # DB files
│   ├── exam_generator.py  # Main logic for generating exams
│   ├── modify_outputs.py  # Functions to clean/modify comprehension output
│   ├── templates.py       # Template handling for exams
│   └── utils.py           # Helper functions
├── env/                   # Virtual environment directory
├── main.py                # Entry point for the FastAPI app
├── test.py                # Testing script 
├── Makefile               # Commands to build, run, and clean
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables file
└── .gitignore             # Git ignored files list
```

---

## 🧪 Requirements

- Python 3.8 or higher
- `make` installed on your machine

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <https://github.com/Israaelhouch/EnglishExamGenerator.git>
cd EXAM_GENERATOR
```

### 2. Create a Virtual Environment and Install Dependencies

```bash
make install
```

This will:
- Create a Python virtual environment in the `env/` folder
- Install all dependencies from `backend/requirements.txt`

---

## ▶️ Running the App

To start the FastAPI server:

```bash
make run
```

Then open your browser and go to:

```
http://0.0.0.0:8080
```

It will reload automatically when you edit Python files.

---

## 🧼 Cleaning the Environment

To remove the virtual environment:

```bash
make clean
```

---

## 📦 Environment Variables

Set up your environment variables in a `.env` file located at the root directory. Example:

```
SECRET_KEY=your-secret-key
DATABASE_URL=your-db-url
```

---

## 🧪 Running Tests

You can run the test script using:

```bash
python test.py
```

Or you can later extend it using `pytest` or similar tools.

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **Uvicorn**
- **Make**



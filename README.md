# 🎙️ Lany – IoT Voice Assistant with Task Management

Lany adalah IoT Voice Assistant berbasis **ESP32 + FastAPI + PostgreSQL + Groq AI** yang mampu melakukan percakapan natural sekaligus mengelola To-Do List melalui perintah suara. Sistem ini mengintegrasikan IoT device, backend API, AI service, dan cloud database dalam satu arsitektur terpadu.

---

# 🏗️ Arsitektur Sistem

```
ESP32
   ↓
FastAPI Backend (Railway)
   ↓
Groq API (STT + LLM + TTS)
   ↓
PostgreSQL (Task Storage)
```

---

# 🚀 Fitur Utama

## 🎧 Conversational AI
- Speech-to-Text (Whisper)
- LLM-based natural response
- Text-to-Speech output
- Session-based conversation memory

## 📝 Task Management via Voice
- Add Task
- View Task
- Complete/Delete Task
- Persistent storage (PostgreSQL)

---

# 🎯 Keyword Voice Commands

Berikut keyword yang digunakan sistem:

---

## ➕ Add Task

**Trigger:**
```
add task
```

**Flow:**
```
User: Lany, add task
System: Okay. What task do you want to add?
User: Finish backend
System: Task added successfully.
```

---

## 📋 View Tasks

**Trigger:**
```
view task
```
atau
```
list task
```

**Flow:**
```
User: view task
System: You have 2 tasks.
1. Finish backend.
2. Buy components.
```

---

## ✅ Complete / Delete Task

**Trigger:**
```
complete task <number>
```

**Contoh:**
```
User: complete task 2
System: Task deleted successfully.
```

**Catatan:**
- Nomor berdasarkan urutan saat "view task"
- Task akan dihapus dari database

---

# 🗄️ Database Schema (PostgreSQL)

Table: `tasks`

| Column       | Type      | Description |
|-------------|-----------|-------------|
| id          | UUID      | Primary key |
| device_id   | String    | Identitas device |
| title       | String    | Isi tugas |
| completed   | Boolean   | Status selesai |
| created_at  | DateTime  | Waktu dibuat |
| updated_at  | DateTime  | Waktu update |

---

# 🛠️ Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Groq API (STT, LLM, TTS)
- Railway (Deployment)
- ESP32 (IoT Device)

---

# ⚙️ Environment Variables

Pastikan variabel berikut tersedia:

```
GROQ_API_KEY=your_key_here
DATABASE_URL=postgres_connection_string
```

Di Railway:
Service → Variables → Add Variable

---

# 📦 Setup Lokal

1️⃣ Install dependency:

```
pip install -r requirements.txt
```

2️⃣ Jalankan server:

```
uvicorn app.main:app --reload
```

3️⃣ Akses Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# 📡 Endpoint

## POST `/process`

**Form-data:**

| Key       | Type |
|-----------|------|
| device_id | Text |
| file      | File |

**Response:**
```
audio/mpeg
```

---

# 📂 Struktur Project

```
app/
│
├── main.py
├── database.py
├── memory.py
│
├── routes/
│   └── voice.py
│
├── services/
│   ├── stt.py
│   ├── llm.py
│   └── tts.py
│
├── models/
│   └── task.py
│
├── static/
│   └── audio/
│
└── utils/
    └── static_audio.py
```

---

# 🔮 Future Improvements

- Parsing angka berbasis kata (contoh: "two" → 2)
- Due date dan priority task
- Reminder berbasis waktu
- Multi-user authentication
- Intent classification berbasis LLM
- Wake-word session management
- Web dashboard untuk monitoring task

---

# 📌 Current Limitations

- Intent detection masih berbasis keyword matching
- Belum mendukung natural language parsing penuh
- Belum ada authentication layer

---

# 🎓 Project Purpose

Project ini dibuat sebagai prototype IoT Voice Assistant yang menggabungkan:

- Embedded System
- Backend API
- AI Integration
- Cloud Deployment
- Database Persistence

Tujuannya adalah membangun sistem voice-based task management yang lightweight, modular, dan scalable.

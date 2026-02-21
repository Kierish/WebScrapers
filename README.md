# 🖼️ Art Collection Scrapers

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)

Two independent Python scrapers designed to archive artwork metadata and images from online art archives.

The focus of this project is **reliability** and **resumable execution** rather than raw scraping speed.

---

## 📂 Projects

### 1. Abraham Mintchine *(Mint Chinese Society)*
- Extracts structured artwork data from a large HTML table.
- Parses metadata fields (dimensions, technique, provenance, bibliography).
- Downloads associated images.
- Supports safe interruption and resume.

### 2. Samuel Bak *(Kunst Archive)*
- Crawls paginated grid listings (100 items per page).
- Navigates to individual artwork pages.
- Extracts complex metadata (date ranges, provenance, exhibitions, bibliography).
- Handles multiple date formats using regex parsing.
- Resumable execution with page + item offset recovery.

---

## ⚙️ Engineering Focus

This project implements:
- **Graceful shutdown** using `signal` handling (`SIGINT`).
- **Incremental JSON persistence** after each artwork.
- **Resume support** based on previously saved data.
- **Stream-based image downloading** for efficient memory usage.
- **Dockerized runtime environments**.

*The goal was to design long-running scrapers that can be safely stopped and resumed without data loss.*

---

## 🛠️ Tech Stack

- **Python 3.10** (`requests`)
- **Parsing:** `BeautifulSoup4` + `lxml`
- **Automation:** `Selenium` (for dynamic content in Mintchine scraper)
- **Deployment:** Docker / Docker Compose

---

## ⚠️ Limitations

- No rate limiting or retry strategy implemented.
- No distributed scraping (Single-threaded execution).
- Hardcoded site structure assumptions.

*This project consciously prioritizes state reliability and structured parsing over high-throughput scraping performance.*

---

## 🚀 Getting Started

### Running with Docker

```bash
cd "Samuel Bak" # or "Abraham Mintchine"
docker-compose up --build

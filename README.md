# Art Collections Web Scrapers

A collection of robust, containerized Python web scrapers designed to archive artwork data and images from various online art galleries and museums.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Headless-43B02A?logo=selenium&logoColor=white)

## 📂 Projects

Each scraper is isolated in its own directory with specific logic for the target website.

| Project | Target Site | Description |
| :--- | :--- | :--- |
| **[Abraham Mintchine](./Abraham%20Mintchine)** | [Mint Chinese Society](https://mintchinesociety.org/) | Scrapes paintings by Abraham Mintchine. Handles dynamic table parsing and downloads high-res images. |
| **[Samuel Bak](./Samuel%20Bak)** | [Kunst Archive](https://www.kunst-archive.net/) | Scrapes the Samuel Bak catalog. Iterates through paginated grids to extract detailed metadata (provenance, exhibitions). |

## ✨ Key Features

Based on the source code, these scrapers implement professional scraping patterns:

*   **🐳 Fully Dockerized:** Each project comes with a `Dockerfile` and `docker-compose.yml` for zero-configuration deployment. Uses `python:3.10-slim` and includes all necessary system dependencies (Chrome, Drivers).
*   **⏯️ Resumable Scraping:** The scripts check existing JSON files (`Abraham.json` / `Samuel.json`) before starting. If the script was interrupted, it **automatically resumes** downloading from the last saved ID/page index to avoid duplicates.
*   **🛑 Graceful Shutdown:** Implements `signal` handling (`SIGINT`). If you press `Ctrl+C` (or stop the Docker container), the script finishes the current iteration and saves data safely before exiting.
*   **🖼️ Asset Management:** Automatically creates an `images/` directory and downloads artwork images alongside the metadata.
*   **Hybrid Scraping:** Uses **Selenium** (Headless Chrome) for handling JavaScript/Dynamic content and **BeautifulSoup/Requests** for high-speed HTML parsing.

## 🛠️ Tech Stack

*   **Language:** Python 3.10
*   **Web Automation:** Selenium WebDriver (Chrome/Chromium)
*   **Parsing:** BeautifulSoup4, lxml
*   **Data Format:** JSON (Structured output)
*   **Containerization:** Docker & Docker Compose

## 🚀 Getting Started

You can run these scrapers either locally or via Docker.

### Option 1: Using Docker (Recommended)

1.  Clone the repository:
    ```bash
    git clone https://github.com/Kierish/WebScrapers.git
    ```
2.  Navigate to the desired project folder (e.g., Samuel Bak):
    ```bash
    cd "WebScrapers/Samuel Bak"
    ```
3.  Build and run:
    ```bash
    docker-compose up --build
    ```
    *The data and images will appear in the project folder mapped via volumes.*

### Option 2: Running Locally

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Ensure you have **Chrome** and **ChromeDriver** installed and in your PATH.
3.  Run the script:
    ```bash
    python Samuel.py
    # or
    python abraham.py
    ```

## 📄 License

This project is for educational and archival purposes. Please respect the `robots.txt` and terms of service of the target websites.

---
**Author:** [Kierish](https://github.com/Kierish)

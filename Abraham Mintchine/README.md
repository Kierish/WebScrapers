# Art Scraper

## Overview

This scraper collects artwork information from the **Abraham Mintchine** collection available on the Mint Chinese Society website. It saves the collected data in a `JSON` file and downloads the images into a directory named `images`. The scraper is written in Python and utilizes libraries like `BeautifulSoup` for parsing the HTML and `Selenium` for handling dynamic content.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/art-scraper.git
    cd art-scraper
    ```

2. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. (Optional) If you prefer running the scraper with Docker, follow the Docker setup below.

## Usage

### Run the Scraper

To run the scraper, simply execute the following command:

```bash
python abraham.py
```

This will begin scraping artwork data and save it to `Abraham.json`, as well as download the images into the `images` directory.

### Docker Usage

To run the scraper using Docker, follow these steps:

1. Build the Docker image:

    ```bash
    docker-compose up --build
    ```

2. The scraper will run inside a Docker container and automatically save images and data.

If you're using Docker, the process will be fully automated.

## Data Format

The scraper stores the collected data in the `Abraham.json` file. Each artwork's information is structured as follows:

```json
[
    {
        "id": 1,
        "name_of_artist": "Abraham Mintchine",
        "title": "Irene in the cot and flowers",
        "dimensions": "100x81 cm",
        "technique": "Oil on canvas",
        "signature": "top left",
        "date": null,
        "exhibitions": null,
        "bibliography": [
            "1989 - Di Veroli, Lorenzelli and Veca, Abraham Mintchine, illustrated p.35, N°22, Ed.Galleria Lorenzelli"
        ],
        "provenance": [
            "René Gimpel, Paris, France",
            "Gimpel Fils Gallery, London, UK",
            "Galerie Di Veroli, Paris, France"
        ],
        "image_url": "https://i0.wp.com/mintchinesociety.org/wp-content/uploads/2022/01/MIN005_com.jpg?resize=236%2C300&ssl=1"
    }
]
```

## Data Structure

- `id`: A unique identifier for the artwork.
- `name_of_artist`: The artist's name (always "Abraham Mintchine").
- `title`: The title of the artwork.
- `dimensions`: The dimensions of the artwork.
- `technique`: The technique used for the artwork.
- `signature`: The artist's signature.
- `date`: The date the artwork was created (nullable).
- `exhibitions`: A list of exhibitions where the artwork was displayed (nullable).
- `bibliography`: A list of bibliographic references for the artwork.
- `provenance`: Provenance history (nullable).
- `image_url`: The URL of the artwork image.

## Notes

- The scraper will keep running until manually stopped (e.g., by pressing `Ctrl+C`).
- All images will be saved in the `images` directory.
- Each artwork's data is saved in a JSON format that includes details like title, artist's name, technique, and more.

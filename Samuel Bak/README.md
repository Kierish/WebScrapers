# Art Scraper

This project is designed to collect information about artworks by Samuel Bak from the Kunst Archive website. The script extracts data about paintings, including titles, dates, techniques, dimensions, signatures, exhibitions, bibliography, and images, and saves them in JSON format. Images are also saved in the `images` directory.

## Project Description

The project consists of two parts:
1. **Scraper** - collects information about paintings from the website.
2. **Docker container** - facilitates deployment and execution of the script in an isolated environment.

## Installation

To use the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Kierish/WebScrapers.git
    cd <project directory>
    ```

2. Install dependencies:

    If you don't want to use Docker:

    ```bash
    pip install -r requirements.txt
    ```

    For Docker usage (recommended):

    1. Build the container:

        ```bash
        docker build -t art_scraper .
        ```

    2. Run the container:

        ```bash
        docker-compose up
        ```

## Running the Script

To run the script that collects data about the artworks, use the command:

```bash
python Samuel.py
```

If you're using Docker, this step will be executed automatically.

## Data Format

The collected data is saved in the `Samuel.json` file and follows this format:

```json
[
    {
        "id": 1,
        "name_of_artist": "Samuel Bak",
        "title": "0,5 & 0,5",
        "date": "2013",
        "provenance": null,
        "technique": "Oil on canvas",
        "dimensions": "51 × 51 cm",
        "signature": "Signed lower left: BAK",
        "exhibitions": [
            "2023 Omaha, NE, In the Beginning: The Artist Samuel Bak",
            "2014 Boston, MA, Told & Foretold . The Cup in the Art of Samuel Bak"
        ],
        "bibliography": [
            "Told & Foretold . The Cup in the Art of Samuel Bak, Lawrence L. Langer, 2014 Boston, MA, p. 31, ill.",
            "Told & Foretold . The Cup in the Art of Samuel Bak, Lawrence L. Langer, 2014 Boston, MA, p. 60, ill."
        ],
        "image_url": "https://www.kunst-archive.net/images/wwwartworkMax/BK1595_printa-(898f1af4-0b91-11e9-96fc-31a773e362eb).jpg"
    }
]
```

## Data Structure

- `id`: Unique identifier for the artwork.
- `name_of_artist`: Name of the artist (always "Samuel Bak").
- `title`: Title of the artwork.
- `date`: Date the artwork was created.
- `provenance`: Provenance history (if available).
- `technique`: Technique used for the artwork.
- `dimensions`: Dimensions of the painting.
- `signature`: Artist's signature.
- `exhibitions`: List of exhibitions where the artwork was displayed.
- `bibliography`: List of bibliographic references for the artwork.
- `image_url`: URL of the painting image.

## Notes

- The scraper will keep running until manually stopped (e.g., by pressing `Ctrl+C`).
- All images will be saved in the `images` directory.
- Each artwork's data is saved in a JSON format that includes details like title, artist's name, technique, and more.
# Daraz Product Scraper

A Python-based web scraper that collects product listings from Daraz Nepal and exports the results into an Excel file.

## Features

- Search products from Daraz Nepal
- Automatically scrape all available pages
- Extract:
  - Product Name
  - Price
  - Rating
  - Seller Name
  - Product Link
- Retry failed requests automatically
- Detect captcha or invalid responses
- Export results to Excel (`results.xlsx`)
- Store each search query in a separate sheet

---

## Project Structure

```text
.
├── scraper.py
├── requirements.txt
└── results.xlsx
```

---

## Installation

Clone the repository:

```bash
git clone 'https://github.com/Sohan-Raj-Adhikari/Daraz-Scraper/'
cd 'Daraz-Scraper'
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Requirements

The required libraries are listed in `requirements.txt`.

Example:

```text
requests
pandas
openpyxl
```

---

## Usage

Run the scraper:

```bash
python scraper.py
```

Enter a product name when prompted:

```text
Enter a product to search: laptop
```

Example output:

```text
Total number of items: 324
Page number : 1
Page number : 2
Page number : 3
Executed successfully. 324 products found.
```

---

## Output

The scraper generates:

```text
results.xlsx
```

Each search query is stored as a separate worksheet.

Example sheet names:

- `laptop_result`
- `phone_result`
- `shoes_result`

---

## Data Collected

| Field | Description |
|------|-------------|
| Name | Product name |
| Price | Product price |
| Rating | Product rating |
| Seller | Seller name |
| Link | Direct product URL |

---

## Error Handling

The scraper includes:

- Request retry mechanism
- Timeout handling
- Captcha detection
- Invalid response handling
- JSON parsing protection

---

## Notes

- Daraz may temporarily block repeated requests.
- Delays are used to reduce request frequency.
- Website response structures may change over time.

---

## Future Improvements

- Add product image links
- Export to CSV
- Use rotating proxies
- Add command-line arguments
- Parallel scraping
- Database storage support

---

## Disclaimer

This project is for educational purposes only.  
Please respect Daraz Nepal's terms of service before scraping.

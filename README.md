# CBSE Result Crawler

## Description
This Python program crawls the CBSE (Central Board of Secondary Education) results from the official CBSE website and saves them as HTML pages for offline access.

## Features
- Fetches CBSE results automatically.
- Saves results as structured HTML pages.
- Can handle multiple roll numbers for batch processing.
- Error handling for invalid roll numbers and network issues.
- Uses session handling to maintain persistent requests.
- Implements colored terminal output for better readability.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  - `requests` (for fetching web pages)
  - `re` (for regex operations)
  - `glob` (for file handling)
  
You can install them using:
```sh
pip install requests
```

## Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/cbse-result-crawler.git
   cd cbse-result-crawler
   ```
2. Run the script using command-line options:
   ```sh
   python crawler.py -s <start_roll_number> -e <end_roll_number> -c <school_code> -n <center_code>
   ```
   Or if no command-line options are provided, the program will prompt for input interactively.

3. The results will be saved as HTML files in the `Results/` directory.

## Warning

- This program is intended for educational purposes only.
- Misuse of this tool to access, scrape, or distribute data without proper authorization may violate laws and terms of service.
- The author is not responsible for any misuse, legal consequences, or damages resulting from the use of this program.

## Notes
- This program is for educational purposes only.
- Ensure that web scraping does not violate CBSE website's terms of service.
- Use responsibly and do not overload CBSE servers.
- Results are checked for validity before saving.
- If a result is already present in the `Results/` directory, it will be skipped.

## License
This project is licensed under the MIT License.

## Author
[Nikunj Vashishta]


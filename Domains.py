import urllib3, re, time, random, sys, os, socket
color = ["\033[31m", "\033[32m", "\033[33m", "\033[34m","\033[35m", "\033[36m", "\033[37m", "\033[39m"]
try: import requests; s = requests.Session()
except:print("{w}Require {g}requests {w}module\n{y}pip install {g}requests".format(w=color[6], y=color[2], g=color[1])); exit()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
thread = 1
outputFile = open("sPc.txt", "a")
tmpSites = []
ipsList = []
retSo = []
retSe = []


def logo():
    os.system(["clear", "cls"][os.name == 'nt'])
    Logo = '''



██   ██  ██ ██      ██      ██████  ██████  ███████ ███    ██ ██████  
██  ██  ███ ██      ██           ██ ██   ██ ██      ████   ██ ██   ██ 
█████    ██ ██      ██       █████  ██████  █████   ██ ██  ██ ██   ██ 
██  ██   ██ ██      ██           ██ ██   ██ ██      ██  ██ ██ ██   ██ 
██   ██  ██ ███████ ███████ ██████  ██   ██ ███████ ██   ████ ██████  
                                                                      
                                                                      
                          
                                                                                                                                                                             
                                                                                                                                               
     {y}Coded By {w}[{g}@{w}] {y}K1LL3rEnd          /_/ {w}v2.0\n'''.format(g=color[1], w=color[7], m=color[4], y=color[2], r=color[0])
    for Line in Logo.split('\n'):
        print(random.choice(color)+Line)
        time.sleep(0.00000001)


def opt():
    siteList = []
    fileName = input(
        " {w}[{g}+{w}] {y}the list {w}> ".format(w=color[6], g=color[1], y=color[2]))
    if os.path.exists(fileName):
        siteList = open(fileName, "r+").readlines()
    else:
        print(" {A}[{B}x{A}] {B}The list not found in current dir".format(A=color[6], B=color[5]))
        exit()
    if siteList == []:
        print(" {A}[{B}x{A}] {B}Empty list".format(A=color[6], B=color[5]))
        exit()
    else:
        return siteList


def revSo(ip):
    global retSo
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    api = "https://sonar.omnisint.io/reverse/"
    try:
        r = s.get(api+ip, headers=headers)
    except:
        if ip not in retSo:
            revSo(ip)
        return "error"
    if r.text == "null":
        r2 = revSe(ip)
        if r2 != "error":
            return r2
        else:
            return "error"
    else:
        r = r.json()
        res = []
        for site in r:
            site = site.replace("www.", "").replace('cpanel.', '').replace('webmail.', '').replace('webdisk.', '').replace('ftp.', '').replace(
                'cpcalendars.', '').replace('cpcontacts.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '').replace('autodiscover.', '')
            res.append(site)
        return res


def revSe(ip):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    cookies = {'_securitytrails_app': 'QTEyOEdDTQ.2dg-yKAWm7FtHoULx71Xx1T0uiUnKFOTKWWeksjkC_jv0mFpLTbHqh1rTf8.CpqARN-2K38WMFAD.iERob28xeHWCtngQqyiveiTWQ1DS9n-RUSCSBhOLh_AaKqfUyiQxJHCOULI2uVv_Lr26zm4kpKB_hBAPfQDXQGl4dfUQAuCzZr1B9fY8pLaiw0WA2SJg1KquCEOLrQmR1-b5ZVTbe7q9ba76iL6lLOZOxPMUI-Jf4O_LQIcd4GaA8azeOaBZp8uefju4uuxI4WymtPsVOnJS3pw4gumtPBcQUEseDZLJoG1j7meC5eMKcIHHV2HTmxGO.5CGzwh12cf-Lp1_OKovvrQ',
               'DFTT_END_USER_PREV_BOOTSTRAPPED': 'true',
               'driftt_aid': 'e361412c-e1fa-46c1-be7c-d17945c6be0e',
               'driftt_sid': '76ae5193-6ddc-4cd8-ab8f-81f419153dcd',
               'mp_679f34927f7b652f13bda4e479a7241d_mixpanel': '%7B%22distinct_id%22%3A%20%22176826a0406500-0471a33fb9abb2-c791039-100200-176826a0407781%22%2C%22%24device_id%22%3A%20%22176826a0406500-0471a33fb9abb2-c791039-100200-176826a0407781%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fsecuritytrails.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22securitytrails.com%22%2C%22app%22%3A%20%22SecurityTrails%22%7D'}
    api = "https://securitytrails.com/app/api/v1/list_new/ip/"
    sites = []
    for i in range(1, 20):
        page = str(i)
        try:
            r = s.post(api+ip+"?page="+page, headers=headers, cookies=cookies)
        except:
            continue
        for site in r.json()['records']:
            site = site['hostname']
            site = site.replace("www.", "").replace('cpanel.', '').replace('webmail.', '').replace('webdisk.', '').replace('ftp.', '').replace(
                'cpcalendars.', '').replace('cpcontacts.', '').replace('mail.', '').replace('ns1.', '').replace('ns2.', '').replace('autodiscover.', '')
            sites.append(site)
        if len(r.json()['records']) != 100:
            break
    if sites is None:
        return "error"
    return sites


def rev(url):
    global tmpSites, outputFile, ipsList
    if url.startswith("http://"):
        url = url.replace("http://", "")
    elif url.startswith("https://"):
        url = url.replace("https://", "")
    url = url.replace("\n", "").replace("\r", "").replace("/", "")
    try:
        ip = socket.gethostbyname(url)
        if ip in ipsList:
            print(" \033[41;1m -- SAME IP -- \033[0m "+url)
            return
        ipsList.append(ip)
        so = revSo(ip)
    except Exception as e:
        print(" \033[41;1m -- ERROR -- \033[0m "+url)
        return
    st = []
    if so != "error":
        for s in so:
            if s not in st:
                st.append(s)
    resultSite = []
    for site in st:
        if site != "":
            if site not in tmpSites:
                outputFile.write(site+"\n")
                tmpSites.append(site)
                resultSite.append(site)
    print(" \033[42;1m -- "+str(len(resultSite))+" SITES -- \033[0m "+url)


if __name__ == "__main__":
    try:
        logo()
        sx = opt()
        print("\n")
        for site in sx:
            rev(site)
        print("\n {A}[{B}+{A}] {Y}Done {A}: {Y}{S} sites".format(Y=color[2],
                                                                 A=color[6], B=color[5], S=(str(len(tmpSites)))))
    except KeyboardInterrupt:
        print(
            "\n {w}[{r}-{w}] {b}Goodbye >//< ".format(w=color[6], r=color[0], b=color[3]))

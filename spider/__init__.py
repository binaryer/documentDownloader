import urllib.request


def makeURL(host, args):
    url = host
    for key in args:
        url += key + '=' + args[key] + '&'
    url = url[0:-1]
    return url


def getHTML(url, byte=False):
    # print("getting " + url)
    html=''
    while True:
        try:
            html = urllib.request.urlopen(url, timeout=30).read()
            break
        except:
            pass
    if not byte:
        html = html.decode('utf-8')
    return html

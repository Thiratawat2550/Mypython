def studentscore(n):
    sum_score=0
    for i in range(n):
        score = int(intput(f"กรุรากรอกคะแนนนักศึกษาคนที่1 {i+1}: " ))
        sum_score += score
        avgscore = sum_score/n
        return avgscore
    
n = int(intput("กรุณากรอกคะแนนนักศึกษา:"))
average = calavgscore(n)
print(f"คะแนนเฉลี่ยของนักศึกษา {n} คือ {average}")
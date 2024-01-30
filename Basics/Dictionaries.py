db = dict()

student_id = int(input())
midterm = float(input())
final = float(input())
db[student_id] = (midterm, final)

student_id = int(input())
midterm = float(input())
final = float(input())
db[student_id] = (midterm, final)

student_id = int(input())
midterm = float(input())
final = float(input())
db[student_id] = (midterm, final)

student_id = int(input())

(midterm, final) = db[student_id]   # notice the tuple matching
average = (midterm + final) / 2
print("{:.1f}".format(average))
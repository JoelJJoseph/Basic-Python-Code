student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

sum=0
for i in student_heights:
    sum=sum+i
print(sum)
    
no=0
for j in student_heights:
    no+=1
print(no)
avg=sum/no
print(int(avg))
    
    
##############  WITH FUNCTION ################

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_h=sum(student_heights)
no_of_stu=len(student_heights)
avg=total_h/no_of_stu
print(int(avg))





############## HIGHEST SCORE ################

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest =0
for i in student_scores:
    if i>highest:
        highest=i
print(f"The highest score in the class is: {highest}")


############ with Function #################
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

print(max(student_scores))


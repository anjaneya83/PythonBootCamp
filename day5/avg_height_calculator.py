'''
You are going to write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights

1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Example Input 1
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

Example Output 1
total height = 857
number of students = 5
average height = 171
'''
student_input = input("Enter the height of students in integer format with comma separated delimiter:\n ")
student_heights = student_input.split(",")
print(student_heights)
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
height_sum=0
count=0
for height in student_heights:
    height_sum+=height
    count+=1
avg_height = height_sum/count
print(f"total_height = {height_sum}")
print(f"number of students = {count}")
print(f"average height = {avg_height}")















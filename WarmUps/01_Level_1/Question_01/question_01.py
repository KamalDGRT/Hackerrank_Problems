# Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    student = student_marks[query_name]

    average = 0.0
    list_size = len(student)
    for marks in student:
        average = average + marks

    average /= list_size
    print (format(average, '.2f'))

def main():

    student = input("Enter student name: ")

    grade1 = int(input("Enter grade 1: "))
    grade2 = int(input("Enter grade 2: "))
    grade3 = int(input("Enter grade 3: "))
    grade4 = int(input("Enter grade 4: "))
    grade5 = int(input("Enter grade 5: "))

    allGrades = [grade1, grade2, grade3, grade4, grade5]
    print("List of grades:", allGrades)

    print(" ")

    print(student)

    averageGrade = sum(allGrades) / len(allGrades)
    print("Average:", averageGrade)

    if averageGrade <= 100 and averageGrade >= 90 :
        print("Letter Grade: A")

    elif averageGrade <= 89 and averageGrade >= 80 :
        print("Letter Grade: B")

    elif averageGrade <= 79 and averageGrade >= 70 :
        print("Letter Grade: C")

    elif averageGrade <= 69 and averageGrade >= 60 :
        print("Letter Grade: D")

    elif averageGrade <= 59 :
        print("Letter Grade: F")

main()




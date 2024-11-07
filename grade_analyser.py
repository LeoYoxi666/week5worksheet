import csv

def calculate_classification(average_grade):
    
    if average_grade >= 70:
        return "1"
    elif average_grade >= 60:
        return "2:1"
    elif average_grade >= 50:
        return "2:2"
    elif average_grade >= 40:
        return "3"
    else:
        return "F"

def process_student_grades(input_filename):
    
    output_filename = input_filename + "_out.csv"
    with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            student_id = row[0]
            
            grades = [int(grade) for grade in row[1:] if grade]
            
            average_grade = sum(grades) / len(grades)
           
            classification = calculate_classification(average_grade)
            
            writer.writerow([student_id, f"{average_grade:.2f}", classification])

def main():
    input_filename = input("Enter the filename of the student file: ")
    process_student_grades(input_filename)
    print(f"Output file generated: {input_filename}_out.csv")

if __name__ == "__main__":
    main()

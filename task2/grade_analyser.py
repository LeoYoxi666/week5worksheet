file_name = input("which file you wants to classify?:")
new_file_name = file_name+"_out.csv"
with open(file_name, "r") as file: 
    content=file.readlines()
with open(new_file_name, "w") as out_file:
     for line in content[1:]:
          grade_line = line.strip().split(',')
          ID_code = grade_line[0]
          grade = [int(grade) for grade in grade_line[1:] if grade]
          average_grade = sum(grade) / len(grade)
          if average_grade >= 70:
               level = "1"
          elif average_grade >= 60 and average_grade < 70:
               level = "2:1"
          elif average_grade >= 50 and average_grade < 60:
               level = "2:2"
          elif average_grade >= 40 and average_grade < 50:
               level = "3"
          elif average_grade <= 60:
               level = "F"
          result_classity = f"{ID_code},{average_grade:.2f},{level}"+"\n"
          out_file.write(result_classity)

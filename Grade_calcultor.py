## Hello kids let play a game! can you provide me with your grade for the 5 below subjects (math,AC,reading....)
print ("Please enter your grade number (between 0-100) below for each subject")
sub1= float(input("Enter a number your grade for math:\n"))
sub2= float(input("Enter a number your grade for reading:\n"))
sub3= float(input("Enter a number your grade for ac:\n"))
sub4= float(input("Enter a number your grade for science:\n"))
sub5= float(input("Enter a number your grade for music:\n"))

sum=sub1+sub2+sub3+sub4+sub5
average_grade= sum/5

if average_grade > 90:
    print("Execllent job your grade is: A")
elif  average_grade >80:
    print("Great job your overall grade is: B")
elif    average_grade > 70:
    print( "keep working your overall grade is:D")
elif average_grade > 60:
    print("Keep pushing your overall grade is: C")
else:
    print("you can do better push hard it is possible your grade is :E")

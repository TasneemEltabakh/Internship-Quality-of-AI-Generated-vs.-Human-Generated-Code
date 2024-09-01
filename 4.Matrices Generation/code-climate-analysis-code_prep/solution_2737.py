print("Enter marks of 5 subjects out of 100:")
sub1=float(input("Enter sub1 marks:"))
sub2=float(input("Enter sub2 marks:"))
sub3=float(input("Enter sub3 marks:"))
sub4=float(input("Enter sub4 marks:"))
sub5=float(input("Enter sub5 marks:"))

total_marks=sub1+sub2+sub3+sub4+sub5;
avg=total_marks/5.0;
percentage=total_marks/500*100;

print("Total Marks:",total_marks)
print("Average:",avg)
print("Percentage:",percentage,"%")
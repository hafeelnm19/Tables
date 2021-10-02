from prettytable import PrettyTable
#Add the coumn names
Table=PrettyTable(["Student Name","Grade","Subject","Percentage"])
#Add rows
Table.add_row(["John","Grade 12","Physics","97%"])
Table.add_row(["maradona","Grade 13","Chemistry","90%"])
Table.add_row(["Mars","Grade 12","Physics","80%"])
Table.add_row(["Nick","Grade 12","Mathemtics","75%"])
#display the table
print(Table)

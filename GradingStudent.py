def gradingStudents(grades):
    gra = []
    for grade in grades:
        if(grade < 38):
            gra.append(grade)
        elif(grade % 5  >= 3):
            gra.append(grade + 5 - (grade % 5))   
        else:
            gra.append(grade)
    return gra 

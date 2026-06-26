from django.shortcuts import render
def fruit_student(request):
    fruitList=['banana','apple','muskmelon','kiwi']
    studentList=['bhavvi','katti','kempi','macchi','rasgulla']
    context={
        'fruitList':fruitList,
        'studentList':sorted(studentList)
    }
    return render(request,'fruit_student/fruit_student.html',context)


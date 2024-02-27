from django.shortcuts import render

# Create your views here.
def home(request):
    # return render(request,'home.html',{'name':'Kishore'})    we can do this or we can do like the one in below also

    my_context={
        'name' : 'Kishore',
        'age' : '21',
        'hobbie' : 'Cricket'
    }
    return render(request,'home.html',my_context)


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request , 'result.html' , {'result':res})
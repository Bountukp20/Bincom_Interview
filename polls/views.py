from django.shortcuts import render

# Create your views here.

from django.db import connection
from django.shortcuts import render

def polling_unit(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM polling_unit where polling_unit_name = 'Sapele Ward 8 PU _'")
        rows = cursor.fetchall()

    # Process the rows and return the response
    return render(request, 'polls/polling_unit.html', {'rows': rows})

def sum_polling_unit(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM polling_unit")
        rows = cursor.fetchall()

    # Process the rows and return the response
    return render(request, 'polls/sum_total_of_polling_unit.html', {'rows': rows})

def add_new_polling_unit(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            with connection.cursor() as cursor:
                # Assuming 'your_table' is the name of your table and 'content_field' is the field name
                cursor.execute("INSERT INTO polling_unit (polling_unit_id) VALUES (%s)", [content])
            return render(request, 'polls/success.html')

    return render(request, 'polls/add_polling_unit.html')
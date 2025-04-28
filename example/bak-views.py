# example/views.py
from datetime import datetime

from django.http import HttpResponse
def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Python + Django + MySQL hosted at Vercel Cloud</h1>
            <p>The current time is { now }.</p>
            <p>Note: The Administration part is able to use both SQLlite and MySQL :-) </p>
            
        </body>
    </html>
    '''
    return HttpResponse(html)
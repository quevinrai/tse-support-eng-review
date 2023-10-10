import re

from django.shortcuts import render
from jira.models import MonthlyQuickNumber

def home(request):
    data = MonthlyQuickNumber.objects.all()
    print(data.values()[0]['url_param_value'])

    return render(request, 'TSESupportEngReview/index.html')

def month_year(request, month, year):
    context = {
        'month': month,
        'year': year
    }

    data = MonthlyQuickNumber.objects.all()
    created_gte = re.search('created\s>=\s(\d{4})-(\d{2})-(\d{2})', data.values()[0]['jql'])
    print(created_gte.group(1) + '/' + created_gte.group(2) + '/' + created_gte.group(3))

    return render(request, 'TSESupportEngReview/index.html', context)
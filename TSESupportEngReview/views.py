import re
import datetime

from datetime import datetime, timedelta
from django.shortcuts import render
from jira.models import MonthlyQuickNumber

"""
FUNCTION-BASED VIEWS
"""

def home(request):
    current_month = datetime.now().replace(day=1)
    current_month_full = datetime.now().strftime('%B')
    current_month_num = datetime.now().strftime('%m')
    current_year = datetime.now().strftime('%Y')

    previous_month = (datetime.utcnow().replace(day=1) - timedelta(days=1)).replace(day=1)
    print(f'Previous month: {previous_month.strftime("%Y")}-{previous_month.strftime("%m")}-{previous_month.strftime("%d")}')
    # print(f'Previous month: {current_month.strftime("%Y")}-{current_month.strftime("%m")}-{current_month.strftime("%d")}')

    new_created_date_gte = f'created >= {current_year}-{current_month_num}-01'
    new_created_date_lte = f'created <= {current_year}-{current_month_num}-01'

    data = MonthlyQuickNumber.objects.all()
    created_gte = re.sub('created\s>=\s(\d{4})-(\d{2})-(\d{2})', new_created_date_gte, data.values()[0]['jql'])
    # print(created_gte)

    context = {
        'month': current_month_full,
        'year': current_year
    }

    return render(request, 'TSESupportEngReview/index.html', context)

def month_year(request, month, year):
    context = {
        'month': month,
        'year': year
    }

    data = MonthlyQuickNumber.objects.all()
    created_gte = re.search('created\s>=\s(\d{4})-(\d{2})-(\d{2})', data.values()[0]['jql'])
    print(created_gte.group(1) + '/' + created_gte.group(2) + '/' + created_gte.group(3))

    return render(request, 'TSESupportEngReview/index.html', context)

"""
UTILITY FUNCTIONS
"""

def update_created_date(previous_month, current_month, data):
    pass
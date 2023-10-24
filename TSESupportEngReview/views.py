import re
import datetime
import calendar

from datetime import datetime
from django.shortcuts import render, redirect
from jira.models import MonthlyQuickNumber

"""
FUNCTION-BASED VIEWS
"""

def home(request):
    current_month = datetime.now().replace(day=1)
    current_month_full = datetime.now().strftime('%B')
    current_month_num = datetime.now().strftime('%m')
    current_year = datetime.now().strftime('%Y')

    # previous_month = (datetime.utcnow().replace(day=1) - timedelta(days=1)).replace(day=1)
    # print(f'Previous month: {previous_month.strftime("%Y")}-{previous_month.strftime("%m")}-{previous_month.strftime("%d")}')
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
    try:
        year_number = int(year)
    except Exception:
        print('ERROR: Invalid year was entered.')
        return redirect('/')

    try:
        month_number = int(month)
        month = calendar.month_name[month_number]
    except ValueError:
        try:
            month_number = datetime.strptime(month, '%b').month if len(month) == 3 else datetime.strptime(month, '%B').month
            month = calendar.month_name[month_number] if len(month) == 3 else month
        except ValueError:
            print('ERROR: Invalid month was entered.')
            return redirect('/')

    current_month = get_current_month(year_number, month_number)
    previous_month = get_previous_month(year_number, month_number)

    print(f'Previous month: {previous_month}')
    print(f'Current month: {current_month}')

    data = MonthlyQuickNumber.objects.all()
    data_monthly_quick_numbers = dict()

    temp_str = data.values()[0]['url_param']
    new_temp_str = temp_str.replace('2023-05-01', previous_month).replace('2023-06-01', current_month)

    data_monthly_quick_numbers[data.values()[0]['name']] = new_temp_str

    print(data_monthly_quick_numbers)

    context = {
        'month': month,
        'year': year
    }

    return render(request, 'TSESupportEngReview/index.html', context)

"""
UTILITY FUNCTIONS
"""

def update_created_date(previous_month, current_month, data):
    pass

def get_current_month(year, month, day = 1):
    return f'{year}-0{month}-0{day}' if len(str(month)) == 1 else f'{year}-{month}-0{day}'

def get_previous_month(year, month, day = 1):
    if month == 1:
        return f'{year - 1}-12-0{day}'
    else:
        return f'{year}-0{month - 1}-0{day}' if len(str(month)) == 1 else f'{year}-{month - 1}-0{day}'
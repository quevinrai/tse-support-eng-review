import calendar

from datetime import datetime
from django.shortcuts import render, redirect
from jira.models import MonthlyQuickNumber

""" CLASS """

class C(object):
    def __init__(self):
        self._month = None
        self._year = None
        self._month_number = None
        self._year_number = None
        self._previous_month = None
        self._current_month = None

    """ Getters """
    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    @property
    def month_number(self):
        return self._month_number

    @property
    def year_number(self):
        return self._year_number

    @property
    def previous_month(self):
        return self._previous_month

    @property
    def current_month(self):
        return self._current_month

    """ Setters """
    @month.setter
    def month(self, value):
        self._month = value

    @year.setter
    def year(self, value):
        self._year = value

    @month_number.setter
    def month_number(self, value):
        self._month_number = value

    @year_number.setter
    def year_number(self, value):
        self._year_number = value

    @previous_month.setter
    def previous_month(self, value):
        self._previous_month = value

    @current_month.setter
    def current_month(self, value):
        self._current_month = value

c = C()

""" FUNCTION-BASED VIEWS """

def home(request):
    return render(request, 'TSESupportEngReview/index.html')

def month_year(request, month, year):

    """ Validate URL parameter values """
    validate_month_year(month, year)

    print(f'Previous month: {c.previous_month}')
    print(f'Current month: {c.current_month}')

    data = MonthlyQuickNumber.objects.all()
    data_monthly_quick_numbers = dict()

    for x in range(len(data)):
        data_url_parameter = data.values()[x]['url_parameter'].replace('0000-00-01', c.previous_month).replace('1000-00-01', c.current_month)
        data_monthly_quick_numbers[data.values()[x]['name']] = data_url_parameter

    print(data_monthly_quick_numbers)

    context = {
        'month': month,
        'year': year
    }

    return render(request, 'TSESupportEngReview/09_2023.html', context)

""" UTILITY FUNCTIONS """

def validate_month_year(month, year):
    """ Validation for 'year' url parameter
    • Check if 'year' value can be converted to an integer.
    • If not successful, throw exception and return to 'home' path.
    """
    try:
        c.year_number = int(year)
    except Exception:
        print('ERROR: Invalid year was entered.') # Replace with Django FlashMessages
        return redirect('/')

    """ Validation for 'month' url parameter
    • Check if 'month' value is a valid month name.
    """
    try:
        c.month_number = int(month)
        month = calendar.month_name[c.month_number]
    except ValueError:
        try:
            c.month_number = datetime.strptime(month, '%b').month if len(month) == 3 else datetime.strptime(month, '%B').month
            month = calendar.month_name[c.month_number] if len(month) == 3 else month
        except ValueError:
            print('ERROR: Invalid month was entered.') # Replace with Django FlashMessages
            return redirect('/')

    set_previous_month()
    set_current_month()

def set_current_month():
    c.current_month = f'{c.year_number}-0{c.month_number}-01' if len(str(c.month_number)) == 1 else f'{c.year_number}-{c.month_number}-01'

def set_previous_month():
    if c.month_number == 1:
        c.previous_month = f'{c.year_number - 1}-12-01'
    else:
        c.previous_month = f'{c.year_number}-0{c.month_number - 1}-01' if len(str(c.month_number)) == 1 else f'{c.year_number}-{c.month_number - 1}-01'
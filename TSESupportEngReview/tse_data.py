from jira.models import MonthlyQuickNumber

def main():
    pass

def get_data_monthly_quick_numbers(previous_month, current_month):
    data = MonthlyQuickNumber.objects.all()
    new_data = dict()

    for x in range(len(data)):
        data_name = data.values()[x]['name']
        data_url_parameter = data.values()[x]['url_parameter'].replace('0000-00-01', previous_month).replace('1000-00-01', current_month)

        new_data[data_name] = data_url_parameter

    return new_data

# asyncio.run(main())
# print("--- %s seconds ---" % (time.time() - start_time))
from jira.models import MonthlyQuickNumber

def main():
    data = MonthlyQuickNumber.objects.all()
    print(data)

main()

# asyncio.run(main())
# print("--- %s seconds ---" % (time.time() - start_time))
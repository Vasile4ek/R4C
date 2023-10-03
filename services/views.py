
def weekly_report(request):
    wb = Workbook()
    today = datetime.now()
    week = today - timedelta(days=7)
    print(today.isoformat(), week.isoformat())
    robots = Robot.objects.filter(created__range=["2011-01-01", "2011-01-31"])
    print(robots)

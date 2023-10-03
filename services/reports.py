from datetime import datetime, timedelta
from io import BytesIO

from openpyxl import Workbook

from django.http import HttpResponse

from robots.models import Robot


def weekly_report(request):
    return create_excel()


def create_excel():


    today = datetime.now()
    week_ago = today - timedelta(days=7)
    print(today.isoformat(), week_ago.isoformat())

    robots = Robot.objects.filter(created__range=[week_ago, today])
    robots_dict = {}
    for robot in robots:
        print(robot)
        if robot.model in robots_dict:
            if robot.version in robots_dict[robot.model]:
                robots_dict[robot.model][robot.version] += 1
            else:
                robots_dict[robot.model][robot.version] = 1
        else:
            robots_dict[robot.model] = {robot.version: 1}

    print(robots_dict)

    wb = Workbook()
    ws = wb.create_sheet()

    excel_file = BytesIO()
    wb.save(excel_file)

    response = HttpResponse(excel_file.getvalue(), content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="Robots_weekly_report.xlsx"'
    return response

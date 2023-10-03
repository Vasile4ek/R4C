from datetime import datetime, timedelta
from io import BytesIO

from openpyxl import Workbook


def create_excel(robot_db_model):
    today = datetime.now()
    week_ago = today - timedelta(days=7)

    robots = robot_db_model.objects.filter(created__range=[week_ago, today])

    robots_dict = {}
    for robot in robots:
        robots_dict[robot.model] = robots_dict.get(robot.model, {})
        robots_dict[robot.model][robot.version] = robots_dict[robot.model].get(robot.version, 0)
        robots_dict[robot.model][robot.version] += 1

    wb = Workbook()
    wb.remove_sheet(wb.active)

    for model, versions in robots_dict.items():
        ws = wb.create_sheet(model)
        ws.append(["Модель", "Версия", "Количество за неделю"])
        for version, count in versions.items():
            ws.append([model, version, count])

    excel_file = BytesIO()
    wb.save(excel_file)
    return excel_file


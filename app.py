from flask import Flask
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu
import datetime
import locale
import requests
from requests.auth import HTTPBasicAuth

from jira_functions import get_all_issues
from extract_info_functions import extract_issues_types, extract_hisotrical_info, extract_weekly_info
from report_functions import generate_report_template


# Set the Spanish language
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
# Get days from last week
today = datetime.date.today()
start_of_week = today - datetime.timedelta(days=today.weekday()) - datetime.timedelta(weeks=1)
end_of_week = start_of_week + datetime.timedelta(days=6)
#print(start_of_week)
#print(end_of_week)


app = Flask(__name__)

@app.route('/report/<proyect_key>')
def generate_report(proyect_key):
    all_issues = get_all_issues(proyect_key)

    issues_types = extract_issues_types(all_issues)

    print(f'Issues Types: {issues_types}')
    table_historical = extract_hisotrical_info(issues_types, all_issues)

    table_weekly_description, table_weekly = extract_weekly_info(issues_types, all_issues, start_of_week, end_of_week)
    #print(len(table_weekly_description))
    generate_report_template(start_of_week, end_of_week, table_weekly, table_historical, table_weekly_description)
    return '¡¡Reporte Generado!!'
    

if __name__ == '__main__':
    app.run()
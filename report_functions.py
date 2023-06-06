from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu
import datetime

def generate_report_template(start_of_week, end_of_week, table_weekly, table_historical, table_weekly_description):
    template = DocxTemplate('Reporte Semanal (1).docx')
    # Set context values for the document
    context = {
        'week_start': start_of_week,
        'week_end': end_of_week,
        'day': datetime.datetime.now().strftime('%d'),
        'month': datetime.datetime.now().strftime('%B'),
        'year': datetime.datetime.now().strftime('%Y'),
        'table_weekly': table_weekly,
        'table_historical': table_historical,
        'table_weekly_description': table_weekly_description
    }
    # Render automated report 
    template.render(context)
    template.save('generated_report_jira_get_flask.docx')
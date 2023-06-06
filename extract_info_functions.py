

import datetime



def extract_issues_types(all_issues):
    issues_types = set()
    for item in all_issues:
        issue_type = item['fields']['issuetype']['name'] 
        issues_types.add(issue_type)
    return issues_types


def extract_hisotrical_info(issues_types, all_issues):
    table_historical = []
    for issue_type in issues_types:
        canceld_issues = 0
        open_issues = 0
        for issue in all_issues:
            if issue['fields']['issuetype']['name'] == issue_type:
                if issue['fields']['status']['name'] == "Canceled" or issue['fields']['status']['name'] == "Done" or issue['fields']['status']['name'] == "Passed":
                    canceld_issues = canceld_issues + 1
                else:
                    open_issues = open_issues + 1
        table_historical.append({
            'Type': issue_type,
            'Quantity': open_issues + canceld_issues,
            'Open': open_issues,
            'Close': canceld_issues
        })
        print(f'--HISTORICO-- Tipo: {issue_type} - Total: { open_issues + canceld_issues} - Abiertos: {open_issues} - Cerrados: {canceld_issues}')
    return table_historical



def extract_weekly_info(issues_types, all_issues, start_of_week, end_of_week):
    component_list = []
    table_weekly_description = []
    table_weekly = []
    for issue_type in issues_types:
        canceld_issues = 0
        open_issues = 0
        for issue in all_issues:
            created_date = datetime.datetime.strptime(issue['fields']['created'], "%Y-%m-%dT%H:%M:%S.%f%z")
            updated_date = datetime.datetime.strptime(issue['fields']['updated'], "%Y-%m-%dT%H:%M:%S.%f%z")
            if created_date.date() >= start_of_week and created_date.date() <= end_of_week:
                if issue['fields']['issuetype']['name'] == issue_type:
                    if issue['fields']['status']['name'] == "Canceled" or issue['fields']['status']['name'] == "Done" or issue['fields']['status']['name'] == "Passed":
                        canceld_issues = canceld_issues + 1
                    else:
                        open_issues = open_issues + 1
                    component = issue['fields']['components']
                    for i in component:
                        component_list.append(i['name'])
                    table_weekly_description.append({
                        'Key': issue['key'],
                        'Type_issue': issue['fields']['issuetype']['name'],
                        'Summary': issue['fields']['summary'],
                        'Status': issue['fields']['status']['name'],
                        'Assignee': issue['fields']['assignee']['displayName'] if issue['fields']['assignee'] is not None else '',
                        'Customer_Reporter': issue['fields']['reporter']['displayName'],
                        'Component': ', '.join(component_list) if len(component_list) > 1 else '',
                        'Created': f'{created_date.year} - {created_date.month} - {created_date.day}',
                        'Update': f'{updated_date.year} - {updated_date.month} - {updated_date.day}',
                    })
        table_weekly.append({
            'Type': issue_type,
            'Quantity': open_issues + canceld_issues,
            'Open': open_issues,
            'Close': canceld_issues
        })
        print(f'--SEMANAL-- Tipo: {issue_type} - Total: { open_issues + canceld_issues} - Abiertos: {open_issues} - Cerrados: {canceld_issues}')
    return table_weekly_description, table_weekly



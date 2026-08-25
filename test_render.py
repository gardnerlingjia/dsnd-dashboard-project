import sys
sys.path.insert(0, '.')
from report.dashboard import report
from employee_events import Employee

try:
    html = report('25', Employee())
    print('Success - HTML len:', len(str(html)))
except Exception as e:
    print(f'Error: {type(e).__name__} - {e}')
    import traceback
    traceback.print_exc()

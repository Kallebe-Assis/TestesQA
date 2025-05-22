import pytest
import os
import datetime

def run_tests():
    # Create reports directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')
    if not os.path.exists('reports/screenshots'):
        os.makedirs('reports/screenshots')

    # Generate timestamp for report
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f'reports/test_report_{timestamp}.html'

    # Run all tests with HTML report
    pytest.main([
        'tests/',
        f'--html={report_file}',
        '--self-contained-html',
        '-v'
    ])

if __name__ == '__main__':
    run_tests() 
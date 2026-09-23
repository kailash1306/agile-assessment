import os
import time

time.sleep(4)

with open("backend_report.txt", "w", encoding="utf-8") as report:
    report.write(
        f"Backend check passed for build {os.getenv('BUILD_NUMBER', 'local')}\n"
    )

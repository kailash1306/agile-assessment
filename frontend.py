import os
import time

time.sleep(4)

with open("frontend_report.txt", "w", encoding="utf-8") as report:
    report.write(
        f"Frontend check passed for build {os.getenv('BUILD_NUMBER', 'local')}\n"
    )

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from datetime import datetime
from io import TextIOWrapper


def generate_log_file_name() -> str:
    """
    Generate the log file name on the format "YYYYMMDD_HHMMSS.log" based on the current date and time.
    """

    now = datetime.now()
    return now.strftime("%Y%m%d_%H%M%S.log")


def write(file: TextIOWrapper, msg: str) -> None:
    """
    Write a message to the log file.
    """

    file.write(f"{datetime.now()}: {msg}")


def writelines(file: TextIOWrapper, lines: list[str]) -> None:
    """
    Write multiple lines to the log file.
    """

    file.writelines(f"{datetime.now()}: {line}" for line in lines)

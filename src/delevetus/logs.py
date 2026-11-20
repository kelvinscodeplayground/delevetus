# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from datetime import datetime


def generate_log_file_name() -> str:
    """
    Generate the log file name on the format "YYYYMMDD_HHMMSS.log" based on the current date and time.
    """

    now = datetime.now()
    return now.strftime("%Y%m%d_%H%M%S.log")

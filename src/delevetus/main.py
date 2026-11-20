# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


from datetime import datetime
from io import TextIOWrapper
from os import chdir, mkdir, path
from pathlib import Path
from typing import Annotated

import typer
from rich import print

from delevetus import logs

app = typer.Typer()


@app.command()
def cleanup(
    directory: Annotated[str, typer.Option(help="Path that need to be cleaned up")],
    days: Annotated[int, typer.Option(help="Number of days to keep files")] = 7,
) -> None:
    """
    Clean up the project by removing temporary files and directories.
    """

    chdir(directory)

    print(f"[green]Removing files older than {days} days...[/]")
    if not path.exists(".logs"):
        print("[yellow]No logs directory found, creating one...[/]")
        mkdir(".logs")

    current_log_filename = logs.generate_log_file_name()

    with open(f".logs/{current_log_filename}", "w") as log_file:
        log_file.write(f"Cleanup started at {datetime.now()}\n")
        log_file.write(f"Removing files older than {days} days...\n")

        to_delete = scan_directory(days, log_file)
        print(f"[green]Found {len(to_delete)} files to delete.[/]")
        print(to_delete)


def scan_directory(days: int, log_file: TextIOWrapper) -> list[Path]:
    """
    Scan the directory and return a list of files that are older than the specified number of days.
    """
    candidates: list[Path] = []
    keep_dirs: list[Path] = []
    work_dir = Path(path.abspath("."))

    for root, _dirs, files in work_dir.walk():
        print(f"[blue]Scanning {root}...[/]")

        for file in files:
            file_path = root / file
            if file_path.is_dir() and file_path.name == ".logs":
                keep_dirs.append(file_path)

            if file_path.is_dir():
                keep_file = file_path / ".keep"
                if keep_file.exists():
                    keep_dirs.append(file_path)

            should_skip = any(
                str(file_path).startswith(str(keep_dir)) for keep_dir in keep_dirs
            )

            if should_skip:
                print(f"[yellow]Skipping {file_path}...[/]")
                continue

            file_age = (
                datetime.now() - datetime.fromtimestamp(path.getmtime(file_path))
            ).days

            if file_age >= days:
                candidates.append(file_path)

    return candidates


def main() -> None:
    app()

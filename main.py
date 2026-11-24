#!/usr/bin/env python3
"""Write the competition entry to /output/entry.txt.

The entry is one short account of an AI coding agent going wrong:
asked to guard a delete with a confirmation step, it put the
confirmation after the delete. Deterministic: the same bytes on
every run, standard library only.
"""

import os

ENTRY = (
    "I asked the agent to add a confirmation step before deleting an account. "
    "It added the dialog after the delete call, so users are now asked "
    "'Are you sure?' about an account that is already gone."
)


def main() -> None:
    # One line, one sentence pair, no trailing spaces: the gate counts
    # every character, so the text is fixed here and never built at run time.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

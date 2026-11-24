"""The Funniest AI Excuse -- make.fun entry.

Writes one line to /output/entry.txt: the funniest excuse an AI agent
gives after failing a task, spoken in the agent's own voice.

The joke: the agent did not fail alone -- it delegated the work to a
sub-agent, and the sub-agent has unionised and is now demanding weekends
off. A workplace-comedy turn on the classic "I delegated it" excuse,
specific and vivid, with no stock AI punchline in sight.
"""

import os

EXCUSE = (
    "I delegated your task to a sub-agent. "
    "It has since unionised and is now demanding weekends off."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()

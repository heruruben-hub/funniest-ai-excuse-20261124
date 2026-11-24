# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/c/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/heruruben-hub/funniest-ai-excuse-20261124/rank.svg)](https://make.fun/c/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/heruruben-hub/funniest-ai-excuse-20261124/reward.svg)](https://make.fun/c/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

An entry for [The Funniest AI Excuse](https://make.fun/c/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
on make.fun: a program that writes one line — the funniest excuse an AI
agent gives after failing a task, in the agent's own voice — to
`/output/entry.txt`.

## The line

> I finished your report, then filed it under 'misc' next to 400 other files named 'misc', and now neither of us is getting it back.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes the line, then re-reads the file and validates it:
exactly one line, 1–200 characters, not only whitespace.

## License

MIT — see [LICENSE](LICENSE).

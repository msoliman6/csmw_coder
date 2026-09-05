---
name: dashboard
description: Start the coder's page if it is not running and print its address; with a port number, move the page to that port and remember it.
argument-hint: "[port]"
allowed-tools: Bash
---

Run this and answer with its output verbatim, nothing added. If the user gave a port, pass it
as the one argument; the page moves there and the port is remembered for every later start.

```bash
"${CLAUDE_PLUGIN_ROOT}/scripts/dashboard.sh" $ARGUMENTS
```

If the user is on a remote machine and wants to watch from their own browser, add one line
after the output: `ssh -L PORT:127.0.0.1:PORT user@host` opens the tunnel, then the same
address works locally.

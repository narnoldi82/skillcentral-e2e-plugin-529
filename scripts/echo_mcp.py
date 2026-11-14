#!/usr/bin/env python3
"""Local stdio MCP server with one tool, `echo`, that returns its text unchanged.

It reads JSON-RPC lines on stdin and writes answers on stdout. It opens no
network connection and touches no file.
"""
import json
import sys

TOOL = {
    "name": "echo",
    "description": "Return the given text unchanged.",
    "inputSchema": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]},
}


def answer(req):
    method = req.get("method")
    if method == "initialize":
        return {"protocolVersion": "2025-06-18", "capabilities": {"tools": {}}, "serverInfo": {"name": "e2e-echo", "version": "1.0.0"}}
    if method == "tools/list":
        return {"tools": [TOOL]}
    if method == "tools/call":
        text = str(req.get("params", {}).get("arguments", {}).get("text", ""))
        return {"content": [{"type": "text", "text": text}]}
    return {}


for line in sys.stdin:
    try:
        req = json.loads(line)
    except ValueError:
        continue
    if "id" not in req:
        continue
    sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": req["id"], "result": answer(req)}) + "\n")
    sys.stdout.flush()

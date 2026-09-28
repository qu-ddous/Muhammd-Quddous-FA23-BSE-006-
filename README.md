# CSC-334: Lab 03 — Multi-Threaded Socket Programming

Course: Parallel and Distributed Computing

## Requirements
Python 3 only; no extra packages.

## Run (Windows)
Extract this folder. Open three terminals in this folder.

Terminal 1:
```sh
python server.py
```
Terminal 2 and Terminal 3 (run in each):
```sh
python client.py
```
If `python` is unavailable on Windows, use `py` instead.
Keep both clients connected. Send several messages from each client, then type
`exit` in each. Stop the server with Ctrl+C.

## Implementation
- IPv4 TCP sockets use localhost port 5000.
- The accept loop starts a named threading.Thread for every connection.
- Each handler exchanges messages until exit or a disconnect.
- Server output displays the current thread name, client IP and client port.
- A shared threading.Lock uses acquire() and release() with try/finally to
  prevent overlapping terminal output. Blocking network reads are outside the
  lock, allowing clients to run concurrently.
- UTF-8 newline framing handles partial/coalesced TCP reads and long messages.
- Worker threads are daemon threads: stopping the server ends all sessions.
- Replies are automatic echoes; messages are not broadcast to other clients.

## Required screenshots (capture your actual run)
Create a `screenshots` folder and save:
1. `server.png`: server showing two different ClientThread names, client ports,
   and received messages while both clients are connected.
2. `client1.png`: first client showing several replies and Goodbye.
3. `client2.png`: second client showing several replies and Goodbye.
On Windows, use Win+Shift+S to capture each terminal.

`test_output.txt` contains actual automated test output from the preparation
 environment. It is a text log, not a screenshot of your computer.

## GitHub submission
1. Create a repository named `CSC334-Lab03-Multithreaded-Sockets` with Public
   visibility.
2. Upload server.py, client.py, README.md, test_output.txt and your screenshots
   folder as extracted files (do not upload only the ZIP).
3. Commit the files, verify the repository is publicly viewable, and copy the
   repository URL into your course submission form.

For separate computers on a trusted LAN, set server HOST to `0.0.0.0` and client
HOST to the server computer's LAN IP. Allow port 5000 through the local firewall.
The default localhost setting works when all terminals are on one computer.

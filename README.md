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


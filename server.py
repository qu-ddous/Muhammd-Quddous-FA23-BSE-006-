"""CSC-334 Lab 03: multi-threaded TCP echo server (Python 3)."""
import socket
import threading

HOST = '127.0.0.1'
PORT = 5000
print_lock = threading.Lock()


def log(message):
    # Keep each terminal output line intact across concurrent threads.
    print_lock.acquire()
    try:
        print(message, flush=True)
    finally:
        print_lock.release()


def handle_client(connection, address):
    ip, port = address
    name = threading.current_thread().name
    label = f'Thread: {name} | Client IP: {ip} | Port: {port}'
    log(f'[CONNECTED] {label}')
    try:
        with connection:
            # Newlines frame messages: TCP itself does not preserve messages.
            with connection.makefile('r', encoding='utf-8') as reader:
                for line in reader:
                    message = line.rstrip('\n')
                    log(f'[MESSAGE] {label} | {message}')
                    if message.strip().lower() == 'exit':
                        connection.sendall(b'Goodbye!\n')
                        break
                    reply = f'Server received: {message}\n'
                    connection.sendall(reply.encode('utf-8'))
    except (OSError, UnicodeError) as error:
        log(f'[ERROR] {label} | {error}')
    finally:
        log(f'[DISCONNECTED] {label}')


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(10)
        log(f'[LISTENING] {HOST}:{PORT} | Press Ctrl+C to stop.')
        client_number = 0
        try:
            while True:
                connection, address = server.accept()
                client_number += 1
                worker = threading.Thread(
                    target=handle_client,
                    args=(connection, address),
                    name=f'ClientThread-{client_number}',
                    daemon=True,
                )
                worker.start()
        except KeyboardInterrupt:
            log('[STOPPED] Server shutting down.')


if __name__ == '__main__':
    main()

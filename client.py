"""CSC-334 Lab 03: interactive TCP client (Python 3)."""
import socket


HOST = '127.0.0.1'
PORT = 5000


def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))
            print(f'Connected to {HOST}:{PORT}. Type exit to disconnect.', flush=True)
            with client.makefile('r', encoding='utf-8') as reader:
                while True:
                    try:
                        message = input('You: ')
                    except EOFError:
                        message = 'exit'
                    client.sendall((message + '\n').encode('utf-8'))
                    reply = reader.readline()
                    if not reply:
                        print('Server closed the connection.')
                        break
                    print(f'Server: {reply.rstrip()}', flush=True)
                    if message.strip().lower() == 'exit':
                        break
    except KeyboardInterrupt:
        print('\nClient stopped.')
    except (OSError, UnicodeError) as error:
        print(f'Connection error: {error}')


if __name__ == '__main__':
    main()

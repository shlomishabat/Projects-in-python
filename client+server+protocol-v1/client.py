
import socket
import protocol

imageSavePath='C:\screenClient.jpg'

def handle_server_response(my_socket, cmd, serverResponse):
    cmd = cmd.split(" ", 1)
    if cmd[0] == "SEND_PHOTO":
        with open(imageSavePath, 'w+b') as file:
            data = my_socket.recv(int(serverResponse))
            file.write(data)
            file.close()
            my_socket.recv(35).decode()
            print("the photo is in : 'C:'")
    else:
        print(serverResponse)





def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("127.0.0.1", 8888))

    print('Welcome to remote computer application. Available commands are:\n')
    print('TAKE_SCREENSHOT\nSEND_PHOTO\nDIR\nDELETE\nCOPY\nEXECUTE\nEXIT')
    # loop until user requested to exit
    while True:
        cmd = input("Please enter command:\n")
        try:
            if protocol.check_cmd(cmd):
                packet = protocol.create_msg(cmd)
                my_socket.send(packet.encode())
                length = my_socket.recv(4).decode()
                valid = protocol.get_msg(length)
                if valid:
                    serverResponse = my_socket.recv(int(length)).decode()
                    handle_server_response(my_socket, cmd, serverResponse)
                if serverResponse == "bay":
                    my_socket.close()
                    break
        except TypeError:
            print("invalid commend")
        except IndexError:
            print("invalid commend")


if __name__ == '__main__':
    main()
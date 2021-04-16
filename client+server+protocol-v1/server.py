
import socket
import protocol
import glob
import os
import shutil
import subprocess
import pyautogui



def check_client_request(cmd):
    try:
        cmd = cmd.split(" ", 1)
        commendsWparam = ["DIR", "DELETE", "EXECUTE", "COPY"]
        for i in commendsWparam:
            if cmd[0] == i:
                return True, cmd[0], cmd[1]
        commends = ["TAKE_SCREENSHOT", "SEND_PHOTO", "EXIT"]
        for i in commends:
            if cmd[0] == i:
                return True, cmd[0], "null"
        return False, "null", "null"
    except:
        print("invalid commend")
        return False, "null", "null"


def handle_client_request(command, params, client_socket):
    if command == "DIR":
        files = glob.glob(params + "\*.*")
        print(glob.glob(params))
        reply = "the dir contain :" + str(files)
        return reply
    elif command == "DELETE":
        os.remove(str(params))
        reply = "the file is delited" + params
        return reply
    elif command == "COPY":
        params = params.split(" ")
        if param_valid(params[0]) & param_valid(params[1]):
            shutil.copy(params[0], params[1])
            return "the operation done"
    elif command == "EXECUTE":
        valid = params.find(":")
        if valid > 0:
            params = r''+params+''
            print(params)
            subprocess.call([params], shell=True)
            return "the operation done"
    elif command == "TAKE_SCREENSHOT":
        image = pyautogui.screenshot()
        image.save(r'C:\screenServer.jpg')
        return "The server took a screenshot if you want to get the picture please enter - SEND_PHOTO "
    elif command == "SEND_PHOTO":
        filename='C:\screenServer.jpg'
        f = open(filename, 'rb')
        bytes = f.read()
        size = os.path.getsize(filename)
        size = str(size)
        client_socket.send(protocol.create_msg(size).encode())
        client_socket.sendall(bytes)
        f.close()
        print("photo sent")
        return "The server sent a screenshot"
    elif command == "EXIT":
        return "bay"


def param_valid(param):
    if ' ' in param:
        return False
    else:
        return True


def main():
    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", 8888))
    server_socket.listen()
    print("The server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client is connected")

    while True:
        length = client_socket.recv(4).decode()
        valid_protocol = protocol.get_msg(length)
        if valid_protocol:
            cmd = client_socket.recv(int(length)).decode()
            valid_cmd, command, params = check_client_request(cmd)
            if valid_cmd:
                reply = handle_client_request(command, params, client_socket)
                client_socket.send(protocol.create_msg(reply).encode())
                if command == "EXIT":
                    break

            else:
                # prepare proper error to client
                response = 'Bad command or parameters'
                client_socket.send(protocol.create_msg(response).encode())

        else:
            # prepare proper error to client
            response = 'Packet not according to protocol'
            client_socket.send(protocol.create_msg(response).encode())
            client_socket.recv(1024)

    # close sockets
    print("Closing connection")
    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()

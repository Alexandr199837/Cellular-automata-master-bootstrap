from app import *
from views import index

if __name__ == '__main__':
    socket.run(app, debug=True, host = '127.0.0.1', port = '5050')
    # 192.168.43.217 Кирилл
    # 192.168.1.100 Александр
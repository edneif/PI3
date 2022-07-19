# echo-client.py
import socket
import time
import psycopg2
import psycopg2.extras
import matplotlib.pyplot as plt
from datetime import datetime

DB_HOST = "127.0.0.1"
DB_NAME = "utilidades"
DB_USER = "postgres"
DB_PASS = "241500"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)


cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


cur.execute("SELECT MAX(ID) FROM ar_comprimido")
id = cur.fetchone()
id[0] = id[0] + 1

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST)


cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


cur.execute("SELECT MAX(ID) FROM ar_comprimido")
id = cur.fetchone()
id[0] += 1

valor = 5.6


# HOST = "192.168.0.111"  # The server's hostname or IP address
HOST = "10.1.1.120"  # The server's hostname or IP address
PORT = 7  # The port used by the server

data_atual = datetime.today()
data = data_atual.strftime("%Y%m%d%H%M%S")
n2 = data.encode()


while 1:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(n2)
        data = s.recv(1024)

    print(f"Received {data!r}")
    entrada = data.decode('utf-8')
    valor = entrada[0:2]  # valor adc0
    data = entrada[5:13]
    hora = entrada[16:27]

    cur.execute("INSERT INTO ar_comprimido(id,data,hora,valor,tipo,central) VALUES(%s,%s,%s,%s,0,0)",
                (id[0], data, hora, int(valor)/10))
    conn.commit()
    id[0] += 1
    count = cur.rowcount
    print(count, "Record inserted successfully into mobile table")

    data_atual = datetime.today()
    data = data_atual.strftime("%Y%m%d%H%M%S")
    n2 = data.encode()

    time.sleep(60)  # time em segundos

cur.close()
conn.close()

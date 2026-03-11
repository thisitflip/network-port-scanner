import socket

target = input("Digite o IP ou domínio: ")

print(f"\nEscaneando portas em {target}\n")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Porta {port} aberta")

    s.close()

print("\nScan finalizado.")

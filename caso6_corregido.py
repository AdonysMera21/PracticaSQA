#Andreina Arteaga Bazurto
#Adonys Ariel Mera
class User:
    def __init__(self, username):
        self.username = username
        self.messages = []

    def send_message(self, message, receiver):
        """Envia un mensaje a otro usuario."""
        receiver.receive_message(message, self)

    def receive_message(self, message, sender):
        """Recibe un mensaje de otro usuario y lo guarda en la lista de mensajes."""
        self.messages.append((sender.username, message))
        print(f"Nuevo mensaje de {sender.username}: {message}")

    def list_messages(self):
        """Lista todos los mensajes recibidos."""
        if self.messages:
            for sender, message in self.messages:
                print(f"{sender}: {message}")
        else:
            print("No hay mensajes.")

def main():
    users = {}

    while True:
        action = input("Seleccione una acción: 1. Crear usuario, 2. Enviar mensaje, 3. Listar mensajes, 4. Salir: ")

        if action == "1":
            username = input("Ingrese el nombre del usuario: ")
            if username in users:
                print("El usuario ya existe.")
            else:
                users[username] = User(username)
                print(f"Usuario {username} creado.")

        elif action == "2":
            sender_username = input("Ingrese el nombre del remitente: ")
            receiver_username = input("Ingrese el nombre del destinatario: ")
            if sender_username in users and receiver_username in users:
                message = input("Ingrese el mensaje: ")
                users[sender_username].send_message(message, users[receiver_username])
            else:
                print("Uno o ambos usuarios no existen.")

        elif action == "3":
            username = input("Ingrese el nombre del usuario: ")
            if username in users:
                print(f"Mensajes para {username}:")
                users[username].list_messages()
            else:
                print("El usuario no existe.")

        elif action == "4":
            break

        else:
            print("Acción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
import sys
from unicodedata import name
clients = [

  {
    'name': 'Pablo',
    'company': 'Google',
    'email': 'pablo@google.com',
    'position': 'Software engineer'
  },
  {
    'name': 'Ricardo',
    'company': 'Facebook',
    'email': 'ricardo@facebook.com',
    'position': 'Data engineer'
  }
]

def create_client(client_name):
  global clients
  if client_name not in clients:
    clients.append(client_name)
  else:
    print('Client already is in the client\'s list')

def list_clients():
  for index, client in enumerate(clients):
    print('{uid} | {name} | {company} | {email} | {position}'.format(
      uid = index,
      name=client['name'],
      company=client['company'],
      email = client['email'],
      position=client['position']
    ))

def update_client(clientName, field, value):
  global clients
  for index, client in enumerate(clients):
    if client["name"] == clientName:
      print(f'index is {index}')
      clients[index][field] = value
    else:
      continue

"""   if client_name in clients:
    index = clients.index(client_name)
    clients[index]=updated_client_name
  else:
    print('Client is not in clien\'s list') """

def delete_client(client_name):
  global clients
  if client_name in clients:
    clients.remove(client_name)
  else:
    print('Client is not in clients list')


def search_client(client_name):
  for client in clients:
    if client != client_name:
      continue
    else:
      return True

def _print_welcome():
  print('WELCOME TO PLATZI VENTAS')
  print('*'*50)
  print('What would you like to do today?')
  print('[C]reate client')
  print('[L]ist clients')
  print('[U]pdate client')
  print('[D]elete client')
  print('[S]earch Client')

def _get_client_field(field_name):
  field = None
  while not field:
    field = input(f'What is the client {field_name}')
  return field

def _get_client_name():
  client_name = None
  while not client_name:
    client_name = input('What is the client name?')
    if client_name == 'exit':
      client_name = None
      break
  if not client_name:
    sys.exit()
  return client_name


if __name__ == '__main__':
  _print_welcome()
  command = input()
  command = command.upper()

  if command == 'C':
    client = {
      'name': _get_client_field('name'),
      'company': _get_client_field('company'),
      'email': _get_client_field('email'),
      'position': _get_client_field('position')
    }
    create_client(client)
    list_clients()
  elif command == 'L':
    list_clients()
  elif command == 'D':
    client_name = _get_client_name()
    delete_client(client_name)
    list_clients()
  elif command == 'U':
    client_name = _get_client_name()
    field = input('What field would you liek to change? ')
    value = input('What is the client value you would like to change? ')
    update_client(client_name, field, value)
  elif command == 'S':
    client_name = _get_client_name()
    found = search_client(client_name)

    if found:
      print('The client is in the client\'s list')
    else:
      print('The client: {} is not in our client\'s list'.format(client_name))
  else:
    print('Invalid command')
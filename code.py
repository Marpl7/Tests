documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(doc_number):

    name = ([docs['name'] for docs in documents if doc_number == docs['number']])
    if not name:
        return False
    else:
        return name[0]


def shelf(doc_number):

    shelf = ([shelf for shelf, docs in directories.items() if doc_number in docs])
    if not shelf:
        return False
    else:
        return shelf[0]


def list_docs():

    return documents


def add(doc_number, doc_type, doc_name, shelf_number):

    docs_to_add = {'type': doc_type, 'number': doc_number, 'name': doc_name}
    if docs_to_add['number'] in [doc['number'] for doc in documents]:
        return False
    elif shelf_number not in directories.keys():
        return False
    else:
        directories[shelf_number].append(doc_number)
        documents.append(docs_to_add)
        return True


def delete(doc_number):

    shelf = ([shelf for shelf, docs in directories.items() if doc_number in docs])
    if not shelf:
        return False
    else:
        directories[shelf[0]].remove(doc_number)
        [documents.remove(doc) for doc in documents if doc_number == doc['number']]
        return True


def move(doc_number, shelf_number):

    current_shelf = ([shelf for shelf, docs in directories.items() if doc_number in docs])
    if not current_shelf:
        return False
    elif shelf_number not in directories.keys():
        return False
    elif current_shelf[0] == shelf_number:
        return False
    else:
        directories[shelf_number].append(doc_number)
        directories[current_shelf[0]].remove(doc_number)
        return True


def add_shelf(shelf_number):

    if shelf_number in directories.keys():
        return False
    else:
        directories[shelf_number] = []
        return True


from collections import deque # double ended queue

grath = {}
grath['you'] = ['alice', 'bob', 'claire']
grath["bob"] = ["anuj", "peggy"]
grath["alice"] = ["peggy"]
grath["claire"] = ["thom", "jonny"]
grath["anuj"] = []
grath["peggy"] = []
grath["thom"] = []
grath["jonny"] = []


def seller_person(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += grath[name]
    verify = []
    while search_queue:
        person = search_queue.popleft()
        if not person in verify:
            if seller_person(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += grath[person]
                verify.append(person)
    return False

search('you')
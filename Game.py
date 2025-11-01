def show_status():
    print('---------------')
    print(f'You are in the {current_room}')
    if inventory:
        print('Inventory:', ', '.join(inventory))
    else:
        print('Inventory: (empty)')
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print('---------------')


rooms = {
    'kitchen': {'east': 'living_room', 'item': 'flashlight'},
    'living_room': {'north': 'library', 'south': 'dining_room', 'west': 'kitchen','east':'bedroom','item': 'cell_phone'},
    'bedroom': {'north': 'bathroom', 'west': 'living_room', 'item': 'house_key'},
    'bathroom': {'south': 'bedroom', 'item': 'evil step mom'},
    'dining_room': {'north': 'living_room', 'east': 'garden', 'item': 'remote'},
    'den': {'west': 'library', 'item': 'diary'},
    'library': {'south': 'living_room', 'east': 'den', 'item': 'snack'},
    'garden': {'west': 'dining_room', 'item': 'photos'}
}

current_room = 'kitchen'
inventory = []

while True:
    show_status()
    if "item" in rooms[current_room]:
        item_name = rooms[current_room]['item']
        pick = input(f"Do you want to pick up the {item_name}? (yes/no): ").strip().lower()
        if pick == 'yes':
            inventory.append(item_name.lower())
            print(f'You picked up the {item_name}!')
            del rooms[current_room]['item']

        # Win condition
        if set(inventory) == {'flashlight', 'cell_phone', 'house_key', 'remote', 'diary', 'snack', 'photos'}:
            print('You gathered all the items and escaped the Evil Step Mom’s house. YOU WIN!')
            break

    move = input('Enter your move (north/south/east/west or quit): ').lower().strip()

    if not move:
        print('Please enter a direction.')
        continue

    if move == 'quit':
        print('Thanks for playing!')
        break


    if move in ['north', 'south', 'east', 'west']:
        if move in rooms[current_room]:
            current_room = rooms[current_room][move]
            if 'item' in rooms[current_room] and rooms[current_room]['item'].lower() == 'evil step mom':
                print('Oh no! The Evil Step Mom caught you! GAME OVER!')
                break
        else:
            print("You can’t go that way!")
    else:
        print("Invalid command. Type a direction or 'quit' to exit.")

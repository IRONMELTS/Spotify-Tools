import random

song_queue=[]

while True:
    command_name=input("Command name: ")
    if command_name.lower().startswith("add"):
        command_enter=command_name
        count=0
        song=("")
        for x in command_name:
            count+=1
            if count<5:
                False
            else:
                song=(f"{song}{x}")
        song_name=song
        song_queue.append(song_name)
        print(f'"{song_name}" has been added to queue.')
    if command_name.lower()=="add_":
        while True:
            song_name=input("Enter name of song: ")
            if song_name.lower()=="__kill__":
                break
            else: 
                song_queue.append(song_name)
                print(f'"{song_name}" has been added to queue.')
    if command_name.lower()=="clear":
        print(f"{len(song_queue)} songs has been cleared.")
        song_queue.clear()
    if command_name.lower()=="len":
        print(f"There are {len(song_queue)} songs in queue.")
    if command_name.lower()=="list":
        if len(song_queue)==0:
            print("There are no songs in queue.")
        if len(song_queue)==1:
            print(f"The songs in queue are:\n{len(song_queue)}.) {song_queue[0]}")
        if len(song_queue)>1:
            song_print=""
            song_number=0
            for x in song_queue:
                song_number+=1
                if song_print.lower()=="":
                    song_print=(f"{song_number}.) {x}")
                else:
                    song_print=(f"{song_print}\n{song_number}.) {x}")
            print(f"The songs in queue are:\n{song_print}")
    if command_name.lower()=="__kill__":
        break
    if command_name.lower()=="shuffle":
        if len(song_queue)==0:
            print("There are no songs in queue.")
        if len(song_queue)==1:
            print(f"There should be more than 1 song in queue.")
        else:
            random.shuffle(song_queue)
            print("Queue has been shuffled.")
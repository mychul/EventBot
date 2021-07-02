import json

def create_server_events(guildID):
# Initial command to create an empty event file, needs to be called once per server by the admin.
    server_events = {}

    with open(f'./server_data/{guildID}.json', 'w') as fileOut:
        json.dump(server_events, fileOut, indent=2)

def load_server_event(guildID):
# This is to retrieve the JSON file that has all the events in a particular server.
    with open(f'./server_data/{guildID}.json', 'w') as fileIn:
        return json.load(fileIn)

def save_server_event(guildID, server_events):
# This is to save the JSON file for all the events in a particular server.
    with open(f'./server_data/{guildID}.json', 'w') as fileOut:
        json.dump(server_events, fileOut, indent=2)

async def add_server_event(guildID, discordID, title, date, time, desc, members):
# This is going to be the funtion in pair with the ,host command that we wanted for the bot. Things to keep in mind are that should be able to .update the dictionary and possible check if there is already a file that has their guildID in it. Therefore there should be no need for a called once create_sever_events as a bot command.
    return
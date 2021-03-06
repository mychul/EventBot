import json
import os

dirPath = os.getcwd()

async def create_server_events(guildID):
# Initial command to create an empty event file, needs to be called once per server by the admin.
    serverEvents = {
        'Event Counter': 0,
        'BASE': {
            'Owner':'discordID',
            'Title':'title',
            'Date': 'date',
            'Time': 'time',
            'Desc':'desc',
            'Members':'[discordID]'
        }
    }

    save_server_event(guildID, serverEvents)

def load_server_event(guildID):
# This is to retrieve the JSON file that has all the events in a particular server.
    with open(f'{dirPath}/server_data/{guildID}.json', 'r') as fileIn:
        serverEvents = json.load(fileIn)
        return serverEvents

def save_server_event(guildID, serverEvents):
# This is to save the JSON file for all the events in a particular server.
    with open(f'{dirPath}/server_data/{guildID}.json', 'w') as fileOut:
        json.dump(serverEvents, fileOut, indent=2)

async def add_server_event(guildID, discordID, title, date, time, desc):
# This is going to be the funtion in pair with the ,host command that we wanted for the bot. Things to keep in mind are that should be able to .update the dictionary and possible check if there is already a file that has their guildID in it. Therefore there should be no need for a called once create_sever_events as a bot command.
    serverEvents = load_server_event(guildID)
    # print(serverEvents)
    # print('server event loaded')
    if 'BASE' in serverEvents:
        del serverEvents['BASE']
        # print('BASE found and deleted from Server Events')

    serverEvents['Event Counter'] = int(serverEvents['Event Counter'])+1
    
    newEvents = {
        serverEvents['Event Counter']: {
            'Owner':discordID,
            'Title':title,
            'Date':date,
            'Time':time,
            'Desc':desc,
            'Members':[discordID]
        }
    }
    # print(newEvents)
    serverEvents.update(newEvents)
    # print('server event updated')
    save_server_event(guildID,serverEvents)
    # print('server event saved')

async def display_events(guildID):
    serverEvents = load_server_event(guildID=guildID)
    return serverEvents

async def join_server_event(guildID, discordID, eventID):
    eventID = str(eventID)
    serverEvents = load_server_event(guildID)
    serverEvents[eventID]['Members'].append(discordID)
    save_server_event(guildID, serverEvents)
    return

async def join_server_event_check(guildID, discordID, eventID):
    eventID = str(eventID)
    serverEvents = load_server_event(guildID)
    # print(serverEvents)
    # print(f'{eventID}, {type(eventID)}')
    # print(type(serverEvents[eventID]['Members']))
    checker = discordID in serverEvents[eventID]['Members']
    # print(checker)
    return checker

async def cancel_server_event(guildID, eventID):
    eventID = str(eventID)
    serverEvents = load_server_event(guildID)
    serverEvents.pop(eventID)
    save_server_event(guildID,serverEvents)
    return

async def check_event_owner(guildID, discordID, eventID):
    eventID = str(eventID)
    serverEvents = load_server_event(guildID)
    if serverEvents[eventID]["Owner"] == discordID:
        return True
    else:
        return False

async def leave_server_event(guildID, discordID, eventID):
    eventID = str(eventID)
    serverEvents = load_server_event(guildID)
    serverEvents[eventID]['Members'].remove(discordID)
    save_server_event(guildID, serverEvents)
    return

async def remove_event_member(guildID, discordID, eventID):
    eventID = str(eventID)
    serverEvents = load_server_event(guildID)
    serverEvents[eventID]['Members'].remove(int(discordID))
    save_server_event(guildID, serverEvents)
    return

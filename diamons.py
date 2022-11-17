import subprocess, requests, time, os, re, traceback, random, logging, telethon, colorama, csv, json, configparser
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest
import subprocess, requests, time, os, re, traceback, random, logging, telethon, colorama, csv, json, configparser
import subprocess, requests, time, os, re, traceback, random, logging, telethon, colorama, csv, json, configparser
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest

from csv import reader

#from test import *
from datetime import MINYEAR, datetime, timedelta


from colorama import Fore, Back, Style, init


from telethon.sync import TelegramClient


from telethon import functions, types, TelegramClient, connection, sync, utils, errors


from telethon.tl.types import InputPeerEmpty, UserStatusOffline, UserStatusRecently, UserStatusLastMonth, UserStatusLastWeek, PeerUser, PeerChannel, InputPeerChannel, InputPeerUser


from telethon.tl.functions.contacts import GetContactsRequest, DeleteContactsRequest


from telethon.tl.functions.photos import DeletePhotosRequest


from telethon.tl.functions.messages import GetDialogsRequest, ImportChatInviteRequest


from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest


from telethon.errors import SessionPasswordNeededError


from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError, YouBlockedUserError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError


from telethon.sessions import StringSession


# In the same way, you can also leave such channel
from telethon.tl.functions.channels import LeaveChannelRequest

from scraper_online import *

import subprocess, requests, time, os, re, traceback, random, logging, telethon, colorama, csv, json, configparser
from telethon.tl.functions.photos import UploadProfilePhotoRequest


from csv import reader


from datetime import MINYEAR, datetime, timedelta


from colorama import Fore, Back, Style, init


from telethon.sync import TelegramClient


from telethon import functions, types, TelegramClient, connection, sync, utils, errors
from telethon import *

from telethon.tl.types import InputPeerEmpty, UserStatusOffline, UserStatusRecently, UserStatusLastMonth, UserStatusLastWeek, PeerUser, PeerChannel, InputPeerChannel, InputPeerUser


from telethon.tl.functions.contacts import GetContactsRequest, DeleteContactsRequest


from telethon.tl.functions.photos import DeletePhotosRequest


from telethon.tl.functions.messages import GetDialogsRequest, ImportChatInviteRequest


from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest
#GetMessagesViewsRequest

from telethon.errors import SessionPasswordNeededError


from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError, YouBlockedUserError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError


#from telethon.tl.functions.channels import GetMessagesViewsRequest
#from telethon.tl.types import GetMessagesViewsRequest
from telethon.sync import TelegramClient
from telethon import functions, types

from telethon.tl.functions.messages import GetMessagesViewsRequest
# You need both
from telethon.sessions import StringSession
from telethon import TelegramClient
import telethon
from telethon import *
from csv import reader

#from test import *
from datetime import MINYEAR, datetime, timedelta


from colorama import Fore, Back, Style, init


from telethon.sync import TelegramClient


from telethon import functions, types, TelegramClient, connection, sync, utils, errors


from telethon.tl.types import InputPeerEmpty, UserStatusOffline, UserStatusRecently, UserStatusLastMonth, UserStatusLastWeek, PeerUser, PeerChannel, InputPeerChannel, InputPeerUser


from telethon.tl.functions.contacts import GetContactsRequest, DeleteContactsRequest


from telethon.tl.functions.photos import DeletePhotosRequest


from telethon.tl.functions.messages import GetDialogsRequest, ImportChatInviteRequest


from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, InviteToChannelRequest


from telethon.errors import SessionPasswordNeededError


from telethon.errors.rpcerrorlist import UsernameInvalidError, ChannelInvalidError, PhoneNumberBannedError, YouBlockedUserError, PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError


from telethon.sessions import StringSession


# In the same way, you can also leave such channel
from telethon.tl.functions.channels import LeaveChannelRequest

from scraper_online import *




channelxd = "https://t.me/THANOS_PRO"
groupxd = "thanosprosss"
ye = Fore.YELLOW
API_ID = 16746680
chatop = 777000

HashID = 'd038e172eb99839b69c39c3c25cd98cf'





re="\033[1;31m"


gr="\033[1;32m"


cy="\033[1;36m"


wi="\033[1,35m"





if not os.path.exists('./sessions'):


    os.mkdir('./sessions')


if not os.path.exists('phone.csv'):


    open("phone.csv","w")











def login():
    banner()
    with open('phone.csv', 'r')as f:


        str_list = [row[0] for row in csv.reader(f)]


        po = 0


        for pphone in str_list:


            phone = utils.parse_phone(pphone)


            po += 1





            print(Style.BRIGHT + Fore.GREEN + f"Login {phone}")


            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)


            client.start(phone)
            client(JoinChannelRequest(channelxd))


            client.disconnect()


            print()


        done = True


    print(Style.BRIGHT + Fore.RESET + 'All Number added Done !' if done else "Error!")


    print(Style.BRIGHT + Fore.YELLOW + 'Press enter to back')


    input()

def BanFilter():





    api_id = int(API_ID)


    api_hash = str(HashID)


    MadeByTHANOS_PRO = []





    done = False


    with open('phone.csv', 'r') as f:


        str_list = [row[0] for row in csv.reader(f)]





        po = 0


        for unparsed_phone in str_list:


            po += 1





            phone = utils.parse_phone(unparsed_phone)





            print(f"Login {phone}")


            client = TelegramClient(f"sessions/{phone}", api_id, api_hash)


            # client.start(phone)


            client.connect()


            if not client.is_user_authorized():


                try:


                    print('This Phone Has Been Revoked')


                    THANOS_PRO = str(po)


                    Nero_op = str(unparsed_phone)


                    MadeByTHANOS_PRO.append(Nero_op)


                    continue





                except PhoneNumberBannedError:


                    print('Ban')


                    THANOS_PRO = str(po)


                    Nero_op = str(unparsed_phone)


                    MadeByTHANOS_PRO.append(Nero_op)





                    continue





            # client.disconnect()


            print()


        done = True


        print('List Of Banned Numbers')


        print(*MadeByTHANOS_PRO, sep='\n')


        print('Saved In BanNumers.csv')


        with open('BanNumbers.csv', 'w', encoding='UTF-8') as writeFile:


            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")





            writer.writerows(MadeByTHANOS_PRO)








    def autoremove():








        collection = []


        nc = []


        collection1 = []


        nc1 = []


        maind = []





        with open("phone.csv", "r") as infile:


            for line in infile:


                collection.append(line)





        for x in collection:


            mod_x = str(x).replace("\n", "")


            nc.append(mod_x)





        with open("BanNumbers.csv") as infile, open("outfile.csv", "w") as outfile:


            for line in infile:


                outfile.write(line.replace(",", ""))





        with open("outfile.csv", "r") as outfile:


            for line1 in outfile:


                collection1.append(line1)





        for i in collection1:


            mod_i = str(i).replace("\n", "")


            nc1.append(mod_i)





        unique = set(nc)


        unique1 = set(nc1)





        itd = unique.intersection(unique1)





        for x in nc:


            if x not in itd:


                maind.append(x)





        with open('unban.csv', 'w', encoding='UTF-8') as writeFile:


            writer = csv.writer(writeFile, lineterminator="\n")


            writer.writerows(maind)





        with open("unban.csv") as last, open("phone.csv", "w") as final:


            for line3 in last:


                mod_i = str(line3).replace("\n", "")


                final.write(mod_i)





        os.remove("phone.csv")


        os.rename("unban.csv", "phone.csv")


        print("Done,All Banned Number Have Been Removed")
def Scraper():


    config = configparser.ConfigParser()


    config.read("config.ini")


    link1 = (config['THANOS_PRO']['FromGroup']).strip()


    links = link1.split(',')


    phone = (config['THANOS_PRO']['PhoneNumber']).strip()


    logging.basicConfig(level=logging.WARNING)





    print(Style.BRIGHT + Fore.RESET + f'\nLogging For {phone}')


    try:


        client = TelegramClient(f"sessions/{phone}", API_ID, HashID)


        client.connect()


        if client.is_user_authorized():


            print(Style.BRIGHT + Fore.GREEN + f'login Done')


            count = 1


            today = datetime.now()


            last_week = today + timedelta(days=-7)


            last_month = today + timedelta(days=-30)


            f = open("data.csv", "w", encoding='UTF-8')


            writer = csv.writer(f, delimiter=",", lineterminator="\n")


            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])


            try:


                for link in links:


                    try:


                        client(JoinChannelRequest(link))


                    except Exception as e:


                        pass


                    print(Style.BRIGHT + Fore.YELLOW + f'Scrabing Members from {link} group.....')


                    all_participants = []


                    try:


                        all_participants = client.iter_participants(link, aggressive=True)


                    except Exception as e:


                        # print(e)


                        pass


                    for user in all_participants:


                        if user.username:


                            username = user.username


                        else:


                            username = ""


                        if user.first_name:


                            name = user.first_name


                        else:


                            name = "THANOS_PRO"


                        if isinstance(user.status, UserStatusRecently):


                            date_online = today


                        else:


                            if isinstance(user.status, UserStatusLastMonth):


                                date_online = last_month


                            if isinstance(user.status, UserStatusLastWeek):


                                date_online = last_week


                            if isinstance(user.status, UserStatusOffline):


                                date_online = user.status.was_online


                        date_online_str = date_online.strftime("%Y%m%d")


                        writer.writerow([count, username, user.id, name, link, date_online_str])


                        count = count + 1


            except Exception as e:


                # print(1,e)


                pass


            f.close()


            print('Count : ', count)


        else:


            print(Style.BRIGHT + Fore.RED + f'login fail {phone}')


    except Exception as e:


        print(Style.BRIGHT + Fore.RED + f'login fail')





    # Filter by usname start from here


    lines = list()








    def main():


        lines = list()


        with open('data.csv', 'r', encoding='UTF-8') as readFile:





            reader = csv.reader(readFile)





            for row in reader:





                lines.append(row)





                for field in row:





                    if field == '':


                        lines.remove(row)


        with open('1.csv', 'w', encoding='UTF-8') as writeFile:


            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")





            writer.writerows(lines)








    def main1():


        lines = list()


        with open('1.csv', 'r', encoding='UTF-8') as readFile:





            reader = csv.reader(readFile)





            for row in reader:





                lines.append(row)





                for field in row:





                    if field == 'username':


                        lines.remove(row)





        with open('2.csv', 'w', encoding='UTF-8') as writeFile:


            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")





            writer.writerows(lines)








    main()


    main1()





    with open("2.csv", "r", encoding='UTF-8') as source:


        rdr = csv.reader(source)





        with open("data.csv", "w", encoding='UTF-8') as f:


            writer = csv.writer(f, delimiter=",", lineterminator="\n")


            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])


            i = 0


            for row in rdr:


                i += 1


                writer.writerow((i, row[1], row[2], row[3], row[4], row[5]))





    os.remove("1.csv")


    os.remove("2.csv")


    # os.remove("data.csv")


    print(Style.BRIGHT + Fore.GREEN + "Task completed")


    print(Style.BRIGHT + Fore.RESET + "Enter any key to exit")


    input()

def AdderForPhone():





    init()


    r = Fore.LIGHTRED_EX


    gr = Fore.GREEN


    n = Fore.RESET


    bl = Fore.BLUE


    ye = Fore.YELLOW








    config = configparser.ConfigParser()


    config.read("config.ini")


    grouplink = config['THANOS_PRO']['ToGroup']


    groupid = config['THANOS_PRO']['GroupID']


    stopnum = config['THANOS_PRO']['EnterStop']


    stacno = config['THANOS_PRO']['StartingAccount']


    endacno = config['THANOS_PRO']['EndAccount']





    phone = []





    with open('phone.csv', 'r') as delta_obj:


        csv_reader = reader(delta_obj)


        list_of_phone = tuple(csv_reader)


        for phone_ in list_of_phone:


            phone.append(int(phone_[0]))


    pphone = phone





    print(f'{gr}Total account: {n} {r}{str(len(phone))}{n}')












    def autos():


        print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')


        THANOS_PRO_dev = int(input())


        THANOS_PRO = 'data.csv'


        rexlink = str(grouplink)


        id = int(groupid)


        From = int(stacno) - 1


        Upto = int(endacno)


        rex = int(1)


        hacks = int(50) - 1


        stop = int(stopnum)





        with open('memory.csv', 'w', encoding='UTF-8') as file:


            writer = csv.writer(file, delimiter=",", lineterminator="\n")


            writer.writerow([rex, rex + hacks])


        a = 0


        indexx = 0


        for xd in pphone[From:Upto]:


            indexx += 1


            print(f'Index : {indexx}')


            phone = utils.parse_phone(xd)


            print(f"Login {phone}")


            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)


            client.connect()


            if not client.is_user_authorized():


                print(f'{r}some thing has changed{n}')


                client.send_code_request(phone)


                client.sign_in(phone, input('Enter the code: '))





            input_file = THANOS_PRO


            users = []


            with open(input_file, encoding='UTF-8') as f:


                rows = csv.reader(f, delimiter=",", lineterminator="\n")


                next(rows, None)


                for row in rows:


                    user = {}


                    user['srno'] = row[0]


                    user['username'] = row[1]


                    user['id'] = int(row[2])


                    # user['access_hash'] = int(row[2])


                    user['name'] = row[3]


                    users.append(user)





            with open('memory.csv', 'r') as hash_obj:





                csv_reader = reader(hash_obj)





                list_of_rows = list(csv_reader)


                row_number = 1


                col_number = 1


                numnext = list_of_rows[row_number - 1][col_number - 1]





            startfrom = int(numnext)


            nextstart = startfrom + hacks





            with open('memory.csv', 'r') as hash_obj:


                csv_reader = reader(hash_obj)


                list_of_rows = list(csv_reader)


                row_number = 1


                col_number = 2


                numend = list_of_rows[row_number - 1][col_number - 1]





            endto = int(numend)


            nextend = endto + hacks





            with open("memory.csv", "w", encoding='UTF-8') as df:  # Enter your file name.





                writer = csv.writer(df, delimiter=",", lineterminator="\n")





                writer.writerow([nextstart, nextend])





            client(JoinChannelRequest(rexlink))


            time.sleep(5)


            channel = client.get_input_entity(PeerChannel(id))


            channelinfo = client(GetFullChannelRequest(channel=channel))





            rexprodeltanoob = int(channelinfo.full_chat.participants_count)


            print(f'Members: {rexprodeltanoob}')


            if rexprodeltanoob >= stop:


                print(f'The Goal Of {stop} Has Been Completed')


                input()


                quit()





            it = 0


            for user in users:


                if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):


                    try:


                        it += 1


                        if user['username'] == "":


                            print(f"{r}no username, moving to next{n}")


                            continue





                        client(functions.channels.InviteToChannelRequest(rexlink, [user['username']]))


                        print(f'{it} - done')


                        time.sleep(THANOS_PRO_dev)








                    except ChatWriteForbiddenError as cwfe:


                        client(JoinChannelRequest(rexlink))


                        time.sleep(5)


                        continue











                    except errors.RPCError as e:


                        status = e.__class__.__name__


                        print(f'{it} - {status}')

















                    except:


                        traceback.print_exc()


                        print(f"{ye}Unexpected Error{n}")


                        continue





            a += 1


        os.remove("memory.csv")








    def private():


        print(Style.BRIGHT + Fore.GREEN + 'Enter Delay Time Per Request 0 For None : ')


        THANOS_PRO_dev = int(input())


        THANOS_PRO = 'data.csv'


        rexlink = str(grouplink)


        id = int(groupid)


        From = int(stacno) - 1


        Upto = int(endacno)


        rex = int(1)


        hacks = int(50) - 1


        stop =int(stopnum)


        with open('memory.csv', 'w', encoding='UTF-8') as file:


            writer = csv.writer(file, delimiter=",", lineterminator="\n")


            writer.writerow([rex, rex + hacks])


        a = 0


        indexx = 0


        for xd in pphone[From:Upto]:


            indexx += 1


            print(f'Index : {indexx}')


            phone = utils.parse_phone(xd)


            print(f"Login {phone}")


            client = TelegramClient(f"sessions/{phone}", API_ID, HashID)


            client.connect()


            if not client.is_user_authorized():


                print(f'{r}some thing has changed{n}')


                client.send_code_request(phone)


                client.sign_in(phone, input('Enter the code: '))





            input_file = THANOS_PRO


            users = []


            with open(input_file, encoding='UTF-8') as f:


                rows = csv.reader(f, delimiter=",", lineterminator="\n")


                next(rows, None)


                for row in rows:


                    user = {}


                    user['srno'] = row[0]


                    user['username'] = row[1]


                    user['id'] = int(row[2])


                    # user['access_hash'] = int(row[2])


                    user['name'] = row[3]


                    users.append(user)





            with open('memory.csv', 'r') as hash_obj:





                csv_reader = reader(hash_obj)





                list_of_rows = list(csv_reader)


                row_number = 1


                col_number = 1


                numnext = list_of_rows[row_number - 1][col_number - 1]





            startfrom = int(numnext)


            nextstart = startfrom + hacks





            with open('memory.csv', 'r') as hash_obj:


                csv_reader = reader(hash_obj)


                list_of_rows = list(csv_reader)


                row_number = 1


                col_number = 2


                numend = list_of_rows[row_number - 1][col_number - 1]





            endto = int(numend)


            nextend = endto + hacks





            with open("memory.csv", "w", encoding='UTF-8') as df:  # Enter your file name.





                writer = csv.writer(df, delimiter=",", lineterminator="\n")





                writer.writerow([nextstart, nextend])





            client(ImportChatInviteRequest(rexlink))


            time.sleep(5)


            channel = client.get_input_entity(PeerChannel(id))


            channelinfo = client(GetFullChannelRequest(channel=channel))


            rexprodeltanoob = int(channelinfo.full_chat.participants_count)


            print(f'Members: {rexprodeltanoob}')


            if rexprodeltanoob >= stop:


                print(f'The Goal Of {stop} Has Been Completed')


                input()


                quit()





            it = 0


            for user in users:


                if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):


                    print(f'Members: {rexprodeltanoob}')


                    try:


                        it += 1


                        if user['username'] == "":


                            print(f"{r}no username, moving to next{n}")


                            continue





                        client(functions.channels.InviteToChannelRequest(rexlink, [user['username']]))


                        print(f'{it} - done')





                        time.sleep(THANOS_PRO_dev)





                    except ChatWriteForbiddenError as cwfe:


                        client(ImportChatInviteRequest(rexlink))


                        time.sleep(5)


                        continue











                    except errors.RPCError as e:


                        status = e.__class__.__name__





                        print(f'{it} - {status}')

















                    except:


                        traceback.print_exc()


                        print(f"{ye}Unexpected Error{n}")


                        continue





            a += 1


        os.remove("memory.csv")








    rexchoose = str(input(f'{bl}Press Y if group is private else N : {n}'))


    if rexchoose == 'Y':


        private()


    elif rexchoose == 'N':


        autos()
def DeleteALreadyMembers():





    logging.basicConfig(level=logging.WARNING)





    config = configparser.ConfigParser()


    config.read("config.ini")


    link = (config['THANOS_PRO']['ToGroup']).strip()


    phone = (config['THANOS_PRO']['PhoneNumber']).strip()





    #with open('data.csv', 'r' , encoding='utf-8') as f:


    #     existing_numbers = f.read().split('\n')


    #     print(type(existing_numbers))


    #     exit()





    with open('data.csv', 'r', encoding='utf-8') as f:


        users1 = csv.reader(f)


        users = [i for i in users1]





    with open('data.csv', 'r', encoding='utf-8') as f:


        users1 = csv.reader(f)


        userlist = [str(i[2]) for i in users1]





    client = TelegramClient(f"sessions/{phone}", API_ID, HashID)


    client.connect()


    if not client.is_user_authorized():


        print(f'\nLogin fail, for number {phone} need Login first\n')


    else:


        chats = []


        last_date = None


        chunk_size = 200


        groups = []


        n = 0


        while n != -1:


            try:


                group = client.get_entity(link)


                if group.megagroup == True:


                    group_id = str(group.id)


                    all_participants = client.iter_participants(group, aggressive=False)


                    results = []


                    results1 = []


                    count = 0


                    index1 = []


                    for user in all_participants:


                        try:


                            if str(user.id) in userlist:


                                index1.append(userlist.index(str(user.id)))


                        except:


                            print("Error get user")


                    f.close()


                    client.disconnect()


                    index1.sort(reverse=True)


                    for i in index1:


                        del users[i]


                    with open('data.csv', 'w', encoding="utf-8", newline='') as f:


                        write = csv.writer(f)


                        write.writerows(users)


                    n = -1


                else:


                    print(Style.BRIGHT + Fore.RED + "\nInvalid Group..\n")


                n = -1


            except telethon.errors.rpcerrorlist.ChatWriteForbiddenError:


                client(JoinChannelRequest(link))


            except ValueError:


                print(Style.BRIGHT + Fore.GREEN + "\nOnly Public Group Allowed..\n")


                n = -1


            except:


                print(Style.BRIGHT + Fore.RED + "\nInvalid Group....\n")


                n = -1


    # Filter by usname start from here


    lines = list()








    def main():


        lines = list()


        with open('data.csv', 'r', encoding='UTF-8') as readFile:





            reader = csv.reader(readFile)





            for row in reader:





                lines.append(row)





                for field in row:





                    if field == '':


                        lines.remove(row)


        with open('1.csv', 'w', encoding='UTF-8') as writeFile:


            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")





            writer.writerows(lines)








    def main1():


        lines = list()


        with open('1.csv', 'r', encoding='UTF-8') as readFile:





            reader = csv.reader(readFile)





            for row in reader:





                lines.append(row)





                for field in row:





                    if field == 'username':


                        lines.remove(row)





        with open('2.csv', 'w', encoding='UTF-8') as writeFile:


            writer = csv.writer(writeFile, delimiter=",", lineterminator="\n")





            writer.writerows(lines)








    main()


    main1()





    with open("2.csv", "r", encoding='UTF-8') as source:


        rdr = csv.reader(source)





        with open("data.csv", "w", encoding='UTF-8') as f:


            writer = csv.writer(f, delimiter=",", lineterminator="\n")


            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'group', 'Status'])


            i = 0


            for row in rdr:


                i += 1


                writer.writerow((i, row[1], row[2], row[3], row[4], row[5]))





    os.remove("1.csv")


    os.remove("2.csv")


    # os.remove("data.csv")





    print(Style.BRIGHT + Fore.RESET + "Already Member Deleted Done !")


    print(Style.BRIGHT + Fore.GREEN + 'Task Completed')


    print(Style.BRIGHT + Fore.YELLOW + "press enter to exit")


    input()
def Viewotp():
	   banner()
	   with open('phone.csv', 'r')as f:
	   	str_list = [row[0] for row in csv.reader(f)]
	   	po = 0 
	   	for pphone in str_list:
	   		phone = utils.parse_phone(pphone)
	   		po += 1
	   		print(cy+ f"Getting Telegram message Otp {phone}")
	   		client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
	   		client.start(phone)
	   		messages = client.get_messages(chatop)
	   		print(ye+ f"{messages[0].text}")
	
def Viewotps(): #bio changing plugins 
	   banner()
	   bios = input("ENTER BIO")
	   with open('phone.csv', 'r')as f:
	   	str_list = [row[0] for row in csv.reader(f)]
	   	po = 0 
	   	for pphone in str_list:
	   		phone = utils.parse_phone(pphone)
	   		po += 1
	   		print(cy+ f"WAIT CHANGING BIO {phone}")
	   		client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
	   		client.start(phone)
	   		client(UpdateProfileRequest(about=bios))
	   		print("done")

def Viewotpss(): #bio changing plugins 
	   banner()
	   bios = input("ENTER NEW PASSWORD")
	   with open('phone.csv', 'r')as f:
	   	str_list = [row[0] for row in csv.reader(f)]
	   	po = 0 
	   	for pphone in str_list:
	   		phone = utils.parse_phone(pphone)
	   		po += 1
	   		print(cy+ f"WAIT PROCESSING {phone}")
	   		client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
	   		client.start(phone)
	   		client.edit_2fa(new_password=bios)
	   		print("done")

def firstnamechange(): #bio changing plugins 
	   banner()
	   fname = input("ENTER FIRST NAME")
	   #lname = input("ENTER LAST NAME")
	   with open('phone.csv', 'r')as f:
	   	str_list = [row[0] for row in csv.reader(f)]
	   	po = 0 
	   	for pphone in str_list:
	   		phone = utils.parse_phone(pphone)
	   		po += 1
	   		print(cy+ f"WAIT CHANGING FIRST NAME {phone}")
	   		client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
	   		client.start(phone)
	   		client(UpdateProfileRequest(first_name=fname))
	           #client(UpdateProfileRequest(last_name=lname))
	   		print("done")
	
def Lastnamechange(): #bio changing plugins 
	   banner()
	   fname = input("ENTER LAST NAME")
	   #lname = input("ENTER LAST NAME")
	   with open('phone.csv', 'r')as f:
	   	str_list = [row[0] for row in csv.reader(f)]
	   	po = 0 
	   	for pphone in str_list:
	   		phone = utils.parse_phone(pphone)
	   		po += 1
	   		print(cy+ f"WAIT CHANGING LAST NAME {phone}")
	   		client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
	   		client.start(phone)
	   		client(UpdateProfileRequest(last_name=fname))
	           #client(UpdateProfileRequest(last_name=lname))
	   		print("done")
def Joingroup(): #bio changing plugins 
	   banner()
	   grouplink = input("ENTER GROUP LINK")
	  # lname = input("ENTER LAST NAME")
	   with open('phone.csv', 'r')as f:
	   	str_list = [row[0] for row in csv.reader(f)]
	   	po = 0 
	   	for pphone in str_list:
	   		phone = utils.parse_phone(pphone)
	   		po += 1
	   		print(cy+ f"WAIT JOINING GROUP {phone}")
	   		client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
	   		client.start(phone)
	   		client(JoinChannelRequest(grouplink))
	           #client(UpdateProfileRequest(last_name=lname))
	   		print("done")
	   		
	   		
def leavgrousp(): #bio changing plugins 
	   banner()
	   grouplink = input("ENTER GROUP LINK")
	  # lname = input("ENTER LAST NAME")
	   with open('phone.csv', 'r')as f:
	   	str_list = [row[0] for row in csv.reader(f)]
	   	po = 0 
	   	for pphone in str_list:
	   		phone = utils.parse_phone(pphone)
	   		po += 1
	   		print(cy+ f"WAIT LEAVING GROUP {phone}")
	   		client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
	   		client.start(phone)
	   		client(LeaveChannelRequest(grouplink))
	           #client(UpdateProfileRequest(last_name=lname))
	   		print("done")
	
def Leavegroup(): #bio changing plugins 
	   banner()
	   #channel = input("ENTER link")
	  # lname = input("ENTER LAST NAME")
	   with open('phone.csv', 'r')as f:
	   	str_list = [row[0] for row in csv.reader(f)]
	   	po = 0 
	   	for pphone in str_list:
	   		phone = utils.parse_phone(pphone)
	   		po += 1
	   		print(cy+ f"WAIT CHANGING PIC {phone}")
	   		client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
	   		client.start(phone)
	   		client(UploadProfilePhotoRequest(
               client.upload_file('main.jpg')))
	           #client(UpdateProfileRequest(last_name=lname))
	   		print("done")
def Viewincrease(): #bio changing plugins 
	   banner()
	   channel = input("ENTER LINK")
	   ids = int(input("ENTER MESSAGE ID"))
	   with open('phone.csv', 'r')as f:
	   	str_list = [row[0] for row in csv.reader(f)]
	   	po = 0 
	   	for pphone in str_list:
	   		phone = utils.parse_phone(pphone)
	   		po += 1
	   		print(cy+ f"WAIT  {phone}")
	   		client = TelegramClient(f"sessions/{phone}", API_ID, HashID)
	   		client.start(phone)
	   		client(GetMessagesViewsRequest(
    peer=channel,
    id=[ids],
    increment=True
))
	           #client(UpdateProfileRequest(last_name=lname))
	   		print("done")
	
def updated():
	print('Checking for updates...')
	try:
		version = requests.get('https://raw.githubusercontent.com/rishabhhotmail/Diamon/main/version.txt')
	except:
		print(' You are not connected to the internet')
        print('Please connect to the internet and retry')
        exit()

	if float(version.text) > 1.1:
		prompt = str(input(f'[~] Update available[Version {version.text}]. Download?[y/n]: '))
		if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
			print('Downloading updates...')
			if os.name == 'nt':
				os.system('del diamond.py')
			else:
				os.system('rm diamond.py')
				
			os.system('curl -l -O https://raw.githubusercontent.com/rishabhhotmail/Diamon/main/diamon.py')
			print(f'[*] Updated to version: {version.text}')
			input('Press enter to exit...')
			exit()
		else:
			print('[!] Update aborted.')
			input('Press enter to goto main menu...')
	else:
		print(f'{lg}[i] Your thanos is already up to date')
        input('Press enter to goto main menu...')
	
def banner():
    os.system('clear')
    print(re+ """  
    

██████╗░██╗░█████╗░███╗░░░███╗░█████╗░███╗░░██╗
██╔══██╗██║██╔══██╗████╗░████║██╔══██╗████╗░██║
██║░░██║██║███████║██╔████╔██║██║░░██║██╔██╗██║
██║░░██║██║██╔══██║██║╚██╔╝██║██║░░██║██║╚████║
██████╔╝██║██║░░██║██║░╚═╝░██║╚█████╔╝██║░╚███║
╚═════╝░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝
   """)

## importing socket module
import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
import requests
re = requests.get('https://ipinfo.io/').text
#print(re)
co = re.split('"ip": "')[1]
cou = co.split('"')[0]

	
def main_menu():


    banner()

    
	#print(cou)
    print(" OWNER - @thanosceo ")
    print(ye+'ꜱᴇʟᴇᴄᴛᴇ ᴀ ᴏᴘᴛɪᴏɴ')

    print(cy+'╭────⇌ᴅɢᴀᴅᴅᴇʀ⇋────')
    print(cy+'◈┈˃‌ <1> ʟᴏɢɪɴ')


    print(cy+'◈┈˃‌ <2> ʙᴀɴꜰɪʟᴛᴇʀ')


    #print(cy+'            [3] spambotcheaker + remover')


    #print(cy+'           # [3] Scraper')


    print(cy+'◈┈˃‌ <3> ᴅᴇʟᴇᴛᴇ ᴀʟʀᴇᴀᴅʏ ᴍᴇᴍʙᴇʀ')


    print(cy+'◈┈˃‌ <4> ᴠɪᴇᴡ ᴛᴇʟᴇɢʀᴀᴍ ᴏᴛᴘ')
    

    #print(cy+'            [7] Deletealreadynumbers')


    #print(cy+'            [8] set profile')


    #print(cy+'            [9] delete profile')


    #print(ye+'Contact Adder Option:')


    #print(cy+'            [10] Autoaddcontact - For Phone')


    #print(cy+'            [11] Deletecontact  ')


    #print(cy+'            [12] Bulk Adder')


    #print(cy+'            [13] SingleAdder')


    #print(ye+'Additional Adder options')


    #print(cy+'            [14] Adder')


    print(cy+'◈┈˃‌ <5> ᴀᴅᴅᴇʀ  ')
    print(cy+'◈┈˃‌ <6> ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ')
    print(cy+'◈┈˃‌ <7> ᴄʜᴀɴɢᴇ ꜰɪʀꜱᴛ ɴᴀᴍᴇ')
    print(cy+'◈┈˃‌ <8> ꜱᴇᴛ 2ꜱᴛᴇᴘ ᴘᴀꜱꜱᴡᴏʀᴅ')
    print(cy+'◈┈˃‌ <9> ꜱᴇᴛ ʙɪᴏ')
    print(cy+'◈┈˃‌ <10>ᴄʜᴀɴɢᴇ ʟᴀꜱᴛ ɴᴀᴍᴇ')
    print(cy+'◈┈˃‌ <11>ᴊᴏɪɴ ɢʀᴏᴜᴘ')
    print(cy+'◈┈˃‌ <12>ꜱᴇᴛ ᴘʀᴏꜰɪʟᴇ ᴘɪᴄ')
    #print(cy+'            [16] Multiple adder')
    

    #print(ye+'Additional Options:')


    #print(cy+'            [17] Send Message')

    print(cy+'◈┈˃‌ <13>ᴏɴʟɪɴᴇ ꜱᴄʀᴀᴘᴇʀ')
    print(cy+'◈┈˃‌ <14>ᴘᴏꜱᴛ ᴠɪᴇᴡ ɪɴᴄʀᴇᴀꜱᴇʀ')
    print(cy+'◈┈˃‌ <15> ꜱʜᴜᴛᴅᴏᴡɴ')
    print(cy+'╰────⇌ᴅɢᴀᴅᴅᴇʀ⇋────')


    a = int(input('\nᴇɴᴛᴇʀ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ -->  '))


    if a==1:


        login()


    elif a==2:


        BanFilter()


    elif a==113:


        Scraper()

    elif a==11:


        Joingroup()    
    
    elif a==6:


        leavgrousp()    
        
    elif a==12:


        Leavegroup()    

    elif a==13:
    	onscraper()

    elif a==5:


        AdderForPhone()
    elif a ==3:
        DeleteALreadyMembers()


    elif a==4:
    	Viewotp()
    elif a==15:
    	updated()
    
    elif a==7:
    	firstnamechange()

    elif a==8:
    	Viewotpss()
    elif a==9:
    	Viewotps()
    
    elif a==10:
    	Lastnamechange()
 
    elif a==14:

        Viewincrease()
    elif a==15:

        quit()

#if cou == "157.42.241.173":
	
main_menu()



	
"""else:
	print(cou)
	print("    ur ip not activated ")
	print("    Contact @thanosceo")
	print("    and buy diamond software")"""


        



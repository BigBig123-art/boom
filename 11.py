# -*- coding: utf-8 -*-

from Saibot.linepy import *
from Saibot.akad.ttypes import Message
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from Saibot.akad.ttypes import ContentType as Type
from Saibot.akad.ttypes import ChatRoomAnnouncementContents
from Saibot.akad.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from gtts import gTTS
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from wikiapi import WikiApi
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


cl = LINE('')
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))


lineProfile = cl.getProfile()
mid = cl.getProfile().mid

oepoll = OEPoll(cl)
call = cl
creator = ["ud15ef5f9e63555fc09fc41a1a9b22a3f","uf14f6dd93c4b9f008de857c418eeae1b"]
owner = ["ud15ef5f9e63555fc09fc41a1a9b22a3f","uf14f6dd93c4b9f008de857c418eeae1b"]
admin = ["ud15ef5f9e63555fc09fc41a1a9b22a3f","uf14f6dd93c4b9f008de857c418eeae1b"]
staff = ["ud15ef5f9e63555fc09fc41a1a9b22a3f","uf14f6dd93c4b9f008de857c418eeae1b"]
#==============================================================================
lineProfile = cl.getProfile()
mid = cl.getProfile().mid

KAC = [cl]
Bots = [mid]
Saints = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)
#===============================================================================
protectcancel = []
welcome = []
targets = []
protectname = []
userTemp = {}
userKicked = []
dict = {}
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
warmode = []
ghost = []
offbot = []
msg_image={}
msg_video={}
msg_sticker={}
detectUnsend = []
simisimi = []
message = []
#===============================================================================
settings = {
    "autoBlock": False,
    "autoRead": False,
    "autolike": False,
    "com": False,
    "postId": [],
    "commet": "auto like by : sai",
    "postEndUrl": False,
    "checkPost": False,
    "welcome": False,
    "leave": False,
    "mid": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": False,
    "checkPost": False,
    "setKey": "",
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":False,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 2,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "postId": [],
    "staff":{},
    "dhenza":{},
    "likeOn": False,
    "Timeline": False,
    "invite":False,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "contact":False,
    "downos":False,
    'autoJoin':True,
    'autoAdd':False,
    'autoCancel':{"on":True, "members":3},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "MentionKick":False,
    "welcomeOn":False,
    "sticker":False,  
    "selfbot":True,
    "mention":"",
    "Respontag":"",
    "welcome":"",
    "comment":"",
    "comment1":"",
    "message":""
}

protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "protect":[],
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
dzProfile = cl.getProfile()
myProfile["displayName"] = dzProfile.displayName
myProfile["statusMessage"] = dzProfile.statusMessage
myProfile["pictureStatus"] = dzProfile.pictureStatus

    
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
unsendOpen = codecs.open("unsend.json","r","utf-8")
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)
unsend = json.load(unsendOpen)
mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

#-------------------------------======Flex&Liff=======------------------------------------------------#
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Saibot  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getContact("ubd78f3da598d3c32e075e062e88545ec").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1646816542-yz70BWBz', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1646816542-yz70BWBz', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1646816542-yz70BWBz', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def bcTemplate2(friend, data):
    xyz = LiffChatContext(friend)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1646816542-yz70BWBz', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendCarousel(to, data):
    data = json.dumps(data)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1646816542-yz70BWBz', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=data, headers=headers)
def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1646816542-yz70BWBz', xyzz)
    token = cl.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)

def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1646816542-yz70BWBz', xyzz)
    token = cl.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def ClonerV2(to):
    try:
        contact = cl.getContact(to)
        profile = cl.profile
        profileName = cl.profile
        profileStatus = cl.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        cl.updateProfile(profileName)
        cl.updateProfile(profileStatus)
        profile.pictureStatus = cl.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if cl.getProfileCoverId(to) is not None:
            cl.updateProfileCoverById(cl.getProfileCoverId(to))
        cl.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return cl.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        cl.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
#------------------------------=======จบFlex&Liff=======------------------------------------------------#
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
 

        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendLineMusic(to):
    contentMetadata = {
        'countryCode': 'ID',
        'i-installUrl': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'a-packageName': 'com.spotify.music',
        'linkUri': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'type': 'mt',
        'previewUrl':"http://dl.profile.line-cdn.net/{}".format(cl.profile.pictureStatus),
        'a-linkUri': "http://line.me/ti/p/{}".format(cl.getUserTicket().id),
        'text': cl.profile.displayName,
        'id': 'mt000000000a6b79f9',
        'subText': cl.profile.statusMessage
    }
    return cl.sendMessage(to, cl.profile.displayName, contentMetadata, 19)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d ว̶ั̶น̶ %02d ช̶ม̶.̶ %02d น̶า̶ท̶ี̶ %02d ว̶ิ̶น̶า̶ท̶ี̶' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d ว̶ั̶น̶ %02d ช̶ม̶.̶ %02d น̶า̶ท̶ี̶ %02d ว̶ิ̶น̶า̶ท̶ี̶' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
                        
def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        userid = "https://line.me/ti/p/~" + cl.profile.userid
                        cl.sendFooter(tmp, "Spam is over , Now Bots Actived !", str(userid), "http://dl.profile.line-cdn.net/"+cl.getContact(mid).pictureStatus, line.getContact(mid).displayName)
                    except Exception as error:
                        logError(error)
                        
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
                        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
    
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def backupProfile():
    profile = cl.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = cl.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
    
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "จำนวนการแท็ค {}  คน\n\n╔━━━━[•B̶o̶t̶ ̶N̶o̶N̶a̶m̶e̶ ̶O̶S̶M̶ ̶1̶.̶1̶.̶2̶ •]━━\n╠❂➣✏1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠❂➣✏%i.  " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ •B̶o̶t̶ ̶N̶o̶N̶a̶m̶e̶ ̶O̶S̶M̶ ̶1̶.̶1̶.̶2̶ • ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print(error)

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nช̶ื̶̶่อ̶ก̶ล̶̶̶ุ่ม̶ "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2019,3,18)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\nJam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nGroup : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nxpired : In "+hari+"\nVersion : Sempak Bot\nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        ki.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kk.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention3(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kc.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention4(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        km.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention5(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        kb.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention6(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        sw.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention7(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        dz.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")      

              

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd

def help():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = """•B̶o̶t̶ ̶N̶o̶N̶a̶m̶e̶ ̶O̶S̶M̶ ̶1̶.̶1̶.̶2̶ •

✭sai
✭รูปโปรวิดีโอ
✭การตูน
✭me
✭#me
✭me1
✭ค้นหายูทูป [คำค้นหา]
✭ประกาศ [ไส่คำ/ไอดีไลน์]
✭@@
✭on
✭off
✭เชคค่า
✭คท
✭ไอดี
✭bot
✭ไอดี @
✭ดึงหมด @
✭คท @
✭ลบแชท
✭รีบูท
✭ออน
✭ข้อมูลกลุ่ม
✭เพื่อน
✭รายการบล็อค
✭เวอร์ชั่น
✭ลิ้ง
✭กลุ่ม
✭ลิ้งปิด
✭ลิ้งเปิด
✭/ลบรัน
✭เปลี่ยนรูปกลุ่ม
✭อัพโปร
✭ชื่อ [ไส่ชื่อ]
✭แทค
✭บอท
✭เชคแอด
✭ออกละ
✭ออก [ชื่อห้อง]
✭ทดสอบ
✭sp
✭แอบเปิด
✭แอบปิด
✭Idline [ไส่ไอดีไลน์]
✭ทักทายเปิด
✭ทักทายปิด
✭คลิ้ก @
✭เตะดึง @
✭เตะ @
✭เตะดำ @
✭ตั้งแอด @
✭เพิ่มคทแอด [ส่งคทที่เพิ่มแอดมิน]
✭ลบคทแอด [ส่งคทที่ลบแอดมิน]
✭หยุดการเพิ่ม [พิมทุกครั้งหลังจากเพิ่มแอดมินละ]
✭คทแอด
✭คทแอด2
✭เชคคทเปิด
✭เชคคทปิด
✭แอดเปิด
✭แอดปิด
✭เข้าเปิด
✭เข้าปิด
✭บล็อคเปิด
✭บล็อคปิด
✭มุดลิ้งเปิด
✭มุดลิ้งปิด
✭ดำ @
✭ขาว @
✭ดำ [ส่งคทที่เพิ่มบชดำ]
✭ขาว [ส่งคทที่เพิ่มบชขาว]
✭บชดำ @
✭บชขาว @
✭บชดำ [ส่งคทที่เพิ่มบชดำ]
✭บชขาว [ส่งคทที่เพิ่มบชขาว]
✭เชคบชดำ
✭เชคดำ
✭คทบชดำ
✭คทดำ
✭ตั้งทักทาย [ข้อความ]
✭ตั้งคนแอด [ข้อคงาม]
✭ตั้งอ่าน [ข้อความ]
✭เชคทักทาย
✭เชคคนแอด
✭เชคตั้งอ่าน

"""
    return helpMessage

def helpbot():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "เทสระบบ2"
    return helpMessage2
    
def helpbot1():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "เทสระบบ3"
    return helpMessage3
    
def helpbot2():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = "เทสระบบ4"
    return helpMessage4

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoBlock"] == True:
                cl.blockContact(op.param1)
        if op.type == 5:
            print ("[ 5 ] Add Contact")
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)                           

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)	
#====================================================================                           
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        pass
                                                    
                return                                       
#====================================================================
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                                                    
                return                                
#====================================================================                            
        if op.type == 19:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                                                    
                return                      
#====================================================================                                
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
             
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoBlock"] == True:
                if op.param2 not in Bots and op.param2 not in admin:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])
                        

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param3 in Bots:
                    if op.param2 not in Bots and op.param2 not in Team:
                        wait["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in wait["blacklist"]:
                                cl.findAndAddContactsByMid(op.param1)
                                cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

#====================================================================                            
        if op.type == 19:
            if op.param1 in protect["proall"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    if op.param3 in wait["blacklist"]:
                        pass
                    else:
                        cl.findAndAddContactsByMid(op.param3)                       
                        wait["blacklist"][op.param2] = True

            if op.param1 in protect["protect"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                elif op.param2 in Bots:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
 
                if op.param3 in owner:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in admin:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in staff:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in staff:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True              
            # except:
                # pass
#===================================================================================================   
  
        if op.type in [25, 26]:           
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != mid: to = sender
                else: to = receiver
                if receiver in temp_flood:
                    if temp_flood[receiver]["expire"] == True:
                        if cmd == "open" and sender == mid:
                            temp_flood[receiver]["expire"] = False
                            temp_flood[receiver]["time"] = time.time()
                            cl.sendMessage(to, "Bot kembali aktif")
                        return
                    elif time.time() - temp_flood[receiver]["time"] <= 1:
                        temp_flood[receiver]["flood"] += 1
                        if temp_flood[receiver]["flood"] >= 20:
                            temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["expire"] = True
                            ret_ = " {}".format(setKey)
                            cl.sendMessage(to, str(ret_))
                    else:
                         temp_flood[receiver]["flood"] = 0
                         temp_flood[receiver]["time"] = time.time()
                else:
                    temp_flood[receiver] = {
    	                "time": time.time(),
    	                "flood": 0,
    	                "expire": False
                    }             
#===================================================================================================        
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)
                        cl.sendMessage(op.param1, None, contentMetadata={"STKID":"13162615","STKPKGID":"1326453","STKVER":"1"}, contentType=7)
                                                                     
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\nSticker Info"
                   ret_ += "\nSticker ID : {}".format(stk_id)
                   ret_ += "\nSticker Version : {}".format(stk_ver)
                   ret_ += "\nSticker Package : {}".format(pkg_id)
                   ret_ += "\nSticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                   if msg._from in wait["blacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if msg.contentType == 16:
                   if msg.toType in [2,1,0]:
                       print ("AutoLikeCommat")
                       try:
                           if settings["autolike"] == True:
                               purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                               if purl[1] not in wait['postId']:
                                   cl.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                               if settings["com"] == True:
                                   cl.createComment(purl[0], purl[1], settings["commet"])
                                   wait['postId'].append(purl[1])
                               else:
                                   pass
                       except Exception as e:
                               if settings["autolike"] == True:
                                   purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                                   if purl[1] not in wait['postId']:
                                       cl.likePost(msg._from, purl[1], random.choice([1001,1002,1003,1004,1005]))
                                   if settings["com"] == True:
                                       cl.createComment(msg._from, purl[1], settings["commet"])
                                       wait['postId'].append(purl[1])
                                   else:pass
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           saints = cl.getContact(msg._from)
                           sendMention(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"PRDID":"a0768339-c2d3-4189-9653-2909e9bb6f58","PRDTYPE":"THEME","MSGTPL":"6"}, contentType=9)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["MentionKick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           cl.sendMessage(msg.to, "Done Tag Me !")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
        
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"ร̶ะ̶บ̶บ̶เ̶ช̶็̶ค̶I̶D̶ส̶ต̶ิ̶̶๊ก̶เ̶ก̶อ̶ร̶์̶\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"ช̶ื̶̶่อ̶ : " + msg.contentMetadata["displayName"] + "\nʍ̶ɨ̶ɖ̶ : " + msg.contentMetadata["mid"] + "\nส̶เ̶ต̶ต̶ั̶ส̶ : " + contact.statusMessage + "\nล̶ิ̶̶้ง̶ค̶์̶ร̶̶ูป̶ : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"   ร̶ะ̶บ̶บ̶เ̶ช̶็̶ค̶ค̶ท̶\nช̶ื̶̶่อ̶ " + msg.contentMetadata["displayName"] + "\nʍ̶ɨ̶ɖ̶ " + msg.contentMetadata["mid"] + "\nส̶เ̶ต̶ต̶ั̶ส̶ " + contact.statusMessage + "\nล̶ิ̶̶้ง̶ค̶์̶ร̶̶ูป̶โ̶ป̶ร̶ http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            cl.sendMessage(msg.to, "ก̶ร̶̶ุณ̶า̶ต̶ิ̶ด̶ต̶̶่อ̶ผ̶̶̶ู้ด̶̶ูแ̶ล̶ะ̶ร̶ะ̶บ̶บ̶")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "\nช̶ื̶̶่อ̶ "
                                  ret_ = "OK"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  cl.sendText(msg.to,"ค̶̶ุณ̶ม̶ี̶ข̶ี̶ด̶ ̶จ̶ำ̶ก̶ั̶ด̶")
                                  wait["invite"] = False
                                  break
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["AddstickerTag"]["status"] == True:
                         settings["AddstickerTag"]["sid"] = msg.contentMetadata["STKID"]
                         settings["AddstickerTag"]["spkg"] = msg.contentMetadata["STKPKGID"]
                         cl.sendMessage(msg.to, "ส̶̶่ง̶ส̶ต̶ิ̶̶้ก̶เ̶ก̶อ̶ร̶์̶")
                         settings["AddstickerTag"]["status"] = False
                         
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            cl.sendMessage(msg.to,"ส̶̶่ง̶ร̶̶ูป̶ภ̶า̶พ̶")

               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                      print ("Read")
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                          if msg._from in mid:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in mid:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in mid:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in mid:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Sเ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶ล̶ะ̶")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"ไ̶ม̶̶่พ̶บ̶")

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "เ̶ป̶ล̶ี̶̶่ย̶น̶ร̶̶ูป̶ก̶ล̶̶̶ุ่ม̶ส̶ำ̶เ̶ร̶็̶จ̶แ̶ล̶̶้ว̶")
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = cl.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     cl.updateProfilePicture(path1)
                     cl.sendMessage(msg.to, "เ̶ป̶ล̶ี̶̶่ย̶น̶ร̶̶ูป̶โ̶ป̶ร̶เ̶ส̶ร̶็̶จ̶ล̶ะ̶")
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "คำสั่ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                        elif cmd == "sai":
                          if msg._from in admin:
                            gifnya = ['https://stickershop.line-scdn.net/stickershop/v1/sticker/114872844/ANDROID/sticker.png;compress=true']
                            data = {
                                "type": "template",
                                "altText": "ѕєℓƒвσт ву.ѕαι",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~appbotline"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd == "รูปโปรวิดีโอ":
                          # if msg._from in admin:
                            contact = cl.getContact(sender)
                            data = {
                                "type": "video",
                                "originalContentUrl": "https://rest.farzain.com/api/tiktok.php?apikey=fn",
                                "previewImageUrl": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                }
                            sendTemplate(to, data)
                        elif cmd == "การตูน":
                          if msg._from in admin:
                            gifnya = ['https://thumbs.gfycat.com/AngelicCloudyJaeger-size_restricted.gif','https://thumbs.gfycat.com/AgedZealousBlackfootedferret-size_restricted.gif','https://thumbs.gfycat.com/FondHastyChinesecrocodilelizard-size_restricted.gif','https://thumbs.gfycat.com/LividCrazyDipper-size_restricted.gif','https://thumbs.gfycat.com/LoathsomeDevotedGossamerwingedbutterfly-size_restricted.gif','https://thumbs.gfycat.com/SamePhysicalHarrierhawk-size_restricted.gif','https://thumbs.gfycat.com/ColorlessPinkLangur-size_restricted.gif','https://thumbs.gfycat.com/ThoseBitesizedBrahmanbull-size_restricted.gif','https://thumbs.gfycat.com/FakeSlowBengaltiger-size_restricted.gif','https://thumbs.gfycat.com/TanSpitefulChupacabra-size_restricted.gif']
                            data = {
                                "type": "template",
                                "altText": "ѕєℓƒвσт ву.ѕαι",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl": "{}".format(random.choice(gifnya)),
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~appbotline"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd == "#me":
                          if msg._from in admin:
                            contact = cl.getContact(mid)
                            LINKFOTO = "https://os.line.naver.jp/os/p/" + mid
                            LINKVIDEO = "https://os.line.naver.jp/os/p/" + mid + "/vp"
                            data = {
                                "type": "flex",
                                "altText": "{} ѕєℓƒвσт ву.ѕαι".format(cl.getProfile().displayName),
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#333333'
                                            },
                                            "body": {
                                                "backgroundColor": '#333333'
                                            },
                                            "footer": {
                                                "backgroundColor": '#333333'
                                            },
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~appbotline"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "margin": "lg",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "Nama",
                                                                    "color": "#aaaaaa",
                                                                    "size": "sm",
                                                                    "flex": 1
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "{}".format(contact.displayName),
                                                                    "color": "#666666",
                                                                    "size": "sm",
                                                                    "flex": 5
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "Mid",
                                                                    "color": "#aaaaaa",
                                                                    "size": "sm",
                                                                    "flex": 1
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "{}".format(contact.mid),
                                                                    "color": "#666666",
                                                                    "size": "sm",
                                                                    "flex": 5
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "Bio",
                                                                    "color": "#aaaaaa",
                                                                    "size": "sm",
                                                                    "flex": 1
                                                                },
                                                                {
                                                                    "type": "text",
                                                                    "text": "{}".format(contact.statusMessage),
                                                                    "color": "#666666",
                                                                    "wrap": True,
                                                                    "size": "sm",
                                                                    "flex": 5
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "button",
                                                    "style": "link",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Message Creator",
                                                        "uri": "line://ti/p/~appbotline"
                                                    }                                                   
                                                },
                                                {
                                                    "type": "spacer",
                                                    "size": "sm",
                                                }
                                            ],
                                            "flex": 0
                                        }
                                    }
                                }
                            sendTemplate(to, data)
                        elif cmd == "me1":
                          if msg._from in admin:
                            contact = cl.getContact(mid)
                            LINKFOTO = "https://os.line.naver.jp/os/p/" + mid
                            LINKVIDEO = "https://os.line.naver.jp/os/p/" + mid + "/vp"
                            data = {
                                "type": "flex",
                                "altText": "{} ѕєℓƒвσт ву.ѕαι".format(cl.getProfile().displayName),   #ส่วนที่1คือชื่อ
                                "contents": {
                                    "type": "bubble",
                                        'styles': {
                                            "header": {
                                                "backgroundColor": '#333333'
                                            },
                                            "body": {
                                                "backgroundColor": '#333333'
                                            },
                                            "footer": {
                                                "backgroundColor": '#333333'
                                            },
                                        },
                                    "header": {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(contact.displayName),
                                                "weight": "bold",
                                                "color": "#FFFFFF",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),  #ส่วนรุปโปรฟาย
                                        "size": "full",
                                        "aspectRatio": "1:1",
                                        "aspectMode": "fit",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://nv/profilePopup/mid=ubd78f3da598d3c32e075e062e88545ec"
                                        }
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "ชื่อคุณ   :",
                                                                "color": "#FFFFFF",
                                                                "size": "sm",
                                                                "flex": 1
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "{}".format(contact.displayName),  #ส่วนชื่อ
                                                                "color": "#FFFFFF",
                                                                "size": "sm",
                                                                "flex": 2
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "สเตตัสคุณ  :",
                                                                "color": "#FFFFFF",
                                                                "size": "sm",
                                                                "flex": 3
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "{}".format(contact.statusMessage),  #ส่วนสเตตัส
                                                                "color": "#FFFFFF",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 4
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "MyProfile",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=video&ocu={}&piu={}".format(LINKVIDEO,LINKFOTO)
                                                }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 5
                                    }
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd.startswith("ค้นหายูทูป"):
                          if msg._from in admin:
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#ffffff"
                                            },
                                            "body": {
                                               "backgroundColor": "#ffffff",
                                               "separator": True,
                                               "separatorColor": "#000000"
                                            },
                                            "footer": {
                                                "backgroundColor": "#ffffff",
                                                "separator": True,
                                               "separatorColor": "#000000"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                                    "type": "text",
                                                    "text": "ค้นหายูทูป",
                                                    "weight": "bold",
                                                    "color": "#1C1C1C",
                                                    "size": "sm"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=ubd78f3da598d3c32e075e062e88545ec"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    # "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    "url": "https://img.live/images/2018/12/28/-1.png",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#000000"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "Title",
                                                    "color": "#000000",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#000000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#000000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#000000",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "type": "flex",
                                        "altText": "Youtube",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                    }
                                    sendTemplate(to, data)

                        elif msg.text.lower().startswith("ประกาศ"):
                            if msg._from in admin:
                                    delcmd = msg.text.split(" ")
                                    get = msg.text.replace(delcmd[0]+" ","").split("/")
                                    kw = get[0]
                                    ans = get[1]
                                    groups = cl.getGroupIdsJoined()
                                    for group in groups:
                                        sa = "{}".format(str(kw))
                                        data = {
                                            "type": "flex",
                                            "altText": "มีคนกล่าวถึงคุณในแชท",
                                            "contents": {
                                                "type": "bubble",
                                                "hero": {
                                                    "type": "image",
                                                    "url": "https://i.imgur.com/9EXisOi.jpg",
                                                    "size": "full",
                                                    "aspectRatio": "1:1",
                                                    "aspectMode": "cover",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://ti/p/~appbotline"
                                                    }
                                                },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                           "type": "text",
                                                           "text": sa,
                                                           "wrap": True,
                                                           "align": "center",
                                                           "gravity": "center",
                                                           "size": "md"
                                                       },
                                                       {  
                                                           "type":"text",
                                                           "text":" "
                                                       },
                                                       {
                                                           "type":"button",
                                                           "style":"primary",
                                                           "color":"#0000ff",
                                                           "action": {
                                                               "type": "uri",
                                                               "label": "ติดต่อเรา",
                                                               "uri": "line://ti/p/~{}".format(ans),
                                                           }
                                                       }
                                                   ]
                                                }
                                            }
                                        }
                                        sendTemplate(group, data)
                                        time.sleep(1)
                                    cl.sendMessage(to, "ฝ̶า̶ก̶แ̶ล̶̶้ว̶จ̶ำ̶น̶ว̶น̶  {} ก̶ล̶̶̶ุ่ม̶ ".format(str(len(groups))))
                        if cmd == "นอต1":
                            rah = text.split(" ")
                            matt = text.replace(rah[0] + " ","")
                            sender_profile = cl.getContact(sender)
                            groups = cl.getGroupIdsJoined()
                            for gr in groups:
                                dataProfile = [{"type":"bubble","header":{"type":"box","layout":"vertical","flex":0,"contents":[{"type":"text","text":"เทสระบบ","size":"xl","align":"center","gravity":"center","weight":"bold","color":"#2eb07c","action":{"type":"uri","uri":"https://line.me/R/ti/p/ลิ้งไลน์"}}]},"hero":{"type":"image","url":"https://www.img.in.th/images/24afba7c6cbc83ac1b6c20210ebb2a50.jpg","size":"full","aspectRatio":"1:1","aspectMode":"cover","action":{"type":"uri","label":"Action","uri":"https://line.me/R/ti/p/ลิ้งไลน์"}},"body":{"type":"box","layout":"vertical","spacing":"md","action":{"type":"uri","label":"Action","uri":"https://line.me/R/ti/p/ลิ้งไลน์"},"contents":[{"type":"text","text":"กดเพื่อรับสติกเกอร์ฟรี","size":"lg","align":"center","weight":"bold","color":"#2eb07c","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40xig5083j"}},{"type":"image","url":"https://www.img.in.th/images/8fbd178a8bdef60194478fefc15a03d3.th.jpg","size":"full","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40xig5083j"}}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"spacer","size":"xs"},{"type":"button","action":{"type":"uri","label":"กดเลยจ้า","uri":"https://line.me/R/ti/p/%40xig5083j"},"color":"#00ff40","height":"md","style":"primary"}]}}]
                                data = {
                                    "type": "flex",
                                    "altText": "มาแล้วจ้าสติ๊กเกอร์",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": dataProfile
                                   }
                                }
                                bcTemplate(gr, data)
                                time.sleep(1)
                        if cmd == "นอต2":
                            rah = text.split(" ")
                            matt = text.replace(rah[0] + " ","")
                            sender_profile = cl.getContact(sender)
                            groups = cl.getGroupIdsJoined()
                            for gr in groups:
                                data = {"type": "flex","altText": "บริการนวด","contents": {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"สนใจใช้บริการ","margin":"md","size":"xl","align":"center","weight":"bold","color":"#FFFFFF"}]},"hero":{"type":"image","url":"https://www.img.in.th/images/9296797c5e2edfce2e6f77e9bc790ad2.th.jpg","size":"full","aspectRatio":"1:1","aspectMode":"fit","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40syc4846y"}},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"สนใจใช้บริการ","align":"center","color":"#FFFBFB","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40syc4846y"},"wrap":True}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"button","action":{"type":"uri","label":"เข้าร่วมกลุ่ม","uri":"https://line.me/R/ti/p/%40syc4846y"},"color":"#0B0202","style":"primary"},{"type":"button","action":{"type":"uri","label":"กลุ่ม VIP","uri":"https://line.me/R/ti/p/%40syc4846y"},"style":"primary"}]},"styles":{"header":{"backgroundColor":"#160202"},"body":{"backgroundColor":"#050505"}}}}
                                bcTemplate(gr, data)
                                time.sleep(1)
                        if cmd == "นอต3":
                            rah = text.split(" ")
                            matt = text.replace(rah[0] + " ","")
                            sender_profile = cl.getContact(sender)
                            groups = cl.getGroupIdsJoined()
                            for gr in groups:
                           #     dataProfile = [{"type":"bubble","hero":{"type":"image","url":"https://www.img.in.th/images/05147dd16131f7d44992c3d72710148e.th.jpg","margin":"none","size":"full","aspectRatio":"1:1","aspectMode":"cover","backgroundColor":"#160606","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40usn2235f"}},"body":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"text","text":"","size":"xl","weight":"bold","color":"#0C0909","wrap":True},{"type":"box","layout":"baseline","flex":1,"contents":[{"type":"text","text":"","flex":0,"size":"xl","weight":"bold","wrap":True}]}]},"footer":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"button","action":{"type":"uri","label":"สนใจเข้ากลุ่ม กด","uri":"https://line.me/R/ti/p/%40usn2235f"},"flex":2,"color":"#161616","style":"primary"},{"type":"button","action":{"type":"uri","label":"สนใจนวด กด","uri":"https://line.me/R/ti/p/%40usn2235f"},"flex":2,"color":"#208110","height":"md","style":"primary"}]}}]
                                data = {"type": "flex","altText": "โหลดสติ๊กเกอร์ที่นี่","contents": {"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"โหลดสติ๊กเกอร์ กด","margin":"md","size":"xl","align":"center","weight":"bold","color":"#FFFFFF"}]},"hero":{"type":"image","url":"https://www.img.in.th/images/05147dd16131f7d44992c3d72710148e.th.jpg","size":"full","aspectRatio":"1:1","aspectMode":"fit","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40usn2235f"}},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"รับสติ๊กเกอร์ กด","align":"center","color":"#FFFBFB","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40usn2235f"},"wrap":True}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"button","action":{"type":"uri","label":"Download","uri":"https://line.me/R/ti/p/%40usn2235f"},"color":"#0B0202","style":"primary"},{"type":"button","action":{"type":"uri","label":"รับฟรี","uri":"https://line.me/R/ti/p/%40usn2235f"},"style":"primary"}]},"styles":{"header":{"backgroundColor":"#160202"},"body":{"backgroundColor":"#050505"}}}}
                                bcTemplate(gr, data)
                                time.sleep(1)
                        if cmd == "นอต4":
                            rah = text.split(" ")
                            matt = text.replace(rah[0] + " ","")
                            sender_profile = cl.getContact(sender)
                            groups = cl.getGroupIdsJoined()
                            for gr in groups:
                                dataProfile = [{"type":"bubble","header":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"แจกฟรี 5,000บาท","size":"xxl","align":"center","weight":"bold","color":"#090808","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40pxn2655j"}}]},"hero":{"type":"image","url":"https://www.img.in.th/images/700acbf525519c5f44cfe1843e1dc97f.jpg","size":"full","aspectRatio":"1:1","aspectMode":"cover","action":{"type":"uri","label":"Action","uri":"https://line.me/R/ti/p/%40pxn2655j"}},"body":{"type":"box","layout":"horizontal","spacing":"md","contents":[{"type":"button","action":{"type":"uri","label":"แจกเงินสดง่ายๆ 3,000บาท","uri":"https://line.me/R/ti/p/%40pxn2655j"},"style":"primary"}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"button","action":{"type":"uri","label":"คลิกได้เลย!!","uri":"https://line.me/R/ti/p/%40pxn2655j"},"style":"primary"}]},"styles":{"body":{"backgroundColor":"#121010"},"footer":{"backgroundColor":"#0B0808","separatorColor":"#050202"}}}]
                                data = {
                                    "type": "flex",
                                    "altText": "แจกเงินสดฟรี 5,000บาท",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": dataProfile
                                   }
                                }
                                bcTemplate(gr, data)
                                time.sleep(1)
                        if cmd == "นอต5":
                            rah = text.split(" ")
                            matt = text.replace(rah[0] + " ","")
                            sender_profile = cl.getContact(sender)
                            groups = cl.getGroupIdsJoined()
                            for gr in groups:
                                dataProfile = [{"type":"bubble","direction":"ltr","header":{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"รับติดตั้งบอท","size":"xl","align":"center","gravity":"center","weight":"bold","color":"#000000","action":{"type":"uri","uri":"http://line.me/ti/p/~appbotline"}}]},"hero":{"type":"image","url":"https://www.img.in.th/images/7c173b55eda42c040c4152c9c87b09b2.jpg","align":"center","gravity":"center","size":"full","aspectRatio":"20:13","aspectMode":"cover","action":{"type":"uri","label":"Action","uri":"http://line.me/ti/p/~appbotline"}},"body":{"type":"box","layout":"horizontal","spacing":"md","contents":[{"type":"box","layout":"vertical","flex":1,"contents":[{"type":"image","url":"https://www.img.in.th/images/7c173b55eda42c040c4152c9c87b09b2.jpg","gravity":"bottom","size":"sm","aspectRatio":"4:3","aspectMode":"cover","action":{"type":"uri","uri":"http://line.me/ti/p/~appbotline"}},{"type":"image","url":"https://www.img.in.th/images/7c173b55eda42c040c4152c9c87b09b2.jpg","margin":"md","size":"sm","aspectRatio":"4:3","aspectMode":"cover","action":{"type":"uri","uri":"http://line.me/ti/p/~appbotline"}}]},{"type":"box","layout":"vertical","flex":2,"contents":[{"type":"text","text":"บอทป้องกันV10","flex":1,"size":"xs","align":"center","gravity":"center","weight":"bold","color":"#ff0000"},{"type":"separator"},{"type":"text","text":"เชลบอท บอทแทก","flex":2,"size":"xs","align":"start","gravity":"center","weight":"bold","color":"#ff0000"},{"type":"separator"},{"type":"text","text":"เชลบอทประกาศ ปักหมุด ","flex":2,"size":"xs","align":"start","gravity":"center","weight":"bold","color":"#ff0000"},{"type":"separator"},{"type":"text","text":"บอทแทก ต้อนรับ","flex":1,"size":"xs","align":"start","gravity":"center","weight":"bold","color":"#ff0000"}]}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"button","action":{"type":"uri","label":"สนใจระบบกด","uri":"http://line.me/ti/p/~appbotline"},"style":"primary"}]},"styles":{"header":{"backgroundColor":"#F7EBEB"},"body":{"backgroundColor":"#E8CDCD"}}}]
                                data = {
                                    "type": "flex",
                                    "altText": "ทดสอบระบบโฆษณา",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": dataProfile
                                   }
                                }
                                bcTemplate(gr, data)
                                time.sleep(1)
                        if cmd == "นอต6":
                            rah = text.split(" ")
                            matt = text.replace(rah[0] + " ","")
                            sender_profile = cl.getContact(sender)
                            groups = cl.getGroupIdsJoined()
                            for gr in groups:
                                dataProfile = [{"type":"bubble","hero":{"type":"image","url":"https://media.giphy.com/media/1fhHhtoNZkJ4On3hhR/giphy.gif","size":"full","aspectRatio":"1:1","aspectMode":"cover","action":{"type":"uri","uri":"https://saibotnoname.com"}},"body":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"box","layout":"horizontal","contents":[{"type":"text","text":"วัยเยสสด\u200b #คลิปเพียบ","flex":0,"size":"lg","weight":"bold","action":{"type":"uri","uri":"https://saibotnoname.com"},"wrap":True}]}]},"footer":{"type":"box","layout":"vertical","spacing":"sm","contents":[{"type":"button","action":{"type":"uri","label":"กลุ่มลับ","uri":"https://saibotnoname.com"},"style":"primary"},{"type":"button","action":{"type":"uri","label":"เพิ่มเติม....","uri":"https://saibotnoname.com"},"color":"#0E0202","style":"primary"}]},"styles":{"body":{"backgroundColor":"#EEE5E5"}}}]
                                data = {
                                    "type": "flex",
                                    "altText": "ทดสอบระบบโฆษณา",
                                    "contents": {
                                        "type": "carousel",
                                        "contents": dataProfile
                                   }
                                }
                                bcTemplate(gr, data)
                                time.sleep(1)
                        elif cmd == "นอต7":
                          groups = cl.getGroupIdsJoined()
                          for gr in groups:
                              data = {"type": "flex","altText": "ใส่ข้อความหน้าแชท","contents": {"type":"bubble","hero":{"type":"image","url":"https://i.imgur.com/b7vcxPU.gif","size":"full","aspectRatio":"1:1","aspectMode":"cover","action":{"type":"uri","uri":"https://line.me/R/ti/p/%40xig5083j"}}}}
                              bcTemplate(gr, data)
                              time.sleep(1)
  #---------------------------------------=========แบบเลื่อน 2เลื่อน==========---------------------------------------#
                        elif msg.text.lower().startswith("นอต8"):
                                    groups = cl.getGroupIdsJoined()
                                    contact = cl.getContact(mid)
                                    cover = cl.getProfileCoverURL(mid)
                                    for group in groups:
                                        data = {"type":"flex","altText": "Appทดสอบระบบ1","contents":{"type":"carousel","contents":[{"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"โปรโมชั่นดีๆมีที่นี้","size":"xl","align":"center","color":"#DBB800"}]},"hero":{"type":"image","url":"https://thepbodint.ac.th/news/images/2720.jpg","size":"full","aspectMode":"cover","action":{"type":"uri","label":"ฝาก","uri":"https://saibotnoname.com"}},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"บริการโดยทีมงานมืออาซีพ","size":"xxl","align":"center","weight":"bold","color":"#FF0202"},{"type":"text","text":"การันตีเรื่งความชัว","size":"xl","align":"center","weight":"bold","color":"#007F0A"}]},"footer":{"type":"box","layout":"vertical","contents":[{"type":"button","action":{"type":"uri","label":"ถอนเงิน","uri":"https://saibotnoname.com"},"color":"#73FF00","style":"link"},{"type":"button","action":{"type":"uri","label":"ถอนเงิน","uri":"https://saibotnoname.com"},"style":"primary"}]},"styles":{"header":{"backgroundColor":"#000000"},"hero":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#000000"}}},{"type":"bubble","direction":"ltr","header":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"แจกโบนัสทุกวัน","size":"xl","align":"center","color":"#DBB800"}]},"hero":{"type":"image","url":"https://static.posttoday.com/media/content/2018/05/16/A68E1944F29848CA9E9737F6B33A10FC.jpg","size":"full","aspectMode":"cover"},"body":{"type":"box","layout":"horizontal","spacing":"md","contents":[{"type":"box","layout":"vertical","contents":[{"type":"image","url":"https://brandinside.asia/wp-content/uploads/2018/06/shutterstock_717904957-kl8654.jpg","size":"sm","action":{"type":"uri","label":"ฝาก","uri":"https://saibotnoname.com"}},{"type":"image","url":"https://brandinside.asia/wp-content/uploads/2018/06/shutterstock_717904957-kl8654.jpg","margin":"md","size":"sm","action":{"type":"uri","label":"ฝาก","uri":"https://saibotnoname.com"}}]},{"type":"box","layout":"vertical","flex":2,"contents":[{"type":"text","text":"สมัครสมาชิกรับโบนัสฟรีๆ","flex":1,"size":"md","color":"#DBB800"},{"type":"separator","color":"#DBB800"},{"type":"text","text":"ฝาก-ถอนได้ตลอด 24ชม","flex":1,"size":"md","gravity":"center","color":"#DBB800"},{"type":"separator","color":"#DBB800"},{"type":"text","text":"บริหารงานโดยทีมงามตลอด24ชม.","flex":2,"size":"lg","gravity":"center","color":"#DBB800"},{"type":"separator","color":"#DBB800"},{"type":"text","text":"เว็บเราเปิดมานาน","flex":1,"size":"xs","gravity":"bottom","color":"#DBB800"}]}]},"footer":{"type":"box","layout":"horizontal","contents":[{"type":"button","action":{"type":"uri","label":"สมัครสมาชิก","uri":"https://saibotnoname.com"},"style":"primary"}]},"styles":{"header":{"backgroundColor":"#000000"},"hero":{"backgroundColor":"#000000","separatorColor":"#000000"},"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#000000"}}}]}} 
                                        sendTemplate(group, data)
                                        time.sleep(1)
                                    cl.sendMessage(to, "ฝ̶า̶ก̶แ̶ล̶̶้ว̶จ̶ำ̶น̶ว̶น̶{} ก̶ล̶̶̶ุ่ม̶ ".format(str(len(groups))))
#---------------------------------------=========แบบเลื่อน 3เลื่อน==========---------------------------------------#
                        elif msg.text.lower().startswith("นอต9"):
                                    groups = cl.getGroupIdsJoined()
                                    contact = cl.getContact(mid)
                                    cover = cl.getProfileCoverURL(mid)
                                    for group in groups:
                                        data = {"type":"flex","altText": "Appทดสอบระบบ2","contents":{"type":"carousel","contents":[{"type":"bubble","direction":"ltr","hero":{"type":"image","url":"https://i.imgur.com/Uz7W8ZU.jpg","size":"full","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"สมัครสมาชิกรับเงินฟรี","size":"lg","align":"center","weight":"bold","color":"#DBB800"}]},"footer":{"type":"box","layout":"vertical","spacing":"md","contents":[{"type":"button","action":{"type":"uri","label":"ถอดยอด","uri":"https://saibotnoname.com"},"style":"primary"},{"type":"button","action":{"type":"uri","label":"สมัครสมาชิก","uri":"https://saibotnoname.com"},"color":"#D91C1C","style":"primary"}]},"styles":{"hero":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#000000"}}},{"type":"bubble","direction":"ltr","hero":{"type":"image","url":"https://i.imgur.com/Uz7W8ZU.jpg","size":"full","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"ให้ยริการตลอด24ชม.","size":"lg","align":"center","weight":"bold","color":"#DBB800"}]},"footer":{"type":"box","layout":"vertical","spacing":"md","contents":[{"type":"button","action":{"type":"uri","label":"แทงบอลได้ตลอดเวลา","uri":"https://saibotnoname.com"},"style":"primary"},{"type":"button","action":{"type":"uri","label":"รวดเร็วตลอด 24 ชม.","uri":"https://saibotnoname.com"},"color":"#D91C1C","style":"primary"}]},"styles":{"hero":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#000000"}}},{"type":"bubble","direction":"ltr","hero":{"type":"image","url":"https://i.imgur.com/Uz7W8ZU.jpg","size":"full","aspectMode":"cover"},"body":{"type":"box","layout":"vertical","contents":[{"type":"text","text":"บริหารงานโดยมืออาซีพ","size":"md","align":"center","weight":"bold","color":"#DBB800"}]},"footer":{"type":"box","layout":"vertical","spacing":"md","contents":[{"type":"button","action":{"type":"uri","label":"รับแทงบอลตลอด24ชม.","uri":"https://saibotnoname.com"},"style":"primary"},{"type":"button","action":{"type":"uri","label":"เดิมพันขั้นต่ำเท่าไรก็ได้","uri":"https://saibotnoname.com"},"color":"#D91C1C","style":"primary"}]},"styles":{"hero":{"backgroundColor":"#000000"},"body":{"backgroundColor":"#000000"},"footer":{"backgroundColor":"#000000"}}}]}} 
                                        sendTemplate(group, data)
                                        time.sleep(1)
                                    cl.sendMessage(to, "ฝ̶า̶ก̶แ̶ล̶̶้ว̶จ̶ำ̶น̶ว̶น̶{} ก̶ล̶̶̶ุ่ม̶ ".format(str(len(groups))))
#*******************************************************************************************#
                        elif cmd == '@@@':
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Sai \n'
                                cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                cl.sendMessage(to, "จ̶ำ̶น̶ว̶น̶ท̶ี̶̶่ส̶ั̶̶่ง̶แ̶ท̶็̶ค̶  {}  ค̶น̶".format(str(len(nama))))

                        elif cmd == "คำสั่ง2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage2))
                               
                        elif cmd == "คำสั่ง3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage3 = helpbot1()
                               cl.sendMessage(msg.to, str(helpMessage3)) 
                              
                        elif cmd == "คำสั่ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage4 = helpbot2()
                               cl.sendMessage(msg.to, str(helpMessage4)) 
                                                                                       
                        if cmd == "on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "ร̶ะ̶บ̶บ̶เ̶ซ̶ล̶บ̶อ̶ท̶เ̶ร̶ิ̶̶่ม̶ท̶ำ̶ง̶า̶น̶")
                                
                        elif cmd == "off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "ร̶ะ̶บ̶บ̶เ̶ซ̶ล̶บ̶อ̶ท̶ถ̶̶ูก̶ป̶ิ̶ด̶ก̶า̶ร̶ต̶อ̶บ̶ส̶น̶อ̶ง̶")
        
                        elif cmd == "เชคค่า":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "   •B̶o̶t̶ ̶N̶o̶N̶a̶m̶e̶ ̶O̶S̶M̶ ̶1̶.̶1̶.̶2̶ •\n"
                                if wait["sticker"] == True: md+="【✔】เ̶ช̶็̶ค̶ส̶ต̶ิ̶̶๊ก̶เ̶ก̶อ̶ร̶์̶\n"
                                else: md+="【✘】เ̶ช̶็̶ค̶ส̶ต̶ิ̶̶๊ก̶เ̶ก̶อ̶ร̶์̶r\n"
                                if wait["contact"] == True: md+="【✔】เ̶ช̶็̶ค̶ค̶ท̶\n"
                                else: md+="【✘】เ̶ช̶็̶ค̶ค̶ท̶\n"
                                if wait["autoJoin"] == True: md+="【✔】เ̶ข̶̶้า̶อ̶อ̶โ̶ต̶̶้\n"
                                else: md+="【✘】เ̶ข̶̶้า̶อ̶อ̶โ̶ต̶̶้\n"
                                if settings["autoJoinTicket"] == True: md+="【✔】ม̶̶ุด̶ล̶ิ̶̶้ง̶ค̶์̶อ̶อ̶โ̶ต̶̶้\n"
                                else: md+="【✘】ม̶̶ุด̶ล̶ิ̶̶้ง̶ค̶์̶อ̶อ̶โ̶ต̶̶้\n"
                                if wait["autoAdd"] == True: md+="【✔】แ̶อ̶ด̶อ̶ั̶ต̶โ̶น̶ม̶ั̶ต̶ิ̶\n"
                                else: md+="【✘】แ̶อ̶ด̶อ̶ั̶ต̶โ̶น̶ม̶ั̶ต̶ิ̶\n"
                                cl.sendMessage(msg.to, md+"\nว̶ั̶น̶ท̶ี̶̶่ "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nเ̶ว̶ล̶า̶ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")

                        elif cmd == "คท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:                                           
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': msg._from}
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)
                                # path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                                # image = 'http://dl.profile.line.naver.jp'+path
                                # cl.sendImageWithURL(msg.to, image)
                                
                        elif cmd == "me":                       	
                    	    if msg._from in admin: 
                              contact = cl.getContact(sender)
                              image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                              cl.sendMessage(msg.to, "ช̶ื̶̶่อ̶ค̶̶ุณ̶  : "+str(contact.displayName))
                              cl.sendMessage(msg.to, None,contentMetadata={'mid': sender}, contentType=13)
                              
                                                                       
                        elif text.lower() == "ไอดี":
                               cl.sendMessage(msg.to, msg._from)
                        elif text.lower() == 'bot':
                               cl.sendMessage(msg.to, "•B̶o̶t̶ ̶N̶o̶N̶a̶m̶e̶ ̶O̶S̶M̶ ̶1̶.̶1̶.̶2̶ •")
                               

                        elif ("ไอดี " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "ช̶ื̶̶่อ̶ค̶̶ุณ̶ : "+str(mi.displayName)+"\nʍ̶ɨ̶ɖ̶ : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("ดึงหมด " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "ช̶ื̶̶่อ̶ : "+str(mi.displayName)+"\nʍ̶ɨ̶ɖ̶ : " +key1+"\nส̶เ̶ต̶ต̶ั̶ส̶ "+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                        elif ("คท " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)



                        elif cmd  == "mybot":
                          if msg._from in admin:
                              cl.sendContact(to, mid)
                               
                        elif cmd  == "midbot":
                          if msg._from in admin:
                              cl.sendMessage(msg.to,mid)
                              
                               

                        elif text.lower() == "ลบแชท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"ล̶บ̶แ̶ช̶ท̶เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶")

                               except:
                                   pass

                        elif cmd == "รีบูท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ก̶ำ̶ล̶ั̶ง̶เ̶ร̶ิ̶̶่ม̶ก̶า̶ร̶ร̶ี̶บ̶̶ูท̶โ̶ป̶ร̶ร̶อ̶")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Done...")
                            
                        elif cmd == "ออน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "เ̶ว̶ล̶า̶ล̶็̶อ̶ค̶อ̶ิ̶น̶ " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ข้อมูลกลุ่ม":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "ป̶ิ̶ด̶"
                                    gTicket = "ป̶ิ̶ด̶"
                                else:
                                    gQr = "เ̶ป̶ิ̶ด̶"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "    เ̶ช̶็̶ค̶ร̶ะ̶บ̶บ̶ก̶ล̶̶̶ุ่ม̶ \n\nช̶ื̶̶่อ̶ก̶ล̶̶̶ุ่ม̶ : {}".format(G.name)+ "\nไ̶อ̶ด̶ี̶ก̶ล̶̶̶ุ่ม̶ : {}".format(G.id)+ "\nผ̶̶̶ู้ส̶ร̶̶้า̶ง̶ก̶ล̶̶̶ุ่ม̶ : {}".format(G.creator.displayName)+ "\nว̶ั̶น̶ท̶ี̶̶่ส̶ร̶̶้า̶ง̶ : {}".format(str(timeCreated))+ "\nส̶ม̶า̶ช̶ิ̶ก̶ : {}".format(str(len(G.members)))+ "\nค̶̶้า̶ง̶เ̶ช̶ิ̶ญ̶ : {}".format(gPending)+ "\nล̶ิ̶̶้ง̶ค̶์̶ก̶ล̶̶̶ุ่ม̶ : {}".format(gQr)+ "\nล̶ิ̶̶้ง̶ค̶์̶ก̶ล̶̶̶ุ่ม̶ : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd == "เพื่อน":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"   ร̶า̶ย̶ช̶ื̶̶่อ̶เ̶พ̶ื̶̶่อ̶น̶ \n\n"+ma+"\nจ̶ำ̶น̶ว̶น̶  "+str(len(gid))+" ค̶น̶")
                        elif cmd == "รายการบล็อค":
                          if msg._from in admin:
                            blockedlist = cl.getBlockedContactIds()
                            kontak = cl.getContacts(blockedlist)
                            num=1
                            msgs=" •B̶o̶t̶ ̶N̶o̶N̶a̶m̶e̶ ̶O̶S̶M̶ ̶1̶.̶1̶.̶2̶ •\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nจ̶ำ̶น̶ว̶น̶ก̶า̶ร̶บ̶ล̶็̶อ̶ค̶ %i คน" % len(kontak)
                            hello = "{}".format(str(msgs))
                            data = {
                                "type": "text",
                                "text": "{}".format(str(msgs)),
                                "sentBy": {
                                    "label": "{}".format(cl.getContact(mid).displayName),
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(cl.getContact(mid).pictureStatus),
                                    "linkUrl": "line://ti/p/~appbotline"
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd == "เวอร์ชั่น":
                          if msg._from in admin:
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2019
                                bln = 3   
                                hr = 19   
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                Downostag = "ubd78f3da598d3c32e075e062e88545ec"
                                h = cl.getContact(mid)
                                groups = cl.getGroupIdsJoined()
                                contactlist = cl.getAllContactIds()
                                kontak = cl.getContacts(contactlist)
                                favorite = cl.getFavoriteMids()
                                blockedlist = cl.getBlockedContactIds()
                                kontak2 = cl.getContacts(blockedlist)
                                ret_ = "ร̶า̶ย̶ล̶ะ̶เ̶อ̶ี̶ย̶ด̶ข̶อ̶ง̶บ̶อ̶ท̶\n"
                                ret_ += "\nช̶ื̶̶่อ̶ผ̶̶̶ู้ใ̶ช̶̶้  {}".format(h.displayName)
                                ret_ += "\nจ̶ำ̶น̶ว̶น̶ก̶ล̶̶̶ุ่ม̶   {}".format(str(len(groups)))
                                ret_ += "\nจ̶ำ̶น̶ว̶น̶เ̶พ̶ื̶̶่อ̶น̶ {}".format(str(len(kontak)))
                                ret_ += "\nจ̶ำ̶น̶ว̶น̶ก̶า̶ร̶บ̶ล̶็̶อ̶ค̶  {}".format(str(len(kontak2)))
                                ret_ += "\nร̶า̶ย̶ก̶า̶ร̶โ̶ป̶ร̶ด̶  {}".format(str(len(favorite)))
                                ret_ += "\n\nเ̶ว̶อ̶ร̶์̶ช̶ั̶̶่น̶ข̶อ̶ง̶บ̶อ̶ท̶\n"
                                ret_ += "\nV̶e̶r̶s̶i̶o̶n̶ : •B̶o̶t̶ ̶N̶o̶N̶a̶m̶e̶ ̶O̶S̶M̶ ̶1̶.̶1̶.̶2̶ •\n"
                                ret_ += "\nอ̶ั̶พ̶เ̶ด̶ท̶ล̶̶่า̶ส̶̶ุด̶ : 1̶8̶/̶0̶3̶/̶2̶0̶1̶9̶ ̶1̶0̶:̶3̶0̶:̶5̶2̶\n"
                                ret_ += "\nผู้สร้าง  @!   "
                                mentions(to, str(ret_),[Downostag])
                            except Exception as e:
                                cl.generateReplyMessage(msg.id)
                                cl.sendReplyMessage(msg.id, to, str(e))
                        elif cmd == "ลิ้ง":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "ชื่อกลุ่ม "+str(x.name)+ "\nลิ้งค์กลุ่ม   http://line.me/R/ti/g/"+gurl)
                        elif cmd == "กลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += " " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"   ร̶า̶ย̶ก̶า̶ร̶ก̶ล̶̶̶ุ่ม̶\n"+ma+" จ̶ำ̶น̶ว̶น̶"+str(len(gid))+" ก̶ล̶̶̶ุ่ม̶")
                        elif cmd == "ลิ้งปิด":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "ป̶ิ̶ด̶ล̶ิ̶̶้ง̶ค̶์̶ล̶ะ̶")

                        elif cmd == "ลิ้งเปิด":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "ช̶ื̶̶่อ̶ก̶ล̶̶̶ุ่ม̶ : "+str(x.name)+ "\nล̶ิ̶̶้ง̶ค̶์̶ก̶ล̶̶̶ุ่ม̶ : http://line.me/R/ti/g/"+gurl)
                        elif cmd == "แท็ก2":
                            group = cl.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(cl.getProfile().mid)
                            cl.datamention(to,'Mention',nama)

                        elif "/ลบรัน" in msg.text.lower():
                            spl = re.split("/ลบรัน",msg.text,flags=re.IGNORECASE)
                            if spl[0] == "":
                                spl[1] = spl[1].strip()
                                ag = cl.getGroupIdsInvited()
                                txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                                if spl[1] != "":
                                    txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                                txt = txt + "\nกรุณารอสักครู่.."
                                message(to, str(text))
                                procLock = len(ag)
                                for gr in ag:
                                    try:
                                        cl.acceptGroupInvitation(gr)
                                        if spl[1] != "":
                                            cl.sendMessage(gr,spl[1])
                                        cl.leaveGroup(gr)
                                    except:
                                        pass
                                sis = "สำเร็จแล้ว (｀・ω・´)"
                                message(to, str(sis))

                        elif cmd == "เปลี่ยนรูปกลุ่ม":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"ก̶ร̶̶ุณ̶า̶ส̶̶่ง̶ร̶̶ุป̶ม̶า̶") 
                        elif cmd == "อัพโปร":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["changePicture"] = True
                                cl.sendMessage(msg.to,"ก̶ร̶̶ุณ̶า̶ส̶̶่ง̶ร̶̶ุป̶ม̶า̶") 

                        elif cmd.startswith("ชื่อ "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"เ̶ป̶ล̶ี̶̶่ย̶น̶ช̶ื̶̶่อ̶เ̶ป̶็̶น̶ " + string)
                                                        
                        elif cmd == "แทค" or text.lower() == '@@':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for o in range (140, 159):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm8)
                                   for o in range (160, 179):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm9)
                                   for o in range (180, 199):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm10)
                                   for o in range (200, 219):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm11)
                                   for o in range (220, 239):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm12)
                                   for o in range (240, 259):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm13)
                                   for o in range (260, 279):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm14)
                                   for o in range (280, 299):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm15)
                                   for o in range (300, 319):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm16)
                                   for o in range (320, 339):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm17)
                                   for o in range (340, 359):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm18)
                                   for o in range (360, 379):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm19)
                                   for o in range (380, 399):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm20)
                                   for o in range (400, 419):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm21)
                                   for o in range (420, 439):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm22)
                                   for o in range (440, 459):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm23)
                                   for o in range (460, 479):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm24)
                                   for o in range (480, 495):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm25)
                                   for p in range (495, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                        elif cmd == "บอท":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"ร̶า̶ย̶ช̶ื̶̶่อ̶บ̶อ̶ท̶    \n\n\n"+ma+"\n%s Bots" %(str(len(Bots))))



                        elif cmd == "เชคแอด":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"    ร̶า̶ย̶ช̶ื̶̶่อ̶แ̶อ̶ด̶ม̶ิ̶น̶\n\nแ̶อ̶ด̶ม̶ิ̶น̶2̶\n"+ma+"\nแ̶อ̶ด̶ม̶ิ̶น̶\n"+mb+"\nแ̶อ̶ด̶ม̶ิ̶น̶3̶\n"+mc+"\n%s ค̶น̶" %(str(len(owner)+len(admin)+len(staff))))
                       
                        elif cmd == "ออกละ":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "บ̶า̶ย̶ "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("ออก "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        cl.sendMessage(i, "ร̶ะ̶บ̶บ̶ถ̶̶ูก̶ส̶ั̶̶่ง̶อ̶อ̶ก̶จ̶า̶ก̶แ̶อ̶ด̶ม̶ิ̶น̶")
                                        cl.leaveGroup(i)
                                        cl.sendMessage(to,"ก̶ำ̶ล̶ั̶ง̶เ̶ร̶ิ̶̶่ม̶อ̶อ̶ก̶จ̶า̶ก̶ก̶ล̶̶̶ุ่ม̶ " +h)

                        elif cmd == "ทดสอบ":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "   •B̶o̶t̶ ̶N̶o̶N̶a̶m̶e̶ ̶O̶S̶M̶ ̶1̶.̶1̶.̶2̶ •\n\n ค̶ว̶า̶ม̶เ̶ร̶็̶ว̶ร̶ั̶บ̶โ̶ป̶ร̶\n   %.10f\n ค̶ว̶า̶ม̶เ̶ร̶็̶ว̶ร̶ั̶บ̶ค̶อ̶น̶แ̶ท̶ค̶\n   %.10f\n ค̶ว̶า̶ม̶เ̶ร̶็̶ว̶ใ̶น̶ก̶ล̶̶̶ุ่ม̶\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()                               
                               cl.sendMessage(msg.to, "•B̶o̶t̶ ̶N̶o̶N̶a̶m̶e̶ ̶O̶S̶M̶ ̶1̶.̶1̶.̶2̶ •")                               
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "         ค̶ว̶า̶ม̶เ̶ร̶็̶ว̶ \n{}".format(str(elapsed_time)))

                        elif cmd == "แอบเปิด":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "   เ̶ร̶ิ̶̶่ม̶ต̶ร̶ว̶จ̶ส̶อ̶บ̶ก̶า̶ร̶อ̶̶่า̶น̶ \n\nว̶ั̶น̶ท̶ี̶̶่ "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nเ̶ว̶ล̶า̶  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "แอบปิด":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "ป̶ิ̶ด̶ก̶า̶ร̶เ̶ช̶็̶ค̶ก̶า̶ร̶อ̶̶่า̶น̶\n\nว̶ั̶น̶ท̶ี̶̶่ "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nเ̶ว̶ล̶า̶   "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  cl.sendMessage(msg.to, "ป̶ิ̶ด̶ก̶า̶ร̶เ̶ช̶็̶ค̶ก̶า̶ร̶อ̶̶่า̶น̶")

                        elif 'Idline ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('Idline ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
   
                        elif ("คลิ้ก " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           cl.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif text.lower() == 'เตะดำ':
                           if msg._from in admin:
                              gid = cl.getGroupIdsJoined()
                              group = cl.getGroup(to)
                              gMembMids = [contact.mid for contact in group.members]
                              ban_list = []
                              for tag in wait["blacklist"]:
                                    ban_list += filter(lambda str: str == tag, gMembMids)
                              if ban_list == []:
                                    cl.sendMessage(to, "ไ̶ม̶̶่พ̶บ̶บ̶ั̶ญ̶ช̶ี̶ด̶ำ̶")
                                    return
                              else:
                                    for i in gid:
                                    	for jj in ban_list:
                                         if jj in admin:
                                                pass
                                         elif jj in staff:
                                                pass
                                         elif jj in Bots:
                                                pass
                                         else:
                                                cl.kickoutFromGroup(i, [jj])
                                                
                        elif "เตะดึง " in msg.text:
                           if msg._from in admin:
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]                                                                                                                                
                              targets = []
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:                                                                                                                                       
                                  try:
                                      cl.kickoutFromGroup(msg.to,[target])
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                      cl.cancelGroupInvitation(msg.to,[target])
                                      cl.inviteIntoGroup(msg.to,[target])
                                  except:
                                      pass
                                      
                        elif "เตะ " in msg.text:
                           if msg._from in admin:
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]                                                                                                                                
                              targets = []
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:                                                                                                                                       
                                  try:
                                      cl.kickoutFromGroup(msg.to,[target])
                                  except:
                                      pass
                        elif ("ตั้งแอด " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"ต̶ั̶̶้ง̶ผ̶̶̶ู้ใ̶ช̶̶้เ̶ข̶̶้า̶ส̶̶̶ุ่ร̶ะ̶บ̶บ̶แ̶อ̶ด̶ม̶ิ̶น̶2̶เ̶ร̶ี̶ย̶บ̶ร̶̶้อ̶ย̶")
                                       except:
                                           pass

                        elif cmd == "เพิ่มคทแอด" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"ก̶ร̶̶ุณ̶า̶ส̶̶่ง̶ค̶ท̶ม̶า̶")

                        elif cmd == "ลบคทแอด" or text.lower() == 'adminexpl:on':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"ก̶ร̶̶ุณ̶า̶ส̶̶่ง̶ค̶ท̶ม̶า̶")

                        elif cmd == "หยุดการเพิ่ม" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to,"•B̶o̶t̶ ̶N̶o̶N̶a̶m̶e̶ ̶O̶S̶M̶ ̶1̶.̶1̶.̶2̶ •")

                        elif cmd == "คทแอด" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "เชคคทเปิด" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"เ̶ป̶ิ̶ด̶ร̶ะ̶บ̶บ̶เ̶ช̶ท̶ค̶ท̶")

                        elif cmd == "เชคคทปิด" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"ป̶ิ̶ด̶ร̶ะ̶บ̶บ̶เ̶ช̶ท̶ค̶ท̶")

                        elif cmd == "แอดเปิด" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"เ̶ป̶ิ̶ด̶ร̶ะ̶บ̶บ̶อ̶อ̶โ̶ต̶̶้แ̶อ̶ด̶")

                        elif cmd == "แอดปิด" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"ป̶ิ̶ด̶ร̶ะ̶บ̶บ̶อ̶อ̶โ̶ต̶̶้แ̶อ̶ด̶")
                        elif cmd == "ฝากตามเวลาเปิด" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["downos"] = True
                                cl.sendMessage(msg.to,"เ̶ป̶ิ̶ด̶ร̶ะ̶บ̶บ̶ต̶ั̶̶้ง̶เ̶ว̶ล̶า̶ฝ̶า̶ก̶̶")

                        elif cmd == "เข้าเปิด":
                            if msg._from in admin:
                                settings["autoJoin"] = True
                                cl.sendMessage(to, "เ̶ข̶̶้า̶ก̶ล̶̶̶ุ่ม̶อ̶อ̶โ̶ต̶̶้เ̶ป̶ิ̶ด̶")
                        elif cmd == "เข้าปิด":
                            if msg._from in admin:	
                                settings["autoJoin"] = False
                                cl.sendMessage(to, "เ̶ข̶̶้า̶ก̶ล̶̶̶ุ่ม̶อ̶อ̶โ̶ต̶̶้ป̶ิ̶ด̶")
                        elif cmd == "บล็อคเปิด":
                           if msg._from in admin:
                                settings["autoBlock"] = True
                                cl.sendMessage(to, "บ̶ล̶็̶อ̶ค̶ก̶า̶ร̶แ̶อ̶ด̶เ̶ป̶ิ̶ด̶")
                        elif cmd == "บล็อคปิด":    
                            if msg._from in admin: 	
                                settings["autoBlock"] = False
                                cl.sendMessage(to, "บ̶ล̶็̶อ̶ค̶ก̶า̶ร̶แ̶อ̶ด̶ป̶ิ̶ด̶")
                        elif cmd == "มุดลิ้งเปิด":
                        	if msg._from in admin:
                                 settings["autoJoinTicket"] = True
                                 cl.sendMessage(to, "เ̶ป̶ิ̶ด̶ร̶ะ̶บ̶บ̶ก̶า̶ร̶เ̶ข̶̶้า̶ล̶ิ̶̶้ง̶ค̶์̶อ̶อ̶โ̶ต̶̶้")
                        elif cmd == "มุดลิ้งปิด":
                           if msg._from in admin:
                                 settings["autoJoinTicket"] = False
                                 cl.sendMessage(to, "ป̶ิ̶ด̶ร̶ะ̶บ̶บ̶ก̶า̶ร̶เ̶ข̶̶้า̶ล̶ิ̶̶้ง̶ค̶์̶อ̶อ̶โ̶ต̶̶้")  
                        elif ("ดำ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"เ̶พ̶ิ̶̶่ม̶ล̶ง̶บ̶ช̶ด̶ำ̶ล̶ะ̶")
                                       except:
                                           pass

                        elif ("ขาว " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"เ̶พ̶ิ̶̶่ม̶ล̶ง̶บ̶ช̶ข̶า̶ว̶ล̶ะ̶")
                                       except:
                                           pass

                        elif cmd == "ดำ" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"ก̶ร̶̶ุณ̶า̶ส̶̶่ง̶ค̶ท̶ม̶า̶")

                        elif cmd == "ขาว" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"ก̶ร̶̶ุณ̶า̶ส̶̶่ง̶ค̶ท̶ม̶า̶")

                        elif ("บชดำ " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"เ̶พ̶ิ̶̶่ม̶ร̶า̶ย̶ก̶า̶ร̶ล̶ะ̶")
                                       except:
                                           pass

                        elif ("บชขาว " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"เ̶พ̶ิ̶̶่ม̶ร̶า̶ย̶ก̶า̶ร̶ล̶ะ̶")
                                       except:
                                           pass

                        elif cmd == "บชดำ" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"ก̶ร̶̶ุณ̶า̶ส̶̶่ง̶ค̶ท̶ม̶า̶")

                        elif cmd == "บชขาว" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"ก̶ร̶̶ุณ̶า̶ส̶̶่ง̶ค̶ท̶ม̶า̶")

                        elif cmd == "เชคบชดำ" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"ไ̶ม̶̶่พ̶บ̶ร̶า̶ย̶ก̶า̶ร̶")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"ร̶า̶ย̶ช̶ื̶̶่อ̶ผ̶̶̶ู้อ̶ย̶̶̶ู่ใ̶น̶บ̶ช̶ด̶ำ̶\n\n"+ma+"\n %s ค̶น̶" %(str(len(wait["blacklist"]))))
                                

                        elif cmd == "เชคดำ" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"ไ̶ม̶̶่พ̶บ̶ร̶า̶ย̶ก̶า̶ร̶")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to," ร̶า̶ย̶ช̶ื̶̶่อ̶ผ̶̶̶ู้อ̶ย̶̶̶ู่ใ̶น̶บ̶ช̶ด̶ำ̶\n\n"+ma+"\nจ̶ำ̶น̶ว̶น̶ %s ค̶น̶" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "คทบชดำ" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"ไ̶ม̶̶่พ̶บ̶ร̶า̶ย̶ก̶า̶ร̶")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "คทดำ" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                    cl.sendMessage(msg.to,"ไ̶ม̶̶่พ̶บ̶ร̶า̶ย̶ก̶า̶ร̶")
                              else:
                                    ma = ""
                                    for i in wait["Talkblacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif msg.text.lower().startswith("ตั้งคนแอด "):
                           if msg._from in admin:
                            text = msg.text.lower().replace("ตั้งคนแอด ","")
                            wait["message"] = text
                            cl.sendMessage(msg.to, "ข้อความคนแอดมา คือ : {}".format(str(wait["message"])))

                        elif 'ตั้งอ่าน ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('ตั้งอ่าน ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "ไ̶ม̶̶่ส̶า̶ม̶า̶ร̶ถ̶ต̶ั̶̶้ง̶ไ̶ด̶̶้")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "ค̶ำ̶ท̶ี̶̶่ค̶̶ุณ̶ต̶ั̶̶้ง̶ค̶ื̶อ̶\n\n{}".format(str(spl)))

                        elif text.lower() == "เชคคนแอด":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ค̶ำ̶ท̶ี̶̶่ค̶̶ุณ̶ต̶ั̶̶้ง̶ค̶ื̶อ̶\n\n " + str(wait["message"]))

                        elif text.lower() == "เชคตั้งอ่าน":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ค̶ำ̶ท̶ี̶̶่ค̶̶ุณ̶ต̶ั̶̶้ง̶ค̶ื̶อ̶\n\n " + str(wait["mention"]))
                                                                                    
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     group1 = cl.findGroupByTicket(ticket_id)
                                                                        
    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)


import requests
import json
import time
import sys
import random
import argparse
import colorama
import pathlib
import math
import getpass
import socket
import datetime as dt
import keyboard
from colorama import Fore, Back, Style
from random import randint, uniform
from datetime import datetime, date, timedelta
from datetime import date
from datetime import timedelta
from urllib.request import Request, urlopen
from os import system, name
from inputimeout import inputimeout, TimeoutOccurred
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

colorama.init(autoreset=True)

# SET BETSET
parser = argparse.ArgumentParser(description="WOLF.BET BOT @beducode")
parser.add_argument(
    "-c", "--betset", default=0, help="Enter Your Betset Number (default: 0)"
)
my_namespace = parser.parse_args()
nobet = int(my_namespace.betset)

# LOAD SETTING
with open("settings.json", "r") as filesetup:
    data = filesetup.read()
ob = json.loads(data)

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value,
                     OperatingSystem.LINUX.value]

user_agent_rotator = UserAgent(
    software_names=software_names, operating_systems=operating_systems, limit=100
)


# CONFIG WARNA
res = Style.RESET_ALL
putih = Style.NORMAL + Fore.WHITE
putih2 = Style.BRIGHT + Fore.WHITE
hitam = Style.BRIGHT + Fore.BLACK
hitam2 = Style.BRIGHT + Fore.BLACK
ungu = Style.NORMAL + Fore.MAGENTA
hijau = Style.NORMAL + Fore.GREEN
hijau2 = Style.BRIGHT + Fore.GREEN
merah = Style.NORMAL + Fore.RED
merah2 = Style.BRIGHT + Fore.RED
biru = Style.NORMAL + Fore.BLUE
biru2 = Style.BRIGHT + Fore.BLUE
biru3 = Style.BRIGHT + Fore.LIGHTCYAN_EX
profcolor = Style.BRIGHT + Back.GREEN + Fore.WHITE
losecolor = Style.BRIGHT + Back.RED + Fore.WHITE
rccolor = Style.BRIGHT + Back.WHITE + Fore.BLACK
rcfontcolor = Style.NORMAL + Fore.BLACK
kuning = Style.NORMAL + Fore.YELLOW
kuning2 = Style.BRIGHT + Fore.YELLOW
cyan = Style.NORMAL + Fore.CYAN
cyan2 = Style.BRIGHT + Fore.LIGHTCYAN_EX


c = requests.Session()
user_agent = user_agent_rotator.get_random_user_agent()
proxies = []
freeversion = False
stoponwinactivated = False
uuid = ""
startbals = 0
client = FaunaClient(secret="fnAEAcAKliACCJH00BfVSH2dPZ0EIMPWHlMCTbEX")

auth = {
    "user-agent": user_agent,
    "Authorization": "Bearer " + ob["Account"]["Auth Key"] + "",
    "X-Requested-With": "XMLHttpRequest",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}

# CONTROLLER PROCESS

# KEYBOARD SHORTCUT
stoponwinkey = "ctrl+shift+w"


def stoponwin_triger():
    global stoponwinactivated
    stoponwinactivated = True


# BANNER
def banner():
    banner = "\n\n"
    banner = banner + biru2 + "▄▄▌ ▐ ▄▌      ▄▄▌  ·▄▄▄▄▄▄▄· ▄▄▄ .▄▄▄▄▄\n"
    banner = banner + "██· █▌▐█▪     ██•  ▐▄▄·▐█ ▀█▪▀▄.▀·•██  \n"
    banner = banner + "██▪▐█▐▐▌ ▄█▀▄ ██▪  ██▪ ▐█▀▀█▄▐▀▀▪▄ ▐█." + biru + "▪\n"
    banner = banner + "▐█▌██▐█▌▐█▌.▐▌▐█▌▐▌██▌.██▄▪▐█▐█▄▄▌ ▐█▌·\n"
    banner = banner + " ▀▀▀▀ ▀▪ ▀█▄▀▪.▀▀▀ ▀▀▀ ·▀▀▀▀  ▀▀▀  ▀▀▀ \n"
    banner = banner + "\n"

    banner = banner + putih2 + "Author      : "
    banner = banner + biru2 + "github@beducode\n"
    banner = banner + putih2 + "Contact     : "
    banner = banner + biru2 + "@beduplay | @riosuyanto \n"
    banner = banner + putih2 + "Version     : "
    banner = banner + biru2 + "v.1.2.0\n" + res
    print(banner)


def timeprocess(sec):
    minutes, seconds = divmod(sec, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    stopwatchx = (days, hours, minutes, seconds)

    return stopwatchx


# CLEAN PAGE
def clear():

    # WINDOWS
    if name == "nt":
        _ = system("cls")

    # MAC / LINUX
    else:
        _ = system("clear")


# FORMAT DECIMAL 8 DIGIT


def rev(num):
    if len(num) < 8:
        panjang_nol = int(8 - len(num))
        num = (panjang_nol * "0") + str(num)
        result = "0." + num
    if len(num) == 8:
        panjang_nol = int(8 - len(num))
        num = (panjang_nol * "0") + str(num)
        result = "0." + num
    else:
        len_num = len(num)
        end = num[-8:]
        first = num[: len_num - 8]
        result = first + "." + end
    return result


# FORMAT DECIMAL 10 DIGIT


def revwolf(num):
    if len(num) < 10:
        panjang_nol = int(10 - len(num))
        num = (panjang_nol * "0") + str(num)
        result = "0." + num
    if len(num) == 10:
        panjang_nol = int(10 - len(num))
        num = (panjang_nol * "0") + str(num)
        result = "0." + num
    else:
        len_num = len(num)
        end = num[-10:]
        first = num[: len_num - 10]
        result = first + "." + end
        tmprs = int(float(result) * (10 ** 10))
        result = first + "." + end
    return result


# FORMAT 11 DIGIT
def revwolfbet(num):
    if len(num) < 11:
        panjang_nol = int(11 - len(num))
        num = (panjang_nol * "0") + str(num)
        result = "0." + num
    if len(num) == 11:
        panjang_nol = int(11 - len(num))
        num = (panjang_nol * "0") + str(num)
        result = "0." + num
    else:
        len_num = len(num)
        end = num[-11:]
        first = num[: len_num - 11]
        result = first + "." + end
        tmprs = int(float(result) * (10 ** 11))
        result = first + "." + end
    return result


# REFRESH PAGE
def refresh_page():
    clear()
    banner()


# API INDODAX FOR GET LAST PRICE


def indodax(coin):
    try:
        pair = (coin).lower() + "_idr"

        url = "https://indodax.com/api/" + str(pair) + "/ticker"

        indx = c.get(url)
        jsindx = json.loads(indx.text)
        pricepair = int(jsindx["ticker"]["last"])
    except:
        coinpair = (coin).lower() + "_idr"

        url = "https://beducode-price.herokuapp.com/price/" + str(coinpair)

        price = c.get(url)
        data = json.loads(price.text)
        pricepair = data["last"]

    return pricepair


# FORMAT VALUE TO IDR


def rupiah_format(angka):
    return "Rp " + "{:0,.2f}".format(angka)


# FORMAT VALUE TO USD


def dollar_format(angka):
    return "$ " + "{:0,.2f}".format(angka)


# LIST END POINT


def navigate_api(nav):
    if nav == "start":
        endpoint = "https://wolf.bet/api/v1/user/balances"
    elif nav == "bet":
        endpoint = "https://wolf.bet/api/v1/dice/manual/play"
    elif nav == "limbo":
        endpoint = "https://wolf.bet/api/v2/limbo/manual/play"
    else:
        endpoint = "https://wolf.bet/api/v1/game/seed/refresh"

    return endpoint


def call_api(method, url, hd, dt):
    result = None
    while result is None:
        if method == "GET":
            try:
                # connect
                result = c.get(url, headers=hd, data=dt)
                if result.status_code != 200:
                    time.sleep(2)
                    result = None
                    call_api(method, url, hd, dt)
            except:
                time.sleep(2)
        else:
            try:
                # connect
                result = c.post(url, headers=hd, data=dt)
                if result.status_code != 200:
                    time.sleep(2)
                    result = None
                    call_api(method, url, hd, dt)
            except:
                time.sleep(2)

    return json.loads(result.text)


#
def resetseed():
    url = navigate_api("serverseed")

    # GET SERVER SEED
    dataseed = call_api("GET", url, auth, {})


def konverttoint(nil):
    result = int(float(nil) * (10 ** 8))
    return result


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier


def checklogin(status):
    if status is True:
        clear()
        banner()

        print(merah2 + "Periksa Kembali API key Anda Pada File settings.json" + res)
        sys.exit()
    else:
        pass


def checkcurr(val):
    if val is True:
        clear()
        banner()

        print(merah2 + "Pilihan Koin Pada File Setting.json Tidak Tersedia!" + res)
        sys.exit()
    else:
        pass


def chtab(num):
    panjangrd = len(str(num))

    if panjangrd == 1:
        tab = str(num) + "     "
    if panjangrd == 2:
        tab = str(num) + "    "
    if panjangrd == 3:
        tab = str(num) + "   "
    if panjangrd == 4:
        tab = str(num) + "  "
    if panjangrd == 5:
        tab = str(num) + " "

    return tab


# VALIDATION


# def trialexpired():
    refresh_page()

    print(
        kuning2
        + " "
        + "Account Trial Anda Sudah Expired, Silahkan Hubungi Kontak Untuk Info Lebih Lanjut!"
        + res
    )
    time.sleep(30)
    sys.exit()


# CHECK EXPIRED DATE
# def checkexpired(id, user):
    member = client.query(
        q.get(q.match(q.index("wolf_register_trial_by_id"), id)))

    nowdate = datetime.strptime(str(dateexpired()), "%d/%m/%y %H:%M:%S")
    expdate = datetime.strptime(member["data"]["expdate"], "%d/%m/%y %H:%M:%S")

    datenow = date(
        int(nowdate.strftime("%Y")),
        int(nowdate.strftime("%m")),
        int(nowdate.strftime("%d")),
    )
    dateexp = date(
        int(expdate.strftime("%Y")),
        int(expdate.strftime("%m")),
        int(expdate.strftime("%d")),
    )

    checkexp = (dateexp - datenow).days

    if checkexp < 0:
        status = 3
    else:
        status = 1

    return status


# NEW REGISTER
# def newregister(id, user):
    try:
        createacc = client.query(
            q.create(
                q.collection("scwolf_trialversion_update"),
                {"data": {"uuid": str(id), "login": str(
                    user), "member_status": "1"}},
            )
        )

        status = 2
    except:
        status = 0

    return status


# DATE NOW
# def dateenow():
    daynow = datetime.now()

    year = daynow.strftime("%Y")
    month = daynow.strftime("%m")
    day = daynow.strftime("%d")
    time = daynow.strftime("%H:%M:%S")

    date_now = daynow.strftime("%d/%m/%y %H:%M:%S")

    return date_now


# EXPIRED TIME
# def dateexpired():
    exp = datetime.now() + timedelta(days=2)

    year = exp.strftime("%Y")
    month = exp.strftime("%m")
    day = exp.strftime("%d")
    time = exp.strftime("%H:%M:%S")

    date_expired = exp.strftime("%d/%m/%y %H:%M:%S")

    return date_expired


# REGISTER TIME
# def dateregister():
    now = datetime.now()

    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")

    date_register = now.strftime("%d/%m/%y %H:%M:%S")

    return date_register


# CHECK TRIAL STATUS OR CREATE NEW ACCOUNT TRIAL
# def checktrialreg(user):
    try:
        member = client.query(
            q.get(q.match(q.index("wolf_register_trial_by_host"), user))
        )
        status = int(member["data"]["member_status"])
    except:
        createacc = client.query(
            q.create(
                q.collection("scwolf_trial_update"),
                {
                    "data": {
                        "hostname": str(user),
                        "regdate": str(dateregister()),
                        "expdate": str(dateexpired()),
                        "member_status": "1",
                    }
                },
            )
        )

        status = 2

    return status


# GET RACE INFO TRIAL
# def authfreever():
    global uuid

    username = (getpass.getuser()).lower()

    status = checktrialreg(username)

    if status == 2:
        statuscek = newregister(uuid, username)
    else:
        statuscek = checkexpired(uuid, username)

    if statuscek == 1:
        pass
    elif statuscek == 2:
        pass
    else:
        trialexpired()


# PREM VERSION
# def authpremver():
    refresh_page()

    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    try:
        inputpass = (
            biru2
            + "\r"
            + putih2
            + ">> "
            + res
            + kuning2
            + "Silahkan Masukan Kode Aktivasi Anda: "
            + res
        )
        passinput = inputimeout(prompt=inputpass, timeout=600)
        if passinput == "":
            authpremver()
        else:
            validcode = checkcodeactivated(passinput)
            if validcode == 1:
                firstregisterprem(ip, passinput)
                createfilepass(passinput)
            else:
                refresh_page()
                print("Kode Aktivasi Yang Anda Masukan Salah, Silahkan Coba Kembali")
                time.sleep(2)
                authpremver()

    except TimeoutOccurred:
        authpremver()


# def checkcodeactivated(code):
    try:
        member = client.query(
            q.get(q.match(q.index("wolf_premium_activated_by_code"), code))
        )

        status = int(member["data"]["activated_status"])

    except:
        status = 0

    return status


# CHECK PREMIUM MEMBER
# def createfilepass(passc):
    f = open("passcode.txt", "w+")
    f.write(passc)
    f.close()


# def readpass(fl):
    f = open(fl, "r")
    if f.mode == "r":
        passc = f.read()

    return passc


# def checkpremstatus(ip, code):
    try:
        member = client.query(
            q.get(q.match(q.index("wolf_premium_by_ip"), ip, code)))

        status = member["data"]["member_status"]

    except:
        status = 0

    return status


# def firstregisterprem(ip, code):
    try:
        createacc = client.query(
            q.create(
                q.collection("scwolf_premium"),
                {
                    "data": {
                        "ip": str(ip),
                        "activated_code": str(code),
                        "regdate": str(dateregister()),
                        "member_status": "1",
                    }
                },
            )
        )
        updateactivatedstatus(code)

    except:
        authpremver()


# UPDATE STATUS ACTIVATION
#  def updateactivatedstatus(code):
    try:
        member = client.query(
            q.get(q.match(q.index("wolf_premium_activated_by_code"), code))
        )
        ref = member["ref"].value["id"]
        client.query(
            q.update(
                q.ref(q.collection("scwolf_premium_activated"), ref),
                {"data": {"activated_status": "0"}},
            )
        )
    except:
        authpremver()


# VERSION VALIDATE
# def validateaccount():
    if freeversion is True:
        authfreever()
    else:
        file = pathlib.Path("passcode.txt")
        if file.exists():
            passcode = readpass(file)
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)

            check = checkpremstatus(ip, passcode)
            if int(check) != 1:
                authpremver()
            else:
                pass
        else:
            authpremver()


# VALIDATE RUNNING SCRIPT

# TARGET LOSS
def targetmaxls(pf, bl, sb, ls):
    refresh_page()
    print(putih2 + "Target Max Lose Strike Telah Tercapai!! " + res)
    print(putih2 + "Total Profit : " + res + hijau2 + rev(str(pf)) + res)
    print(putih2 + "Total Lose Strike : " + res + merah2 + str(ls) + res)
    print(putih2 + "Saldo Anda Saat Ini : " +
          res + hijau2 + revwolf(str(bl)) + res)
    print(putih2 + "Selalu Berhati-hati & Silahkan Jalankan Kembali Script" + res)
    time.sleep(1)
    sys.exit()


# TARGET BET
def cutloss(bl, sb, ls):
    refresh_page()
    ct = sb - bl
    print(putih2 + "Target Bet Telah Tercapai!! " + res)
    print(putih2 + "Loss : " + res + merah2 + revwolf(str(ct)) + res)
    print(putih2 + "Total Lose Strike : " + res + merah2 + str(ls) + res)
    print(putih2 + "Saldo Anda Saat Ini : " +
          res + hijau2 + revwolf(str(bl)) + res)
    print(putih2 + "Selalu Berhati-hati & Silahkan Jalankan Kembali Script" + res)
    time.sleep(1)
    sys.exit()


# TARGET LOSS
def targetloss(bl, sb, ls):
    refresh_page()
    tl = sb - bl
    print(putih2 + "Target Loss Telah Tercapai!! " + res)
    print(putih2 + "Total Lose : " + res + merah2 + revwolf(str(tl)) + res)
    print(putih2 + "Total Lose Strike : " + res + merah2 + str(ls) + res)
    print(putih2 + "Saldo Anda Saat Ini : " +
          res + hijau2 + revwolf(str(bl)) + res)
    print(putih2 + "Selalu Berhati-hati & Silahkan Jalankan Kembali Script" + res)
    time.sleep(1)
    sys.exit()


# TARGET PROFIT
def targetprofit(pf, bl, mb, ls):
    refresh_page()

    print(
        putih2 + "Target Profit Telah Tercapai : " +
        res + hijau2 + rev(str(pf)) + res
    )
    print(putih2 + "Max Bet Terakhir : " + res + merah2 + rev(str(mb)) + res)
    print(putih2 + "Total Lose Strike : " + res + merah2 + str(ls) + res)
    print(putih2 + "Saldo Anda Saat Ini : " +
          res + hijau2 + revwolf(str(bl)) + res)
    print(putih2 + "Selalu Berhati-hati & Silahkan Jalankan Kembali Script" + res)
    time.sleep(1)
    sys.exit()


# TARGET BALANCE
def targetbalance(pf, bl, mb, ls):
    clear()
    banner()
    print(
        putih2 + "Target Balance Telah Tercapai : " +
        res + hijau2 + rev(str(pf)) + res
    )
    print(putih2 + "Max Bet Terakhir : " + res + merah2 + rev(str(mb)) + res)
    print(putih2 + "Total Lose Strike : " + res + merah2 + str(ls) + res)
    print(putih2 + "Saldo Anda Saat Ini : " +
          res + hijau2 + revwolf(str(bl)) + res)
    print(putih2 + "Selalu Berhati-hati & Silahkan Jalankan Kembali Script" + res)
    time.sleep(1)
    sys.exit()


# STOP ON WIN
def stoponwin(pf, bl, mb, ls):
    refresh_page()

    print(
        putih2 + "Stop on win aktif, Profit Anda : " +
        res + hijau2 + rev(str(pf)) + res
    )
    print(putih2 + "Max Bet Terakhir : " + res + merah2 + rev(str(mb)) + res)
    print(putih2 + "Total Lose Strike : " + res + merah2 + str(ls) + res)
    print(putih2 + "Saldo Anda Saat Ini : " +
          res + hijau2 + revwolf(str(bl)) + res)
    print(putih2 + "Selalu Berhati-hati & Silahkan Jalankan Kembali Script" + res)
    time.sleep(1)
    sys.exit()


# FIBONACCHI CALC
def fibocal(n):
    if n <= 1:
        return n + 1
    else:
        return fibocal(n - 1) + fibocal(n - 2)


# UI RANGE CHANCE
def rangeChance(hc):
    panjangrd = len(str(hc))
    if panjangrd == 3:
        chancerand = " " + str(hc) + "   "
    if panjangrd == 4:
        chancerand = " " + str(hc) + "  "
    if panjangrd == 5:
        chancerand = " " + str(hc) + " "

    return chancerand


# LOAD TRIGER CHANCE
def loadTrigetC(num):
    result_triger = random.uniform(1, num)
    return int(result_triger)


# RANDOM CHANCE
def randomChance(min, max):
    hasil_chance = round(random.uniform(float(min), float(max)), 2)

    return hasil_chance


def settingChance(LCMin, LCMax):
    if (
        ob["Betset"][nobet]["Random Chance"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Random Chance"]["Toggle"] == "On"
        or ob["Betset"][nobet]["Random Chance"]["Toggle"] == "on"
    ):

        chanceval = randomChance(LCMin, LCMax)
        chancerand = rangeChance(chanceval)

    else:
        chanceval = float(LCMin)

        chancerand = rangeChance(chanceval)

    return chanceval, chancerand


# CORE DICE PROCESS


def dice(ws, ls):
    resultbet = 0
    valuesbet = 0
    hilostatus = False
    hilo = 0
    hilocount = 0
    overcount = 0
    undercount = 0
    no_win = 0
    no_lose = 0
    total_win = 0
    total_lose = 0
    totalprofit = 0
    maxbet = 0
    balbet = 0
    tmpbalbet = 0
    start_time = time.time()
    stats_rolebet_lose = False
    stats_rolebet_win = False
    no_rolebet = 0
    rolebet = " H "
    roleStatus = False

    MC1 = False
    MC2 = False
    CHSW1 = False
    CHSW2 = False
    condition = ""
    game = 0
    spin = 0
    marketidx = 0
    rsroll = 0
    rollcount = 0
    startbet = dt.datetime.today().timestamp()

    basebet = int(float(ob["Betset"][nobet]["Base Bet"]) * (10 ** 11))
    if (
        ob["Betset"][nobet]["Toggle HiLowSwitch"] == "on"
        or ob["Betset"][nobet]["Toggle HiLowSwitch"] == "On"
        or ob["Betset"][nobet]["Toggle HiLowSwitch"] == "on"
    ):
        hiloSwitch = int(ob["Betset"][nobet]["HiLowSwitch"])
    if (
        ob["Betset"][nobet]["Mode1"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Mode1"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Mode1"]["Toggle"] == "On"
    ):
        payin = basebet
        loseval = float(ob["Betset"][nobet]["Mode1"]["Lose"])
        winval = float(ob["Betset"][nobet]["Mode1"]["Win"])
        profitdiv = int(
            float(ob["Betset"][nobet]["Mode1"]["Profit"]) * (10 ** 8))
        tmpprofit = 0
        wincount = 0
        amount = payin

    elif (
        ob["Betset"][nobet]["Mode2"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Mode2"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Mode2"]["Toggle"] == "On"
    ):
        payin = int(float(ob["Betset"][nobet]["Mode2"]["Prebet"]) * (10 ** 11))
        Mtpreroll = float(ob["Betset"][nobet]["Mode2"]["Multipler"])
        preroll = int(ob["Betset"][nobet]["Mode2"]["Preroll"])

        temproll = preroll
        amount = payin

    elif (
        ob["Betset"][nobet]["Mode3"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Mode3"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Mode3"]["Toggle"] == "On"
    ):
        payin = int(float(ob["Betset"][nobet]["Mode3"]["Prebet"]) * (10 ** 11))
        winGet1 = int(ob["Betset"][nobet]["Mode3"]["Start Strike If Win"])
        winGet2 = int(ob["Betset"][nobet]["Mode3"]["Limit Strike If Win"])
        Mt1 = float(ob["Betset"][nobet]["Mode3"]["Start Multi"])
        Mt2 = float(ob["Betset"][nobet]["Mode3"]["Limit Multi"])

        # Multi Chance #1
        if (
            ob["Betset"][nobet]["Mode3"]["Multi Chance1"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode3"]["Multi Chance1"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode3"]["Multi Chance1"]["Toggle"] == "On"
        ):
            MC1Min = ob["Betset"][nobet]["Mode3"]["Multi Chance1"]["LCMin"]
            MC1Max = ob["Betset"][nobet]["Mode3"]["Multi Chance1"]["LCMax"]
            CHSW1 = True
        else:
            pass

        # Multi Chance #2
        if (
            ob["Betset"][nobet]["Mode3"]["Multi Chance2"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode3"]["Multi Chance2"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode3"]["Multi Chance2"]["Toggle"] == "On"
        ):
            MC2Min = ob["Betset"][nobet]["Mode3"]["Multi Chance2"]["LCMin"]
            MC2Max = ob["Betset"][nobet]["Mode3"]["Multi Chance2"]["LCMax"]
            CHSW2 = True
        else:
            pass

        go = False
        tmplose = 0
        amount = payin

    elif (
        ob["Betset"][nobet]["Mode5"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Mode5"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Mode5"]["Toggle"] == "On"
    ):
        payin = basebet
        profitdiv = int(
            float(ob["Betset"][nobet]["Mode5"]["Profit"]) * (10 ** 8))
        multi1 = float(ob["Betset"][nobet]["Mode5"]["Multi1"])
        multi2 = float(ob["Betset"][nobet]["Mode5"]["Multi2"])
        maxLS = ob["Betset"][nobet]["Mode5"]["MaxLS"]
        switchChance = int(ob["Betset"][nobet]["Mode5"]["SwitchChance"])

        # Multi Chance #1
        if (
            ob["Betset"][nobet]["Mode5"]["Multi Chance1"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode5"]["Multi Chance1"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode5"]["Multi Chance1"]["Toggle"] == "On"
        ):
            MC1Min = ob["Betset"][nobet]["Mode5"]["Multi Chance1"]["LCMin"]
            MC1Max = ob["Betset"][nobet]["Mode5"]["Multi Chance1"]["LCMax"]
            CHSW1 = True
        else:
            pass

        # Multi Chance #2
        if (
            ob["Betset"][nobet]["Mode5"]["Multi Chance2"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode5"]["Multi Chance2"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode5"]["Multi Chance2"]["Toggle"] == "On"
        ):
            MC2Min = ob["Betset"][nobet]["Mode5"]["Multi Chance2"]["LCMin"]
            MC2Max = ob["Betset"][nobet]["Mode5"]["Multi Chance2"]["LCMax"]
            CHSW2 = True
        else:
            pass

        wincount = 0
        tmpprofit = 0
        tmploss = 0
        wintry = 0

        amount = payin

    elif (
        ob["Betset"][nobet]["Mode6"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Mode6"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Mode6"]["Toggle"] == "On"
    ):
        payin = basebet
        preroll = int(ob["Betset"][nobet]["Mode6"]["Preroll"])
        profitdiv = int(
            float(ob["Betset"][nobet]["Mode6"]["Profit"]) * (10 ** 8))
        MTbet = float(ob["Betset"][nobet]["Mode6"]["Multipler"])
        switchChance = False
        MC1Min = ob["Betset"][nobet]["Mode6"]["Multi Chance1"]["LCMin"]
        MC1Max = ob["Betset"][nobet]["Mode6"]["Multi Chance1"]["LCMax"]
        CHSW1 = True
        MC2Min = ob["Betset"][nobet]["Mode6"]["Multi Chance2"]["LCMin"]
        MC2Max = ob["Betset"][nobet]["Mode6"]["Multi Chance2"]["LCMax"]
        CHSW2 = True
        tmpprofit = 0
        tmplose = 0
        limitlose = ob["Betset"][nobet]["Mode6"]["Limitlose"]
        stopbalance = 0

        dlevel = 0
        amount = payin

    elif (
        ob["Betset"][nobet]["Mode7"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Mode7"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Mode7"]["Toggle"] == "On"
    ):
        payin = int(float(ob["Betset"][nobet]["Mode7"]["Prebet"]) * (10 ** 11))
        posin = int(float(ob["Betset"][nobet]["Mode7"]["Posbet"]) * (10 ** 11))
        preroll = int(ob["Betset"][nobet]["Mode7"]["Preroll"])
        posroll = int(ob["Betset"][nobet]["Mode7"]["Posroll"])
        Mtpreroll = float(ob["Betset"][nobet]["Mode7"]["Multipler"])

        temproll = preroll
        tmplose = 0
        amount = payin

    elif (
        ob["Betset"][nobet]["Mode8"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Mode8"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Mode8"]["Toggle"] == "On"
    ):
        payin = int(float(ob["Betset"][nobet]["Mode8"]["Prebet"]) * (10 ** 11))
        roll = ob["Betset"][nobet]["Mode8"]["Preroll"]
        preroll = int(roll[8])
        tcount = int(ob["Betset"][nobet]["Mode8"]["TrigerCount"])

        # CHANCE
        CM1 = ob["Betset"][nobet]["Mode8"]["CM1"]
        CM2 = ob["Betset"][nobet]["Mode8"]["CM2"]
        CM3 = ob["Betset"][nobet]["Mode8"]["CM3"]
        CM4 = ob["Betset"][nobet]["Mode8"]["CM4"]
        CM5 = ob["Betset"][nobet]["Mode8"]["CM5"]
        CM6 = ob["Betset"][nobet]["Mode8"]["CM6"]
        CM7 = ob["Betset"][nobet]["Mode8"]["CM7"]
        CM8 = ob["Betset"][nobet]["Mode8"]["CM8"]
        CM9 = ob["Betset"][nobet]["Mode8"]["CM9"]

        MTCH = 0
        LoseChance = 1
        go = True
        temproll = preroll

        amount = payin

    elif (
        ob["Betset"][nobet]["Mode9"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Mode9"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Mode9"]["Toggle"] == "On"
    ):
        payin = int(float(ob["Betset"][nobet]["Mode9"]["Prebet"]) * (10 ** 11))
        profitdiv = int(
            float(ob["Betset"][nobet]["Mode9"]["Profit"]) * (10 ** 8))
        passroll = int(ob["Betset"][nobet]["Mode9"]["Passrol"])
        Gate = ob["Betset"][nobet]["Mode9"]["Gateway"]
        switchChance = False
        MC1Min = ob["Betset"][nobet]["Mode9"]["Multi Win"]["LCMin"]
        MC1Max = ob["Betset"][nobet]["Mode9"]["Multi Win"]["LCMax"]
        MC2Min = ob["Betset"][nobet]["Mode9"]["Multi Lose"]["LCMin"]
        MC2Max = ob["Betset"][nobet]["Mode9"]["Multi Lose"]["LCMax"]
        tmpprofit = 0
        limitlose = ob["Betset"][nobet]["Mode9"]["Limitlose"]
        stopbalance = 0
        gocount = 0
        tmplose = 0
        passcount = passroll
        tmpls = 0

        fibo = False
        fbcount = 0
        prerollStatus = True
        amount = payin

    elif (
        ob["Betset"][nobet]["Mode10"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Mode10"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Mode10"]["Toggle"] == "On"
    ):
        profitdiv = int(
            float(ob["Betset"][nobet]["Mode10"]["Profit"]) * (10 ** 8))
        payin = int(float(ob["Betset"][nobet]
                          ["Mode10"]["Prebet"]) * (10 ** 11))
        pmin = int(ob["Betset"][nobet]["Mode10"]["Pmin"])
        pmax = int(ob["Betset"][nobet]["Mode10"]["Pmax"])
        preroll = pmin
        G1 = ob["Betset"][nobet]["Mode10"]["GateOne"]
        G2 = ob["Betset"][nobet]["Mode10"]["GateTwo"]
        switchChance = False
        MC1Min = ob["Betset"][nobet]["Mode10"]["Multi Win"]["LCMin"]
        MC1Max = ob["Betset"][nobet]["Mode10"]["Multi Win"]["LCMax"]
        CHSW1 = True
        MC2Min = ob["Betset"][nobet]["Mode10"]["Multi Lose"]["LCMin"]
        MC2Max = ob["Betset"][nobet]["Mode10"]["Multi Lose"]["LCMax"]
        CHSW2 = True
        tmpprofit = 0
        limitlose = ob["Betset"][nobet]["Mode10"]["Limitlose"]
        stopbalance = 0
        gocount = 0

        fibo = False
        fbcount = 0
        amount = payin

    elif (
        ob["Betset"][nobet]["Mode11"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Mode11"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Mode11"]["Toggle"] == "On"
    ):
        # payin = basebet
        profitdiv = int(
            float(ob["Betset"][nobet]["Mode11"]["Profit"]) * (10 ** 8))
        payin = int(float(ob["Betset"][nobet]
                          ["Mode11"]["Prebet"]) * (10 ** 11))
        preroll = int(ob["Betset"][nobet]["Mode11"]["Preroll"])
        Gateway = ob["Betset"][nobet]["Mode11"]["GateWay"]
        switchChance = False
        MC1Min = ob["Betset"][nobet]["Mode11"]["Multi Win"]["LCMin"]
        MC1Max = ob["Betset"][nobet]["Mode11"]["Multi Win"]["LCMax"]
        CHSW1 = True
        MC2Min = ob["Betset"][nobet]["Mode11"]["Multi Lose"]["LCMin"]
        MC2Max = ob["Betset"][nobet]["Mode11"]["Multi Lose"]["LCMax"]
        CHSW2 = True
        maxLS = ob["Betset"][nobet]["Mode11"]["MaxLS"]
        tmpprofit = 0
        stopbalance = 0
        gocount = 0

        fibo = False
        fbcount = 0
        amount = payin

    elif (
        ob["Betset"][nobet]["Mode12"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Mode12"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Mode12"]["Toggle"] == "On"
    ):
        payin = int(float(ob["Betset"][nobet]
                          ["Mode12"]["Prebet"]) * (10 ** 11))
        profitdiv = int(
            float(ob["Betset"][nobet]["Mode12"]["Profit"]) * (10 ** 8))
        passroll = int(ob["Betset"][nobet]["Mode12"]["Passrol"])
        Gate = ob["Betset"][nobet]["Mode12"]["Gateway"]
        MTbet = float(ob["Betset"][nobet]["Mode12"]["Multipler"])
        switchChance = False
        MC1Min = ob["Betset"][nobet]["Mode12"]["Multi Win"]["LCMin"]
        MC1Max = ob["Betset"][nobet]["Mode12"]["Multi Win"]["LCMax"]
        MC2Min = ob["Betset"][nobet]["Mode12"]["Multi Lose"]["LCMin"]
        MC2Max = ob["Betset"][nobet]["Mode12"]["Multi Lose"]["LCMax"]
        # stage = 0
        tmpprofit = 0
        limitlose = ob["Betset"][nobet]["Mode12"]["Limitlose"]
        stopbalance = 0
        gocount = 0
        tmplose = 0
        passcount = passroll
        tmpls = 0

        fibo = False
        fbcount = 0
        prerollStatus = True
        amount = payin

    elif (
        ob["Betset"][nobet]["Fibonachi"]["Toggle"] == "ON"
        or ob["Betset"][nobet]["Fibonachi"]["Toggle"] == "on"
        or ob["Betset"][nobet]["Fibonachi"]["Toggle"] == "On"
    ):
        payin = basebet
        fibo = False
        fbcount = 1
        amount = payin

    else:
        amount = basebet

    while True:
        keyboard.add_hotkey(stoponwinkey, stoponwin_triger)
        rsroll += 1
        resetseedstatus = False
        gamePlay = ob["Play Game"]
        if gamePlay == "dice":
            url = navigate_api("bet")
        else:
            url = navigate_api("limbo")

        current_time = time.time()
        elapsed_time = current_time - start_time
        cy = ob["Account"]["Currency"]

        if rsroll == int(ob["Reset Seed"]):
            resetseed()
            resetseedstatus = True
            rsroll = 0

        if (
            ob["Show Price"] == "ON"
            or ob["Show Price"] == "On"
            or ob["Show Price"] == "on"
        ):
            if spin == 0:
                marketidx = indodax(cy)

            spin += 1

            if spin == 10000:
                marketidx = indodax(cy)
                spin = 1

        if (
            ob["Betset"][nobet]["Bet"]["Hi / Low"]["Toggle"] == "On"
            or ob["Betset"][nobet]["Bet"]["Hi / Low"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Bet"]["Hi / Low"]["Toggle"] == "on"
        ):
            no_rolebet += 1
            if stats_rolebet_win is True:
                if (
                    no_rolebet
                    > int(ob["Betset"][nobet]["Bet"]["Hi / Low"]["If Win"]) - 1
                ):
                    rolebet = " L "
                    roleStatus = False
                if (
                    no_rolebet
                    > int(ob["Betset"][nobet]["Bet"]["Hi / Low"]["If Win"]) * 2 - 1
                ):
                    rolebet = " H "
                    roleStatus = True
                    no_rolebet = 0
            if stats_rolebet_lose is True:
                if (
                    no_rolebet
                    > int(ob["Betset"][nobet]["Bet"]["Hi / Low"]["If Lose"]) - 1
                ):
                    rolebet = " L "
                    roleStatus = False
                if (
                    no_rolebet
                    > int(ob["Betset"][nobet]["Bet"]["Hi / Low"]["If Lose"]) * 2 - 1
                ):
                    rolebet = " H "
                    roleStatus = True
                    no_rolebet = 0
        else:
            rolebet = ob["Betset"][nobet]["Bet"]["Bet"]
            if (
                rolebet == "HI"
                or rolebet == "hi"
                or rolebet == "Hi"
                or rolebet == "High"
                or rolebet == "HIGH"
                or rolebet == "high"
            ):
                rolebet = " H "
                roleStatus = True
            elif (
                rolebet == "LO"
                or rolebet == "lo"
                or rolebet == "Lo"
                or rolebet == "Low"
                or rolebet == "LOW"
                or rolebet == "low"
            ):
                rolebet = " L "
                roleStatus = False
            else:
                refresh_page()
                print(
                    "Terjadi kesalahan pada settings.json, silahkan cek kembali file settings anda"
                )
                time.sleep(5)
                sys.exit()

        # MODE6
        if (
            ob["Betset"][nobet]["Mode6"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode6"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode6"]["Toggle"] == "On"
        ):
            if switchChance is False:
                MC1 = True
                MC2 = False
            else:
                MC1 = False
                MC2 = True

        # MODE9
        if (
            ob["Betset"][nobet]["Mode9"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode9"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode9"]["Toggle"] == "On"
        ):
            if switchChance is False:
                MC1 = True
                MC2 = False
            else:
                MC1 = False
                MC2 = True

        # MODE10
        if (
            ob["Betset"][nobet]["Mode10"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode10"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode10"]["Toggle"] == "On"
        ):
            if switchChance is False:
                MC1 = True
                MC2 = False
            else:
                MC1 = False
                MC2 = True

        # MODE11
        if (
            ob["Betset"][nobet]["Mode11"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode11"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode11"]["Toggle"] == "On"
        ):
            if switchChance is False:
                MC1 = True
                MC2 = False
            else:
                MC1 = False
                MC2 = True

        # MODE12
        if (
            ob["Betset"][nobet]["Mode12"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode12"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode12"]["Toggle"] == "On"
        ):
            if switchChance is False:
                MC1 = True
                MC2 = False
            else:
                MC1 = False
                MC2 = True

        if (
            ob["Betset"][nobet]["Mode8"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode8"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode8"]["Toggle"] == "On"
        ):
            if go is True:
                tc = loadTrigetC(tcount)
                if tc == 1:
                    chanceval, chancerand = settingChance(CM1[0], CM1[0])
                    MTCH = CM1[1]
                    preroll = int(roll[0])
                elif tc == 2:
                    chanceval, chancerand = settingChance(CM2[0], CM2[0])
                    MTCH = CM2[1]
                    preroll = int(roll[1])
                elif tc == 3:
                    chanceval, chancerand = settingChance(CM3[0], CM3[0])
                    MTCH = CM3[1]
                    preroll = int(roll[2])
                elif tc == 4:
                    chanceval, chancerand = settingChance(CM4[0], CM4[0])
                    MTCH = CM4[1]
                    preroll = int(roll[3])
                elif tc == 5:
                    chanceval, chancerand = settingChance(CM5[0], CM5[0])
                    MTCH = CM5[1]
                    preroll = int(roll[4])
                elif tc == 6:
                    chanceval, chancerand = settingChance(CM6[0], CM6[0])
                    MTCH = CM6[1]
                    preroll = int(roll[5])
                elif tc == 7:
                    chanceval, chancerand = settingChance(CM7[0], CM7[0])
                    MTCH = CM7[1]
                    preroll = int(roll[6])
                elif tc == 8:
                    chanceval, chancerand = settingChance(CM8[0], CM8[0])
                    MTCH = CM8[1]
                    preroll = int(roll[7])
                else:
                    chanceval, chancerand = settingChance(CM9[0], CM9[0])
                    MTCH = CM9[1]
                    preroll = int(roll[8])
            else:
                if LoseChance == 1:
                    chanceval, chancerand = settingChance(CM1[0], CM1[0])
                    MTCH = CM1[1]
                elif LoseChance == 2:
                    chanceval, chancerand = settingChance(CM2[0], CM2[0])
                    MTCH = CM2[1]
                elif LoseChance == 3:
                    chanceval, chancerand = settingChance(CM3[0], CM3[0])
                    MTCH = CM3[1]
                elif LoseChance == 4:
                    chanceval, chancerand = settingChance(CM4[0], CM4[0])
                    MTCH = CM4[1]
                elif LoseChance == 5:
                    chanceval, chancerand = settingChance(CM5[0], CM5[0])
                    MTCH = CM5[1]
                elif LoseChance == 6:
                    chanceval, chancerand = settingChance(CM6[0], CM6[0])
                    MTCH = CM6[1]
                elif LoseChance == 7:
                    chanceval, chancerand = settingChance(CM7[0], CM7[0])
                    MTCH = CM7[1]
                elif LoseChance == 8:
                    chanceval, chancerand = settingChance(CM8[0], CM8[0])
                    MTCH = CM8[1]
                else:
                    chanceval, chancerand = settingChance(CM9[0], CM9[0])
                    MTCH = CM9[1]
        else:
            # CHANCE SETTINGS
            if MC1 is True:
                LCMin = MC1Min
                LCMax = MC1Max
                MC2 = False
                chanceval, chancerand = settingChance(LCMin, LCMax)
            elif MC2 is True:
                LCMin = MC2Min
                LCMax = MC2Max
                MC1 = False
                chanceval, chancerand = settingChance(LCMin, LCMax)
            else:
                if (
                    ob["Betset"][nobet]["Random Chance"]["Toggle"] == "ON"
                    or ob["Betset"][nobet]["Random Chance"]["Toggle"] == "On"
                    or ob["Betset"][nobet]["Random Chance"]["Toggle"] == "on"
                ):
                    LCMin = ob["Betset"][nobet]["Random Chance"]["Min"]
                    LCMax = ob["Betset"][nobet]["Random Chance"]["Max"]
                    chanceval, chancerand = settingChance(LCMin, LCMax)
                else:
                    LCMin = ob["Betset"][nobet]["Chance"]
                    LCMax = 0
                    chanceval, chancerand = settingChance(LCMin, LCMax)

        if hilostatus is True:
            hilocount = 0
            if hilo == 1:
                roleStatus = True
                rolebet = " H "
            else:
                roleStatus = False
                rolebet = " L "

        if roleStatus is True:
            condition = "over"
            game = 9999 - (chanceval * 100)
        else:
            condition = "under"
            game = chanceval * 100

        if gamePlay == "dice":
            multiplier = round_half_up(99 / chanceval, 4)
        else:
            multiplier = round_half_up(99 / chanceval)

        bet_value = round(game / 100, 2)

        betamount = int(amount / 1000)

        if gamePlay == "dice":
            bet = {
                "currency": (cy).lower(),
                "game": str(gamePlay),
                "amount": rev(str(betamount)),
                "rule": condition,
                "multiplier": str(multiplier),
                "bet_value": str(bet_value)
            }
        else:
            bet = {
                "currency": (cy).lower(),
                "game": str(gamePlay),
                "amount": rev(str(betamount)),
                "rule": condition,
                "multiplier": str(multiplier),
                "auto": "1",
            }

        betting = call_api("POST", url, auth, bet)

        if (
            ob["Betset"][nobet]["Toggle HiLowSwitch"] == "ON"
            or ob["Betset"][nobet]["Toggle HiLowSwitch"] == "On"
            or ob["Betset"][nobet]["Toggle HiLowSwitch"] == "on"
        ):
            if hilocount > hiloSwitch and hilostatus is False:
                hilostatus = True
                if overcount < undercount:
                    hilo = 0
                else:
                    hilo = 1
            else:
                hilocount += 1

        if "error" in betting:
            refresh_page()
            msgError = betting["error"]["message"]
            if "insufficient balance" in msgError:
                print("Balance " + str((cy).lower()) + " Anda Tidak Mencukupi!")
            else:
                print(msgError)

            time.sleep(2)
            sys.exit()
        else:
            pass

        profit = betting["bet"]["profit"]
        state = betting["bet"]["state"]
        nonce = int(betting["bet"]["nonce"])

        bal = int(amount)
        amountbal = int(float(betting["userBalance"]["amount"]) * (10 ** 10))
        losstarget = int(float(ob["Lose Target"]) * (10 ** 10))
        calctarget = startbals - losstarget

        # EXIT JIKA BALANCE KURANG DARI TARGET LOSS
        if losstarget > 0:
            if amountbal <= losstarget:
                targetloss(amountbal, startbals, total_lose)
            else:
                pass
        else:
            pass

        if (
            ob["Betset"][nobet]["Mode1"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode1"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode1"]["Toggle"] == "On"
        ):
            if state == "win":
                no_win += 1
                no_lose = 0
                go = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                # resetseed()
                # # rollcount = 0
                # resetseedstatus = True
                # rsroll = 0

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                wincount += 1
                if totalprofit > (tmpprofit + profitdiv):
                    wincount = 0
                    tmpprofit = totalprofit
                    amount = payin
                else:
                    amount = amount * winval

            else:
                no_lose += 1
                no_win = 0
                go = False
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                wincount = 0
                amount = amount * loseval

        elif (
            ob["Betset"][nobet]["Mode2"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode2"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode2"]["Toggle"] == "On"
        ):
            if state == "win":
                no_win += 1
                no_lose = 0
                go = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                # resetseed()
                # # rollcount = 0
                # resetseedstatus = True
                # rsroll = 0

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                amount = int(payin)
                preroll = int(ob["Betset"][nobet]["Mode2"]["Preroll"])

            else:
                no_lose += 1
                no_win = 0
                preroll -= 1
                go = False
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                if preroll == 0:
                    amount = int(basebet)
                    prerollStatus = False
                elif preroll < 0:
                    amount = int(amount) * Mtpreroll
                else:
                    amount = int(payin)

        elif (
            ob["Betset"][nobet]["Mode3"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode3"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode3"]["Toggle"] == "On"
        ):
            if state == "win":
                no_win += 1
                no_lose = 0
                go = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                # resetseed()
                # # rollcount = 0
                # resetseedstatus = True
                # rsroll = 0

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                if no_win == winGet1 and go is True:
                    MC1 = False
                    MC2 = True
                    if tmplose != 0:
                        amount = int(tmplose) * Mt1
                    else:
                        amount = int(basebet) * Mt1

                if (
                    int(ob["Betset"][nobet]["Mode3"]
                        ["Limit Strike If Win"]) == 0
                    and total_win != 0
                ):
                    winGet2 = total_win
                else:
                    winGet2 = 1

                if no_win > winGet1 and no_win <= winGet2 and go is True:
                    amount = int(basebet) * Mt2
                    MC1 = True
                    MC2 = False

                if no_win > winGet2 and go is True:
                    MC1 = True
                    MC2 = False
                    tmplose = 0
                    go = False
                    amount = int(payin)

            else:
                no_lose += 1
                no_win = 0
                go = False
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                MC1 = True
                MC2 = False

                if no_lose == 1:
                    if amount > payin:
                        tmplose = int(amount)
                        amount = int(payin)
                    else:
                        amount = int(payin)
                else:
                    amount = int(payin)

        elif (
            ob["Betset"][nobet]["Mode5"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode5"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode5"]["Toggle"] == "On"
        ):

            if state == "win":
                no_win += 1
                tmpnolose = no_lose
                no_lose = 0
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                # resetseed()
                # # rollcount = 0
                # resetseedstatus = True
                # rsroll = 0

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if maxLS == "OFF" or maxLS == "Off" or maxLS == "Off":
                        pass
                    else:
                        if total_lose >= int(maxLS):
                            targetmaxls(totalprofit, amountbal,
                                        startbals, total_lose)

                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + profcolor
                        + putih2
                        + rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + profcolor
                        + putih2
                        + rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                tmploss = 0
                wintry = 0
                MC1 = False
                MC2 = False
                amount = int(payin)

            else:
                no_lose += 1
                no_win = 0
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + losecolor
                        + putih2
                        + rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + losecolor
                        + putih2
                        + rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                if CHSW1 is True and CHSW2 is True:
                    if no_lose <= switchChance:
                        MC1 = True
                        MC2 = False
                        amount = int(amount) * multi1
                        tmploss = tmploss + int(amount)
                    else:
                        wintry += 1
                        MC1 = False
                        MC2 = True
                        if wintry == 1:
                            amount = tmploss * multi2
                        else:
                            amount = int(amount) * multi2
                else:
                    MC1 = True
                    MC2 = False
                    amount = int(amount) * multi1

        elif (
            ob["Betset"][nobet]["Mode6"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode6"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode6"]["Toggle"] == "On"
        ):
            if state == "win":
                no_win += 1
                no_lose = 0
                go = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                stopbalance = wdbalance - ((wdbalance * int(limitlose)) / 100)

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                switchChance = False
                dlevel = 0
                tmplose = 0
                amount = payin
                preroll = int(ob["Betset"][nobet]["Mode6"]["Preroll"])

            else:
                no_lose += 1
                no_win = 0
                preroll -= 1
                go = False
                switchChance = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                dlevel += 1
                if preroll == 0:
                    if tmplose > 0:
                        amount = int(tmplose)
                    else:
                        amount = payin
                elif preroll < 0:
                    amount = amount * MTbet
                else:
                    amount = int(payin) + (payin * dlevel)
                    tmplose = tmplose + amount

        elif (
            ob["Betset"][nobet]["Mode7"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode7"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode7"]["Toggle"] == "On"
        ):
            if state == "win":
                no_win += 1
                no_lose = 0
                go = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                # resetseed()
                # # rollcount = 0
                # resetseedstatus = True
                # rsroll = 0

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                amount = int(payin)
                tmplose = 0
                preroll = int(ob["Betset"][nobet]["Mode7"]["Preroll"])
                posroll = int(ob["Betset"][nobet]["Mode7"]["Posroll"])

            else:
                no_lose += 1
                no_win = 0
                preroll -= 1
                posroll -= 1
                go = False
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                if preroll == 0:
                    amount = int(posin)
                    prerollStatus = False
                elif preroll < 0:
                    if posroll == 0:
                        amount = int(tmplose)
                    elif posroll < 0:
                        amount = int(amount) * Mtpreroll
                    else:
                        amount = int(amount) * Mtpreroll
                        tmplose = tmplose + amount
                else:
                    amount = int(payin)

        elif (
            ob["Betset"][nobet]["Mode8"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode8"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode8"]["Toggle"] == "On"
        ):
            if state == "win":
                no_win += 1
                no_lose = 0
                go = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                temproll = preroll
                # resetseed()
                # # rollcount = 0
                # resetseedstatus = True
                # rsroll = 0

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                # BET
                amount = int(payin)

            else:
                no_lose += 1
                no_win = 0
                preroll -= 1
                go = False
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                temproll = preroll

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                if tc == 1:
                    LoseChance = 1
                elif tc == 2:
                    LoseChance = 2
                elif tc == 3:
                    LoseChance = 3
                elif tc == 4:
                    LoseChance = 4
                elif tc == 5:
                    LoseChance = 5
                elif tc == 6:
                    LoseChance = 6
                elif tc == 7:
                    LoseChance = 7
                elif tc == 8:
                    LoseChance = 8
                else:
                    LoseChance = 9

                # BET
                if preroll == 0:
                    amount = int(basebet)

                elif preroll < 0:
                    amount = int(amount) * float(MTCH)
                else:
                    amount = int(payin)

        elif (
            ob["Betset"][nobet]["Mode9"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode9"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode9"]["Toggle"] == "On"
        ):
            if state == "win":
                no_win += 1
                no_lose = 0
                go = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                stopbalance = wdbalance - ((wdbalance * int(limitlose)) / 100)

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                # BET SETTING
                switchChance = False
                if totalprofit >= (tmpprofit + profitdiv):
                    gocount = 0
                    fbcount = 0
                    tmplose = 0
                    tmpprofit = totalprofit
                    amount = payin
                    passcount = passroll
                else:
                    gocount = 0
                    amount = payin
                    passcount = passroll

            else:
                no_lose += 1
                no_win = 0
                go = False
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                switchChance = True
                if passcount == 1:
                    if gocount == int(Gate):
                        amount = int(basebet) * fibocal(fbcount)
                        gocount = 0
                        passcount = passroll
                        fbcount += 1
                    else:
                        amount = int(basebet) * fibocal(fbcount)

                    gocount += 1
                else:
                    passcount -= 1
                    amount = payin

        elif (
            ob["Betset"][nobet]["Mode10"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode10"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode10"]["Toggle"] == "On"
        ):
            fibo = True
            if state == "win":
                no_win += 1
                no_lose = 0
                go = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                stopbalance = wdbalance - ((wdbalance * int(limitlose)) / 100)

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                switchChance = False
                if totalprofit > (tmpprofit + profitdiv):
                    gocount = 0
                    fbcount = 0
                    tmpprofit = totalprofit
                    preroll = round(random.uniform(pmin, pmax))
                    amount = payin
                else:
                    gocount = 0
                    preroll = round(random.uniform(pmin, pmax))
                    amount = payin

            else:
                no_lose += 1
                no_win = 0
                preroll -= 1
                go = False
                switchChance = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                if preroll <= 0:
                    gocount += 1
                    if gocount == 1:
                        if fbcount == 0:
                            amount = int(basebet)
                        else:
                            fbcount += 1
                            amount = int(basebet) * fibocal(fbcount)

                    if gocount == int(G1) + 1:
                        fbcount += 1
                        amount = int(basebet) * fibocal(fbcount)

                    if gocount == int(G2) + 1:
                        gocount = 0
                        preroll = round(random.uniform(int(G1), int(G2)))
                        amount = payin
                else:
                    amount = int(payin)

        elif (
            ob["Betset"][nobet]["Mode11"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode11"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode11"]["Toggle"] == "On"
        ):
            fibo = True
            if state == "win":
                no_win += 1
                no_lose = 0
                go = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if maxLS == "OFF" or maxLS == "Off" or maxLS == "Off":
                        pass
                    else:
                        if total_lose >= int(maxLS):
                            targetmaxls(totalprofit, amountbal,
                                        startbals, total_lose)

                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                switchChance = False
                if totalprofit >= (tmpprofit + profitdiv):
                    gocount = 0
                    fbcount = 0
                    tmpprofit = totalprofit
                    preroll = int(ob["Betset"][nobet]["Mode11"]["Preroll"])
                    amount = payin
                else:
                    gocount = 0
                    preroll = int(ob["Betset"][nobet]["Mode11"]["Preroll"])
                    amount = payin

            else:
                no_lose += 1
                no_win = 0
                preroll -= 1
                go = False
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                switchChance = True
                if preroll <= 0:
                    if gocount == int(Gateway):
                        fbcount += 1
                        amount = int(basebet) * fibocal(fbcount)
                        gocount = 0
                    else:
                        amount = int(basebet) * fibocal(fbcount)

                    gocount += 1
                else:
                    amount = int(payin)

        elif (
            ob["Betset"][nobet]["Mode12"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode12"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode12"]["Toggle"] == "On"
        ):
            if state == "win":
                no_win += 1
                no_lose = 0
                go = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                stopbalance = wdbalance - ((wdbalance * int(limitlose)) / 100)

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                # BET SETTING
                switchChance = False
                if totalprofit >= (tmpprofit + profitdiv):
                    gocount = 0
                    fbcount = 0
                    tmplose = 0
                    tmpprofit = totalprofit
                    amount = payin
                    passcount = passroll
                    # stage = 0
                else:
                    passcount = passroll
                    gocount = 0
                    amount = payin

            else:
                no_lose += 1
                no_win = 0
                go = False
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                switchChance = True
                if passcount == 0:
                    if gocount == int(Gate):
                        amount = int(basebet) * MTbet
                        gocount = 0
                        passcount = passroll
                        # stage += 1
                        fbcount += 1
                    else:
                        if tmplose == 0:
                            amount = int(basebet) * MTbet
                            tmplose = amount
                        else:
                            amount = int(tmplose) * MTbet
                            tmplose = amount

                    gocount += 1
                else:
                    passcount -= 1
                    amount = payin

        elif (
            ob["Betset"][nobet]["Fibonachi"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Fibonachi"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Fibonachi"]["Toggle"] == "On"
        ):
            fibo = True
            if state == "win":
                no_win += 1
                no_lose = 0
                fbcount = 0
                go = True
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal
                # resetseed()
                # # rollcount = 0
                # resetseedstatus = True
                # rsroll = 0

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if balbet > tmpbalbet:
                    tmpbalbet = balbet
                    balbet = 0
                else:
                    tmpbalbet = tmpbalbet
                    balbet = 0

                if totalprofit > 0:
                    if stoponwinactivated is True:
                        stoponwin(totalprofit, amountbal, maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                amount = int(payin)

            else:
                no_lose += 1
                no_win = 0
                go = False
                totalprofit = totalprofit + int(float(profit) * (10 ** 8))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                fbcount += 1
                amount = int(payin) * fibocal(fbcount)
        else:
            if state == "win":
                no_lose += 1
                no_win = 0
                totalprofit = totalprofit + int(float(profit) * (10 ** 10))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                # resetseed()
                # # rollcount = 0
                # resetseedstatus = True
                # rsroll = 0

                hilocount = 0
                hilostatus = False
                undercount = 0
                overcount = 0

                if betamount > maxbet:
                    maxbet = betamount

                if totalprofit > 0:
                    if totalprofit >= int(float(ob["Target Profit"]) * (10 ** 8)):
                        targetprofit(totalprofit, amountbal,
                                     maxbet, total_lose)

                    if totalprofit >= int(float(ob["Target Win"]) * (10 ** 8)):
                        targetbalance(totalprofit, amountbal,
                                      maxbet, total_lose)

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + profcolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + hijau2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                amount = int(amount) * float(ob["Betset"][nobet]["If Win"])

            else:
                no_lose += 1
                no_win = 0
                totalprofit = totalprofit + int(float(profit) * (10 ** 10))
                wdbalance = float(int(amountbal)) / (10 ** 10)
                lastprice = marketidx
                wd = rupiah_format(lastprice * wdbalance)
                balbet = balbet + bal

                if totalprofit > 0:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + hijau2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )
                else:
                    print(
                        rccolor
                        + rcfontcolor
                        + chancerand
                        + res
                        + losecolor
                        + putih2
                        + str(rolebet)
                        + res
                        + " "
                        + merah2
                        + "+"
                        + revwolfbet(str(bal))
                        + res
                        + biru2
                        + " Balance"
                        + res
                        + " : "
                        + revwolf(str(amountbal))
                        + res
                        + merah2
                        + " Profit"
                        + res
                        + " : "
                        + rev(str(totalprofit))
                        + res
                        + kuning2
                        + " Wallet"
                        + res
                        + " : "
                        + str(wd)
                        + res
                    )

                amount = int(amount) * float(ob["Betset"][nobet]["If Lose"])

        if no_win > total_win:
            stats_rolebet_win = True
            stats_rolebet_lose = False
            total_win += 1
        if no_lose > total_lose:
            stats_rolebet_lose = True
            stats_rolebet_win = False
            total_lose += 1

        # STOP BET
        if (
            ob["Betset"][nobet]["Mode6"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode6"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode6"]["Toggle"] == "On"
        ):
            if stopbalance == 0:
                stopbalance = wdbalance - ((wdbalance * int(limitlose)) / 100)

            if wdbalance <= stopbalance:
                cutloss(amountbal, startbals, total_lose)

        if (
            ob["Betset"][nobet]["Mode9"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode9"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode9"]["Toggle"] == "On"
        ):
            if stopbalance == 0:
                stopbalance = wdbalance - ((wdbalance * int(limitlose)) / 100)

            if wdbalance <= stopbalance:
                cutloss(amountbal, startbals, total_lose)

        if (
            ob["Betset"][nobet]["Mode10"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode10"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode10"]["Toggle"] == "On"
        ):
            if stopbalance == 0:
                stopbalance = wdbalance - ((wdbalance * int(limitlose)) / 100)

            if wdbalance <= stopbalance:
                cutloss(amountbal, startbals, total_lose)

        if (
            ob["Betset"][nobet]["Mode12"]["Toggle"] == "ON"
            or ob["Betset"][nobet]["Mode12"]["Toggle"] == "on"
            or ob["Betset"][nobet]["Mode12"]["Toggle"] == "On"
        ):
            if stopbalance == 0:
                stopbalance = wdbalance - ((wdbalance * int(limitlose)) / 100)

            if wdbalance <= stopbalance:
                cutloss(amountbal, startbals, total_lose)

        mbTextStatus = (
            " " + rccolor + rcfontcolor + " MB " + rev(str(maxbet)) + " " + res
        )

        rollcount += 1

        time_diff = dt.datetime.today().timestamp() - startbet

        speedbet = round(rollcount / time_diff)

        speedBetText = (
            rccolor + rcfontcolor + " " +
            str(speedbet) + " Bet/Sec" + " " + res
        )

        timelabel = (
            Style.NORMAL
            + Back.WHITE
            + Fore.BLACK
            + " "
            + "%dD %dH %dM %dS" % timeprocess(int(elapsed_time))
            + " "
            + res
        )

        pricekoin = (
            rccolor + rcfontcolor + " " +
            str(rupiah_format(marketidx)) + " " + res
        )

        sys.stdout.write(
            " "
            + res
            + profcolor
            + putih2
            + " WS "
            + str(total_win)
            + " "
            + res
            + " "
            + losecolor
            + putih2
            + " LS "
            + str(total_lose)
            + " "
            + res
            + " "
            + rccolor
            + rcfontcolor
            + " CS "
            + str(no_lose)
            + " "
            + res
            + mbTextStatus
            + res
            + " "
            + speedBetText
            + " "
            + pricekoin
            + " "
            + timelabel
            + "\r"
        )


refresh_page()
url = navigate_api("start")
sdata = call_api("GET", url, auth, {})
invalidlogin = False
if "error" in sdata:
    invalidlogin = True
    checklogin(invalidlogin)
else:
    checklogin(invalidlogin)

# VALIDASI ACCOUNT
# validateaccount()

refresh_page()
i = 0
setawal = True
falsecurr = False
while setawal is True:
    for key in sdata:
        curr = sdata["balances"][i]["currency"]
        bals = int(float(sdata["balances"][i]["amount"]) * (10 ** 10))
        pilcurr = ob["Account"]["Currency"]
        if (curr).lower() == (pilcurr).lower():
            setawal = False
            falsecurr = False
        else:
            i += 1
            if i >= 11:
                pass
            falsecurr = True

# CHECK CURRENCY
checkcurr(falsecurr)
resetseed()
try:
    print(
        profcolor + putih2 + " Balance ",
        res
        + revwolf(str(bals))
        + " "
        + (curr).upper()
        + res
        + " | "
        + res
        + (ob["Play Game"]).upper()
        + " GAME",
    )
    startbals = bals
except:
    sys.exit()

dice(
    int(float(ob["Target Win"]) * (10 ** 8)
        ), int(float(ob["Lose Target"]) * (10 ** 8))
)


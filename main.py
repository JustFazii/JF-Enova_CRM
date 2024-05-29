import eel
from functions.APIGetEcho import APIGetEcho
from functions.APIUpdateStatus import APIUpdateStatus
from functions.APIGetContractors import APIGetContractors
from functions.APIAddContractor import APIAddContractor
from functions.APIUpdateContractor import APIUpdateContractor

@eel.expose
def send_echo(param):
    print(param)
    app = APIGetEcho()
    result = app.send_request(param)
    return result

@eel.expose
def refresh_contractors():
    app = APIGetContractors()
    result = app.send_request("")
    return result

@eel.expose
def update_status():
    app = APIUpdateStatus()
    result = app.send_request("")
    data = result
    return data

@eel.expose
def add_contractor(data):
    app = APIAddContractor()
    result = app.send_request(data)
    return result

@eel.expose
def update_contractor(data):
    app = APIUpdateContractor()
    result = app.send_request(data)
    return result

if __name__ == "__main__":
    eel.init('ui')
    eel.start('index.html', mode='electron')
    while True:
        eel.sleep(1)
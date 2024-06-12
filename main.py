import eel
from app.env_file import SESSION_TOKEN, USER_TOKEN
from api.APIRefreshToken import APIRefreshToken
from app.APPSetSettings import APPSetSettings
from app.APPGetSettings import APPGetSettings
from api.APILogin import APILogin
from api.APILogout import APILogout
from api.APIStatus import APIStatus
from api.APIGetContractors import APIGetContractors
from api.APIGetContractorByID import APIGetContractorByID
from api.APIAddContractor import APIAddContractor
from api.APIUpdateContractor import APIUpdateContractor
from api.APIGetDocumentsZO import APIGetZODocuments
from api.APIGetDocumentsZD import APIGetZDDocuments
from api.APIGetDocumentsPositions import APIGetDocumentsPositions
from api.APICreateZOFVRelation import APICreateZOFVRelation
from api.APICreateZDZKRelation import APICreateZDZKRelation
from api.APIGenerateInvoiceFV import APIGenerateInvoiceFV
from api.APIGenerateInvoiceZK import APIGenerateInvoiceZK
from api.APIGetGoods import APIGetGoods
from api.APIGetInvoices import APIGetInvoices
from api.APIPassEcho import APIPassEcho

@eel.expose
def GetSettings():
    print("Called APPGetSettings")
    APP = APPGetSettings()
    result = APP.getsettings()
    print("Returning APPGetSettings")
    return result

@eel.expose
def SetSettings(ip, port):
    print("Called APPSetSettings")
    APP = APPSetSettings()
    result = APP.setsettings(ip, port)
    print("Returning APPSetSettings")
    return result

@eel.expose
def RefreshToken():
    print("Called APIRefreshToken")
    API = APIRefreshToken()
    result = API.request(USER_TOKEN)
    print("Returning APIRefreshToken")
    return result

@eel.expose
def Login(token):
    print("Called APILogin")
    API = APILogin()
    result = API.request(token)
    print("Returning APILogin")
    return result

@eel.expose
def Logout():
    print("Called APILogout")
    API = APILogout()
    result = API.request()
    print("Returning APILogout")
    return result

@eel.expose
def Status():
    print("Called APIStatus")
    API = APIStatus()
    result = API.request()
    print("Returning APIStatus")
    return result

@eel.expose
def GetContractors():
    print("Called APIGetContractors")
    API = APIGetContractors()
    result = API.request()
    print("Returning APIGetContractors")
    return result

@eel.expose
def GetContractorByID(id):
    print("Called APIGetContractorByID")
    API = APIGetContractorByID()
    result = API.request(id)
    print("Returning APIGetContractorByID")
    return result

@eel.expose
def AddContractor(data):
    print("Called APIAddContractor")
    API = APIAddContractor()
    result = API.request(data)
    print("Returning APIAddContractor")
    return result

@eel.expose
def UpdateContractor(data):
    print("Called APIUpdateContractor")
    API = APIUpdateContractor()
    result = API.request(data)
    print("Returning APIUpdateContractor")
    return result

@eel.expose
def GetZODocuments():
    print("Called APIGetZODocuments")
    API = APIGetZODocuments()
    result = API.request()
    print("Returning APIGetZODocuments")
    return result

@eel.expose
def GetZDDocuments():
    print("Called APIGetZDDocuments")
    API = APIGetZDDocuments()
    result = API.request()
    print("Returning APIGetZDDocuments")
    return result

@eel.expose
def GetDocumentsPositions(id):
    print("Called APIGetDocumentsPositions")
    API = APIGetDocumentsPositions()
    result = API.request(id)
    print("Returning APIGetDocumentsPositions")
    return result

@eel.expose
def CreateZOFVRelation(id):
    print("Called APICreateZOFVRelation")
    API = APICreateZOFVRelation()
    result = API.request(id)
    print("Returning APICreateZOFVRelation")
    return result

@eel.expose
def CreateZDZKRelation(id):
    print("Called APICreateZDZKRelation")
    API = APICreateZDZKRelation()
    result = API.request(id)
    print("Returning APICreateZDZKRelation")
    return result

@eel.expose
def GenerateInvoiceFV(id):
    print("Called APIGenerateInvoiceFV")
    API = APIGenerateInvoiceFV()
    result = API.request(id)
    print("Returning APIGenerateInvoiceFV")
    return result

@eel.expose
def GenerateInvoiceZK(id):
    print("Called APIGenerateInvoiceZK")
    API = APIGenerateInvoiceZK()
    result = API.request(id)
    print("Returning APIGenerateInvoiceZK")
    return result

@eel.expose
def GetGoods():
    print("Called APIGetGoods")
    API = APIGetGoods()
    result = API.request()
    print("Returning APIGetGoods")
    return result

@eel.expose
def GetInvoices():
    print("Called APIGetInvoices")
    API = APIGetInvoices()
    result = API.request()
    print("Returning APIGetInvoices")
    return result

@eel.expose
def PassEcho(string):
    print("Called APIPassEcho")
    API = APIPassEcho()
    result = API.request(string)
    print("Returning APIPassEcho")
    return result

if __name__ == "__main__":
    eel.init('ui')
    eel.start('index.html', mode='electron')
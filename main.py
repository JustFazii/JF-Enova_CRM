import eel
from app.env_file import USER_TOKEN
from api.APIRefreshToken import APIRefreshToken
from app.APPSetSettings import APPSetSettings
from app.APPGetSettings import APPGetSettings
from api.APILogin import APILogin
from api.APILogout import APILogout
from api.APIStatus import APIStatus
from api.APIGetContractors import APIGetContractors
from api.APIGetContractorsDokHan import APIGetContractorsDokHan
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
from api.APIGetGoodsDocHan import APIGetGoodsDocHan
from api.APIGetGoodsByID import APIGetGoodsByID
from api.APIGetInvoices import APIGetInvoices
from api.APIAddHandelDocument import APIAddHandelDocument
from api.APIPassEcho import APIPassEcho

@eel.expose
def GetSettings():
    APP = APPGetSettings()
    result = APP.getsettings()
    return result

@eel.expose
def SetSettings(ip, port):
    APP = APPSetSettings()
    result = APP.setsettings(ip, port)
    return result

@eel.expose
def RefreshToken():
    API = APIRefreshToken()
    result = API.request(USER_TOKEN)
    return result

@eel.expose
def Login(token):
    API = APILogin()
    result = API.request(token)
    return result

@eel.expose
def Logout():
    API = APILogout()
    result = API.request()
    return result

@eel.expose
def Status():
    API = APIStatus()
    result = API.request()
    return result

@eel.expose
def GetContractors():
    API = APIGetContractors()
    result = API.request()
    return result

@eel.expose
def GetContractorsDokHan():
    API = APIGetContractorsDokHan()
    result = API.request()
    return result

@eel.expose
def GetContractorByID(id):
    API = APIGetContractorByID()
    result = API.request(id)
    return result

@eel.expose
def AddContractor(data):
    API = APIAddContractor()
    result = API.request(data)
    return result

@eel.expose
def UpdateContractor(data):
    API = APIUpdateContractor()
    result = API.request(data)
    return result

@eel.expose
def GetZODocuments():
    API = APIGetZODocuments()
    result = API.request()
    return result

@eel.expose
def GetZDDocuments():
    API = APIGetZDDocuments()
    result = API.request()
    return result

@eel.expose
def GetDocumentsPositions(id):
    print(id)
    API = APIGetDocumentsPositions()
    result = API.request(id)
    return result

@eel.expose
def CreateZOFVRelation(id):
    API = APICreateZOFVRelation()
    result = API.request(id)
    return result

@eel.expose
def CreateZDZKRelation(id):
    API = APICreateZDZKRelation()
    result = API.request(id)
    return result

@eel.expose
def GenerateInvoiceFV(id):
    API = APIGenerateInvoiceFV()
    result = API.request(id)
    return result

@eel.expose
def GenerateInvoiceZK(id):
    API = APIGenerateInvoiceZK()
    result = API.request(id)
    return result

@eel.expose
def GetGoods():
    API = APIGetGoods()
    result = API.request()
    return result

@eel.expose
def GetGoodsDocHan():
    API = APIGetGoodsDocHan()
    result = API.request()
    return result

@eel.expose
def GetGoodsByID(id):
    API = APIGetGoodsByID()
    result = API.request(id)
    return result

@eel.expose
def GetInvoices():
    API = APIGetInvoices()
    result = API.request()
    return result

@eel.expose
def AddHandelDocument(data):
    API = APIAddHandelDocument()
    result = API.request(data)
    return result

@eel.expose
def PassEcho(string):
    API = APIPassEcho()
    result = API.request(string)
    return result

if __name__ == "__main__":
    eel.init('ui')
    eel.start('index.html', mode='electron')
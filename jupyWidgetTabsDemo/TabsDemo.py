import ipywidgets as widgets
#from traitlets import Unicode
from traitlets import Int, Unicode, Tuple, CInt, Dict, validate, observe
import json

@widgets.register
class TabsDemo(widgets.DOMWidget):
    _view_name = Unicode('TabsDemoView').tag(sync=True)
    _model_name = Unicode('TabsDemoModel').tag(sync=True)
    _view_module = Unicode('jupyWidgetTabsDemo').tag(sync=True)
    _model_module = Unicode('jupyWidgetTabsDemo').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    msgFromKernel = Unicode("").tag(sync=True)
    _browserState = Unicode("").tag(sync=True)


    def writeToTab(self, tabNumber, msg):
       payload = {"tabNumber": tabNumber, "msg": msg};
       self.msgFromKernel = json.dumps({"cmd": "writeToTab", "status": "request", "callback": "", "payload": payload})

    def raiseTab(self, tabName):
       self.msgFromKernel = json.dumps({"cmd": "raiseTab", "status": "request", "callback": "", "payload": tabName})

    def getBrowserState(self):
        return(json.loads(self._browserState));

    def getRequestCount(self):
        return(self.getBrowserState()["requestCount"])



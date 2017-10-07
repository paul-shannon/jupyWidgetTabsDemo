import ipywidgets as widgets
from traitlets import Unicode

@widgets.register
class TabsDemo(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('TabsDemoView').tag(sync=True)
    _model_name = Unicode('TabsDemoModel').tag(sync=True)
    _view_module = Unicode('jupyWidgetTabsDemo').tag(sync=True)
    _model_module = Unicode('jupyWidgetTabsDemo').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    value = Unicode('TabsDemo World!').tag(sync=True)

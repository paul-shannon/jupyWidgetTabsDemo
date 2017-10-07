from ._version import version_info, __version__

from .TabsDemo import *

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'jupyWidgetTabsDemo',
        'require': 'jupyWidgetTabsDemo/extension'
    }]

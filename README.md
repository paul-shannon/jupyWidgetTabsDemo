jupyWidgetTabsDemo
===============================

jQuery tabs in a jupyter widget

Installation
------------

Simplest approach

    bash> make

To install use pip:

    $ pip install jupyWidgetTabsDemo
    $ jupyter nbextension enable --py --sys-prefix jupyWidgetTabsDemo


For a development installation (requires npm),

    $ git clone https://github.com/paul-shannon/jupyWidgetTabsDemo.git
    $ cd jupyWidgetTabsDemo
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix jupyWidgetTabsDemo
    $ jupyter nbextension enable --py --sys-prefix jupyWidgetTabsDemo

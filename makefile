default:
	(cd ./js; npm update)
	(cd ./js; webpack --config webpack.config.js)
	pip install -e .
	(cd ./js; npm install)
	jupyter nbextension install --user --py jupyWidgetTabsDemo
	jupyter nbextension enable --user --py --sys-prefix jupyWidgetTabsDemo
	(cd ./examples/basicDemo; jupyter notebook simple.ipynb)

clean:
	- rm -rf js/node_modules/*
	- rm -rf js/dist/*
	- rm -rf jupyWidgetTabsDemo/static/*
	- rm -rf jupyWidgetTabsDemo/__pycache__

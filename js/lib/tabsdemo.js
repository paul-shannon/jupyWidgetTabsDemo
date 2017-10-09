var widgets = require('@jupyter-widgets/base');
var _ = require('lodash');


// Custom Model. Custom widgets models must at least provide default values
// for model attributes, including
//
//  - `_view_name`
//  - `_view_module`
//  - `_view_module_version`
//
//  - `_model_name`
//  - `_model_module`
//  - `_model_module_version`
//
//  when different from the base class.

// When serialiazing the entire widget state for embedding, only values that
// differ from the defaults will be specified.
var TabsDemoModel = widgets.DOMWidgetModel.extend({
    defaults: _.extend(widgets.DOMWidgetModel.prototype.defaults(), {
        _model_name : 'TabsDemoModel',
        _view_name : 'TabsDemoView',
        _model_module : 'jupyWidgetTabsDemo',
        _view_module : 'jupyWidgetTabsDemo',
        _model_module_version : '0.1.0',
        _view_module_version : '0.1.0',
        value : 'TabsDemo World'
    })
});


// Custom View. Renders the widget model.
var TabsDemoView = widgets.DOMWidgetView.extend({

   createDiv: function(){
      var tabsOuterDiv = $("<div id='tabsOuterDiv' style='border:1px solid blue; height: 800px; width: 100%%'></div>");
      var tabsList = $("<ul></ul>");
      tabsList.append("<li><a href='#tabs_1'>1</a></li>");
      tabsList.append("<li><a href='#tabs_2'>2</a></li>")
      var tabDiv_1 = $("<div id='tabs_1'>tab one</div>");
      var tabDiv_2 = $("<div id='tabs_2'>tab two</div>");
      tabsOuterDiv.append(tabsList);
      tabsOuterDiv.append(tabDiv_1);
      tabsOuterDiv.append(tabDiv_2);
      return(tabsOuterDiv);
      },


   render: function() {
      this.$el.append(this.createDiv());
       setTimeout(function(){$("#tabsOuterDiv").tabs()}, 0);
      //this.value_changed();
      //this.model.on('change:value', this.value_changed, this);
      },

    value_changed: function() {
       this.el.textContent = this.model.get('value');
    }
});


module.exports = {
    TabsDemoModel : TabsDemoModel,
    TabsDemoView : TabsDemoView
};

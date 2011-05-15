# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1305494106.0255411
_template_filename='/Users/anguyen/projects/easy_api/easy_api/easy_api/templates/main.mako'
_template_uri='/main.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['content', 'header', 'sidebar', 'head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 242
        __M_writer(u'\n\n')
        # SOURCE LINE 246
        __M_writer(u'\n\n')
        # SOURCE LINE 261
        __M_writer(u'\n\n')
        # SOURCE LINE 290
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 263
        __M_writer(u'\n\t<h2>User</h2>\n\t<label>API URL:</label> <input id="apiURL" type="text"/><br/><br/>\n\t<label>API Token:</label> <input id="apiToken" type="text"/><br/><br/>\n\t\n\t<a href="#" id="previousUsers">Select Previous Users</a>\n\t<table id="previousUserList">\n\t</table>\n\t<br/>\n\t\n\t<div id="apiRequest">\n    \t<h2>Request</h2>\n    \t<pre id="request" class="brush: xml; toolbar: false; auto-links:false;">\n    \t</pre>\n\t</div>\n\n\t<a href="#" id="sendRequest">Send Request</a>\n\t\n\t<div id="apiResponse">\n\t\t<h2>Response</h2>\n\t\t<div id="loader">\n\t\t    <img src="/media/ajax-loader.gif"/></br>\n\t\t    <p>Shhh! I&apos;m thinking!</p>\n\t\t</div>\n    \t<pre id="response" class="brush: xml; toolbar: false; auto-links:false;">\n    \t</pre>\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 244
        __M_writer(u'\n\t<img src="/media/easyAPI.png" id="logo"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 248
        __M_writer(u'\n\t<h2>API Calls</h2>\n\t<ul id="functions"></ul>\n\t<div class="clearfix"></div>\n\n\t<h2>Methods</h2>\n\t<ul id="methods"></ul>\n\t<div class="clearfix"></div>\n\t\n\t<h2>Fields</h2>\n\t<div id="fields" class="fields"></div>\n    <div class="clearfix"></div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n\n\t<script type="text/javascript" src="/js/jquery.js"></script>\n\t<script type="text/javascript" src="/js/shCore.js"></script>\n\t<script type="text/javascript" src="/js/shBrushXml.js"></script>\n\t<link href="/css/shCore.css" type="text/css" rel="stylesheet" />\n\t<link href="/css/shThemeDefault.css" type="text/css" rel="stylesheet" />\n\n\t<script type="text/javascript" src="/js/definition.json"></script>\n\t<script type="text/javascript">\n\t    newLine = \'\\r\\n\';\n\n\t\tcurrentElementName = "";\n\t\tcurrentElementMethods = "";\n\t\tcurrentMethodName = "";\n\n\t\t$(document).ready(function(){\n\t\t\tSyntaxHighlighter.highlight();\n\t\t\t// Load up all the API Calls\n\t\t\t$.each(functions, function(key, val) {\n\t\t\t\t$(\'#functions\').append(\'<li><a class="functions" href="#" alt="\' + key + \'">\' + key + \'</a></li>\');\n\t\t\t});\n\t\t\t\n\t\t\t$(\'#sendRequest\').click(function() {\n                makeServerRequest();\n    \t\t    return false;\n    \t\t});\n    \t\t\n    \t\t$(\'#previousUsers\').click(function() {\n    \t\t    $(\'#previousUserList\').toggle();\n\n    \t\t\t$.ajax({\n    \t\t\t\ttype: "Get",\n    \t\t\t\turl: \'/request/listUsers\',\n    \t\t\t\tsuccess: function(users) {\n    \t\t\t\t    $(\'#previousUserList\').html(\'\');\n    \t\t\t\t    \n                        for (var i=0; i < users.length; i++) {\n                            $(\'#previousUserList\').append(\'<tr>\' + \n                                \'<td class="url">\' + users[i].url + \'</td>\' +\n                                \'<td class="token">\' + users[i].token + \'</td>\' +\n                            \'</tr>\')\n                        }\n    \t\t\t\t}\n    \t\t\t});\n    \t\t\treturn false;\n    \t\t});\n\t\t});\n\t\t\n\t\t// Capture the API Call selection\n\t\t$(\'#previousUserList tr\').live("click", function() {\n\t\t    $(\'#previousUserList\').toggle();\n            $(\'#apiURL\').val($(\'td.url\', this).text());\n            $(\'#apiToken\').val($(\'td.token\', this).text());\n\n\t\t\treturn false;\n\t\t});\t\t\n\n\n\t\t// Capture the API Call selection\n\t\t$(\'a.functions\').live("click", function() {\n\n\t\t\t$(\'a.functions\').removeClass("selected");\n\t\t\t$(this).addClass("selected");\n\n\t\t\t//Get the selected element\n\t\t\tcurrentElementName = $(this).attr("alt");\n\t\t\tcurrentElementMethods = functions[currentElementName];\n\n\t\t\t// Clear any methods/functions and add the new ones\n\t\t\t$(\'#methods\').html("");\t\n\t\t\t$(\'#fields\').html("");\n\t\t\t$.each(currentElementMethods, function(key, val) {\n\t\t\t\t$(\'#methods\').append(\'<li><a class="methods" href="#" alt="\' + key + \'">\' + key + \'</a></li>\');\n\t\t\t});\n\n\t\t\treturn false;\n\t\t});\n\n\n\t\t// Capture the Method Selection\n\t\t$(\'a.methods\').live("click", function() {\n\n\t\t\t$(\'a.methods\').removeClass("selected");\n\t\t\t$(this).addClass("selected");\n\n\t\t\t//Extract the fields from the selected method\n\t\t\tcurrentMethodName = $(this).attr("alt");\n\t\t\t$(\'#fields\').html(exploreFields(currentElementMethods[currentMethodName]));\n\n\t\t\t$(\'#currentCurlCommand\').html(currentElementName + \'.\' + currentMethodName);\n\n            var code = createRequest();\n            displayCode(\'request\', code);\n            \n\t\t\t$(\'#fields input:first\').focus();\n\n\t\t\treturn false;\n\t\t});\n\n\t\t// Update the curl command on every text change\n\t\t$(\'input.fields\').live("change", function() {\n            var code = createRequest();\n            displayCode(\'request\', code);\n\t\t});\n\n\n\t\t// Recursively traverses the json object building the html form\n\t\tfunction exploreFields(root) {\n\t\t\tvar fields = "";\n\n\t\t\t$.each(root, function(key, val) {\n\t\t\t\tif (val._text == undefined) {\n\t\t\t\t\tfields += \'<div class="fields" alt="\' + key + \'">\';\n\t\t\t\t\tfields += \'<h3>\' + key + \'</h3>\';\n\t\t\t\t\tfields += exploreFields(val);\n\t\t\t\t\tfields +=\'</div>\';\n\t\t\t\t} else {\n\t\t\t\t\tfields += \'<label>\' + key + \'</label>\';\n\t\t\t\t\tfields += \'<input class="fields" type="text" alt="\' + key + \'"></input><br/>\';\n\t\t\t\t}\n\t\t\t});\n\n\t\t\treturn fields;\n\t\t}\n\n\t\t// Builds the curl command\n\t\tfunction createRequest() {\n\t\t\tvar command = "";\n\n\t\t\tcommand += \'<request method="\' + currentElementName + \'.\' + currentMethodName + \'">\';\n\t\t\tcommand += parseFields(\'#fields\', 1);\n\t\t\tcommand += newLine + \'</request>\';\n\t\t\t\n\t\t\treturn command;\n\t\t}\n\n\t\t// Traverses the parent element in the DOM until it reaches the bottom, to build the curl commands\n\t\tfunction parseFields(parent, level) {\n\t\t    \n\t\t\tvar xml = ""\n\n\t\t\tvar numInputs = 0;\n\t\t\tvar numDivFields = 0;\n\t\t\tvar tempParseResult = ""\n\n\t\t\tnumInputs = $(parent + \' > input\').size();\n\t\t\tnumDivFields = $(parent + \' > div\').size();\n\n            //Base case with no inputs\n\t\t\tif(numInputs == 0) {\n\t\t\t\t$.each($(parent + \' > div\'), function() {\n\t\t\t\t\ttempParseResult = parseFields(parent + \'> div\', level + 1);\n\n\t\t\t\t\tif (tempParseResult != "") {\n\t\t\t\t\t\txml += newLine + tabs(level) + \'<\' + $(this).attr("alt") + \'>\';\n\t\t\t\t\t\txml += \'\' + tempParseResult;\n\t\t\t\t\t\txml += newLine + tabs(level) + \'</\' + $(this).attr("alt") + \'>\';\n\t\t\t\t\t}\n\t\t\t\t});\n\t\t\t\n\t\t\t//Else we have to traverse all the inputs\n\t\t\t} else {\n\t\t\t\t$.each($(parent + \' > input\'), function() {\n\t\t\t\t\tif ($(this).val() != "") {\n\t\t\t\t\t\txml += newLine + tabs(level) + \'<\' + $(this).attr("alt") + \'>\';\n\t\t\t\t\t\txml += $(this).val();\n\t\t\t\t\t\txml += \'</\' + $(this).attr("alt") + \'>\';\n\t\t\t\t\t}\n\t\t\t\t});\n                \n                //Explore sub sections\n\t\t\t\tif (numDivFields > 0) {\n\t\t\t\t\t$.each($(parent + \' > div\'), function() {\n\t\t\t\t\t\ttempParseResult = parseFields(parent + \'> div\', level + 1);\n\n\t\t\t\t\t\tif (tempParseResult != "") {\n\t\t\t\t\t\t\txml += newLine + tabs(level) + \'<\' + $(this).attr("alt") + \'>\';\n\t\t\t\t\t\t\txml += \'\' + tempParseResult;\n\t\t\t\t\t\t\txml += newLine + tabs(level) + \'</\' + $(this).attr("alt") + \'>\';\n\t\t\t\t\t\t}\n\t\t\t\t\t});\t\n\t\t\t\t}\n\t\t\t}\n\n\t\t\treturn xml;\n\t\t}\n\t\t\n\t\tfunction tabs(count) {\n\t\t    var tabs = "";\n\t\t    for (var i = 0; i < count; i++) {\n\t\t        tabs += \'\\t\';\n\t\t    }\n\t\t    \n\t\t    return tabs;\n\t\t}\n\t\t\n\t\tfunction makeServerRequest() {\n\t\t    var apiURL = $(\'#apiURL\').val().trim();\n\t\t    var apiToken = $(\'#apiToken\').val().trim();\n\t\t    \n\t\t    if (apiURL != "" && apiToken != "") {\n                $(\'#response\').hide();\n                $(\'#loader\').show();\n            \n    \t\t\t$.ajax({\n    \t\t\t\ttype: "POST",\n    \t\t\t\turl: \'/request/index\',\n    \t\t\t\tdata: {\n    \t\t\t\t    url: apiURL,\n    \t\t\t\t    token: apiToken,\n    \t\t\t\t    xml: createRequest()\n    \t\t\t\t},\n    \t\t\t\tsuccess: function(xml) {\n                        $(\'#loader\').hide();\n    \t\t\t\t    displayCode(\'response\', xml.response);\n    \t\t\t\t}\n    \t\t\t});\n    \t\t} else {\n    \t\t    alert("Whoopsie Doodles! Don\'t forget to give me your API URl and Token!");\n    \t\t}\n\t\t\t\n\n\t\t}\n\t\t\n\t\tfunction displayCode(sectionID, code) {\n\t\t    var sectionJQ = "#" + sectionID;\n\t\t    var parent = $(sectionJQ).parent();\n\n\t\t\t$(sectionJQ).remove();\n\t        $(parent).append(\'<pre id="\' + sectionID + \'" class="brush: xml; toolbar: false; auto-links:false;"></pre>\');\n\t\t\t$(sectionJQ).append(code);\n\n\t\t\tSyntaxHighlighter.highlight();\n\t\t}\n\t\t\n\n\n\t</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



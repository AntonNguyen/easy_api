# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1305438551.120857
_template_filename=u'/Users/anguyen/projects/easy_api/easy_api/easy_api/templates/base.mako'
_template_uri=u'/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n\t<head>\n\t\t<title>Easy API</title>\n\t\t<link rel="stylesheet" href="/css/reset.css" type="text/css" />\n\t\t<link rel="stylesheet" href="/css/style.css" type="text/css" />\n\t\t<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />\n\t\t')
        # SOURCE LINE 8
        __M_writer(escape(self.head_tags()))
        __M_writer(u'\n\t</head>\n\t<body>\n\t\t<div id="header">\n\t\t\t')
        # SOURCE LINE 12
        __M_writer(escape(self.header()))
        __M_writer(u'\n\t\t</div>\n\t\t\n\t\t<div id="sidebar">\n\t\t\t')
        # SOURCE LINE 16
        __M_writer(escape(self.sidebar()))
        __M_writer(u'\n\t\t</div>\n\t\t\n\t\t<div id="content">\n\t\t\t')
        # SOURCE LINE 20
        __M_writer(escape(self.content()))
        __M_writer(u'\n\t\t</div>\n\t\t\n\t\t<div id="footer">\n\t\t</div>\n\t</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()



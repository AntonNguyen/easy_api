import logging


from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from easy_api.lib.base import BaseController, render

log = logging.getLogger(__name__)

class MainController(BaseController):


    def index(self):
        
        # Return a rendered template
        return render('/main.mako')
        

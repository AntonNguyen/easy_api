import logging
import json
import base64
import httplib
import httplib2
import urllib
import sys
from pylons.decorators import jsonify

from easy_api.lib.base import Session
from easy_api.model import User

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from easy_api.lib.base import BaseController, render

log = logging.getLogger(__name__)

class RequestController(BaseController):

    @jsonify
    def index(self):
        url = request.POST['url']
        token = request.POST['token']
        xmlRequest = request.POST['xml']

        client = httplib2.Http()
        base64_user_pass = base64.b64encode("%s:" % (token, ))

        try:
            headers = {
                        "Authorization": 'Basic %s' % (base64_user_pass, ),
                        "content-type": "application/x-www-form-urlencoded",
                        }
            resp, content = client.request(
                url,
                'POST',
                headers=headers,
                body=xmlRequest
            )

            # Only save the good combinations
            if resp.status=='200':
                user_q = Session.query(User)
                previousUsers = user_q.filter_by(url=url, token=token)

                # Save the user if that one hasn't been used before
                if previousUsers.count() == 0:
                    # Save the user information
                    user = User(url=url, token=token)
                    Session.add(user)
                    Session.commit()

                return dict(response=content)
            else:
                return dict(response='Uh oh! Something messed up. =( Is your API URL or Token correct?')                
        except:
            return dict(response='Uh oh! Something messed up. =( Is your API URL or Token correct?')
            
    @jsonify
    def listUsers(self):
        try:
            users = []
            
            userQuery = Session.query(User)
            for user in userQuery.all():
                users.append(dict(url=user.url, token=user.token))
                
            return dict(users=users)
        except:
            return dict(users=[])

    @jsonify
    def listURLs(self):
        try:
            userQuery = Session.query(User)
            url = [user.url for user in userQuery.all()]

            return dict(urls=url)
        except:
            return dict(urls=[])

    @jsonify
    def listTokens(self):
        try:
            userQuery = Session.query(User)
            tokens = [user.token for user in userQuery.all()]

            return dict(tokens=tokens)
        except:
            return dict(tokens=[])

# -*- coding: utf-8 -*-

from sanic.response import text, json

from . import Resource
from .. import schemas


class AccountsWxapp(Resource):

    async def post(self, request):
        print(request.json)
        print(request.headers)

        return {'id': 'something'}, 200
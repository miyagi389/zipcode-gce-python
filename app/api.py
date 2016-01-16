# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import logging

import endpoints
from protorpc import remote, messages, message_types

from app.api_messages import ZipCodeListResponse
from app.models import ZipCode

u"""Japan ZIP Code API implemented using Google Cloud Endpoints."""

CLIENT_ID = "zipcode-gce-python"


@endpoints.api(
        name="zipcode",
        version="v1",
        description=u"Japan ZIP Code API",
        allowed_client_ids=[CLIENT_ID, endpoints.API_EXPLORER_CLIENT_ID]
)
class ZipCodeApi(remote.Service):
    """Class which defines ZIP Code API v1."""

    LIST_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            offset=messages.IntegerField(1, default=0),
            limit=messages.IntegerField(2, default=100)
    )

    @endpoints.method(
            LIST_RESOURCE,
            ZipCodeListResponse,
            path='jp',
            http_method='GET',
            name='list'
    )
    def list(self, request):
        query = ZipCode.query_all()
        items = [entity.to_message() for entity in query.fetch(request.limit, offset=request.offset)]
        return ZipCodeListResponse(items=items)

    LIST_CODE_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            offset=messages.IntegerField(1, default=0),
            limit=messages.IntegerField(2, default=100),
            code=messages.StringField(3)
    )

    @endpoints.method(
            LIST_CODE_RESOURCE,
            ZipCodeListResponse,
            path='jp/{code}',
            http_method='GET',
            name='list_code'
    )
    def list_code(self, request):
        logging.info("list_code code: " + request.code + '. limit: ' + str(request.limit))
        query = ZipCode.query_code(request.code)
        items = [entity.to_message() for entity in query.fetch(request.limit, offset=request.offset)]
        return ZipCodeListResponse(items=items)


APPLICATION = endpoints.api_server(
        [ZipCodeApi],
        restricted=False
)

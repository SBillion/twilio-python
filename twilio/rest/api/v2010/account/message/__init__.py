# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest import serialize
from twilio.rest.api.v2010.account.message.media import MediaList
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class MessageList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the MessageList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: MessageList
        :rtype: MessageList
        """
        super(MessageList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Messages.json'.format(**self._kwargs)

    def create(self, to, from_, status_callback=values.unset,
               application_sid=values.unset, body=values.unset,
               media_url=values.unset):
        """
        Create a new MessageInstance
        
        :param str to: The phone number to receive the message
        :param str from_: The phone number that initiated the message
        :param str status_callback: URL Twilio will request when the status changes
        :param str application_sid: The application to use for callbacks
        :param str body: The body
        :param str media_url: The media_url
        
        :returns: Newly created MessageInstance
        :rtype: MessageInstance
        """
        data = values.of({
            'To': to,
            'From': from_,
            'Body': body,
            'MediaUrl': media_url,
            'StatusCallback': status_callback,
            'ApplicationSid': application_sid,
        })
        
        return self._version.create(
            MessageInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def stream(self, to=values.unset, from_=values.unset,
               date_sent_before=values.unset, date_sent=values.unset,
               date_sent_after=values.unset, limit=None, page_size=None, **kwargs):
        """
        Streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str to: Filter by messages to this number
        :param str from_: Filter by from number
        :param date date_sent_before: Filter by date sent
        :param date date_sent: Filter by date sent
        :param date date_sent_after: Filter by date sent
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'To': to,
            'From': from_,
            'DateSent<': serialize.iso8601_date(date_sent_before),
            'DateSent': serialize.iso8601_date(date_sent),
            'DateSent>': serialize.iso8601_date(date_sent_after),
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            MessageInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, to=values.unset, from_=values.unset,
             date_sent_before=values.unset, date_sent=values.unset,
             date_sent_after=values.unset, limit=None, page_size=None, **kwargs):
        """
        Reads MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str to: Filter by messages to this number
        :param str from_: Filter by from number
        :param date date_sent_before: Filter by date sent
        :param date date_sent: Filter by date sent
        :param date date_sent_after: Filter by date sent
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            to=to,
            from_=from_,
            date_sent_before=date_sent_before,
            date_sent=date_sent,
            date_sent_after=date_sent_after,
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, to=values.unset, from_=values.unset,
             date_sent_before=values.unset, date_sent=values.unset,
             date_sent_after=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        """
        Retrieve a single page of MessageInstance records from the API.
        Request is executed immediately
        
        :param str to: Filter by messages to this number
        :param str from_: Filter by from number
        :param date date_sent_before: Filter by date sent
        :param date date_sent: Filter by date sent
        :param date date_sent_after: Filter by date sent
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of MessageInstance
        :rtype: Page
        """
        params = values.of({
            'To': to,
            'From': from_,
            'DateSent<': serialize.iso8601_date(date_sent_before),
            'DateSent': serialize.iso8601_date(date_sent),
            'DateSent>': serialize.iso8601_date(date_sent_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            MessageInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: Contextual sid
        
        :returns: MessageContext
        :rtype: MessageContext
        """
        return MessageContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MessageList>'


class MessageContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        """
        Initialize the MessageContext
        
        :param Version version
        :param account_sid: Contextual account_sid
        :param sid: Contextual sid
        
        :returns: MessageContext
        :rtype: MessageContext
        """
        super(MessageContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Messages/{sid}.json'.format(**self._kwargs)
        
        # Dependents
        self._media = None

    def delete(self):
        """
        Deletes the MessageInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def fetch(self):
        """
        Fetch a MessageInstance
        
        :returns: Fetched MessageInstance
        :rtype: MessageInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            MessageInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, body=values.unset):
        """
        Update the MessageInstance
        
        :param str body: The body
        
        :returns: Updated MessageInstance
        :rtype: MessageInstance
        """
        data = values.of({
            'Body': body,
        })
        
        return self._version.update(
            MessageInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def media(self):
        """
        Access the media
        
        :returns: MediaList
        :rtype: MediaList
        """
        if self._media is None:
            self._media = MediaList(
                self._version,
                account_sid=self._kwargs['account_sid'],
                message_sid=self._kwargs['sid'],
            )
        return self._media

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.MessageContext {}>'.format(context)


class MessageInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the MessageInstance
        
        :returns: MessageInstance
        :rtype: MessageInstance
        """
        super(MessageInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'body': payload['body'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'date_sent': deserialize.rfc2822_datetime(payload['date_sent']),
            'direction': payload['direction'],
            'error_code': deserialize.integer(payload['error_code']),
            'error_message': payload['error_message'],
            'from_': payload['from'],
            'num_media': payload['num_media'],
            'num_segments': payload['num_segments'],
            'price': deserialize.decimal(payload['price']),
            'price_unit': payload['price_unit'],
            'sid': payload['sid'],
            'status': payload['status'],
            'subresource_uris': payload['subresource_uris'],
            'to': payload['to'],
            'uri': payload['uri'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: MessageContext for this MessageInstance
        :rtype: MessageContext
        """
        if self._instance_context is None:
            self._instance_context = MessageContext(
                self._version,
                self._kwargs['account_sid'],
                self._kwargs['sid'],
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The unique sid that identifies this account
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """
        :returns: The version of the Twilio API used to process the message.
        :rtype: str
        """
        return self._properties['api_version']

    @property
    def body(self):
        """
        :returns: The text body of the message. Up to 1600 characters long.
        :rtype: str
        """
        return self._properties['body']

    @property
    def date_created(self):
        """
        :returns: The date this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def date_sent(self):
        """
        :returns: The date the message was sent
        :rtype: datetime
        """
        return self._properties['date_sent']

    @property
    def direction(self):
        """
        :returns: The direction of the message
        :rtype: message.direction
        """
        return self._properties['direction']

    @property
    def error_code(self):
        """
        :returns: The error code associated with the message
        :rtype: str
        """
        return self._properties['error_code']

    @property
    def error_message(self):
        """
        :returns: Human readable description of the ErrorCode
        :rtype: str
        """
        return self._properties['error_message']

    @property
    def from_(self):
        """
        :returns: The phone number that initiated the message
        :rtype: str
        """
        return self._properties['from_']

    @property
    def num_media(self):
        """
        :returns: Number of media files associated with the message
        :rtype: str
        """
        return self._properties['num_media']

    @property
    def num_segments(self):
        """
        :returns: Indicates number of messages used to delivery the body
        :rtype: str
        """
        return self._properties['num_segments']

    @property
    def price(self):
        """
        :returns: The amount billed for the message
        :rtype: str
        """
        return self._properties['price']

    @property
    def price_unit(self):
        """
        :returns: The currency in which Price is measured
        :rtype: str
        """
        return self._properties['price_unit']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this message
        :rtype: str
        """
        return self._properties['sid']

    @property
    def status(self):
        """
        :returns: The status of this message
        :rtype: message.status
        """
        return self._properties['status']

    @property
    def subresource_uris(self):
        """
        :returns: The subresource_uris
        :rtype: str
        """
        return self._properties['subresource_uris']

    @property
    def to(self):
        """
        :returns: The phone number that received the message
        :rtype: str
        """
        return self._properties['to']

    @property
    def uri(self):
        """
        :returns: The URI for this resource
        :rtype: str
        """
        return self._properties['uri']

    def delete(self):
        """
        Deletes the MessageInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._context.delete()

    def fetch(self):
        """
        Fetch a MessageInstance
        
        :returns: Fetched MessageInstance
        :rtype: MessageInstance
        """
        return self._context.fetch()

    def update(self, body=values.unset):
        """
        Update the MessageInstance
        
        :param str body: The body
        
        :returns: Updated MessageInstance
        :rtype: MessageInstance
        """
        return self._context.update(
            body=body,
        )

    @property
    def media(self):
        """
        Access the media
        
        :returns: media
        :rtype: media
        """
        return self._context.media

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.MessageInstance {}>'.format(context)
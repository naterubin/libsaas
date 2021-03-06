from libsaas import http, parsers
from libsaas.services import base


class IntercomResource(base.RESTResource):

    def get_url(self):
        return '{0}/{1}'.format(self.parent.get_url(), self.path)

    @base.apimethod
    def get(self, page=None, per_page=None):
        """
        Fetch all of the objects.

        :var page: The page that should be returned. If left as `None`,
            first page are returned.
        :vartype page: int

        :var per_page: How many objects should be returned. The
            maximum is 500. If left as `None`, 500 objects are returned.
        :vartype per_page: int
        """
        params = base.get_params(('page', 'per_page'), locals())
        request = http.Request('GET', self.get_url(), params)

        return request, parsers.parse_json


class UserBase(IntercomResource):

    path = 'users'

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Users(UserBase):

    @base.apimethod
    def update(self, obj):
        """
        Update this resource.

        :var obj: a Python object representing the updated resource, usually in
            the same format as returned from `get`. Refer to the upstream
            documentation for details.
        """
        request = http.Request('PUT', self.get_url(), self.wrap_object(obj))

        return request, parsers.parse_json


class User(UserBase):

    def create(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    @base.apimethod
    def get(self, user_id=None, email=None):
        """
        Fetch the object's data.

        :var user_id: The user_id of the user that should be returned.
            Required if no email.
        :vartype user_id: int

        :var email: The email of the user that should be returned.
            Required if no user_id.
        :vartype email: str
        """
        if not user_id and not email:
           raise TypeError('get() must be passed at least one '
                           'of user_id, email')

        params = base.get_params(('user_id', 'email'), locals())
        request = http.Request('GET', self.get_url(), params)

        return request, parsers.parse_json


class Impressions(IntercomResource):

    path = 'users/impressions'

    def get(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class MessageThreadBase(IntercomResource):

    path = 'users/message_threads'

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class MessageThreads(MessageThreadBase):

    @base.apimethod
    def get(self, user_id=None, email=None):
        """
        Fetch all of the objects for the user.

        :var user_id: The user_id of the user which messages should be
            returned. Required if no email.
        :vartype user_id: int

        :var email: The email of the user which messages that should be
            returned. Required if no user_id.
        :vartype email: str
        """
        if not user_id and not email:
           raise TypeError('get() must be passed at least one '
                           'of user_id, email')

        params = base.get_params(('user_id', 'email'), locals())
        request = http.Request('GET', self.get_url(), params)

        return request, parsers.parse_json

    @base.apimethod
    def reply(self, obj):
        """
        Reply to a message thread from an admin from a user
        """
        request = http.Request('PUT', self.get_url(), self.wrap_object(obj))

        return request, parsers.parse_json


class MessageThread(MessageThreadBase):

    @base.apimethod
    def get(self, thread_id, user_id=None, email=None):
        """
        Fetch all a single object.

        :var thread_id: The thread_id of the message that should be returned.
        :vartype thread_id: int

        :var user_id: The user_id of the user which message should be returned.
            Required if no email.
        :vartype user_id: int

        :var email: The email of the user which message that should be
            returned. Required if no user_id.
        :vartype email: str
        """
        if not user_id and not email:
           raise TypeError('get() must be passed at least one '
                           'of user_id, email')

        params = base.get_params(('user_id', 'email'), locals())
        params['thread_id'] = thread_id
        request = http.Request('GET', self.get_url(), params)

        return request, parsers.parse_json


    def create(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Counts(IntercomResource):

    path = 'counts'

    @base.apimethod
    def get(self, type=None, count=None):
        """
        Get counts of users and companies filtered by certain criteria.

        :var type: The count's type
        :vartype type: str

        :var count: The count's filter criteria
        :vartype count: str
        """
        params = base.get_params(None, locals())
        request = http.Request('GET', self.get_url(), params)

        return request, parsers.parse_json

    def create(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Events(IntercomResource):

    path = 'events'

    @base.apimethod
    def create(self, event_name, created_at, user_id=None, email=None,
               metadata=None):
        """
        Create a new Event object.

        :var event_name: The name of the event that occurred.
        :vartype event_name: str

        :var created_at: The time the event occurred as a UTC Unix timestamp.
        :vartype created_at: int

        :var user_id: The user_id of the user which messages should be
            returned. Required if no email.
        :vartype user_id: int

        :var email: The email of the user which messages that should be
            returned. Required if no user_id.
        :vartype email: str

        :var metadata: Optional metadata about the event.
        :vartype metadata: dict
        """
        if not user_id and not email:
            raise TypeError(
                'create() must be passed at least one of user_id, email')

        params = base.get_params(None, locals())
        request = http.Request('POST', self.get_url(), params)

        return request, parsers.parse_empty

    def get(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Companies(IntercomResource):

    path = 'companies'

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Company(Companies):

    @base.apimethod
    def get(self):
        """
        Fetch the company's data.
        """
        params = {'company_id': self.object_id}
        request = http.Request('GET', self.get_url(), params)

        return request, parsers.parse_json

    @base.apimethod
    def users(self):
        """
        Fetch the company's users.
        """
        params = base.get_params(None, locals())
        url = '{0}/{1}/{2}'.format(self.get_url(), self.object_id, 'users')
        request = http.Request('GET', url, params)

        return request, parsers.parse_json

    def create(self, *args, **kwargs):
        raise base.MethodNotSupported()

from libsaas import http, parsers
from libsaas.services import base

from .resource import ApplicationRelatedResource


class ApplicationInstances(ApplicationRelatedResource):

    path = 'instances'

    @base.apimethod
    def get(self, hostname=None, ids=None, page=None):
        """
        List of instances associated with the given application.

        :var hostname: Filter by server hostname.
        :vartype hostname: str

        :var ids: Filter by application host ids.
        :vartype ids: str

        :var page: Pagination index.
        :vartype page: int
        """
        params = base.get_params(None, locals())
        url = '{0}.json'.format(self.get_url())
        request = http.Request('GET', url, params)

        return request, parsers.parse_json


class ApplicationInstance(ApplicationRelatedResource):

    path = 'instances'

    @base.apimethod
    def get(self):
        """
        Fetch a single application instance.
        """
        url = '{0}.json'.format(self.get_url())
        request = http.Request('GET', url)

        return request, parsers.parse_json

    @base.apimethod
    def metric_names(self, name, page):
        """
        List of known metrics and their value names for the given resource.

        :var name: Filter by metrics name.
        :vartype name: str

        :var page: Pagination index.
        :vartype page: int
        """
        params = base.get_params(None, locals())
        url = '{0}/metrics.json'.format(self.get_url())
        request = http.Request('GET', url, params)

        return request, parsers.parse_json

    @base.apimethod
    def metric_data(self, names, values=None, from_datetime=None,
                    to_datetime=None, summarize=None):
        """
        List of values for each requested metrics.

        :var names: Retrieve specific metrics by name.
        :vartype names: str

        :var values: Retrieve specific metrics values.
        :vartype values: str

        :var from_datetime: Retrieve metrics after this time.
        :vartype from_datetime: str

        :var to_datetime: Retrieve metrics before this time.
        :vartype to_datetime: str

        :var summarize: Sumarize the data.
        :vartype summarize: bool
        """
        params = base.get_params(None, locals())
        if params.get('from_datetime') and params.get('to_datetime'):
            params['from'] = params.pop('from_datetime')
            params['to'] = params.pop('to_datetime')
        url = '{0}/metrics/data.json'.format(self.get_url())
        request = http.Request('GET', url, params)

        return request, parsers.parse_json

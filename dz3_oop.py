class Url:
    def __init__(self, scheme=None, authority=None, path=None, query=None, fragment=None):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __str__(self):
        result = ''
        if self.scheme is not None:
            result += self.scheme + '://'

        if self.authority is not None and (self.path is not None or self.query is not None or self.fragment is not None):
            result += self.authority + '/'

            if self.path is not None and (self.query is not None or self.fragment is not None):
                if type(self.path) == list:
                    for i in self.path:
                        result += str(i) + '/'
                if type(self.path) == str:
                    result += self.path + '/'
            if self.path is not None and self.query is None and self.fragment is None:
                if type(self.path) == list:
                    for i in self.path:
                        if i != self.path[-1]:
                            result += str(i) + '/'
                        else:
                            result += str(i)
                if type(self.path) == str:
                    result += self.path
            if self.authority is not None and self.query is not None and self.path is None:
                result = result[:-1]
            if self.query is not None and self.fragment is not None:
                count = 0
                for i in self.query:
                    count += 1
                    if count == 1 and len(self.query) == 1:
                        result += f'?{i}={self.query[i]}'
                    if count == 1 and len(self.query) > 1:
                        result += f'?{i}={self.query[i]}&'
                    if 1 < count != len(self.query) > 1:
                        result += f'{i}={self.query[i]}&'
                    if count == len(self.query) and len(self.query) > 1:
                        result += f'{i}={self.query[i]}/'

            if self.query is not None and self.fragment is None:
                count = 0
                for i in self.query:
                    count += 1
                    if count == 1 and len(self.query) == 1:
                        result += f'?{i}={self.query[i]}'
                    if count == 1 and len(self.query) > 1:
                        result += f'?{i}={self.query[i]}&'
                    if 1 < count != len(self.query) > 1:
                        result += f'{i}={self.query[i]}&'
                    if count == len(self.query) and len(self.query) > 1:
                        result += f'{i}={self.query[i]}'

            if self.fragment is not None:
                result += self.fragment + '/'
        else:
            if self.authority is not None:
                result += self.authority
        return result

    def __eq__(self, other):
        print(str(self), str(other))
        return str(self) == str(other)


class HttpsUrl(Url):
    def __init__(self, scheme='https', authority=None, path=None, query=None, fragment=None):
        super().__init__(scheme, authority, path, query, fragment)
        self.scheme = scheme


class HttpUrl(Url):
    def __init__(self, scheme='http', authority=None, path=None, query=None, fragment=None):
        super().__init__(scheme, authority, path, query, fragment)
        self.scheme = scheme


class GoogleUrl(Url):
    def __init__(self, scheme='https', authority='google.com', path=None, query=None, fragment=None):
        super().__init__(scheme, authority, path, query, fragment)
        self.authority = authority


class WikiUrl(Url):
    def __init__(self, scheme='https', authority='wikipedia.org', path=None, query=None, fragment=None):
        super().__init__(scheme, authority, path, query, fragment)
        self.authority = authority


assert GoogleUrl() == HttpsUrl(authority='google.com')
assert GoogleUrl() == Url(scheme='https', authority='google.com')
assert GoogleUrl() == 'https://google.com'
assert WikiUrl() == str(Url(scheme='https', authority='wikipedia.org'))
assert WikiUrl(path=['wiki', 'python']) == 'https://wikipedia.org/wiki/python'
assert GoogleUrl(query={'q': 'python', 'result': 'json'}) == 'https://google.com?q=python&result=json'

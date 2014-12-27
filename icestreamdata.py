from HTMLParser import HTMLParser
import urllib2


class IceStreamParser(HTMLParser):

    def __init__(self, title):
        HTMLParser.__init__(self)
        self.all_data = []
        self.title = title
        self.station_namespace = False
        self.listener_namespace = False
        self.listener = None

    def handle_data(self, data):
        if self.listener:
            return
        if data == self.title:
            self.station_namespace = True
            return
        if self.station_namespace:
            if data == "Current Listeners:":
                self.listener_namespace = True
                return
        if self.listener_namespace:
            self.listener = int(data)

    def get_listener(self, html):
        self.station_namespace = False
        self.listener_namespace = False
        self.listener = None
        self.feed(html)
        return self.listener


class IceStreamListener(object):

    def __init__(self, url, title):
        self.url = url
        self.parser = IceStreamParser(title)
    

    def get_statuspage(self):
        response = urllib2.urlopen(self.url)
        return response.read()

    def get_listener(self):
        return self.parser.get_listener(self.get_statuspage())

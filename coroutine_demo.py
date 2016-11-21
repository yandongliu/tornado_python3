import sys
import tornado
import tornado.gen
import tornado.httpclient


@tornado.gen.coroutine
def fetch_page(client, url, n):
    response = yield client.fetch(url)
    print(n, response.code, len(response.body))


@tornado.gen.coroutine
def main():
    client = tornado.httpclient.AsyncHTTPClient(force_instance=True)
    for n in range(0, 10):
        yield fetch_page(client, 'http://www.yahoo.com', n)


print(sys.version_info, '+ tornado', tornado.version)
tornado.ioloop.IOLoop.current().run_sync(main)

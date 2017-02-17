import sys

from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *



class Render(QWebPage):
    def __init__(self, url):
        print "Render.__initi__ <-"
        print "using PyQt WebKit"

        self.app = QtGui.QApplication(sys.argv)

        # Behind the proxy: then do these
        # proxy = QNetworkProxy()
        # proxy.setType(QNetworkProxy.Socks5Proxy);
        # proxy.setType(QNetworkProxy.HttpProxy);
        # proxy.setHostName("org-proxy-abc.com");
        # proxy.setPort(8080);
        # proxy.setUser("user_name");
        # proxy.setPassword("pass_word");
        # QNetworkProxy.setApplicationProxy(proxy);

        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.loadStarted.connect(self._loadStarted)
        self.loadProgress.connect(self._loadProgress)
        self.mainFrame().load(QUrl(url))

        print "Render.__initi__ ->"

        self.app.exec_()
        self.view()

    def _loadStarted(self, result):
        print "_loadStarted"

    def _loadProgress(self, progress):
        print "_loadProgress: ", progress

    def _loadFinished(self, ok):
        print "loading finished", ok
        self.frame = self.mainFrame()
        frame_html = self.frame.toHtml()
        contents = str(frame_html.toAscii())
        print contents
        self.app.quit()


if __name__ == "__main__" :
    try:
        webPage = Render("http://www.google.com")
        print str(webPage.frame.toHtml().toAscii())
    except Exception, e :
        print e.message



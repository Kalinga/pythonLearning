from PyQt4 import QtCore, QtGui, QtWebKit

class WebViewCreator(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.view = QtWebKit.QWebView(self)

        self.view.loadFinished.connect(self.load_finished)
        #self.view.page().loadFinished.connect(self.page_load_finished)
        #self.view.page().loadProgress.connect(self.page_loadProgress)
        #self.view.page().mainFrame().loadFinished.connect(self.page_frame_load_finished)


        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.view)
        url_imdb = 'http://m.imdb.com/feature/bornondate'
        url_from_local = "file:///home/kalinga/Git/pythonLearning/projects/twitter_sentiment/test_data/imdb.html"
        self.view.load(QtCore.QUrl(url_from_local))

    def load_finished(self, ok):
        print ok
        if (ok):
            page_contents = str(self.view.page().mainFrame().toHtml().toAscii())
            print page_contents
        #print self.view.page().mainFrame().toHtml().toAscii()

    def page_loadProgress(self, progress):
        print "page_loadProgress", progress

    def page_load_finished(self, ok):
        print "page_load_finished", ok

    def page_frame_load_Progress(self, progress):
        print progress

    def page_frame_load_finished(self, ok):
        print "page_frame_load_finished", ok

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = WebViewCreator()
    window.show()
    sys.exit(app.exec_())
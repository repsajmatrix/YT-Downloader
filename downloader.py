
import sys
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
        QTextEdit, QGridLayout, QApplication, QComboBox, QRadioButton, QPushButton, QProgressBar, QMessageBox)
from PyQt6 import QtGui
from pytube import YouTube
from pytube import Playlist

typeinput = 'Video'
formatinput = 'MP4'
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)

        self.url_video = QLabel('URL:')
        self.url_video.setStyleSheet("color:#FFFFFF;")
        self.url_video.setFont(font)

        self.type = QLabel('Type:')
        self.type.setStyleSheet("color:#FFFFFF;")
        self.type.setFont(font)

        self.format = QLabel('Format:')
        self.format.setStyleSheet("color:#FFFFFF;")
        self.format.setFont(font)

        self.info = QLabel('Info:')
        self.info.setStyleSheet("color:#FFFFFF;")
        self.info.setFont(font)

        self.url_video_edit = QLineEdit()
        self.url_video_edit.setStyleSheet("border: 1px solid #FFFFFF;\n"
        "color: #FFFFFF;")
        self.url_video_edit.setFont(font)

        self.type_combo = QComboBox(self)
        self.type_combo.addItem('Video')
        self.type_combo.addItem('Playlist')
        self.type_combo.setStyleSheet("border: 1px solid #FFFFFF;\n"
        "color:#FFFFFF;\n"
        "background-color:#000000;")
        self.type_combo.textActivated[str].connect(self.type_text)
        self.type_combo.setFont(font)

        self.format_combo = QComboBox(self)
        self.format_combo.addItem('MP4')
        self.format_combo.addItem('WEBM')
        self.format_combo.setStyleSheet("border: 1px solid #FFFFFF;\n"
        "color:#FFFFFF;\n"
        "background-color:#000000;")
        self.format_combo.textActivated[str].connect(self.format_text)
        self.format_combo.setFont(font)


        self.downloadBtn = QPushButton()
        self.downloadBtn.setFont(font)
        self.downloadBtn.setStyleSheet("QPushButton {background-color: #000000;\n"
        "border: 1px solid #FFFFFF;\n"
        "color: #FFFFFF;}\n"
        "QPushButton:pressed {background-color: #161616;\n"
        "border: 1px solid #FFFFFF;\n"
        "border-color: #FFFFFF;}")
        self.downloadBtn.setText('Download')
        self.downloadBtn.clicked.connect(self.download)

        self.infoBtn = QPushButton()
        self.infoBtn.setFont(font)
        self.infoBtn.setStyleSheet("QPushButton {background-color: #000000;\n"
        "border: 1px solid #FFFFFF;\n"
        "color: #FFFFFF;}\n"
        "QPushButton:pressed {background-color: #161616;\n"
        "border: 1px solid #FFFFFF;\n"
        "border-color: #FFFFFF;}")
        self.infoBtn.setText('Info')
        self.infoBtn.clicked.connect(self.infovideo)

        self.info_text = QTextEdit()
        self.info_text.setStyleSheet("border: 1px solid #FFFFFF;\n"
        "color:#FFFFFF;\n"
        "background-color:#000000;")
        self.info_text.setFont(font)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.url_video, 1, 0)
        grid.addWidget(self.url_video_edit, 1, 1, 1, 5)

        grid.addWidget(self.type, 2, 0)
        grid.addWidget(self.type_combo, 2, 1)
        grid.addWidget(self.format, 2, 2)
        grid.addWidget(self.format_combo, 2, 3)
        grid.addWidget(self.info, 2, 4)
        grid.addWidget(self.infoBtn, 2, 5)

        grid.addWidget(self.downloadBtn, 3, 0, 1, 6)

        grid.addWidget(self.info_text, 4, 0, 4, 6)
        #grid.setColumnStretch(1, 0)

        self.setLayout(grid)

        self.setGeometry(500, 500, 800, 500)
        self.setWindowTitle('YT-Downloader')
        self.showMaximized()
        self.setStyleSheet("background-color:#000000;")
        self.show()

    def type_text(self, text):
        global typeinput
        typeinput = text

    def format_text(self, text):
        global formatinput
        formatinput = text


    def infovideo(self):
        try:
            #self.info_text.zoomIn(+1)
            file = self.url_video_edit.text()
            my_video = YouTube(file)
            self.info_text.setPlainText("Title:\n" + my_video.title
            + "\n\nAuthor:\n" + my_video.author
            + "\n\nDiscription:\n" + my_video.description
            + "\n\nKeyWords:\n" + str(my_video.keywords)
            + "\n\nPublish_Date:\n" + str(my_video.publish_date)
            + "\n\nViews:\n" + str(my_video.views)
            + "\n\nLength:\n" + str("{:.2f}".format(my_video.length/60)) + " Minutes"
            + "\n\nAge_Restricted:\n" + str(my_video.age_restricted)
            + "\n\nCheck_Availability:\n" + str(my_video.check_availability())
            + "\n\nCaptions:\n" + str(my_video.captions)
            + "\n\nCaptions_Tracks:\n" + str(my_video.caption_tracks)
            + "\n\nMetaData:\n" + str(my_video.metadata)
            + "\n\nVideo_URL:\n" + my_video.video_id
            + "\n\nChannel_URL:\n" + my_video.channel_url
            + "\n\nChannel_ID:\n" + my_video.channel_id
            + "\n\nThumbnail_url:\n" + my_video.thumbnail_url
            + "\n\nVideo_Info:\n" + str(my_video.vid_info))
        except:
            self.info_text.setPlainText("URL Is Not Working")

    def download(self):
        global typeinput
        global formatinput

        if typeinput == "Video":
            try:
                file = self.url_video_edit.text()
                my_video = YouTube(file)
                if formatinput == "MP4":
                    vid = my_video.streams.get_highest_resolution()
                    vid.download()
                    msg = QMessageBox()
                    msg.setText("Download Finished")
                    x = msg.exec()
                if formatinput == "WEBM":
                    vid = my_video.streams.get_by_itag(251)
                    vid.download()
                    msg = QMessageBox()
                    msg.setText("Download Finished")
                    x = msg.exec()

            except:
                self.info_text.setPlainText("URL Is Not Working")
    
        if typeinput == "Playlist":
            try:
                playlist = self.url_video_edit.text()
                p = Playlist(playlist)
                if formatinput == "MP4":
                    for video in p.videos:
                        video.streams.get_highest_resolution().download()
                    msg = QMessageBox()
                    msg.setText("Download Finished")
                    x = msg.exec()
                if formatinput == "WEBM":
                    for video in p.videos:
                        video.streams.get_by_itag(251).download()
                    msg = QMessageBox()
                    msg.setText("Download Finished")
                    x = msg.exec()
            except:
                self.info_text.setPlainText("URL Is Not Working")

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
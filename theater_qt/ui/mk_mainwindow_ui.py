# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mk_mainwindow.ui'
#
# Created: Tue Aug  8 18:46:15 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MK_MainWindow(object):
    def setupUi(self, MK_MainWindow):
        MK_MainWindow.setObjectName("MK_MainWindow")
        MK_MainWindow.resize(803, 662)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MK_MainWindow.sizePolicy().hasHeightForWidth())
        MK_MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MK_MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_frame_bottom = QtWidgets.QFrame(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.main_frame_bottom.sizePolicy().hasHeightForWidth())
        self.main_frame_bottom.setSizePolicy(sizePolicy)
        self.main_frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame_bottom.setObjectName("main_frame_bottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_frame_bottom)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_button_music = QtWidgets.QPushButton(self.main_frame_bottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_music.sizePolicy().hasHeightForWidth())
        self.main_button_music.setSizePolicy(sizePolicy)
        self.main_button_music.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/headphone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_music.setIcon(icon)
        self.main_button_music.setObjectName("main_button_music")
        self.horizontalLayout.addWidget(self.main_button_music)
        self.main_button_movie = QtWidgets.QPushButton(self.main_frame_bottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_movie.sizePolicy().hasHeightForWidth())
        self.main_button_movie.setSizePolicy(sizePolicy)
        self.main_button_movie.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/movie_ticket.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_movie.setIcon(icon1)
        self.main_button_movie.setObjectName("main_button_movie")
        self.horizontalLayout.addWidget(self.main_button_movie)
        self.main_button_tv = QtWidgets.QPushButton(self.main_frame_bottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_tv.sizePolicy().hasHeightForWidth())
        self.main_button_tv.setSizePolicy(sizePolicy)
        self.main_button_tv.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/television.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_tv.setIcon(icon2)
        self.main_button_tv.setObjectName("main_button_tv")
        self.horizontalLayout.addWidget(self.main_button_tv)
        self.main_button_tv_live = QtWidgets.QPushButton(self.main_frame_bottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_tv_live.sizePolicy().hasHeightForWidth())
        self.main_button_tv_live.setSizePolicy(sizePolicy)
        self.main_button_tv_live.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../images/television_live.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_tv_live.setIcon(icon3)
        self.main_button_tv_live.setObjectName("main_button_tv_live")
        self.horizontalLayout.addWidget(self.main_button_tv_live)
        self.main_button_home_movie = QtWidgets.QPushButton(self.main_frame_bottom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_home_movie.sizePolicy().hasHeightForWidth())
        self.main_button_home_movie.setSizePolicy(sizePolicy)
        self.main_button_home_movie.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../images/vid_camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_home_movie.setIcon(icon4)
        self.main_button_home_movie.setObjectName("main_button_home_movie")
        self.horizontalLayout.addWidget(self.main_button_home_movie)
        self.gridLayout.addWidget(self.main_frame_bottom, 2, 0, 1, 1)
        self.main_frame_media = QtWidgets.QFrame(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.main_frame_media.sizePolicy().hasHeightForWidth())
        self.main_frame_media.setSizePolicy(sizePolicy)
        self.main_frame_media.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame_media.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame_media.setObjectName("main_frame_media")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.main_frame_media)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.main_frame_left = QtWidgets.QFrame(self.main_frame_media)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.main_frame_left.sizePolicy().hasHeightForWidth())
        self.main_frame_left.setSizePolicy(sizePolicy)
        self.main_frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame_left.setObjectName("main_frame_left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame_left)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_button_inprogress = QtWidgets.QPushButton(self.main_frame_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_inprogress.sizePolicy().hasHeightForWidth())
        self.main_button_inprogress.setSizePolicy(sizePolicy)
        self.main_button_inprogress.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../images/progress.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_inprogress.setIcon(icon5)
        self.main_button_inprogress.setObjectName("main_button_inprogress")
        self.verticalLayout.addWidget(self.main_button_inprogress)
        self.main_button_new = QtWidgets.QPushButton(self.main_frame_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_new.sizePolicy().hasHeightForWidth())
        self.main_button_new.setSizePolicy(sizePolicy)
        self.main_button_new.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../images/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_new.setIcon(icon6)
        self.main_button_new.setObjectName("main_button_new")
        self.verticalLayout.addWidget(self.main_button_new)
        self.main_button_games = QtWidgets.QPushButton(self.main_frame_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_games.sizePolicy().hasHeightForWidth())
        self.main_button_games.setSizePolicy(sizePolicy)
        self.main_button_games.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../images/vid_game.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_games.setIcon(icon7)
        self.main_button_games.setObjectName("main_button_games")
        self.verticalLayout.addWidget(self.main_button_games)
        self.main_button_music_video = QtWidgets.QPushButton(self.main_frame_left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_music_video.sizePolicy().hasHeightForWidth())
        self.main_button_music_video.setSizePolicy(sizePolicy)
        self.main_button_music_video.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../images/music_vid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_music_video.setIcon(icon8)
        self.main_button_music_video.setObjectName("main_button_music_video")
        self.verticalLayout.addWidget(self.main_button_music_video)
        self.horizontalLayout_3.addWidget(self.main_frame_left)
        self.main_graphics = QtWidgets.QGraphicsView(self.main_frame_media)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.main_graphics.sizePolicy().hasHeightForWidth())
        self.main_graphics.setSizePolicy(sizePolicy)
        self.main_graphics.setObjectName("main_graphics")
        self.horizontalLayout_3.addWidget(self.main_graphics)
        self.main_frame_right = QtWidgets.QFrame(self.main_frame_media)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.main_frame_right.sizePolicy().hasHeightForWidth())
        self.main_frame_right.setSizePolicy(sizePolicy)
        self.main_frame_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame_right.setObjectName("main_frame_right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame_right)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_button_images = QtWidgets.QPushButton(self.main_frame_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_images.sizePolicy().hasHeightForWidth())
        self.main_button_images.setSizePolicy(sizePolicy)
        self.main_button_images.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../images/photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_images.setIcon(icon9)
        self.main_button_images.setObjectName("main_button_images")
        self.verticalLayout_2.addWidget(self.main_button_images)
        self.main_button_radio = QtWidgets.QPushButton(self.main_frame_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_radio.sizePolicy().hasHeightForWidth())
        self.main_button_radio.setSizePolicy(sizePolicy)
        self.main_button_radio.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../images/radio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_radio.setIcon(icon10)
        self.main_button_radio.setObjectName("main_button_radio")
        self.verticalLayout_2.addWidget(self.main_button_radio)
        self.main_button_books = QtWidgets.QPushButton(self.main_frame_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_books.sizePolicy().hasHeightForWidth())
        self.main_button_books.setSizePolicy(sizePolicy)
        self.main_button_books.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../images/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_books.setIcon(icon11)
        self.main_button_books.setObjectName("main_button_books")
        self.verticalLayout_2.addWidget(self.main_button_books)
        self.main_button_settings = QtWidgets.QPushButton(self.main_frame_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_button_settings.sizePolicy().hasHeightForWidth())
        self.main_button_settings.setSizePolicy(sizePolicy)
        self.main_button_settings.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../images/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_button_settings.setIcon(icon12)
        self.main_button_settings.setObjectName("main_button_settings")
        self.verticalLayout_2.addWidget(self.main_button_settings)
        self.horizontalLayout_3.addWidget(self.main_frame_right)
        self.gridLayout.addWidget(self.main_frame_media, 1, 0, 1, 1)
        MK_MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MK_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MK_MainWindow)

    def retranslateUi(self, MK_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MK_MainWindow.setWindowTitle(_translate("MK_MainWindow", "MediaKraken"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mk_player.ui'
#
# Created: Tue Aug  8 14:40:11 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MK_Player(object):
    def setupUi(self, MK_Player):
        MK_Player.setObjectName("MK_Player")
        MK_Player.resize(530, 62)
        self.verticalLayout = QtWidgets.QVBoxLayout(MK_Player)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.player_widget = QtWidgets.QWidget(MK_Player)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.player_widget.sizePolicy().hasHeightForWidth())
        self.player_widget.setSizePolicy(sizePolicy)
        self.player_widget.setObjectName("player_widget")
        self.verticalLayout.addWidget(self.player_widget)
        self.control_bar = QtWidgets.QWidget(MK_Player)
        self.control_bar.setObjectName("control_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.control_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(6, 0, 6, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.player_lbl_current_time = QtWidgets.QLabel(self.control_bar)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.player_lbl_current_time.setFont(font)
        self.player_lbl_current_time.setText("")
        self.player_lbl_current_time.setObjectName("player_lbl_current_time")
        self.horizontalLayout_2.addWidget(self.player_lbl_current_time)
        self.player_lbl_divider = QtWidgets.QLabel(self.control_bar)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.player_lbl_divider.setFont(font)
        self.player_lbl_divider.setObjectName("player_lbl_divider")
        self.horizontalLayout_2.addWidget(self.player_lbl_divider)
        self.player_lbl_total_time = QtWidgets.QLabel(self.control_bar)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.player_lbl_total_time.setFont(font)
        self.player_lbl_total_time.setText("")
        self.player_lbl_total_time.setObjectName("player_lbl_total_time")
        self.horizontalLayout_2.addWidget(self.player_lbl_total_time)
        self.player_slider_progress = QtWidgets.QSlider(self.control_bar)
        self.player_slider_progress.setMinimumSize(QtCore.QSize(100, 0))
        self.player_slider_progress.setOrientation(QtCore.Qt.Horizontal)
        self.player_slider_progress.setObjectName("player_slider_progress")
        self.horizontalLayout_2.addWidget(self.player_slider_progress)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.player_btn_play = QtWidgets.QPushButton(self.control_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_btn_play.sizePolicy().hasHeightForWidth())
        self.player_btn_play.setSizePolicy(sizePolicy)
        self.player_btn_play.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.player_btn_play.setFont(font)
        self.player_btn_play.setText("")
        self.player_btn_play.setCheckable(True)
        self.player_btn_play.setObjectName("player_btn_play")
        self.horizontalLayout_3.addWidget(self.player_btn_play)
        self.player_btn_prev = QtWidgets.QPushButton(self.control_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_btn_prev.sizePolicy().hasHeightForWidth())
        self.player_btn_prev.setSizePolicy(sizePolicy)
        self.player_btn_prev.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.player_btn_prev.setFont(font)
        self.player_btn_prev.setFocusPolicy(QtCore.Qt.NoFocus)
        self.player_btn_prev.setText("")
        self.player_btn_prev.setObjectName("player_btn_prev")
        self.horizontalLayout_3.addWidget(self.player_btn_prev)
        self.player_btn_next = QtWidgets.QPushButton(self.control_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_btn_next.sizePolicy().hasHeightForWidth())
        self.player_btn_next.setSizePolicy(sizePolicy)
        self.player_btn_next.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.player_btn_next.setFont(font)
        self.player_btn_next.setFocusPolicy(QtCore.Qt.NoFocus)
        self.player_btn_next.setText("")
        self.player_btn_next.setObjectName("player_btn_next")
        self.horizontalLayout_3.addWidget(self.player_btn_next)
        self.player_audio_select = QtWidgets.QComboBox(self.control_bar)
        self.player_audio_select.setObjectName("player_audio_select")
        self.horizontalLayout_3.addWidget(self.player_audio_select)
        self.player_sub_select = QtWidgets.QComboBox(self.control_bar)
        self.player_sub_select.setObjectName("player_sub_select")
        self.horizontalLayout_3.addWidget(self.player_sub_select)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.player_slider_volume = QtWidgets.QSlider(self.control_bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_slider_volume.sizePolicy().hasHeightForWidth())
        self.player_slider_volume.setSizePolicy(sizePolicy)
        self.player_slider_volume.setMaximum(100)
        self.player_slider_volume.setOrientation(QtCore.Qt.Horizontal)
        self.player_slider_volume.setInvertedAppearance(False)
        self.player_slider_volume.setObjectName("player_slider_volume")
        self.horizontalLayout_3.addWidget(self.player_slider_volume)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.control_bar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(MK_Player)
        QtCore.QMetaObject.connectSlotsByName(MK_Player)

    def retranslateUi(self, MK_Player):
        _translate = QtCore.QCoreApplication.translate
        MK_Player.setWindowTitle(_translate("MK_Player", "Form"))
        self.player_lbl_divider.setText(_translate("MK_Player", "/"))


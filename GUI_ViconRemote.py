# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vicon_External_Trigger.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#

# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import vicon_core_api
from vicon_core_api import *
from vicon_core_api import Client
from vicon_core_api import RPCError
import shogun_live_api
from shogun_live_api import CaptureServices, ApplicationServices
from shogun_live_api.interfaces import CaptureServices, CameraCalibrationServices,SubjectCalibrationServices
from shogun_live_api.interfaces import SubjectServices
#import subject_controller


from Tkinter import *
from PIL import Image, ImageTk
import tkMessageBox
import os
from os import listdir
from os.path import isfile, join
import re
import socket
import time
import shutil
from pathlib import *
import glob
import re
import logging
from datetime import datetime
#from jsonsocket import Client_json, Server
import json
from threading import Thread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        global Start_directory
        global checked
#######################################################################################################################################################################
        C_S_connect=0
        C_T_connect=0
        checked=0
        FOLDER_PATH= "T:\CapturedTrials\\"
        FOLDER_PATH_1= "T:\CapturedTrials"
        FOLDER_PATH_1_S= "S:\MocapDBs\2019_Shogun_database\\"
        Tracker_Database = 'C:\\Users\\sm21438\\Documents\\Framestore\\transfer_test\\Track_DB\\' # temporary master db
        Shogun_Database = 'C:\\Users\\sm21438\\Documents\\Framestore\\transfer_test\\Shogun_DB\\' # temporary master db
        Actor_Cal_Template = 'S:\\Subjects\\' 
        Actor_model_Template = 'S:\\ModelTemplates\\'   
        Actor_Skin_Template = 'S:\\Skin\\'
        Start_directory=os.getcwd()

        Error_Logs="Error_logs"
        try:
            if not os.path.exists(Error_Logs):
                os.makedirs(Error_Logs)
        except OSError:
            pass

        date_output_log=datetime.now()
        date_output_log=date_output_log.strftime("%m_%d_%Y, %H_%M_%S")
        date_output_log=str(date_output_log)
                    
        logging.basicConfig(filename = (''+date_output_log+'_Hub_Error_log.log'), level = logging.INFO)
        error_text="error"
        DESCRIPTION=""
        Select = ""
        external_active=0
        HMC="false"
        recal=0
#######################################################################################################################################################################            
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(820, 634)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(36, 36, 36);\n"
"color: rgb(255, 255, 255);"))
        MainWindow.setWindowIcon(QtGui.QIcon('TheKraken.png'))
        MainWindow.setWindowTitle("Hub")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menubar.setStyleSheet(("""QMenuBar::item{ background: gray;}"""))
        
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)
        self.actionKraken = QtGui.QAction(MainWindow)
        self.actionKraken.setObjectName(_fromUtf8("actionKraken"))
        self.actionKraken.triggered.connect(self.Kraken)
        
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(self.Close)
        ###
        self.actionPrefs = QtGui.QAction(MainWindow)
        self.actionPrefs.setObjectName(_fromUtf8("actionPreferences"))
        self.actionPrefs.triggered.connect(self.properties_window)
        ###
        self.actionActorPrefs = QtGui.QAction(MainWindow)
        self.actionActorPrefs.setObjectName(_fromUtf8("actionActorPrefs"))
        self.actionActorPrefs.triggered.connect(self.Actor_properties_window)
        ###
        self.autotransfer = QtGui.QAction(MainWindow)
        self.autotransfer.setObjectName(_fromUtf8("actionautotransfer"))
        self.autotransfer.triggered.connect(self.activate_autotransfer)                
        ###
        self.actionView_Help = QtGui.QAction(MainWindow)
        self.actionView_Help.setObjectName(_fromUtf8("actionView_Help"))
        self.actionView_Help.triggered.connect(self.Help_PDF)
        ###
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout.triggered.connect(self.About_Hub)
        ###
        self.actionfARsight = QtGui.QAction(MainWindow)
        self.actionfARsight.setObjectName(_fromUtf8("actionfARsight"))
        self.actionfARsight.triggered.connect(self.actionfARsight_func)
        
        self.menuFile.addAction(self.actionKraken)
        self.menuFile.addAction(self.actionfARsight)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionView_Help)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionPrefs)
        self.menuEdit.addAction(self.actionActorPrefs)
        self.menuEdit.addAction(self.autotransfer)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
#######################################################################################################################################################################        
####################################################################################### - Shogun connect button
        self.Shogun_Connect = QtGui.QPushButton(self.centralwidget)
        self.Shogun_Connect.setGeometry(QtCore.QRect(20, 30, 41, 41))
        icon  = QtGui.QPixmap('Shogun.png')
        self.Shogun_Connect.setIcon(QtGui.QIcon(icon))
        self.Shogun_Connect.setText(_fromUtf8(""))
        self.Shogun_Connect.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);"))
        self.Shogun_Connect.setObjectName(_fromUtf8("Shogun_Connect"))
        self.Shogun_Connect.clicked.connect(self.Connect_Shogun)
#######################################################################################################################################################################
####################################################################################### - Tracker connect button
        self.Tracker_Connect = QtGui.QPushButton(self.centralwidget)
        self.Tracker_Connect.setGeometry(QtCore.QRect(20, 80, 41, 41))
        icon  = QtGui.QPixmap('Tracker.png')
        self.Tracker_Connect.setIcon(QtGui.QIcon(icon))
        self.Tracker_Connect.setText(_fromUtf8(""))
        self.Tracker_Connect.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);"))
        self.Tracker_Connect.setObjectName(_fromUtf8("Tracker_Connect"))
        self.Tracker_Connect.clicked.connect(self.Connect_Tracker)           
#######################################################################################################################################################################
####################################################################################### - Shogun connect status   
        self.Shogun_Status = QtGui.QLineEdit(self.centralwidget)
        self.Shogun_Status.setGeometry(QtCore.QRect(70, 50, 231, 20))
        self.Shogun_Status.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Shogun_Status.setText(_fromUtf8(""))
        self.Shogun_Status.setObjectName(_fromUtf8("Shogun_Status"))
#######################################################################################################################################################################
####################################################################################### - Tracker connect status
        self.Tracker_Status = QtGui.QLineEdit(self.centralwidget)
        self.Tracker_Status.setGeometry(QtCore.QRect(70, 100, 231, 20))
        self.Tracker_Status.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Tracker_Status.setText(_fromUtf8(""))
        self.Tracker_Status.setFrame(True)
        self.Tracker_Status.setObjectName(_fromUtf8("Tracker_Status"))
#######################################################################################################################################################################
####################################################################################### - Browse to initial DB
        self.initial_DB_browse = QtGui.QPushButton(self.centralwidget)
        self.initial_DB_browse.setGeometry(QtCore.QRect(260, 410, 97, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.initial_DB_browse.setFont(font)
        self.initial_DB_browse.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.initial_DB_browse.setObjectName(_fromUtf8("Activate_Actor"))
        self.initial_DB_browse.clicked.connect(self.initial_Databases)    
#######################################################################################################################################################################
####################################################################################### - Connect status text
        self.Connect_status = QtGui.QLabel(self.centralwidget)
        self.Connect_status.setGeometry(QtCore.QRect(140, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.Connect_status.setFont(font)
        self.Connect_status.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Connect_status.setObjectName(_fromUtf8("Connect_status"))
#######################################################################################################################################################################
####################################################################################### - IP adress text
        self.IP_Address_Text = QtGui.QLabel(self.centralwidget)
        self.IP_Address_Text.setGeometry(QtCore.QRect(370, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.IP_Address_Text.setFont(font)
        self.IP_Address_Text.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.IP_Address_Text.setObjectName(_fromUtf8("IP_Address_Text"))
#######################################################################################################################################################################
####################################################################################### - Shogun IP address
        self.Shogun_IP = QtGui.QLineEdit(self.centralwidget)
        self.Shogun_IP.setGeometry(QtCore.QRect(320, 50, 171, 20))
        self.Shogun_IP.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Shogun_IP.setText(_fromUtf8(""))
        self.Shogun_IP.setObjectName(_fromUtf8("Shogun_IP"))
#######################################################################################################################################################################
####################################################################################### - Tracker IP address
        self.Tracker_IP = QtGui.QLineEdit(self.centralwidget)
        self.Tracker_IP.setGeometry(QtCore.QRect(320, 100, 171, 20))
        self.Tracker_IP.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Tracker_IP.setText(_fromUtf8(""))
        self.Tracker_IP.setObjectName(_fromUtf8("Tracker_IP"))
#######################################################################################################################################################################
####################################################################################### -Import actor bt
        self.Import_Subject = QtGui.QPushButton(self.centralwidget)
        self.Import_Subject.setGeometry(QtCore.QRect(10, 185, 67, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Import_Subject.setFont(font)
        self.Import_Subject.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Import_Subject.setObjectName(_fromUtf8("Import_Subject"))
        self.Import_Subject.setCheckable(True)
        self.Import_Subject.toggle()
        self.Import_Subject.setEnabled(False)
        self.Import_Subject.clicked.connect(self.Import_Actor_func)
#######################################################################################################################################################################
####################################################################################### - Remove actor button
        self.Remove_Subject = QtGui.QPushButton(self.centralwidget)
        self.Remove_Subject.setGeometry(QtCore.QRect(80, 185, 74, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Remove_Subject.setFont(font)
        self.Remove_Subject.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Remove_Subject.setCheckable(True)
        self.Remove_Subject.toggle()
        self.Remove_Subject.setEnabled(False)
        self.Remove_Subject.setObjectName(_fromUtf8("Remove_Subject"))
        self.Remove_Subject.clicked.connect(self.Remove_Actor_func)
#######################################################################################################################################################################
####################################################################################### - Create actor button
        self.Create_Subject = QtGui.QPushButton(self.centralwidget)
        self.Create_Subject.setGeometry(QtCore.QRect(10, 210, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Create_Subject.setFont(font)
        self.Create_Subject.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Create_Subject.setCheckable(True)
        self.Create_Subject.toggle()
        self.Create_Subject.setEnabled(False)
        self.Create_Subject.setObjectName(_fromUtf8("Create_Subject"))
        self.Create_Subject.clicked.connect(self.Create_Actor_func)
#######################################################################################################################################################################
####################################################################################### - Enable actor button
        self.Enable_Subject = QtGui.QPushButton(self.centralwidget)
        self.Enable_Subject.setGeometry(QtCore.QRect(160, 310, 50, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Enable_Subject.setFont(font)
        self.Enable_Subject.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Enable_Subject.setCheckable(True)
        self.Enable_Subject.toggle()
        self.Enable_Subject.setEnabled(False)
        self.Enable_Subject.setObjectName(_fromUtf8("Create_Subject"))
        self.Enable_Subject.clicked.connect(self.Enable_Actor_func)
#######################################################################################################################################################################
####################################################################################### - Disable actor button
        self.Disable_Subject = QtGui.QPushButton(self.centralwidget)
        self.Disable_Subject.setGeometry(QtCore.QRect(160, 335, 50, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Disable_Subject.setFont(font)
        self.Disable_Subject.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Disable_Subject.setCheckable(True)
        self.Disable_Subject.toggle()
        self.Disable_Subject.setEnabled(False)
        self.Disable_Subject.setObjectName(_fromUtf8("Create_Subject"))
        self.Disable_Subject.clicked.connect(self.Disable_Actor_func)
#######################################################################################################################################################################
####################################################################################### - Set hmc button
        self.Set_HMC_button = QtGui.QPushButton(self.centralwidget)
        self.Set_HMC_button.setGeometry(QtCore.QRect(300, 350, 50, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Set_HMC_button.setFont(font)
        self.Set_HMC_button.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Set_HMC_button.setCheckable(True)
        self.Set_HMC_button.toggle()
        self.Set_HMC_button.setEnabled(False)
        self.Set_HMC_button.setObjectName(_fromUtf8("Create_Subject"))
        self.Set_HMC_button.clicked.connect(self.Set_Actor_Face)
#######################################################################################################################################################################
####################################################################################### - Stop Actor calibration bt
        self.Stop_Actor_Cal = QtGui.QPushButton(self.centralwidget)
        self.Stop_Actor_Cal.setGeometry(QtCore.QRect(10, 270, 85, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Stop_Actor_Cal.setFont(font)
        self.Stop_Actor_Cal.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Stop_Actor_Cal.setCheckable(True)
        self.Stop_Actor_Cal.toggle()
        self.Stop_Actor_Cal.setEnabled(False)
        self.Stop_Actor_Cal.setObjectName(_fromUtf8("Stop_Actor_Cal"))
        self.Stop_Actor_Cal.clicked.connect(self.Stop_Actor_Cal_func)
#######################################################################################################################################################################
####################################################################################### - Cancel Actor calibration bt
        self.Cancel_Actor_Cal = QtGui.QPushButton(self.centralwidget)
        self.Cancel_Actor_Cal.setGeometry(QtCore.QRect(95, 270, 100, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Cancel_Actor_Cal.setFont(font)
        self.Cancel_Actor_Cal.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Cancel_Actor_Cal.setCheckable(True)
        self.Cancel_Actor_Cal.toggle()
        self.Cancel_Actor_Cal.setEnabled(False)
        self.Cancel_Actor_Cal.setObjectName(_fromUtf8("Cancel_Actor_Cal"))
        self.Cancel_Actor_Cal.clicked.connect(self.Cancel_Actor_Cal_func)
#######################################################################################################################################################################
####################################################################################### - recal Actor bt
        self.Actor_reCal = QtGui.QPushButton(self.centralwidget)
        self.Actor_reCal.setGeometry(QtCore.QRect(200, 270, 70, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Actor_reCal.setFont(font)
        self.Actor_reCal.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Actor_reCal.setCheckable(True)
        self.Actor_reCal.toggle()
        self.Actor_reCal.setEnabled(False)
        self.Actor_reCal.setObjectName(_fromUtf8("Cancel_Actor_Cal"))
        self.Actor_reCal.clicked.connect(self.Actor_reCal_func)
#######################################################################################################################################################################
####################################################################################### - T-Pose bt
        self.TPose = QtGui.QPushButton(self.centralwidget)
        self.TPose.setGeometry(QtCore.QRect(10, 235, 80, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.TPose.setFont(font)
        self.TPose.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.TPose.setCheckable(True)
        self.TPose.toggle()
        self.TPose.setEnabled(False)
        self.TPose.setObjectName(_fromUtf8("T-Pose"))
        self.TPose.clicked.connect(self.TPose_Actor_func)
#######################################################################################################################################################################
####################################################################################### - actor Labelling  text
        self.Set_Labelling = QtGui.QLabel(self.centralwidget)
        self.Set_Labelling.setGeometry(QtCore.QRect(170, 185, 97, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Set_Labelling.setFont(font)
        self.Set_Labelling.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Set_Labelling.setObjectName(_fromUtf8("Set_Labelling"))
#######################################################################################################################################################################
####################################################################################### - HMC txt
        self.HMC_text = QtGui.QLabel(self.centralwidget)
        self.HMC_text.setGeometry(QtCore.QRect(290, 290, 97, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.HMC_text.setFont(font)
        self.HMC_text.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.HMC_text.setObjectName(_fromUtf8("HMC_text_t"))
#######################################################################################################################################################################
####################################################################################### - actor Solving text
        self.Set_Solving = QtGui.QLabel(self.centralwidget)
        self.Set_Solving.setGeometry(QtCore.QRect(170, 210, 97, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Set_Solving.setFont(font)
        self.Set_Solving.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Set_Solving.setObjectName(_fromUtf8("Set_Solving"))
#######################################################################################################################################################################
####################################################################################### - actor Skin text
        self.Set_Skin = QtGui.QLabel(self.centralwidget)
        self.Set_Skin.setGeometry(QtCore.QRect(170, 235, 50, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Set_Skin.setFont(font)
        self.Set_Skin.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Set_Skin.setObjectName(_fromUtf8("Set_Skin"))
#######################################################################################################################################################################
####################################################################################### - actor name box
        self.Subject_Name = QtGui.QLineEdit(self.centralwidget)
        self.Subject_Name.setGeometry(QtCore.QRect(83, 216, 75, 15))
        self.Subject_Name.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Subject_Name.setFrame(True)
        self.Subject_Name.setObjectName(_fromUtf8("Subject_Name"))
#######################################################################################################################################################################
####################################################################################### - actor List Widget
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 310, 150, 40))
        self.listWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);""color: rgb(0, 0, 0);\n"))
        self.listWidget.setObjectName(_fromUtf8("scrollArea_3"))
#######################################################################################################################################################################
####################################################################################### - HMC List Widget
        self.listWidget_HMC = QtGui.QListWidget(self.centralwidget)
        self.listWidget_HMC.setGeometry(QtCore.QRect(220, 310, 150, 40))
        self.listWidget_HMC.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);""color: rgb(0, 0, 0);\n"))
        self.listWidget_HMC.setObjectName(_fromUtf8("scrollArea_3"))
#######################################################################################################################################################################
####################################################################################### - Face capture active drop down
        self.Face_Dropdown= QtGui.QComboBox(self.centralwidget)
        self.Face_Dropdown.setGeometry(QtCore.QRect(220, 350, 67, 20))
        self.Face_Dropdown.addItem("false")
        self.Face_Dropdown.addItem("true")
        self.Face_Dropdown.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);"))
#######################################################################################################################################################################
####################################################################################### - Actor Labelling drop down
        self.Label_Dropdown= QtGui.QComboBox(self.centralwidget)
        self.Label_Dropdown.setGeometry(QtCore.QRect(265, 185, 130, 21))
        self.Label_Dropdown.addItem("")
        self.Label_Dropdown.addItem("FrontBackWaist")
        self.Label_Dropdown.addItem("FrontBackWaistFingers")
        self.Label_Dropdown.addItem("SidesWaist")
        self.Label_Dropdown.addItem("SidesWaistFingers")
        self.Label_Dropdown.addItem("VrsFingersSides5me")
        self.Label_Dropdown.addItem("Vrs5me_FrontBackWaistFingers")
        self.Label_Dropdown.addItem("Vrs5me_SidesWaistFingers")
        self.Label_Dropdown.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);"))
        self.Label_Dropdown.currentIndexChanged.connect(self.Set_Actor_Labelling_func)
#######################################################################################################################################################################
####################################################################################### - Actor Solver drop down
        self.Solver_Dropdown= QtGui.QComboBox(self.centralwidget)
        self.Solver_Dropdown.setGeometry(QtCore.QRect(265, 210, 130, 21))
        self.Solver_Dropdown.addItem("")
        self.Solver_Dropdown.addItem("FrontBackWaist")
        self.Solver_Dropdown.addItem("FrontBackWaistFingers")
        self.Solver_Dropdown.addItem("SidesWaist")
        self.Solver_Dropdown.addItem("SidesWaistFingers")
        self.Solver_Dropdown.addItem("VrsFingersSides5me")
        self.Solver_Dropdown.addItem("Vrs5me_FrontBackWaistFingers")
        self.Solver_Dropdown.addItem("Vrs5me_SidesWaistFingers")
        self.Solver_Dropdown.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);"))
        self.Solver_Dropdown.currentIndexChanged.connect(self.Set_Actor_Solving_func)
#######################################################################################################################################################################
####################################################################################### - Actor Skin drop down
        self.Skin_Dropdown= QtGui.QComboBox(self.centralwidget)
        self.Skin_Dropdown.setGeometry(QtCore.QRect(265, 235, 130, 21))
        self.Skin_Dropdown.addItem("")
        self.Skin_Dropdown.addItem("ViconMale")
        self.Skin_Dropdown.addItem("ViconFemale")
        self.Skin_Dropdown.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);"))
        self.Skin_Dropdown.currentIndexChanged.connect(self.Set_Actor_Skin_func)
#######################################################################################################################################################################
####################################################################################### - take name box
        self.Take_Name_Box = QtGui.QLineEdit(self.centralwidget)
        self.Take_Name_Box.setGeometry(QtCore.QRect(20, 470, 231, 20))
        self.Take_Name_Box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Take_Name_Box.setText(_fromUtf8(""))
        self.Take_Name_Box.setFrame(True)
        self.Take_Name_Box.setObjectName(_fromUtf8("Take_Name_Box"))
####################################################################################### - Directory box
        self.Dir_Box = QtGui.QLineEdit(self.centralwidget)
        self.Dir_Box.setGeometry(QtCore.QRect(20, 410, 231, 20))
        self.Dir_Box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Dir_Box.setText(_fromUtf8(""))
        self.Dir_Box.setFrame(True)
        self.Dir_Box.setObjectName(_fromUtf8("Dir_Box"))
#######################################################################################################################################################################
####################################################################################### Set take name button
        self.Set_Take_Name_Button = QtGui.QPushButton(self.centralwidget)
        self.Set_Take_Name_Button.setGeometry(QtCore.QRect(260, 470, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Set_Take_Name_Button.setFont(font)
        self.Set_Take_Name_Button.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Set_Take_Name_Button.setObjectName(_fromUtf8("Set_Take_Name_Button"))
        self.Set_Take_Name_Button.clicked.connect(self.Set_Trial_Name)
#######################################################################################################################################################################
####################################################################################### Record start button
        self.Record_Button_Start = QtGui.QPushButton(self.centralwidget)
        self.Record_Button_Start.setGeometry(QtCore.QRect(30, 500, 211, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.Record_Button_Start.setFont(font)
        self.Record_Button_Start.setStyleSheet(_fromUtf8("background-color: rgb(0, 120, 0);\n"
"color: rgb(255, 255, 255);"))
        self.Record_Button_Start.setFlat(False)
        self.Record_Button_Start.setObjectName(_fromUtf8("Record_Button_Start"))
        self.Record_Button_Start.clicked.connect(self.Start_Recording)
#######################################################################################################################################################################
####################################################################################### - Record stop button
        self.Record_Button_Stop = QtGui.QPushButton(self.centralwidget)
        self.Record_Button_Stop.setGeometry(QtCore.QRect(30, 550, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        self.Record_Button_Stop.setFont(font)
        self.Record_Button_Stop.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(120, 0, 0);"))
        self.Record_Button_Stop.setObjectName(_fromUtf8("Record_Button_Stop"))
        self.Record_Button_Stop.clicked.connect(self.Stop_Recording)
#######################################################################################################################################################################
####################################################################################### -Cancel record button
        self.Cancel_Record_Bt = QtGui.QPushButton(self.centralwidget)
        self.Cancel_Record_Bt.setGeometry(QtCore.QRect(140, 550, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Cancel_Record_Bt.setFont(font)
        self.Cancel_Record_Bt.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);\n"
"color: rgb(255, 255, 255);"))
        self.Cancel_Record_Bt.setObjectName(_fromUtf8("Cancel_Record_Bt"))
        self.Cancel_Record_Bt.clicked.connect(self.Cancel_Recording)
#######################################################################################################################################################################
####################################################################################### - Take Description box
        self.Take_Description_Box = QtGui.QLineEdit(self.centralwidget)
        self.Take_Description_Box.setGeometry(QtCore.QRect(400, 340, 231, 20))
        self.Take_Description_Box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Take_Description_Box.setFrame(True)
        self.Take_Description_Box.setObjectName(_fromUtf8("Take_Description_Box"))
#######################################################################################################################################################################
####################################################################################### - Transfer folder box
        self.folder_Description_Box = QtGui.QLineEdit(self.centralwidget)
        self.folder_Description_Box.setGeometry(QtCore.QRect(20, 440, 231, 20))
        self.folder_Description_Box.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.folder_Description_Box.setFrame(True)
        self.folder_Description_Box.setObjectName(_fromUtf8("folder_Description_Box"))
#######################################################################################################################################################################
####################################################################################### - About button
        self.About_bt = QtGui.QPushButton(self.centralwidget)
        self.About_bt.setGeometry(QtCore.QRect(778, 20, 21, 21))
        icon  = QtGui.QPixmap('FStore.png')
        self.About_bt.setIcon(QtGui.QIcon(icon))
        self.About_bt.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);"))
        self.About_bt.setObjectName(_fromUtf8("About_bt"))
        self.About_bt.clicked.connect(self.About_Hub)
#######################################################################################################################################################################
####################################################################################### - shogun - transfer bt
        self.Shogun_transfer = QtGui.QLabel(self.centralwidget)
        self.Shogun_transfer.setGeometry(QtCore.QRect(720, 310, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.Shogun_transfer.setFont(font)
        self.Shogun_transfer.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Shogun_transfer.setObjectName(_fromUtf8("Shogun_transfer"))
#######################################################################################################################################################################
####################################################################################### - tracker - transfer bt
        self.Transfer_Bt = QtGui.QLabel(self.centralwidget)
        self.Transfer_Bt.setGeometry(QtCore.QRect(720, 500, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.Transfer_Bt.setFont(font)
        self.Transfer_Bt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Transfer_Bt.setObjectName(_fromUtf8("Tracker_transfer"))
#######################################################################################################################################################################
####################################################################################### - close button
        self.Close_Bt = QtGui.QPushButton(self.centralwidget)
        self.Close_Bt.setGeometry(QtCore.QRect(690, 570, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Close_Bt.setFont(font)
        self.Close_Bt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Close_Bt.setObjectName(_fromUtf8("Cancel_Record_Bt"))
        self.Close_Bt.clicked.connect(self.Close)
#######################################################################################################################################################################
####################################################################################### - S database
        self.S_database = QtGui.QListWidget(self.centralwidget)
        self.S_database.setGeometry(QtCore.QRect(400, 180, 311, 141))
        self.S_database.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);""color: rgb(0, 0, 0);\n"))
        self.S_database.setObjectName(_fromUtf8("scrollArea"))
#######################################################################################################################################################################
####################################################################################### - T database
        self.T_database = QtGui.QListWidget(self.centralwidget)
        self.T_database.setGeometry(QtCore.QRect(400, 400, 311, 121))
        self.T_database.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);""color: rgb(0, 0, 0);\n"))
        self.T_database.setObjectName(_fromUtf8("scrollArea_2"))
#######################################################################################################################################################################
####################################################################################### - S icon
        self.Shogun_icon = QtGui.QPushButton(self.centralwidget)
        self.Shogun_icon.setGeometry(QtCore.QRect(750, 270, 31, 31))
        icon  = QtGui.QPixmap('Shogun.png')
        self.Shogun_icon.setIcon(QtGui.QIcon(icon))
        self.Shogun_icon.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);"))
        self.Shogun_icon.setObjectName(_fromUtf8("Shogun_icon"))
        self.Shogun_icon.clicked.connect(self.Transfer_Files_S)
#######################################################################################################################################################################
####################################################################################### - T icon
        self.Tracker_icon = QtGui.QPushButton(self.centralwidget)
        self.Tracker_icon.setGeometry(QtCore.QRect(750, 460, 31, 31))
        icon  = QtGui.QPixmap('Tracker.png')
        self.Tracker_icon.setIcon(QtGui.QIcon(icon))
        self.Tracker_icon.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);"))
        self.Tracker_icon.setObjectName(_fromUtf8("Tracker_icon"))
        self.Tracker_icon.clicked.connect(self.Transfer_Files)
#######################################################################################################################################################################
####################################################################################### - update file descr button
        self.file_desc = QtGui.QPushButton(self.centralwidget)
        self.file_desc.setGeometry(QtCore.QRect(640, 340, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.file_desc.setFont(font)
        self.file_desc.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.file_desc.setObjectName(_fromUtf8("Set_Take_Name_Button_5"))
        self.file_desc.clicked.connect(self.Update_Description)
#######################################################################################################################################################################
####################################################################################### - Set_discard button
        self.Set_discard = QtGui.QPushButton(self.centralwidget)
        self.Set_discard.setGeometry(QtCore.QRect(510, 370, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Set_discard.setFont(font)
        self.Set_discard.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Set_discard.setObjectName(_fromUtf8("Set_Take_Name_Button_5"))
        self.Set_discard.clicked.connect(self.Set_discard_func)
#######################################################################################################################################################################
####################################################################################### - Set_Select button
        self.Set_Select = QtGui.QPushButton(self.centralwidget)
        self.Set_Select.setGeometry(QtCore.QRect(420, 370, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Set_Select.setFont(font)
        self.Set_Select.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Set_Select.setObjectName(_fromUtf8("Set_Take_Name_Button_5"))
        self.Set_Select.clicked.connect(self.Set_Select_func)
#######################################################################################################################################################################
####################################################################################### - AutoTransfer button
        self.Auto_Transfer_bt = QtGui.QCheckBox(self.centralwidget)
        self.Auto_Transfer_bt.setGeometry(QtCore.QRect(360, 570, 110, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Auto_Transfer_bt.setFont(font)
        self.Auto_Transfer_bt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Auto_Transfer_bt.setObjectName(_fromUtf8("Auto_Transfer_bt"))
        self.Auto_Transfer_bt.setCheckable(False)
        self.Auto_Transfer_bt.toggle()
        self.Auto_Transfer_bt.setEnabled(False)
#######################################################################################################################################################################
####################################################################################### - External trigger button
        self.External_trig = QtGui.QCheckBox(self.centralwidget)
        self.External_trig.setGeometry(QtCore.QRect(360, 550, 110, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.External_trig.setFont(font)
        self.External_trig.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.External_trig.setObjectName(_fromUtf8("External_trig"))
        self.External_trig.stateChanged.connect(self.External_control)
#######################################################################################################################################################################
####################################################################################### - Unreal stream button
        self.Unreal_stream_bt = QtGui.QCheckBox(self.centralwidget)
        self.Unreal_stream_bt.setGeometry(QtCore.QRect(260, 550, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Unreal_stream_bt.setFont(font)
        self.Unreal_stream_bt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Unreal_stream_bt.setObjectName(_fromUtf8("Auto_Transfer_bt"))
        self.Unreal_stream_bt.stateChanged.connect(self.UnrealThread)
#######################################################################################################################################################################
####################################################################################### - Face stream button
        self.Face_stream_bt = QtGui.QCheckBox(self.centralwidget)
        self.Face_stream_bt.setGeometry(QtCore.QRect(260, 570, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Face_stream_bt.setFont(font)
        self.Face_stream_bt.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Face_stream_bt.setObjectName(_fromUtf8("Auto_Transfer_bt"))
        self.Face_stream_bt.stateChanged.connect(self.FaceThread)
#######################################################################################################################################################################
####################################################################################### - Actor setup button
        self.Activate_Actor = QtGui.QCheckBox(self.centralwidget)
        self.Activate_Actor.setGeometry(QtCore.QRect(30, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Activate_Actor.setFont(font)
        self.Activate_Actor.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);"))
        self.Activate_Actor.setObjectName(_fromUtf8("Activate_Actor"))
        self.Activate_Actor.stateChanged.connect(self.Actor)
#######################################################################################################################################################################
####################################################################################### - Browse to shogun database
        self.DB_browse = QtGui.QPushButton(self.centralwidget)
        self.DB_browse.setGeometry(QtCore.QRect(715, 185, 100, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.DB_browse.setFont(font)
        self.DB_browse.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.DB_browse.setObjectName(_fromUtf8("Activate_Actor"))
        self.DB_browse.clicked.connect(self.Databases)
#######################################################################################################################################################################
####################################################################################### - Browse to Tracker database
        self.T_DB_browse = QtGui.QPushButton(self.centralwidget)
        self.T_DB_browse.setGeometry(QtCore.QRect(715, 400, 100, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.T_DB_browse.setFont(font)
        self.T_DB_browse.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.T_DB_browse.setObjectName(_fromUtf8("Activate_Actor"))
        self.T_DB_browse.clicked.connect(self.T_Databases)
#######################################################################################################################################################################
####################################################################################### - Logger
        self.Logger = QtGui.QTextBrowser(self.centralwidget)
        self.Logger.setGeometry(QtCore.QRect(500, 50, 271, 70))
        self.Logger.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Logger.setObjectName(_fromUtf8("Logger"))
        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
#######################################################################################
#######################################################################################################################################################################
        self.Subject_Setup = QtGui.QLabel(self.centralwidget)
        self.Subject_Setup.setGeometry(QtCore.QRect(140, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.Subject_Setup.setFont(font)
        self.Subject_Setup.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Subject_Setup.setObjectName(_fromUtf8("Subject_Setup"))
#######################################################################################################################################################################      
        self.Data_Capture_Text = QtGui.QLabel(self.centralwidget)
        self.Data_Capture_Text.setGeometry(QtCore.QRect(90, 380, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.Data_Capture_Text.setFont(font)
        self.Data_Capture_Text.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Data_Capture_Text.setObjectName(_fromUtf8("Data_Capture_Text"))
#######################################################################################################################################################################
        self.Database_transfer = QtGui.QLabel(self.centralwidget)
        self.Database_transfer.setGeometry(QtCore.QRect(470, 150, 151, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.Database_transfer.setFont(font)
        self.Database_transfer.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Database_transfer.setObjectName(_fromUtf8("Database_transfer"))
#######################################################################################################################################################################       
        self.Connect_text = QtGui.QLabel(self.centralwidget)
        self.Connect_text.setGeometry(QtCore.QRect(20, 10, 51, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)  
        self.Connect_text.setFont(font)
        self.Connect_text.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Connect_text.setObjectName(_fromUtf8("Connect_text"))
#######################################################################################################################################################################
        self.About_text = QtGui.QLabel(self.centralwidget)
        self.About_text.setGeometry(QtCore.QRect(775, 0, 51, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.About_text.setFont(font)
        self.About_text.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.About_text.setObjectName(_fromUtf8("About_text"))
#######################################################################################################################################################################
        self.Logger_Text = QtGui.QLabel(self.centralwidget)
        self.Logger_Text.setGeometry(QtCore.QRect(620, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.Logger_Text.setFont(font)
        self.Logger_Text.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Logger_Text.setObjectName(_fromUtf8("Logger_Text"))
#######################################################################################################################################################################
        self.Capture_state = QtGui.QLabel(self.centralwidget)
        self.Capture_state.setGeometry(QtCore.QRect(255, 515, 51, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.Capture_state.setFont(font)
        self.Capture_state.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Capture_state.setObjectName(_fromUtf8("Capture_state"))
#######################################################################################################################################################################
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 130, 821, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
#######################################################################################################################################################################
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 370, 311, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#######################################################################################################################################################################
#######################################################################################################################################################################

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Hub", None))
        self.Connect_status.setText(_translate("MainWindow", "Status", None))
        self.IP_Address_Text.setText(_translate("MainWindow", "IP Address", None))
        self.Data_Capture_Text.setText(_translate("MainWindow", "Data Capture", None))
        self.Set_Take_Name_Button.setText(_translate("MainWindow", "Set Take Name", None))
        self.Record_Button_Start.setText(_translate("MainWindow", "Start", None))
        self.Record_Button_Stop.setText(_translate("MainWindow", "Stop", None))
        self.Cancel_Record_Bt.setText(_translate("MainWindow", "Cancel", None))
        self.Subject_Setup.setText(_translate("MainWindow", "Actor Setup", None))
        self.Import_Subject.setText(_translate("MainWindow", "Import Actor", None))
        self.Create_Subject.setText(_translate("MainWindow", "Create Actor", None))
        self.Set_Labelling.setText(_translate("MainWindow", "Set Label Template", None))
        self.Set_Solving.setText(_translate("MainWindow", "Set Solve Template", None))
        self.Set_Skin.setText(_translate("MainWindow", "Set Skin", None))
        self.Remove_Subject.setText(_translate("MainWindow", "Remove Actor", None))
        self.Close_Bt.setText(_translate("MainWindow", "Close", None))
        self.Transfer_Bt.setText(_translate("MainWindow", "Transfer Files", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionView_Help.setText(_translate("MainWindow", "View Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.Database_transfer.setText(_translate("MainWindow", "Database Transfer", None))
        self.folder_Description_Box.setText(_translate("MainWindow", "New Folder Name...", None))
        self.Dir_Box.setText(_translate("MainWindow", "Save Directory...", None))
        self.Take_Description_Box.setText(_translate("MainWindow", "Take Description...", None))
        self.Shogun_transfer.setText(_translate("MainWindow", "Transfer Files", None))
        self.Subject_Name.setText(_translate("MainWindow", "Actor Name...", None))
        self.file_desc.setText(_translate("MainWindow", "Update File", None))
        self.Connect_text.setText(_translate("MainWindow", "Connect", None))
        self.Auto_Transfer_bt.setText(_translate("MainWindow", "Auto Transfer", None))
        self.Unreal_stream_bt.setText(_translate("MainWindow", "Unreal Stream", None))
        self.Activate_Actor.setText(_translate("MainWindow", "Activate setup", None))
        self.About_text.setText(_translate("MainWindow", "About", None))
        self.DB_browse.setText(_translate("MainWindow", "Browse Database", None))
        self.Capture_state.setText(_translate("MainWindow", "Ready", None))
        self.Logger_Text.setText(_translate("MainWindow", "Log", None))
        self.actionPrefs.setText(_translate("MainWindow", "Database Management", None))
        self.TPose.setText(_translate("MainWindow", "Accept T-pose", None))
        self.Stop_Actor_Cal.setText(_translate("MainWindow", "Stop Calibration", None))
        self.Cancel_Actor_Cal.setText(_translate("MainWindow", "Cancel Calibration", None))
        self.actionActorPrefs.setText(_translate("MainWindow", "Actor Management", None))
        self.Enable_Subject.setText(_translate("MainWindow", "Enable", None))
        self.Disable_Subject.setText(_translate("MainWindow", "Disable", None))
        self.Set_discard.setText(_translate("MainWindow", "Burn", None))
        self.Set_Select.setText(_translate("MainWindow", "Select", None))
        self.External_trig.setText(_translate("MainWindow", "External control", None))
        self.Face_stream_bt.setText(_translate("MainWindow", "Face Stream", None))
        self.actionKraken.setText(_translate("MainWindow", "fARsight Home", None))
        self.HMC_text.setText(_translate("MainWindow", "HMC Status", None))
        self.Set_HMC_button.setText(_translate("MainWindow", "Set", None))
        self.Actor_reCal.setText(_translate("MainWindow", "Recalibrate", None))
        self.T_DB_browse.setText(_translate("MainWindow", "Browse Database", None))
        self.initial_DB_browse.setText(_translate("MainWindow", "Check Database", None))
        self.autotransfer.setText(_translate("MainWindow", "Enable Auto transfer", None))
        self.actionfARsight.setText(_translate("MainWindow", "Launch Farsight light", None))
#######################################################################################################################################################################
       
    def Connect_Shogun(self):

    # Connects to Shogun based on IP adress - Output = database folder location and IP address

        global C_T
        global C_S
        global C_S_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        
        C_S = Client('192.168.1.223')
        
        if C_S.connected ==True:
                Subject_info=SubjectServices(C_S)
                self.Shogun_Status.setText("Connected")
                self.Shogun_IP.setText(str(C_S.socket.getpeername()))
                
                self.capture_service = CaptureServices(C_S)
                _result, capture_folder_S = self.capture_service.capture_folder()  #capture_folder_S shogun local DB
                FOLDER_PATH_1_S=str(capture_folder_S)
                S_drive='S:\\'
                FOLDER_PATH_1_S_split=FOLDER_PATH_1_S.split('E:\\MocapDBs\\')
                if len(FOLDER_PATH_1_S_split)==1:
                        FOLDER_PATH_1_S_split=FOLDER_PATH_1_S_split[0]
                        FOLDER_PATH_1_S_split=str(FOLDER_PATH_1_S_split)
                elif len(FOLDER_PATH_1_S_split)==2:
                        FOLDER_PATH_1_S_split=FOLDER_PATH_1_S_split[1]
                        FOLDER_PATH_1_S_split=str(FOLDER_PATH_1_S_split)
                        
                FOLDER_PATH_1_S= S_drive + FOLDER_PATH_1_S_split
                self.Dir_Box.setText(FOLDER_PATH_1_S)
           
                C_S_connect=1


         #       self.Unreal_stream_bt.setChecked(True)
          #      self.Face_stream_bt.setChecked(True)
                
                if C_S_connect==1:
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error_text=error_time + " " + "Shogun Connected"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
        
        elif C_S.connected ==False:
                try:
                    self.Shogun_IP.setText(str(C_S.socket.getpeername()))
                except IOError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time +e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "Shogun connection error"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################

    def Connect_Tracker(self):

    # Connects to Tracker based on IP adress  - Output = database folder location and IP address

        global C_T
        global C_S
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        C_T = Client('192.168.1.224')
        UDP_IP='192.168.1.224'
        UDP_PORT = 30
        bufferSize  = 1024
        PacketID=0
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        if C_T.connected ==True:
            self.Tracker_Status.setText("Connected")
            self.Tracker_IP.setText(str(C_T.socket.getpeername()))
            C_T_connect=1
            if C_T_connect==1:
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Shogun Connected"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
            
        elif C_T.connected ==False:
            try:
                self.Tracker_IP.setText(str(C_T.socket.getpeername()))
            except IOError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time +e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "Tracker connection error"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
    def UnrealThread(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global New_File_Increment
        global Trial_Name_S
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        t1=Thread(target=self.connect_Unreal)
        t1.setDaemon(True)
        t1.start()
#######################################################################################################################################################################
    def FaceThread(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global New_File_Increment
        global Trial_Name_S
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        t2=Thread(target=self.connect_Face)
        t2.setDaemon(True)
        t2.start()
#######################################################################################################################################################################        
    def connect_Unreal(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global New_File_Increment
        global Trial_Name_S
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

                #### for json file info save ###
        
        Trial_Name_S="Test_01" #temp
        Notes=DESCRIPTION
        Timecode_start="01:03:40:00" #temp
        Tracker_Database = 'C:\\Users\\sm21438\\Documents\\Framestore\\transfer_test\\Track_DB\\' # temporary master db
        Shogun_Database = 'C:\\Users\\sm21438\\Documents\\Framestore\\transfer_test\\Shogun_DB\\' # temporary master db
        FOLDER_PATH_1_S="Test_folder" #temp
        date_output=datetime.now()
        date_output=date_output.strftime("%m/%d/%Y, %H:%M:%S")
        date_output_split=date_output.split(',')
        date=date_output_split[0]
        json_file_U={"Take_Name": Trial_Name_S,
                    "Actors": {
                        "David": False,
                        "Jason": True,
                        "Kate": False},
                    "Select_Status": "Select",
                    "Notes": Notes,
                    "Shogun file path:" : Shogun_Database,
                    "Tracker file path:" : Tracker_Database,
                    "Face file path:" : "C:/Program Files/Epic Games",
                    "Date:" : date,
                    "Timecode In:" : Timecode_start,
                    "Timecode Out:" : "00:00:00:00",
                    "Project:" : FOLDER_PATH_1_S
                    }   
        JSON_String_U=json.dumps(json_file_U)
        if self.Unreal_stream_bt.isChecked()==True:
            sock_U=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            host_U= '192.168.1.225' #connects to the server IP addresss###
            port_U=9000
            server_address_U=(host_U,port_U)
            try:
                sock_U.connect(server_address_U)
                try:
                    message_U = JSON_String_U
                    sock_U.sendall(message_U)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error_text=error_time + " " + "Unreal stream connected"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                
                    while self.Unreal_stream_bt.isChecked()==True:
                      data_U=JSON_String_U
                   #   print("sending", data_U)
                finally:
                    #print('closing socket')
                    sock_U.close()
            except Exception as e:
                e = str(e)
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error = error_time +e
                error_text=error_time + " " + "No Unreal server running"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
        elif self.Unreal_stream_bt.isChecked()==False:
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Unreal stream disconnected"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################                
    def connect_Face(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global New_File_Increment
        global Trial_Name_S
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

                    #### for json file info save ###
        
        Trial_Name_S="Test_01" #temp
        Notes=DESCRIPTION
        Timecode_start="01:03:40:00" #temp
        Tracker_Database = 'C:\\Users\\sm21438\\Documents\\Framestore\\transfer_test\\Track_DB\\' # temporary master db
        Shogun_Database = 'C:\\Users\\sm21438\\Documents\\Framestore\\transfer_test\\Shogun_DB\\' # temporary master db
        FOLDER_PATH_1_S="Test_folder" #temp
        date_output=datetime.now()
        date_output=date_output.strftime("%m/%d/%Y, %H:%M:%S")
        date_output_split=date_output.split(',')
        date=date_output_split[0]
        json_file_F={"Take_Name": Trial_Name_S,
                    "Actors": {
                        "David": False,
                        "Jason": True,
                        "Kate": False},
                    "Select_Status": "Select",
                    "Notes": Notes,
                    "Shogun file path:" : Shogun_Database,
                    "Tracker file path:" : Tracker_Database,
                    "Face file path:" : "C:/Program Files/Epic Games",
                    "Date:" : date,
                    "Timecode In:" : Timecode_start,
                    "Timecode Out:" : "00:00:00:00",
                    "Project:" : FOLDER_PATH_1_S
                    }
        if self.Face_stream_bt.isChecked()==True:
            JSON_String_F=json.dumps(json_file_F)
            sock_F=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            host_F= '192.168.1.226'
            port_F=9000
            server_address_F=(host_F,port_F)
            try:
                sock_F.connect(server_address_F)
            
                try:
                    message_F = JSON_String_F
                    sock_F.sendall(message_F)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error_text=error_time + " " + "Face stream connected"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                    
                    while self.Face_stream_bt.isChecked()==True:
                      data_F=JSON_String_F
                finally:
                    sock_F.close()                

            
            except Exception as e:
                e = str(e)
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error = error_time +e
                error_text=error_time + " " + "No Face server running"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
                
        elif self.Face_stream_bt.isChecked()==False:
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Face stream disconnected"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
        
#######################################################################################################################################################################                             
    def Set_Trial_Name(self):

    # When button pressed trial name for take is set up - initial Tracker start up needs dummy character (i.e. "A") before being armed

        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global New_File_Increment
        global Trial_Name_S
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        Trial_Name_S = str(self.Take_Name_Box.text())
        try:
            self.Take_Name_Box_EXT.setText(_translate("MainWindow", Trial_Name_S, None))
        except AttributeError as e:
                e = str(e)
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error = error_time +e
                error_text=error_time + " " + "Warning external control not open"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
        
        if C_S_connect==1:
            if C_S.connected ==True:
                if external_active==0:
                    Trial_Name_S = str(self.Take_Name_Box.text())
                elif external_active==1:
                    Trial_Name_S = str(self.Take_Name_Box_EXT.text())
                    self.Take_Name_Box.setText(Trial_Name_S)
                    
                services_S = CaptureServices(C_S)
                result_S = services_S.set_capture_name(Trial_Name_S)
                New_File_Increment=re.sub(r'\d+','',Trial_Name_S)
                increment = 0

                
                Vicon_Files=self.folder_Description_Box.text()
                Vicon_Files=str(Vicon_Files)
                Transfer_Path_Orig = FOLDER_PATH_1_S
                Transfer_Path=Transfer_Path_Orig + '\\' + Vicon_Files
                try:
                   if not os.path.exists(Transfer_Path):
                          os.makedirs(Transfer_Path)
                except OSError:
                        pass              
                
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Shogun File Name Updated"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
        if C_T_connect==1:
            if C_T.connected ==True:
                if external_active==0:
                    CAPTURE_NAME = str(self.Take_Name_Box.text())
                elif external_active==1:
                    CAPTURE_NAME = str(self.Take_Name_Box_EXT.text())
                
                self.Take_Description_Box.setObjectName(_fromUtf8("Take_Description_Box"))
                DESCRIPTION=self.Take_Description_Box.text()

                Vicon_Files=self.folder_Description_Box.text()
                Vicon_Files=str(Vicon_Files)
                Transfer_Path_Orig = FOLDER_PATH_1
                Transfer_Path=Transfer_Path_Orig + '\\' + Vicon_Files                    
                ################## Tracker ####### ### move files to new folder in local database #######

                try:
                    if not os.path.exists(Transfer_Path):
                        os.makedirs(Transfer_Path)
                except OSError:
                    pass

                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Tracker File Name Updated"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
                
    def Start_Recording(self):

    # On button press command sent to shogun to start, Tracker command sent (packet ID increments by 1 each time)

        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global Shogun_ENF
        global error_text
        global host
        global port
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        if C_S_connect==1:
            if C_S.connected ==True:
                self.Capture_state.setText(_translate("MainWindow", "Capturing...", None))
                Shogun_ENF = [f for f in listdir(FOLDER_PATH_1_S) if isfile(join(FOLDER_PATH_1_S,f))]
                controller_S=CaptureServices(C_S)
                controller_S.start_capture()

                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Shogun recording"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
        if C_T_connect==1:
            if C_T.connected ==True:
                if PacketID ==0:              
                    PacketID=str(PacketID)
                    CAPTURE_START='<?xml version="1.0" encoding="UTF-8" standalone="no" ?><CaptureStart><Name VALUE="'+ CAPTURE_NAME + '"/><Notes VALUE=""/><Description VALUE=""/><DatabasePath VALUE="'+ FOLDER_PATH + '"/><Delay VALUE="250"/><PacketID VALUE="'+ PacketID + '"/></CaptureStart>\x00';
                    sock.sendto(CAPTURE_START, (UDP_IP, UDP_PORT))
                    PacketID=int(PacketID)
                    PacketID=PacketID+1

                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error_text=error_time + " " + "Tracker recording"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                
                elif PacketID>0:
                    PacketID=PacketID+1
                    PacketID=str(PacketID)
                    CAPTURE_START='<?xml version="1.0" encoding="UTF-8" standalone="no" ?><CaptureStart><Name VALUE="'+ CAPTURE_NAME + '"/><Notes VALUE=""/><Description VALUE=""/><DatabasePath VALUE="'+ FOLDER_PATH + '"/><Delay VALUE="250"/><PacketID VALUE="'+ PacketID + '"/></CaptureStart>\x00';
                    sock.sendto(CAPTURE_START, (UDP_IP, UDP_PORT))
                    PacketID=int(PacketID)
                    
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error_text=error_time + " " + "Tracker recording"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################                          
    def Stop_Recording(self):
    # Triggers Shogun and Tracker to stop - Ouptut = .json document created with take info, take name +1

        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global Shogun_ENF
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        self.Capture_state.setText(_translate("MainWindow", "Saving...", None))
        Timecode_present = 0
        Frames_present = 0
        
        #### updates Actor strings to the correct format ###
        Actor_json=[]
        Act=[["'",str(self.listWidget.item(item).text()),": ",str(self.listWidget_HMC.item(item).text()),", "] for item in range(self.listWidget_HMC.count())]
        print(Act)
        Actor_json=[val for sublist in Act for val in sublist] 
        Actor_json=["{",Actor_json,"}"]      
        Actor_json_combined=[val for sublist in Actor_json for val in sublist]
        Actor_json_combined_new=''.join(map(str,Actor_json_combined))
        print(Actor_json_combined_new)
        Actor_json_Final=Actor_json_combined_new[:-3]+Actor_json_combined_new[-1]
        print(Actor_json_Final)
        try:
           Actor_json_Final_Yes = Actor_json_Final.replace("    Y","'")
           Actor_json_Final_no=Actor_json_Final.replace("    N","'")
        except AttributeError as e:
            e = str(e)
        try:
           Actor_json_Final_Yes_new = Actor_json_Final_Yes.replace("    N","'")
           Actor_json_Final_no_new=Actor_json_Final_no.replace("    Y","'")
           Actor_json_Final=Actor_json_Final_Yes_new
           Actor_json_Final=Actor_json_Final_no_new
        except AttributeError as e:
            e = str(e)
                              
        print(Actor_json_Final)      
        if C_S_connect==1:
            if C_S.connected ==True:
                increment = 1
                controller_S=CaptureServices(C_S)
                controller_S.stop_capture(0)
                time.sleep (.5)
                Shogun_ENF_new= [f for f in listdir(FOLDER_PATH_1_S) if isfile(join(FOLDER_PATH_1_S,f))]
                dup_files = [item for item in Shogun_ENF if item in Shogun_ENF_new]
                for ele in dup_files:
                    Shogun_ENF_new.remove(ele)
                Shogun_ENF_new_2=Shogun_ENF_new[1]
                time.sleep (.5)
                Trial_info=open(FOLDER_PATH_1_S + "\\" + Shogun_ENF_new_2) # figure out take increments
           
                data=Trial_info.readlines()
          
                for line in data:
                    if 'DURATIONTIME=' in line:
                        Total_Frames = line
                        Frames_present = 1
                    if 'STARTTIMECODE=' in line:
                        Timecode=line
                        Timecode_present = 1
                if Frames_present == 1:         
                    Total_Frames_actual=re.findall(r"[+-]?\d*\.\d+|\d+",Total_Frames)
                    Total_Frames_Total=Total_Frames_actual
                    Total_Frames_Total=Total_Frames_Total[0]
                    Total_Frames_Total=str(Total_Frames_Total)
                if Timecode_present == 1:             
                    Timecode_actual=re.findall(r"[+-]?\d*\.\d+|\d+",Timecode)
                    Timecode_start=':'.join(Timecode_actual)    
                    Timecode_start=str(Timecode_start)
                else:
                    Timecode_start="00:00:00:00"
                Trial_info.close()
                
            #### for json file info save ###
                
                Notes=DESCRIPTION
                Tracker_Database = 'C:\\Users\\sm21438\\Documents\\Framestore\\transfer_test\\Track_DB\\' # temporary master db
                Shogun_Database = 'C:\\Users\\sm21438\\Documents\\Framestore\\transfer_test\\Shogun_DB\\' # temporary master db
                date_output=datetime.now()
                date_output=date_output.strftime("%m/%d/%Y, %H:%M:%S")
                date_output_split=date_output.split(',')
                date=date_output_split[0]
                json_file={"A_Take_Name": Trial_Name_S,
                            "Actors": Actor_json_Final, # needs t just be the enabled live actors
                            "Select_Status": "",
                            "Notes": Notes,
                            "Shogun file path:" : Shogun_Database,
                            "Tracker file path:" : Tracker_Database,
                            "Face file path:" : "C:/Program Files/Epic Games",
                            "Date:" : date,
                            "Timecode In:" : Timecode_start,
                            "Timecode Out:" : "00:00:00:00",
                            "Project:" : FOLDER_PATH_1_S
                            }
                
                Vicon_Files_json=self.folder_Description_Box.text()
                Vicon_Files_json=str(Vicon_Files_json)
                Transfer_Path_Orig_json = FOLDER_PATH_1_S
                Transfer_Path_json=Transfer_Path_Orig_json + '\\' + Vicon_Files_json
                with open(Transfer_Path_json+'_'+Trial_Name_S+'.json', 'w') as f:
                    json.dump(json_file,f)
                    
            #### Trial name box update #####
                    
                Trial_Name_S = str(self.Take_Name_Box.text())
                File_Increment=re.search(r'\d+', Trial_Name_S).group(0) # gets the number at end of trial name
                File_Increment=int(File_Increment)        # changes string to integer
                File_Increment2 = File_Increment+increment  #adds integers together
                File_Increment2=str(File_Increment2)
                New_File_Increment2=New_File_Increment + File_Increment2
                self.Take_Name_Box.setText(str(New_File_Increment2))
                Trial_Name_S=New_File_Increment2
                try:
                    self.Take_Name_Box_EXT.setText(_translate("MainWindow", Trial_Name_S, None))
                except AttributeError as e:
                        e = str(e)
        
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Shogun saved"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)

              
                if self.Auto_Transfer_bt.isChecked()==False:
                    Vicon_Files=self.folder_Description_Box.text()
                    Vicon_Files=str(Vicon_Files)
                    Transfer_Path_Orig = FOLDER_PATH_1_S
                    Transfer_Path_shogun=Transfer_Path_Orig + '\\' + Vicon_Files
                    count = 0
                    original_files=[]
                    ################## Shogun #######  ### move files to new folder in local database #######
                    Destination = Transfer_Path_shogun # original shoot database with new file name
                    try:
                        All_Files = [f for f in listdir(Transfer_Path_Orig) if isfile(join(Transfer_Path_Orig,f))]
                        for f in All_Files:
                            if not os.path.exists(os.path.join(Destination,f)):            ### only copies the new files, ignores duplicates
                                shutil.move(Transfer_Path_Orig + '\\' +f, Destination)
                                    #################### updates file widget ###################
                      #  self.S_database.clear()
                        for index in range(len(All_Files)):
                               File_list=All_Files[index]
                               if File_list.endswith(".json"):
                                   self.S_database.addItem(File_list)

                    except WindowsError as e:
                                e = str(e)
                                error_time=datetime.now()
                                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                                error_time=str(error_time)
                                error = error_time +e
                                logging.exception(error)
                                logging.exception("")
                                error_text=error_time + " " + "No local Shogun network path found"
                                self.Log_text()
                                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
                    
        self.Capture_state.setText(_translate("MainWindow", "Ready", None))
        
#######################################################################################################################################################################
        if C_T_connect==1:
            if C_T.connected ==True:
                increment = 1
                PacketID=PacketID+1
                PacketID=str(PacketID)
                CAPTURE_STOP='<?xml version="1.0" encoding="UTF-8" standalone="no" ?><CaptureStop RESULT="SUCCESS"><Name VALUE="'+ CAPTURE_NAME + '"/><DatabasePath VALUE="'+ FOLDER_PATH + '"/><Delay VALUE="0"/><PacketID VALUE="'+ PacketID + '"/></CaptureStop>\x00';
                sock.sendto(CAPTURE_STOP, (UDP_IP, UDP_PORT))
                PacketID=int(PacketID)
                PacketID=PacketID+1
                PacketID=str(PacketID)
                CAPTURE_COMPLETE='<?xml version="1.0" encoding="UTF-8" standalone="no" ?><CaptureComplete><Name VALUE="'+ CAPTURE_NAME + '"/><DatabasePath VALUE="'+ FOLDER_PATH + '"/><Delay VALUE="0"/><PacketID VALUE="'+ PacketID + '"/></CaptureComplete>\x00';
                sock.sendto(CAPTURE_COMPLETE, (UDP_IP, UDP_PORT))
                PacketID=int(PacketID)
                time.sleep (.5)
                
        ########### Creation of .txt info file ############## -needs to be updated

                Trial_info=open(FOLDER_PATH + "\\" + CAPTURE_NAME + ".system")
                data=Trial_info.readlines()
                for line in data:
                    if 'Param name="FramesCaptured"' in line:
                        Total_Frames = line
                        Frames_present = 1
                if Frames_present == 1:         
                    Total_Frames_actual=re.findall(r"[+-]?\d*\.\d+|\d+",Total_Frames)
                    Total_Frames_Total=Total_Frames_actual[0]
                    Trial_info.close()

                Trial_info=open(FOLDER_PATH + "\\" + CAPTURE_NAME + ".xcp")
                data=Trial_info.readlines()
                for line in data:
                    if 'Capture END_TEMP="0" END_TIME=' in line:
                        Timecode = line
                        Timecode_present = 1
                    
                if Timecode_present == 1:             
                    Timecode_actual=re.findall(r"[+-]?\d*\.\d+|\d+",Timecode)
                    Time_code_start=':'.join(Timecode_actual)
                    Time_code_start=str(Time_code_start)


                Trial_info.close()
                Text_File_T = open(FOLDER_PATH + "\\" + CAPTURE_NAME + ".txt","w")
                for i in range (1):
                    Text_File_T.write(CAPTURE_NAME +",   "+Total_Frames_Total+",   "+Time_code_start+"\n")
                for i in range (1):
                    Text_File_T.write("Description:\n")
                for i in range (1):
                    Text_File_T.write("-\n") 
                Text_File_T.close()
                        
                Trial_Name_S = str(self.Take_Name_Box.text())
                File_Increment=re.search(r'\d+', Trial_Name_S).group(0) # gets the number at end of trial name
                File_Increment=int(File_Increment)        # changes string to integer
                File_Increment2 = File_Increment+increment  #adds integers together
                File_Increment2=str(File_Increment2)
                CAPTURE_NAME=New_File_Increment2
                try:
                    self.Take_Name_Box_EXT.setText(_translate("MainWindow", CAPTURE_NAME , None))
                except AttributeError as e:
                        e = str(e)
                
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Tracker saved"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
                if self.Auto_Transfer_bt.isChecked()==False:
                    Vicon_Files=self.folder_Description_Box.text()
                    Vicon_Files=str(Vicon_Files)
                    Transfer_Path_Orig = FOLDER_PATH_1
                    Transfer_Path_track=Transfer_Path_Orig + '\\' + Vicon_Files
                    
                    ################## Tracker ####### ### move files to new folder in local database #######

                    try:
                        if not os.path.exists(Transfer_Path):
                            os.makedirs(Transfer_Path)
                    except OSError:
                        pass
                    Destination = Transfer_Path_track
                    try:
                        
                        All_Files = [f for f in listdir(Transfer_Path_Orig) if isfile(join(Transfer_Path_Orig,f))]        
                        for f in All_Files:
                            if not os.path.exists(os.path.join(Destination,f)):            ### only copies the new files, ignores duplicates
                                shutil.move( Transfer_Path_Orig + '\\' +f, Destination)
                                                #################### updates file widget ###################
                       # self.T_database.clear()
                        for index in range(len(All_Files)):
                            File_list=All_Files[index]
                     
                            if File_list.endswith(".txt"):
                               self.T_database.addItem(File_list)  
                                

                        
                    except WindowsError as e:
                                e = str(e)
                                error_time=datetime.now()
                                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                                error_time=str(error_time)
                                error = error_time +e
                                logging.exception(error)
                                logging.exception("")
                                error_text=error_time + " " + "No Tracker network path found"
                                self.Log_text()
                                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
        if self.Auto_Transfer_bt.isChecked():
           if C_T_connect==1:
               self.Transfer_Files()
           if C_S_connect==1:
               self.Transfer_Files_S()
                
        self.Capture_state.setText(_translate("MainWindow", "Ready", None))
#######################################################################################################################################################################                
    def Cancel_Recording(self):

    # Calls the Shogun cancel function and also sends Tracker commands to cancel = No change in file name
    
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        self.Capture_state.setText(_translate("MainWindow", "Canceling...", None))
        
        if C_S_connect==1:
            if C_S.connected ==True:
                controller_S=CaptureServices(C_S)
                controller_S.cancel_capture(0)

                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Shogun record cancelled"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
        if C_T_connect==1:
            if C_T.connected ==True:
                PacketID=PacketID+1
                PacketID=str(PacketID)
                CAPTURE_CANCEL='<?xml version="1.0" encoding="UTF-8" standalone="no"?><CaptureStop RESULT="CANCEL"><Name VALUE="'+ CAPTURE_NAME + '"/><DatabasePath VALUE="'+ FOLDER_PATH + '"/><Delay VALUE="0"/><PacketID VALUE="'+ PacketID + '"/></CaptureStop>\x00'; 
                sock.sendto(CAPTURE_CANCEL, (UDP_IP, UDP_PORT))
                PacketID=int(PacketID)
                PacketID=PacketID+1
                PacketID=str(PacketID)
                CAPTURE_COMPLETE='<?xml version="1.0" encoding="UTF-8" standalone="no" ?><CaptureComplete><Name VALUE="'+ CAPTURE_NAME + '"/><DatabasePath VALUE="'+ FOLDER_PATH + '"/><Delay VALUE="0"/><PacketID VALUE="'+ PacketID + '"/></CaptureComplete>\x00';
                sock.sendto(CAPTURE_COMPLETE, (UDP_IP, UDP_PORT))
                PacketID=int(PacketID)

                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Tracker record cancelled"
                self.Log_text()
                
        self.Capture_state.setText(_translate("MainWindow", "Ready", None))

#######################################################################################################################################################################
                
    def Import_Actor_func(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        
        if C_S_connect==1:
            ### opens the Actor into the scene
            Actor_lists=SubjectServices(C_S)
            os.chdir(Actor_Cal_Template)
            Actor_name =str(QFileDialog.getOpenFileName())
            Actor_name_Split=Actor_name.split('/')
            Actor_name_Split=Actor_name_Split[-1]
            Actor_name_Split_split=Actor_name_Split.split('.')
            Actor_name_unicode=unicode(Actor_name_Split_split[0],"utf-8")
            Actor_lists.import_subject(Actor_Cal_Template, Actor_name_unicode, Actor_lists.ESubjectType(1) ) #1 = multisegment actor
            Actor_lists_open = Actor_lists.subjects()

            self.listWidget.addItem(Actor_name_Split_split[0] + "    Y")
            self.listWidget_HMC.addItem(HMC)
            
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error_text=error_time + " " + "Actor Imported and enabled"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)

            ### gets list of all actors within the scene #### including clusters
            Actor_lists_live = Actor_lists.subjects()
            Actor_lists_enabled = Actor_lists.enabled_subjects()
            Actor_list_utuple=Actor_lists_live[1]
            Actor_live_utuple=Actor_lists_enabled[1]
            
            Actor_list_tuple=[str(x) for x in Actor_list_utuple]
            Actor_live_tuple=[str(x) for x in Actor_live_utuple]
            
        elif C_S_connect==0:
            e="Error"
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error = error_time +e
            logging.exception(error)
            logging.exception("")
            error_text=error_time + " " + "Shogun connection error"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
        
    def Remove_Actor_func(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        if C_S_connect==1:

            try:
                Selected_Actor=self.listWidget.selectedIndexes()[0]
                Selected_Actor_str=Selected_Actor.data().toString()
                Selected_Actor_str=str(Selected_Actor_str[:-5])
                Actor_lists.remove_subject(Selected_Actor_str)
                
                actor_number=self.listWidget.count()
                actor_item=self.listWidget.currentRow()
                
                for i in range(self.listWidget.count()):
                    if i ==actor_item:
                        item=self.listWidget.takeItem(self.listWidget.currentRow())
                        item=None
                        item_hmc=self.listWidget_HMC.takeItem(actor_item)

                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Actor Removed"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
            except IndexError as e:
                        e = str(e)
                        error_time=datetime.now()
                        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                        error_time=str(error_time)
                        error = error_time + e
                        logging.exception(error)
                        logging.exception("")
                        error_text=error_time + " " + "No actor selected"
                        self.Log_text()
                        self.Logger.moveCursor(QtGui.QTextCursor.End)
            
        if C_S_connect==0:
            e="Error"
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error = error_time +e
            logging.exception(error)
            logging.exception("")
            error_text=error_time + " " + "Shogun connection error"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################        
    def Create_Actor_func(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        New_Actor_Name=self.Subject_Name.text() #temp
        if C_S_connect==1:
            try:
                New_Actor_Name=self.Subject_Name.text()
                New_Actor_Name=unicode(New_Actor_Name,"utf-8")
                new_actors=SubjectCalibrationServices(C_S)            
                Actor_Name=new_actors.set_new_subject_name(New_Actor_Name)
                
                Model_Label_unicode=unicode(Model_Label,"utf-8")
                Model_Solve_unicode=unicode(Model_Solve,"utf-8")
                Model_Skin_unicode=unicode(Model_Skin,"utf-8")

                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Actor created"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
                new_actors.set_subject_labelling_template(Model_Label_unicode)
                new_actors.set_subject_solving_template(Model_Solve_unicode)
                new_actors.set_subject_skin(Model_Skin_unicode)

                
                Result,subject_calibration_session=new_actors.start_subject_calibration("")

                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Calibration started, looking for T-Pose"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)

            except NameError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time + e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No Templates selected"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
        #accept_t_pose
    def Set_Actor_Skin_func (self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        Model_Skin= self.Skin_Dropdown.currentText()
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        error_text=error_time + " " + "Skin template set"
        self.Log_text()
        self.Logger.moveCursor(QtGui.QTextCursor.End)
 #######################################################################################################################################################################       
    def Set_Actor_Solving_func (self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        Model_Solve= self.Solver_Dropdown.currentText()
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        error_text=error_time + " " + "Solver template set"
        self.Log_text()
        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
    def Set_Actor_Labelling_func (self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        Model_Label= self.Label_Dropdown.currentText()
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        error_text=error_time + " " + "Model template set"
        self.Log_text()
        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
    def Set_Actor_Face (self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        actor_number=self.listWidget.count()
        actor_item=self.listWidget.currentRow()
        for item in range(self.listWidget_HMC.count()):
            if item ==actor_item:
                self.listWidget_HMC.takeItem(item)
                self.listWidget_HMC.insertItem(item,str(self.Face_Dropdown.currentText()))
        try:
            Selected_Act_HMC=self.listWidget.selectedIndexes()[0]
            Selected_Act_HMC=Selected_Act_HMC.data().toString()
            Selected_Act_HMC_str=str(Selected_Act_HMC)
        except IndexError as e:
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error_text=error_time + " " + "please Select Actor"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
            
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        try:
            error_text=error_time + " " + Selected_Act_HMC_str +" - HMC=" + str(self.Face_Dropdown.currentText())
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
        except UnboundLocalError as e:
            error_text=error_time + " " +" Error"
            self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################                
    def Stop_Actor_Cal_func (self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        New_Actor_Name=self.Subject_Name.text() # temp
        New_Actor_Name_created=str(New_Actor_Name)
        self.listWidget.addItem(New_Actor_Name_created + "    Y")
        self.listWidget_HMC.addItem(HMC)
        
        if C_S_connect==1:
            try:
                if recal==0:
                    new_actors.stop_subject_calibration(subject_calibration_session)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error_text=error_time + " " + "Calibration complete"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                    
                    New_Actor_Name=self.Subject_Name.text()
                    New_Actor_Name_created=str(New_Actor_Name)
                    self.listWidget.addItem(New_Actor_Name_created + "    Y")
                    self.listWidget_HMC.addItem(HMC)
                    Actor_lists=SubjectServices(C_S)
                     
                elif recal==1:
                    recal_actor.stop_subject_calibration(subject_recalibration_session)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error_text=error_time + " " + "recalibration complete"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                    recal=0
            except NameError as e:
                        e = str(e)
                        error_time=datetime.now()
                        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                        error_time=str(error_time)
                        error = error_time + e
                        logging.exception(error)
                        logging.exception("")
                        error_text=error_time + " " + "No Actor name set"
                        self.Log_text()
                        self.Logger.moveCursor(QtGui.QTextCursor.End)
            except TypeError as e:
                        e = str(e)
                        error_time=datetime.now()
                        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                        error_time=str(error_time)
                        error = error_time + e
                        logging.exception(error)
                        logging.exception("")
                        error_text=error_time + " " + "No calibration started"
                        self.Log_text()
                        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
    def Cancel_Actor_Cal_func(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        if C_S_connect==1:
            try:
                if recal==0:
                    new_actors.cancel_subject_calibration(subject_calibration_session)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error_text=error_time + " " + "Calibration cancelled"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                elif recal==1:
                    recal_actor.cancel_subject_calibration(subject_recalibration_session)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error_text=error_time + " " + "recalibration cancelled"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                    recal=0
                    
                
            except NameError as e:
                        e = str(e)
                        error_time=datetime.now()
                        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                        error_time=str(error_time)
                        error = error_time + e
                        logging.exception(error)
                        logging.exception("")
                        error_text=error_time + " " + "No Actor name set"
                        self.Log_text()
                        self.Logger.moveCursor(QtGui.QTextCursor.End)
                        
            except TypeError as e:
                        e = str(e)
                        error_time=datetime.now()
                        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                        error_time=str(error_time)
                        error = error_time + e
                        logging.exception(error)
                        logging.exception("")
                        error_text=error_time + " " + "No calibration started"
                        self.Log_text()
                        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
    def Actor_reCal_func(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        recal=1

        if C_S_connect==1:
            try:
                Selected_Actor_recal=self.listWidget.selectedIndexes()[0]
                Selected_Actor_recal=Selected_Actor_recal.data().toString()
                Selected_Actor_recal_str=str(Selected_Actor_recal[:-5])
                
                Selected_Actor_recal_unicode=unicode(Selected_Actor_recal_str,"utf-8")
                recal_actor=SubjectCalibrationServices(C_S)
                recal_actor.set_new_subject_name(Selected_Actor_recal_unicode)
                Result,subject_recalibration_session=recal_actor.start_subject_recalibration(Selected_Actor_recal_unicode)
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Actor recalibrating"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
            except IndexError as e:
                e = str(e)
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error = error_time + e
                logging.exception(error)
                logging.exception("")
                error_text=error_time + " " + "No actor selected"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)

#######################################################################################################################################################################
    def TPose_Actor_func(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        
        if C_S_connect==1:
            try:
                if recal==0:
                    new_actors.accept_t_pose(subject_calibration_session)                
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error_text=error_time + " " + "T-pose accepted, undertake RoM"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)

                elif recal==1:
                    recal_actor.accept_t_pose(subject_recalibration_session)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error_text=error_time + " " + "T-pose accepted, undertake RoM"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                 
                
            except NameError as e:
                        e = str(e)
                        error_time=datetime.now()
                        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                        error_time=str(error_time)
                        error = error_time + e
                        logging.exception(error)
                        logging.exception("")
                        error_text=error_time + " " + "No Actor name set"
                        self.Log_text()
                        self.Logger.moveCursor(QtGui.QTextCursor.End)
                        
            except TypeError as e:
                        e = str(e)
                        error_time=datetime.now()
                        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                        error_time=str(error_time)
                        error = error_time + e
                        logging.exception(error)
                        logging.exception("")
                        error_text=error_time + " " + "No calibration started"
                        self.Log_text()
                        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
    def Enable_Actor_func(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor           
                        
        if C_S_connect==1:
            try:
                Selected_Actor=self.listWidget.selectedIndexes()[0]
                Selected_Actor_str=Selected_Actor.data().toString()
                Selected_Actor_str=str(Selected_Actor_str[:-5])
                Actor_name_unicode=unicode(Selected_Actor_str,"utf-8")
                Actor_lists.set_subject_enabled(Actor_name_unicode, 1) # enable
             
                for i in range(self.listWidget.count()):
                    if i ==self.listWidget.currentRow():
                        self.listWidget.takeItem(i)
                        Selected_Actor_No=Selected_Actor_str.split("    N")
                        self.listWidget.insertItem(i,str(Selected_Actor_No[0] + "    Y"))
                        break
                
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + "Actor Enabled"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                

            except IndexError as e:
                e = str(e)
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error = error_time + e
                logging.exception(error)
                logging.exception("")
                error_text=error_time + " " + "No actor selected"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
    def Disable_Actor_func(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        if C_S_connect==1:
            try:
                Selected_Actor=self.listWidget.selectedIndexes()[0]
                Selected_Actor_str=Selected_Actor.data().toString()
                Selected_Actor_str=str(Selected_Actor_str[:-5])
                Actor_name_unicode=unicode(Selected_Actor_str,"utf-8")
                Actor_lists.set_subject_enabled(Actor_name_unicode, 0) # disable
            
                for i in range(self.listWidget.count()):
                    if i ==self.listWidget.currentRow():
                        self.listWidget.takeItem(i)
                        Selected_Actor_No=Selected_Actor_str.split("    Y")
                        self.listWidget.insertItem(i,str(Selected_Actor_No[0] + "    N"))
                        break
                        
                
                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")

                error_time=str(error_time)
                error_text=error_time + " " + "Actor Disabled"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
            except IndexError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time + e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No actor selected"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################                        
    def Transfer_Files(self): 

    # Creates sub folder in Tracker local database based on user input, copies recorded takes, copies and moves to external Database
    
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global Database
        global Database_s
        global Database_t
        global FOLDER_PATH_1_S
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        Vicon_Files=self.folder_Description_Box.text()
        Vicon_Files=str(Vicon_Files)
        Transfer_Path_Orig = FOLDER_PATH_1
        Transfer_Path=Transfer_Path_Orig + '\\' + Vicon_Files

        count = 0
        original_files=[]
        
        ################## Tracker ####### ### move files to new folder in local database #######

        try:
            if not os.path.exists(Transfer_Path):
                os.makedirs(Transfer_Path)
        except OSError:
            pass
        Destination = Transfer_Path
        try:
            
            All_Files = [f for f in listdir(Transfer_Path_Orig) if isfile(join(Transfer_Path_Orig,f))]        
            for f in All_Files:
                if not os.path.exists(os.path.join(Destination,f)):            ### only copies the new files, ignores duplicates
                    shutil.move( Transfer_Path_Orig + '\\' +f, Destination)
                    

            
        except WindowsError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time +e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No Tracker network path found"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
        Database_orig = Tracker_Database
        Database_t=os.path.join(Tracker_Database,Vicon_Files)
            
        ################### Copies files into network database location ###################################
        try:
            try:
                if not os.path.exists(Database_t):
                    os.makedirs(Database_t)
            except OSError:
                pass
        except NameError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time +e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No Tracker network path found"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
        try:    
            All_Files_database = [f for f in listdir(Destination) if isfile(join(Destination,f))]            
            for f in All_Files_database:
                if not os.path.exists(os.path.join(Database_t,f)):            ### only copies the new files, ignores duplicates
                    shutil.copy(Destination + '\\' +f, Database_t)
                    count+=1        
                else:
                        pass
                    
            #################### updates file widget ###################
            self.T_database.clear()
            for index in range(len(All_Files_database)):
                   File_list=All_Files_database[index]
         
                   if File_list.endswith(".txt"):
                       self.T_database.addItem(File_list)           
            count2=str(count)

            if self.Auto_Transfer_bt.isChecked()==False:
                Tk().withdraw()
                tkMessageBox.showinfo('Success', 'Transferred ' + count2 +' Files')

                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + count2 + " " "tracker files transferred"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
            count2=0
        except WindowsError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time +e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No tracker network path found"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                    
#######################################################################################################################################################################
#######################################################################################################################################################################
    def Transfer_Files_S(self): 

        # Creates sub folder in Tracker local database based on user input, copies recorded takes, copies and moves to external Database
    
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        Vicon_Files=self.folder_Description_Box.text()
        Vicon_Files=str(Vicon_Files)
        Transfer_Path_Orig = FOLDER_PATH_1_S
        Transfer_Path=Transfer_Path_Orig + '\\' + Vicon_Files
        count = 0
        original_files=[]
        ################## Shogun #######  ### move files to new folder in local database #######
        try:
            if not os.path.exists(Transfer_Path):
                os.makedirs(Transfer_Path)
        except OSError:
            pass
        Destination = Transfer_Path # original shoot database with new file name
  
        try:
            All_Files = [f for f in listdir(Transfer_Path_Orig) if isfile(join(Transfer_Path_Orig,f))]
            for f in All_Files:
                if not os.path.exists(os.path.join(Destination,f)):            ### only copies the new files, ignores duplicates
                    shutil.move(Transfer_Path_Orig + '\\' +f, Destination)

        except WindowsError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time +e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No local Shogun network path found"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
        Database_orig = Shogun_Database
        Database_s=os.path.join(Shogun_Database,Vicon_Files)
        
        ################### Copies files into network database location ###################################
        try:
            try:
                if not os.path.exists(Database_s):
                    os.makedirs(Database_s)
            except OSError:
                pass
        except NameError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time +e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No master Shogun network path found"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
        try:
            
            All_Files_database = [f for f in listdir(Destination) if isfile(join(Destination,f))]
           
            for f in All_Files_database:

                if not os.path.exists(os.path.join(Database_s,f)):            ### only copies the new files, ignores duplicates
                    shutil.copy(Destination + '\\' +f, Database_s)
                    count+=1        
                else:
                        pass
                    
            #################### updates file widget ###################
            self.S_database.clear()
            for index in range(len(All_Files_database)):
                   File_list=All_Files_database[index]
                   if File_list.endswith(".json"):
                       self.S_database.addItem(File_list)
               
            count2=str(count)

            if self.Auto_Transfer_bt.isChecked()==False:
                Tk().withdraw()
                tkMessageBox.showinfo('Success', 'Transferred ' + count2 +' Files')

                error_time=datetime.now()
                error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                error_time=str(error_time)
                error_text=error_time + " " + count2 + " " "Shogun files transferred"
                self.Log_text()
                self.Logger.moveCursor(QtGui.QTextCursor.End)
                
            count2=0
        except WindowsError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time +e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No Shogun network path found"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
#######################################################################################################################################################################

    def Actor(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        if self.Activate_Actor.isChecked():
            

            self.Import_Subject.setCheckable(False)
            self.Import_Subject.setEnabled(True)
            self.Remove_Subject.setCheckable(False)
            self.Remove_Subject.setEnabled(True)
            self.Create_Subject.setCheckable(False)
            self.Create_Subject.setEnabled(True)
            self.Stop_Actor_Cal.setCheckable(False)
            self.Stop_Actor_Cal.setEnabled(True)
            self.Cancel_Actor_Cal.setCheckable(False)
            self.Cancel_Actor_Cal.setEnabled(True)
            self.TPose.setCheckable(False)
            self.TPose.setEnabled(True)
            self.Disable_Subject.setCheckable(False)
            self.Disable_Subject.setEnabled(True)
            self.Enable_Subject.setCheckable(False)
            self.Enable_Subject.setEnabled(True)
            self.Set_HMC_button.setCheckable(False)
            self.Set_HMC_button.setEnabled(True)
            self.Actor_reCal.setCheckable(False)
            self.Actor_reCal.setEnabled(True)
            
        if self.Activate_Actor.isChecked()==False:
            
            self.Import_Subject.setCheckable(True)
            self.Import_Subject.toggle()
            self.Import_Subject.setEnabled(False)     
            self.Remove_Subject.setCheckable(True)
            self.Remove_Subject.toggle()
            self.Remove_Subject.setEnabled(False)
            self.Create_Subject.setCheckable(True)
            self.Create_Subject.toggle()
            self.Create_Subject.setEnabled(False)
            self.Stop_Actor_Cal.setCheckable(True)
            self.Stop_Actor_Cal.toggle()
            self.Stop_Actor_Cal.setEnabled(False)
            self.Cancel_Actor_Cal.setCheckable(True)
            self.Cancel_Actor_Cal.toggle()
            self.Cancel_Actor_Cal.setEnabled(False)
            self.TPose.setCheckable(True)
            self.TPose.setEnabled(False)
            self.TPose.toggle()
            self.Disable_Subject.setCheckable(True)
            self.Disable_Subject.setEnabled(False)
            self.Disable_Subject.toggle()
            self.Enable_Subject.setCheckable(True)
            self.Enable_Subject.setEnabled(False)
            self.Enable_Subject.toggle()
            self.Set_HMC_button.setCheckable(True)
            self.Set_HMC_button.setEnabled(False)
            self.Set_HMC_button.toggle()
            self.Actor_reCal.setCheckable(True)
            self.Actor_reCal.setEnabled(False)
            self.Actor_reCal.toggle()
#######################################################################################################################################################################            
    def Update_Description(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        DESCRIPTION=self.Take_Description_Box.text()
        DESCRIPTION=str(DESCRIPTION)
        try:
            View_File_tr=self.T_database.selectedIndexes()[0]
            View_File_tr=View_File_tr.data().toString()
            View_File_tr=str(View_File_tr)
            Database_new_t=Database_t+"\\"
            View_File_t=os.path.join(Database_new_t,View_File_tr)
            
            #### for json file info save ###

            with open(View_File_t, 'r+') as f:
                View_file_t=json.load(f)
                try:
                   View_file_t["Notes"]=DESCRIPTION
                   f.seek(0)
                   json.dump(View_file_t,f)
                except KeyError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time + e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No valid JSON file"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                                        
        except IndexError as e:
            e = str(e)
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error = error_time + e
            logging.exception(error)
            logging.exception("")
            error_text=error_time + " " + "No Tracker file selected"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)        
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error_text=error_time + " " + "Tracker description updated"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
                                  
        try:
            View_File_sh=self.S_database.selectedIndexes()[0]
            View_File_sh=View_File_sh.data().toString()
            View_File_sh=str(View_File_sh)
            Database_new_s=Database_s+"\\"
            View_File_s=os.path.join(Database_new_s,View_File_sh)
        
                        #### for json file info save ###

            with open(View_File_s, 'r+') as f:
                View_file_s=json.load(f)
                try:
                   View_file_s["Notes"]=DESCRIPTION
                   f.seek(0)
                   json.dump(View_file_s,f)
                except KeyError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time + e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No valid JSON file"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                    
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error_text=error_time + " " + "Shogun Description updated"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)

            
        except IndexError as e:
            e = str(e)
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error = error_time + e
            logging.exception(error)
            logging.exception("")
            error_text=error_time + " " + "No Shogun file selected"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################            
    def Databases (self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        Shogun_Files = str(QFileDialog.getExistingDirectory())
        Database_s=Shogun_Files
        self.S_database.clear()
        self.S_database.clear()
        all_files_S=os.listdir(Shogun_Files)          
        for index in range(len(all_files_S)):
           File_list_S=all_files_S[index]
           self.S_database.addItem(File_list_S)
           
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        error_text=error_time + " " + "Shogun database opened"
        self.Log_text()
        self.Logger.moveCursor(QtGui.QTextCursor.End)
        
    def T_Databases(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        Tracker_Files = str(QFileDialog.getExistingDirectory())
        Database_t=Tracker_Files
        self.T_database.clear()
        all_files_T=os.listdir(Tracker_Files)          
        for index in range(len(all_files_T)):
           File_list_T=all_files_T[index]
           self.T_database.addItem(File_list_T)
           
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        error_text=error_time + " " + "Tracker database opened"
        self.Log_text()
        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
    def initial_Databases(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        if C_S.connected ==True:
            _result, capture_folder_S = self.capture_service.capture_folder()  #capture_folder_S shogun local DB
            self.Dir_Box.setText(capture_folder_S)
                
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        error_text=error_time + " " + "Database set"
        self.Log_text()
        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
    def Set_discard_func(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        Select = "Burn"

        try:
            Burn_File_tr=self.T_database.selectedIndexes()[0]
            Burn_File_tr=Burn_File_tr.data().toString()
            Burn_File_tr=str(Burn_File_tr)
            json_file_name_tr, ext=Burn_File_tr.split('.')
            Database_new_t=Database_t+"\\"
            Burn_File_t=os.path.join(Database_new_t,Burn_File_tr)
            
            #### for json file info save ###

            with open(Burn_File_t, 'r+') as f:
                burn_file_t=json.load(f)
                try:
                   burn_file_t["Select_Status"]=Select
                   f.seek(0)
                   json.dump(burn_file_t,f)
                except KeyError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time + e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No valid JSON file"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                    
            with open(Burn_File_t, 'rb+') as f:
                    f.seek(0,2)
                    size=f.tell()
                    f.truncate(size-2)
                    
                        
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error_text=error_time + " " + "Tracker file burn indicated"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
            
        except IndexError as e:
            e = str(e)
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error = error_time + e
            logging.exception(error)
            logging.exception("")
            error_text=error_time + " " + "No Tracker file selected"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
            
        try:
            Burn_File_sh=self.S_database.selectedIndexes()[0]
            Burn_File_sh=Burn_File_sh.data().toString()
            Burn_File_sh=str(Burn_File_sh)
            json_file_name_sh, ext=Burn_File_sh.split('.')
            Database_new_s=Database_s+"\\"
            Burn_File_s=os.path.join(Database_new_s,Burn_File_sh)
        
            #### for json file info save ###
            with open(Burn_File_s, 'r+') as f:
                burn_file_s=json.load(f)
                try:
                   burn_file_s["Select_Status"]=Select
                   f.seek(0)
                   json.dump(burn_file_s,f)
                except KeyError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time + e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No valid JSON file"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
            with open(Burn_File_s, 'rb+') as f:
                    f.seek(0,2)
                    size=f.tell()
                    f.truncate(size-2)
        

            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error_text=error_time + " " + "Shogun file burn indicated"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)

            
        except IndexError as e:
            e = str(e)
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error = error_time + e
            logging.exception(error)
            logging.exception("")
            error_text=error_time + " " + "No Shogun file selected"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################        
    def Set_Select_func(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        Select = "Select"

        try:
            Select_File_tr=self.T_database.selectedIndexes()[0]
            Select_File_tr=Select_File_tr.data().toString()
            Select_File_tr=str(Select_File_tr)
            Database_new_t=Database_t+"\\"
            Select_File_t=os.path.join(Database_new_t,Burn_File_tr)
            
            #### for json file info save ###

            with open(Select_File_t, 'r+') as f:
                select_file_t=json.load(f)
                try:
                   select_file_t["Select_Status"]=Select
                   f.seek(0)
                   json.dump(select_file_t,f)
                except KeyError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time + e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No valid JSON file"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)
                                 
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error_text=error_time + " " + "Tracker file select indicated"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
            
        except IndexError as e:
            e = str(e)
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error = error_time + e
            logging.exception(error)
            logging.exception("")
            error_text=error_time + " " + "No Tracker file selected"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
            
        try:
            Select_File_sh=self.S_database.selectedIndexes()[0]
            Select_File_sh=Select_File_sh.data().toString()
            Select_File_sh=str(Select_File_sh)
            Database_new_s=Database_s+"\\"
            Select_File_s=os.path.join(Database_new_s,Select_File_sh)
        
            #### for json file info save ###
            with open(Select_File_s, 'r+') as f:
                select_file_s=json.load(f)
                try:
                   select_file_s["Select_Status"]=Select
                   f.seek(0)
                   json.dump(select_file_s,f)
                except KeyError as e:
                    e = str(e)
                    error_time=datetime.now()
                    error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
                    error_time=str(error_time)
                    error = error_time + e
                    logging.exception(error)
                    logging.exception("")
                    error_text=error_time + " " + "No valid JSON file"
                    self.Log_text()
                    self.Logger.moveCursor(QtGui.QTextCursor.End)

            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error_text=error_time + " " + "Shogun file select indicated"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)

            
        except IndexError as e:
            e = str(e)
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error = error_time + e
            logging.exception(error)
            logging.exception("")
            error_text=error_time + " " + "No Shogun file selected"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################

    def External_control(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        if self.External_trig.isChecked()==False:
            self.EXT_Window.close()
            self.Record_Button_Start.setCheckable(False)
            self.Record_Button_Start.setEnabled(True)
            self.Record_Button_Stop.setCheckable(False)
            self.Record_Button_Stop.setEnabled(True)
            self.Cancel_Record_Bt.setCheckable(False)
            self.Cancel_Record_Bt.setEnabled(True)
            external_active=0
        elif self.External_trig.isChecked()==True:
            external_active=1

            
            self.EXT_Window = QtGui.QMainWindow()
            self.EXT_Window.setObjectName(_fromUtf8("propWindow"))
            self.EXT_Window.resize(370,250)
            self.EXT_Window.setStyleSheet(_fromUtf8("background-color: rgb(36, 36, 36);\n"
        "color: rgb(255, 255, 255);"))
            self.EXT_Window.setWindowIcon(QtGui.QIcon('TheKraken.png'))
            self.EXT_Window.setWindowTitle("External Control")
            self.centralwidget_E = QtGui.QWidget(self.EXT_Window)
            self.centralwidget_E.setObjectName(_fromUtf8("controlwidge"))
            self.centralwidget_E.setGeometry(QtCore.QRect(0,0,370,250))
############################################################################################ - close button
            self.EXT_close = QtGui.QPushButton(self.centralwidget_E)
            self.EXT_close.setGeometry(QtCore.QRect(270, 220, 81, 21))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Arial"))
            self.EXT_close.setFont(font)
            self.EXT_close.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
    "background-color: rgb(0, 100, 130);"))
            self.EXT_close.setObjectName(_fromUtf8("Create_Subject"))
            self.EXT_close.clicked.connect(self.EXT_close_func)      
    ####################################################################################### Record start button
            self.Record_Button_Start_EXT = QtGui.QPushButton(self.centralwidget_E)
            self.Record_Button_Start_EXT.setGeometry(QtCore.QRect(80, 90, 211, 31))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Arial"))
            font.setPointSize(8)
            self.Record_Button_Start_EXT.setFont(font)
            self.Record_Button_Start_EXT.setStyleSheet(_fromUtf8("background-color: rgb(0, 120, 0);\n"
    "color: rgb(255,255, 255);"))
            self.Record_Button_Start_EXT.setFlat(False)
            self.Record_Button_Start_EXT.setObjectName(_fromUtf8("Record_Button_Start"))
            self.Record_Button_Start_EXT.clicked.connect(self.Start_Recording)
    ####################################################################################### - Record stop button
            self.Record_Button_Stop_EXT = QtGui.QPushButton(self.centralwidget_E)
            self.Record_Button_Stop_EXT.setGeometry(QtCore.QRect(140, 130, 101, 41))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Arial"))
            font.setPointSize(8)
            self.Record_Button_Stop_EXT.setFont(font)
            self.Record_Button_Stop_EXT.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
    "background-color: rgb(120, 0, 0);"))
            self.Record_Button_Stop_EXT.setObjectName(_fromUtf8("Record_Button_Stop"))
            self.Record_Button_Stop_EXT.clicked.connect(self.Stop_Recording)
    ####################################################################################### -Cancel record button
            self.Cancel_Record_Bt_EXT = QtGui.QPushButton(self.centralwidget_E)
            self.Cancel_Record_Bt_EXT.setGeometry(QtCore.QRect(150, 180, 81, 21))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Arial"))
            self.Cancel_Record_Bt_EXT.setFont(font)
            self.Cancel_Record_Bt_EXT.setStyleSheet(_fromUtf8("background-color: rgb(0, 100, 130);\n"
    "color: rgb(255, 255,255);"))
            self.Cancel_Record_Bt_EXT.setObjectName(_fromUtf8("Cancel_Record_Bt"))
            self.Cancel_Record_Bt_EXT.clicked.connect(self.Cancel_Recording)            
    ####################################################################################### - take name box
            self.Take_Name_Box_EXT = QtGui.QLabel(self.centralwidget_E)
            self.Take_Name_Box_EXT.setGeometry(QtCore.QRect(90, 50, 231, 20))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Arial"))
            font.setPointSize(10)
            font.setBold(False)
            font.setItalic(True)
            font.setUnderline(False)
            font.setWeight(50)
            
            self.Take_Name_Box_EXT.setFont(font)
            self.Take_Name_Box_EXT.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
            self.Take_Name_Box_EXT.setObjectName(_fromUtf8("Take_Name_Box"))
    ####################################################################################### Set take name button
            self.Set_Take_Name_Button_EXT = QtGui.QLabel(self.centralwidget_E)
            self.Set_Take_Name_Button_EXT.setGeometry(QtCore.QRect(10, 50, 81, 21))
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Arial"))
            font.setPointSize(10)
            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(True)
            font.setWeight(50)
            
            self.Set_Take_Name_Button_EXT.setFont(font)
            self.Set_Take_Name_Button_EXT.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
            self.Set_Take_Name_Button_EXT.setObjectName(_fromUtf8("Take_Name_Box"))
            
            self.EXT_close.setText(_translate("MainWindow", "Close", None))
            self.Record_Button_Start_EXT.setText(_translate("MainWindow", "Start Recording", None))
            self.Record_Button_Stop_EXT.setText(_translate("MainWindow", "Stop Recording", None))
            self.Cancel_Record_Bt_EXT.setText(_translate("MainWindow", "Cancel", None))
            self.Set_Take_Name_Button_EXT.setText(_translate("MainWindow", "Take Name:", None))
         
            
            self.EXT_Window.show()

            self.Record_Button_Start.setCheckable(True)
            self.Record_Button_Start.toggle()
            self.Record_Button_Start.setEnabled(False)
            self.Record_Button_Stop.setCheckable(True)
            self.Record_Button_Stop.toggle()
            self.Record_Button_Stop.setEnabled(False)
            self.Cancel_Record_Bt.setCheckable(True)
            self.Cancel_Record_Bt.toggle()
            self.Cancel_Record_Bt.setEnabled(False)            
#######################################################################################################################################################################        
    def EXT_close_func(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        self.EXT_Window.close()
        self.Record_Button_Start.setCheckable(False)
        self.Record_Button_Start.setEnabled(True)
        self.Record_Button_Stop.setCheckable(False)
        self.Record_Button_Stop.setEnabled(True)
        self.Cancel_Record_Bt.setCheckable(False)
        self.Cancel_Record_Bt.setEnabled(True)
        self.External_trig.setChecked(False)
        
#######################################################################################################################################################################        
    def About_Hub(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        Tk().withdraw()
        tkMessageBox.showinfo('About', 'fARsight Hub Version 1.0')
#######################################################################################################################################################################        
    def Log_text(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        self.Logger.insertPlainText(error_text + '\n')
#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################
    def properties_window(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        
        self.Window = QtGui.QMainWindow()
        self.Window.setObjectName(_fromUtf8("propWindow"))
        self.Window.resize(500, 200)
        self.Window.setStyleSheet(_fromUtf8("background-color: rgb(36, 36, 36);\n"
    "color: rgb(255, 255, 255);"))
        self.Window.setWindowIcon(QtGui.QIcon('TheKraken.png'))
        self.Window.setWindowTitle("Master Database Location")
        self.centralwidget_P = QtGui.QWidget(self.Window)
        self.centralwidget_P.setObjectName(_fromUtf8("PropWidg"))
        self.centralwidget_P.setGeometry(QtCore.QRect(0,0,500,200))
        ####################################################################################### - OK button
        self.Prop_OK = QtGui.QPushButton(self.centralwidget_P)
        self.Prop_OK.setGeometry(QtCore.QRect(270, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Prop_OK.setFont(font)
        self.Prop_OK.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Prop_OK.setObjectName(_fromUtf8("Create_Subject"))
        self.Prop_OK.clicked.connect(self.Prop_OK_var)
        ####################################################################################### - cancel button
        self.Prop_cancel = QtGui.QPushButton(self.centralwidget_P)
        self.Prop_cancel.setGeometry(QtCore.QRect(390, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Prop_cancel.setFont(font)
        self.Prop_cancel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Prop_cancel.setObjectName(_fromUtf8("Create_Subject"))
        self.Prop_cancel.clicked.connect(self.Prop_OK_var)
        ####################################################################################### - Shogun master DB_textbox
        self.S_master_Database = QtGui.QLineEdit(self.centralwidget_P)
        self.S_master_Database.setGeometry(QtCore.QRect(10, 50, 400, 20))
        self.S_master_Database.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.S_master_Database.setText(_fromUtf8(""))
        self.S_master_Database.setObjectName(_fromUtf8("S_master_Database"))
        self.S_master_Database.setText(Shogun_Database)
        ####################################################################################### - Tracker master DB_textbox
        self.T_master_Database = QtGui.QLineEdit(self.centralwidget_P)
        self.T_master_Database.setGeometry(QtCore.QRect(10, 110, 400, 20))
        self.T_master_Database.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.T_master_Database.setText(_fromUtf8(""))
        self.T_master_Database.setObjectName(_fromUtf8("T_master_Database"))
        self.T_master_Database.setText(Tracker_Database)
        ####################################################################################### - Set Shogun master database button
        self.Shogun_DB_browse = QtGui.QPushButton(self.centralwidget_P)
        self.Shogun_DB_browse.setGeometry(QtCore.QRect(420, 50, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Shogun_DB_browse.setFont(font)
        self.Shogun_DB_browse.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Shogun_DB_browse.setObjectName(_fromUtf8("Shogun_DB_browse"))
        self.Shogun_DB_browse.clicked.connect(self.Master_S_Databases)
        ####################################################################################### - Set Tracker master database button
        self.Tracker_DB_browse = QtGui.QPushButton(self.centralwidget_P)
        self.Tracker_DB_browse.setGeometry(QtCore.QRect(420, 110, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Tracker_DB_browse.setFont(font)
        self.Tracker_DB_browse.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Tracker_DB_browse.setObjectName(_fromUtf8("Activate_Actor"))
        self.Tracker_DB_browse.clicked.connect(self.Master_T_Databases)

        self.Master_Database_transfer = QtGui.QLabel(self.centralwidget_P)
        self.Master_Database_transfer.setGeometry(QtCore.QRect(100, 10, 300, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.Master_Database_transfer.setFont(font)
        self.Master_Database_transfer.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Master_Database_transfer.setObjectName(_fromUtf8("Database_transfer"))

                
        self.Prop_OK.setText(_translate("MainWindow", "OK", None))
        self.Prop_cancel.setText(_translate("MainWindow", "Cancel", None))
        self.Shogun_DB_browse.setText(_translate("MainWindow", "Browse", None))
        self.Tracker_DB_browse.setText(_translate("MainWindow", "Browse", None))
        self.Master_Database_transfer.setText(_translate("MainWindow", "Master Database Location", None))
        
        self.Window.show()
#######################################################################################################################################################################
    def Prop_OK_var(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        self.Window.close()
#######################################################################################################################################################################
    def Master_S_Databases (self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        Shogun_Database = str(QFileDialog.getExistingDirectory())
        self.S_master_Database.setText(Shogun_Database)
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        error_text=error_time + " " + "Shogun master database location set"
        self.Log_text()
        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################        
    def Master_T_Databases (self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        Tracker_Database = str(QFileDialog.getExistingDirectory())
        self.T_master_Database.setText(Tracker_Database)
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        error_text=error_time + " " + "Tracker master database location set"
        self.Log_text()
        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################

    def Actor_properties_window(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        self.Window_Actor = QtGui.QMainWindow()
        self.Window_Actor.setObjectName(_fromUtf8("propWindow"))
        self.Window_Actor.resize(500, 200)
        self.Window_Actor.setStyleSheet(_fromUtf8("background-color: rgb(36, 36, 36);\n"
    "color: rgb(255, 255, 255);"))
        self.Window_Actor.setWindowIcon(QtGui.QIcon('TheKraken.png'))
        self.Window_Actor.setWindowTitle("Actor Properties Location")
        self.centralwidget_A = QtGui.QWidget(self.Window_Actor)
        self.centralwidget_A.setObjectName(_fromUtf8("PropWidg"))
        self.centralwidget_A.setGeometry(QtCore.QRect(0,0,500,200))
        ####################################################################################### - OK button
        self.Act_OK = QtGui.QPushButton(self.centralwidget_A)
        self.Act_OK.setGeometry(QtCore.QRect(270, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Act_OK.setFont(font)
        self.Act_OK.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Act_OK.setObjectName(_fromUtf8("Create_Subject"))
        self.Act_OK.clicked.connect(self.Act_OK_var)
        ####################################################################################### - cancel button
        self.Act_cancel = QtGui.QPushButton(self.centralwidget_A)
        self.Act_cancel.setGeometry(QtCore.QRect(390, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Act_cancel.setFont(font)
        self.Act_cancel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Act_cancel.setObjectName(_fromUtf8("Create_Subject"))
        self.Act_cancel.clicked.connect(self.Act_OK_var)
        ####################################################################################### - Actor location textbox
        self.Actor_Location = QtGui.QLineEdit(self.centralwidget_A)
        self.Actor_Location.setGeometry(QtCore.QRect(10, 50, 400, 20))
        self.Actor_Location.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Actor_Location.setText(_fromUtf8(""))
        self.Actor_Location.setObjectName(_fromUtf8("Actor_Template_Database"))
        self.Actor_Location.setText(Actor_Cal_Template)
        ####################################################################################### - Actor Templates textbox
        self.Actor_Template_Database = QtGui.QLineEdit(self.centralwidget_A)
        self.Actor_Template_Database.setGeometry(QtCore.QRect(10, 80, 400, 20))
        self.Actor_Template_Database.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Actor_Template_Database.setText(_fromUtf8(""))
        self.Actor_Template_Database.setObjectName(_fromUtf8("Actor_Template_Database"))
        self.Actor_Template_Database.setText(Actor_model_Template)
        ####################################################################################### - Skin textbox
        self.Actor_Skin_Database = QtGui.QLineEdit(self.centralwidget_A)
        self.Actor_Skin_Database.setGeometry(QtCore.QRect(10, 110, 400, 20))
        self.Actor_Skin_Database.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.Actor_Skin_Database.setText(_fromUtf8(""))
        self.Actor_Skin_Database.setObjectName(_fromUtf8("T_master_Database"))
        self.Actor_Skin_Database.setText(Actor_Skin_Template)
        ####################################################################################### - Set Actor location button
        self.Actor_Location_browse = QtGui.QPushButton(self.centralwidget_A)
        self.Actor_Location_browse.setGeometry(QtCore.QRect(420, 50, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Actor_Location_browse.setFont(font)
        self.Actor_Location_browse.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Actor_Location_browse.setObjectName(_fromUtf8("Shogun_DB_browse"))
        self.Actor_Location_browse.clicked.connect(self.Actor_Location_DB)
        ####################################################################################### - Set Actor templates database button
        self.Actor_Template_browse = QtGui.QPushButton(self.centralwidget_A)
        self.Actor_Template_browse.setGeometry(QtCore.QRect(420, 80, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Actor_Template_browse.setFont(font)
        self.Actor_Template_browse.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Actor_Template_browse.setObjectName(_fromUtf8("Shogun_DB_browse"))
        self.Actor_Template_browse.clicked.connect(self.Actor_Template_DB)
        ####################################################################################### - Set Skin database button
        self.Actor_Skin_browse = QtGui.QPushButton(self.centralwidget_A)
        self.Actor_Skin_browse.setGeometry(QtCore.QRect(420, 110, 70, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Actor_Skin_browse.setFont(font)
        self.Actor_Skin_browse.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 100, 130);"))
        self.Actor_Skin_browse.setObjectName(_fromUtf8("Activate_Actor"))
        self.Actor_Skin_browse.clicked.connect(self.Actor_Skin_DB)

        self.Actor_Management = QtGui.QLabel(self.centralwidget_A)
        self.Actor_Management.setGeometry(QtCore.QRect(100, 10, 300, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.Actor_Management.setFont(font)
        self.Actor_Management.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Actor_Management.setObjectName(_fromUtf8("Actor Management"))

                
        self.Act_OK.setText(_translate("MainWindow", "OK", None))
        self.Act_cancel.setText(_translate("MainWindow", "Cancel", None))
        
        self.Actor_Template_browse.setText(_translate("MainWindow", "Template", None))
        self.Actor_Skin_browse.setText(_translate("MainWindow", "Skin", None))
        self.Actor_Location_browse.setText(_translate("MainWindow", "Actor", None))
        self.Actor_Management.setText(_translate("MainWindow", "Actor Master Location", None))
        
        self.Window_Actor.show()
#######################################################################################################################################################################

    def Act_OK_var(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        self.Window_Actor.close()
#######################################################################################################################################################################

    def Actor_Template_DB (self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        Actor_model_Template = str(QFileDialog.getExistingDirectory())
        self.Actor_Template_Database.setText(Actor_Cal_Template)
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        error_text=error_time + " " + "Actor template location set"
        self.Log_text()
        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
        
    def Actor_Skin_DB (self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        Actor_Skin_Template = str(QFileDialog.getExistingDirectory())
        self.Actor_Skin_Database.setText(Actor_Skin_Template)
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        error_text=error_time + " " + "Actor skin location set"
        self.Log_text()
        self.Logger.moveCursor(QtGui.QTextCursor.End)        
#######################################################################################################################################################################       
    def Actor_Location_DB (self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor

        Actor_Cal_Template = str(QFileDialog.getExistingDirectory())
        self.Actor_Location.setText(Actor_Cal_Template)
        error_time=datetime.now()
        error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
        error_time=str(error_time)
        error_text=error_time + " " + "Actor save location set"
        self.Log_text()
        self.Logger.moveCursor(QtGui.QTextCursor.End)
#######################################################################################################################################################################
#######################################################################################################################################################################
#######################################################################################################################################################################
      
    def Kraken(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        MainWindow.close()
        MainWindow.destroy()
        os.popen("fARsight_home")
        
#######################################################################################################################################################################
    def Help_PDF(self):
        global C_T
        global C_S
        global C_S_connect
        global C_T_connect
        global increment
        global Trial_Name_S
        global New_File_Increment
        global CAPTURE_NAME
        global FOLDER_PATH
        global PacketID
        global sock
        global UDP_IP
        global UDP_PORT
        global FOLDER_PATH_1
        global Tracker_Database
        global Shogun_Database
        global FOLDER_PATH_1_S
        global Database
        global Database_s
        global Database_t
        global error_text
        global Actor_Cal_Template
        global Actor_Skin_Template
        global Actor_model_Template
        global Actor_lists
        global Actor_name_Split_split
        global Model_Label
        global Model_Solve
        global Model_Skin
        global new_actors
        global subject_calibration_session
        global new_actors
        global subject_calibration_session
        global DESCRIPTION
        global Select
        global external_active
        global HMC
        global subject_recalibration_session
        global recal
        global date_output_log
        global Error_Logs
        global recal_actor
        
        try:
            os.startfile ("fARsight_userguide.PDF")
        except WindowsError as e:
            e = str(e)
            error_time=datetime.now()
            error_time=error_time.strftime("%m/%d/%Y, %H:%M:%S")
            error_time=str(error_time)
            error = error_time + e
            logging.exception(error)
            logging.exception("")
            error_text=error_time + " " + "No help file found"
            self.Log_text()
            self.Logger.moveCursor(QtGui.QTextCursor.End)
            
    def activate_autotransfer(self):
            global checked

            if checked==0:
                self.Auto_Transfer_bt.setCheckable(True)        
                self.Auto_Transfer_bt.setEnabled(True)
                self.autotransfer.setText(_translate("MainWindow", "Disable Auto transfer", None))
                checked=1
            elif checked==1:
                self.Auto_Transfer_bt.setCheckable(False)
                self.Auto_Transfer_bt.toggle()
                self.Auto_Transfer_bt.setEnabled(False)
                self.autotransfer.setText(_translate("MainWindow", "Enable Auto transfer", None))
                checked=0

    def actionfARsight_func(self):
        MainWindow.close()
        MainWindow.destroy()
        os.popen("fARsight_Hub_Light")
                    
    def Close(self):
        global date_output_log
        global Error_Logs
        global Start_directory
        MainWindow.close()
        MainWindow.destroy()
        os.system("taskkill /f /im  python.exe")
        logging.shutdown()
       
        shutil.move(Start_directory+ '\\' +''+date_output_log+'_Hub_Error_log.log',Start_directory+ '\\'+'Error_Logs') ##change to specific location
            
if __name__ == "__main__":
    import sys
    global t1
    global t2
    global Start_directory
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



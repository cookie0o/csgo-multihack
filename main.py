#imports
import webbrowser,time,keyboard,numpy as np,pymem,pymem.process
from PyQt5 import QtCore,QtGui,QtWidgets
from threading import Thread

#import offsets
from offsets import *

#github link and version
github_url='https://github.com/cookie_o'
CURRENT_VERSION='1._'



def main(self):

    try:
        pm=pymem.Pymem("csgo.exe")
        client=pymem.process.module_from_name(pm.process_handle,'client.dll').lpBaseOfDll
        engine=pymem.process.module_from_name(pm.process_handle,'engine.dll').lpBaseOfDll
        enginepointer=pm.read_int(engine+dwClientState)
    except pymem.exception.ProcessNotFound:
        pass


    while True:
  
      time.sleep(0.01)
      BUNNYHOP_on_off=0
      if self.BUNNYHOP_ON_checkbox.isChecked():
        BUNNYHOP_on_off=1

      if BUNNYHOP_on_off==1:
        try:
        
          if pm.read_int(client+dwLocalPlayer):
            player=pm.read_int(client+dwLocalPlayer)
            force_jump=client+dwForceJump
            on_ground=pm.read_int(player+m_fFlags)
            velocity=pm.read_float(player+m_vecVelocity)

            if keyboard.is_pressed('space')and on_ground==257:

              if velocity<1 and velocity>-1:
                pass
              else:
                pm.write_int(force_jump,5)
                time.sleep(0.17)
                pm.write_int(force_jump,4)

        except:
          pass

      else:
        pass


      NO_FLASH_on_off =0
      if self.NO_FLASH_ON_checkbox.isChecked():
        NO_FLASH_on_off=1
      if NO_FLASH_on_off==1:
        player=pm.read_int(client+dwLocalPlayer)
        if player:
          flash_value=player+m_flFlashMaxAlpha
          if flash_value:
              pm.write_float(flash_value,float(0))

      else:
        pass

      RADAR_on_off=0
      if self.RADAR_ESP_ON_checkbox.isChecked():
        RADAR_on_off=1
      if RADAR_on_off==1:
        for i in range(1,32):
          entity=pm.read_int(client+dwEntityList+i*16)
          if entity:
              pm.write_uchar(entity+m_bSpotted,1)


      else:
        pass


      #T
      T_RED_VALUE_=self.T_RED_VALUE.text()
      T_GREEN_VALUE_=self.T_GREEN_VALUE.text()
      T_BLUE_VALUE_=self.T_BLUE_VALUE.text()

      #CT
      CT_RED_VALUE_=self.CT_RED_VALUE.text()
      CT_GREEN_VALUE_=self.CT_GREEN_VALUE.text()
      CT_BLUE_VALUE_=self.CT_BLUE_VALUE.text()


      T_R=T_RED_VALUE_.replace('',"0")
      T_G=T_GREEN_VALUE_.replace('',"0")
      T_B=T_BLUE_VALUE_.replace('',"0")
      CT_R=CT_RED_VALUE_.replace('',"0")
      CT_G=CT_GREEN_VALUE_.replace('',"0")
      CT_B=CT_BLUE_VALUE_.replace('',"0")


      ESP_ct_on_off=0
      ESP_t_on_off=0

      if self.CT_GLOW_ON_checkbox.isChecked():
        ESP_ct_on_off=1
      if self.T_GLOW_ON_checkbox.isChecked():
        ESP_t_on_off=1

      glow_manager=pm.read_int(client+dwGlowObjectManager)
      for i in range(1,32):
        
        entity=pm.read_int(client+dwEntityList+i*16)
        if entity:
            
          entity_team_id=pm.read_int(entity+m_iTeamNum)
          entity_glow=pm.read_int(entity+m_iGlowIndex)


          if ESP_t_on_off==1:    
            if entity_team_id==2:
              pm.write_float(glow_manager+entity_glow*56+8,float(T_R))
              pm.write_float(glow_manager+entity_glow*56+12,float(T_G))
              pm.write_float(glow_manager+entity_glow*56+16,float(T_B))
              pm.write_float(glow_manager+entity_glow*56+20,float(1))
              pm.write_int(glow_manager+entity_glow*56+40,ESP_t_on_off)

            if ESP_ct_on_off==1:
              if entity_team_id==3:
                    pm.write_float(glow_manager+entity_glow*56+8,float(CT_R))
                    pm.write_float(glow_manager+entity_glow*56+12,float(CT_G))
                    pm.write_float(glow_manager+entity_glow*56+16,float(CT_B))
                    pm.write_float(glow_manager+entity_glow*56+20,float(1))
                    pm.write_int(glow_manager+entity_glow*56+40,ESP_ct_on_off)



def main_start(self):
    try:
      pymem.Pymem("csgo.exe")
    except pymem.exception.ProcessNotFound:
      print('Launch Game')

    Thread(target=main(self)).start()


#MAIN UI
class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(535, 270)
        main_window.setMinimumSize(QtCore.QSize(535, 270))
        main_window.setMaximumSize(QtCore.QSize(535, 270))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setStyleSheet("background-color: rgb(83, 83, 83);")
        self.tabWidget = QtWidgets.QTabWidget(main_window)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 541, 271))
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = QtWidgets.QWidget()
        self.home_tab.setObjectName("home_tab")
        self.title = QtWidgets.QLabel(self.home_tab)
        self.title.setGeometry(QtCore.QRect(0, 0, 531, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.version = QtWidgets.QLabel(self.home_tab)
        self.version.setGeometry(QtCore.QRect(490, 60, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.version.setFont(font)
        self.version.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.version.setObjectName("version")
        self.github_link_button = QtWidgets.QPushButton(self.home_tab)
        self.github_link_button.setGeometry(QtCore.QRect(330, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.github_link_button.setFont(font)
        self.github_link_button.setStyleSheet("color: rgb(0, 165, 165);")
        self.github_link_button.setFlat(True)
        self.github_link_button.setObjectName("github_link_button")
        self.label = QtWidgets.QLabel(self.home_tab)
        self.label.setGeometry(QtCore.QRect(0, 90, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.home_tab)
        self.frame.setGeometry(QtCore.QRect(-20, 130, 581, 151))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.inject_notice = QtWidgets.QLabel(self.frame)
        self.inject_notice.setGeometry(QtCore.QRect(20, 10, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.inject_notice.setFont(font)
        self.inject_notice.setStyleSheet("color: rgb(255, 85, 255);")
        self.inject_notice.setLineWidth(2)
        self.inject_notice.setAlignment(QtCore.Qt.AlignCenter)
        self.inject_notice.setObjectName("inject_notice")
        self.inject_button = QtWidgets.QPushButton(self.frame)
        self.inject_button.setGeometry(QtCore.QRect(140, 50, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.inject_button.setFont(font)
        self.inject_button.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.inject_button.setObjectName("inject_button")
        self.tabWidget.addTab(self.home_tab, "")
        self.esp_tab = QtWidgets.QWidget()
        self.esp_tab.setObjectName("esp_tab")
        self.CT_box = QtWidgets.QGroupBox(self.esp_tab)
        self.CT_box.setGeometry(QtCore.QRect(0, 10, 261, 231))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.CT_box.setFont(font)
        self.CT_box.setStyleSheet("color: rgb(0, 255, 255);")
        self.CT_box.setObjectName("CT_box")
        self.CT_GLOW_ON_checkbox = QtWidgets.QCheckBox(self.CT_box)
        self.CT_GLOW_ON_checkbox.setGeometry(QtCore.QRect(180, 10, 71, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.CT_GLOW_ON_checkbox.setFont(font)
        self.CT_GLOW_ON_checkbox.setChecked(True)
        self.CT_GLOW_ON_checkbox.setObjectName("CT_GLOW_ON_checkbox")
        self.ct_red_value_text = QtWidgets.QLabel(self.CT_box)
        self.ct_red_value_text.setGeometry(QtCore.QRect(10, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ct_red_value_text.setFont(font)
        self.ct_red_value_text.setStyleSheet("color: rgb(255, 0, 0);")
        self.ct_red_value_text.setObjectName("ct_red_value_text")
        self.ct_blue_value_text = QtWidgets.QLabel(self.CT_box)
        self.ct_blue_value_text.setGeometry(QtCore.QRect(10, 150, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ct_blue_value_text.setFont(font)
        self.ct_blue_value_text.setStyleSheet("color: rgb(0, 0, 255);")
        self.ct_blue_value_text.setObjectName("ct_blue_value_text")
        self.ct_green_value_text = QtWidgets.QLabel(self.CT_box)
        self.ct_green_value_text.setGeometry(QtCore.QRect(10, 120, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.ct_green_value_text.setFont(font)
        self.ct_green_value_text.setStyleSheet("color: rgb(0, 255, 0);")
        self.ct_green_value_text.setObjectName("ct_green_value_text")
        self.CT_RED_VALUE = QtWidgets.QLineEdit(self.CT_box)
        self.CT_RED_VALUE.setGeometry(QtCore.QRect(150, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.CT_RED_VALUE.setFont(font)
        self.CT_RED_VALUE.setMaxLength(3)
        self.CT_RED_VALUE.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_RED_VALUE.setObjectName("CT_RED_VALUE")
        self.CT_GREEN_VALUE = QtWidgets.QLineEdit(self.CT_box)
        self.CT_GREEN_VALUE.setGeometry(QtCore.QRect(150, 120, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.CT_GREEN_VALUE.setFont(font)
        self.CT_GREEN_VALUE.setMaxLength(3)
        self.CT_GREEN_VALUE.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_GREEN_VALUE.setObjectName("CT_GREEN_VALUE")
        self.CT_BLUE_VALUE = QtWidgets.QLineEdit(self.CT_box)
        self.CT_BLUE_VALUE.setGeometry(QtCore.QRect(150, 160, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.CT_BLUE_VALUE.setFont(font)
        self.CT_BLUE_VALUE.setMaxLength(3)
        self.CT_BLUE_VALUE.setAlignment(QtCore.Qt.AlignCenter)
        self.CT_BLUE_VALUE.setObjectName("CT_BLUE_VALUE")
        self.ct_color_value_text = QtWidgets.QLabel(self.CT_box)
        self.ct_color_value_text.setGeometry(QtCore.QRect(10, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.ct_color_value_text.setFont(font)
        self.ct_color_value_text.setStyleSheet("color: rgb(255, 85, 0);")
        self.ct_color_value_text.setAlignment(QtCore.Qt.AlignCenter)
        self.ct_color_value_text.setObjectName("ct_color_value_text")
        self.T_box = QtWidgets.QGroupBox(self.esp_tab)
        self.T_box.setGeometry(QtCore.QRect(270, 10, 261, 231))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.T_box.setFont(font)
        self.T_box.setStyleSheet("color: rgb(0, 255, 255);")
        self.T_box.setObjectName("T_box")
        self.T_GLOW_ON_checkbox = QtWidgets.QCheckBox(self.T_box)
        self.T_GLOW_ON_checkbox.setGeometry(QtCore.QRect(180, 10, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.T_GLOW_ON_checkbox.setFont(font)
        self.T_GLOW_ON_checkbox.setChecked(True)
        self.T_GLOW_ON_checkbox.setTristate(False)
        self.T_GLOW_ON_checkbox.setObjectName("T_GLOW_ON_checkbox")
        self.t_red_value_text = QtWidgets.QLabel(self.T_box)
        self.t_red_value_text.setGeometry(QtCore.QRect(10, 80, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.t_red_value_text.setFont(font)
        self.t_red_value_text.setStyleSheet("color: rgb(255, 0, 0);")
        self.t_red_value_text.setObjectName("t_red_value_text")
        self.t_green_value_text = QtWidgets.QLabel(self.T_box)
        self.t_green_value_text.setGeometry(QtCore.QRect(10, 120, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.t_green_value_text.setFont(font)
        self.t_green_value_text.setStyleSheet("color: rgb(0, 255, 0);")
        self.t_green_value_text.setObjectName("t_green_value_text")
        self.t_blue_value_text = QtWidgets.QLabel(self.T_box)
        self.t_blue_value_text.setGeometry(QtCore.QRect(10, 150, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.t_blue_value_text.setFont(font)
        self.t_blue_value_text.setStyleSheet("color: rgb(0, 0, 255);")
        self.t_blue_value_text.setObjectName("t_blue_value_text")
        self.T_RED_VALUE = QtWidgets.QLineEdit(self.T_box)
        self.T_RED_VALUE.setGeometry(QtCore.QRect(150, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.T_RED_VALUE.setFont(font)
        self.T_RED_VALUE.setMaxLength(3)
        self.T_RED_VALUE.setAlignment(QtCore.Qt.AlignCenter)
        self.T_RED_VALUE.setObjectName("T_RED_VALUE")
        self.T_GREEN_VALUE = QtWidgets.QLineEdit(self.T_box)
        self.T_GREEN_VALUE.setGeometry(QtCore.QRect(150, 120, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.T_GREEN_VALUE.setFont(font)
        self.T_GREEN_VALUE.setMaxLength(3)
        self.T_GREEN_VALUE.setAlignment(QtCore.Qt.AlignCenter)
        self.T_GREEN_VALUE.setObjectName("T_GREEN_VALUE")
        self.T_BLUE_VALUE = QtWidgets.QLineEdit(self.T_box)
        self.T_BLUE_VALUE.setGeometry(QtCore.QRect(150, 160, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.T_BLUE_VALUE.setFont(font)
        self.T_BLUE_VALUE.setMaxLength(3)
        self.T_BLUE_VALUE.setAlignment(QtCore.Qt.AlignCenter)
        self.T_BLUE_VALUE.setObjectName("T_BLUE_VALUE")
        self.t_color_value_text = QtWidgets.QLabel(self.T_box)
        self.t_color_value_text.setGeometry(QtCore.QRect(10, 30, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.t_color_value_text.setFont(font)
        self.t_color_value_text.setStyleSheet("color: rgb(255, 85, 0);")
        self.t_color_value_text.setAlignment(QtCore.Qt.AlignCenter)
        self.t_color_value_text.setObjectName("t_color_value_text")
        self.T_box.raise_()
        self.CT_box.raise_()
        self.tabWidget.addTab(self.esp_tab, "")
        self.misc_tab = QtWidgets.QWidget()
        self.misc_tab.setObjectName("misc_tab")
        self.BUNNYHOP_ON_checkbox = QtWidgets.QCheckBox(self.misc_tab)
        self.BUNNYHOP_ON_checkbox.setGeometry(QtCore.QRect(10, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BUNNYHOP_ON_checkbox.setFont(font)
        self.BUNNYHOP_ON_checkbox.setObjectName("BUNNYHOP_ON_checkbox")
        self.NO_FLASH_ON_checkbox = QtWidgets.QCheckBox(self.misc_tab)
        self.NO_FLASH_ON_checkbox.setGeometry(QtCore.QRect(10, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NO_FLASH_ON_checkbox.setFont(font)
        self.NO_FLASH_ON_checkbox.setObjectName("NO_FLASH_ON_checkbox")
        self.RADAR_ESP_ON_checkbox = QtWidgets.QCheckBox(self.misc_tab)
        self.RADAR_ESP_ON_checkbox.setGeometry(QtCore.QRect(10, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RADAR_ESP_ON_checkbox.setFont(font)
        self.RADAR_ESP_ON_checkbox.setObjectName("RADAR_ESP_ON_checkbox")
        self.label_2 = QtWidgets.QLabel(self.misc_tab)
        self.label_2.setGeometry(QtCore.QRect(280, 170, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(200, 0, 200);")
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.misc_tab, "")



        #BUTTONS

        #github open button
        self.github_link_button.clicked.connect(lambda: webbrowser.open_new(github_url))


        #inject button
        self.inject_button.clicked.connect(lambda: Thread(target=main_start(self)).start())


        self.retranslateUi(main_window)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "(っ◔◡◔)っ ♥ cs:go multyhack [by; cookie0_o] ♥"))
        self.title.setText(_translate("main_window", "cs:go multyhack by;                 "))
        self.version.setText(_translate("main_window", "v1.0"))
        self.github_link_button.setText(_translate("main_window", "cookie0_o"))
        self.label.setText(_translate("main_window", "have fun cheating!"))
        self.inject_notice.setText(_translate("main_window", "inject cheat with selected features;"))
        self.inject_button.setText(_translate("main_window", "INJECT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("main_window", "home"))
        self.CT_box.setTitle(_translate("main_window", "COUNTER TERRORIST GLOW"))
        self.CT_GLOW_ON_checkbox.setText(_translate("main_window", "CT glow on"))
        self.ct_red_value_text.setText(_translate("main_window", "Red      value;"))
        self.ct_blue_value_text.setText(_translate("main_window", "BLUE    value;"))
        self.ct_green_value_text.setText(_translate("main_window", "GREEN value;"))
        self.CT_RED_VALUE.setText(_translate("main_window", "0"))
        self.CT_GREEN_VALUE.setText(_translate("main_window", "0"))
        self.CT_BLUE_VALUE.setText(_translate("main_window", "1"))
        self.ct_color_value_text.setText(_translate("main_window", "color value;"))
        self.T_box.setTitle(_translate("main_window", "TERRORIST GLOW"))
        self.T_GLOW_ON_checkbox.setText(_translate("main_window", " T glow on"))
        self.t_red_value_text.setText(_translate("main_window", "Red      value;"))
        self.t_green_value_text.setText(_translate("main_window", "GREEN value;"))
        self.t_blue_value_text.setText(_translate("main_window", "BLUE    value;"))
        self.T_RED_VALUE.setText(_translate("main_window", "1"))
        self.T_GREEN_VALUE.setText(_translate("main_window", "0"))
        self.T_BLUE_VALUE.setText(_translate("main_window", "0"))
        self.t_color_value_text.setText(_translate("main_window", "color value;"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.esp_tab), _translate("main_window", "esp"))
        self.BUNNYHOP_ON_checkbox.setText(_translate("main_window", "bunnyhop"))
        self.NO_FLASH_ON_checkbox.setText(_translate("main_window", "no flash"))
        self.RADAR_ESP_ON_checkbox.setText(_translate("main_window", "radar esp"))
        self.label_2.setText(_translate("main_window", " if you see this\n"
" pls star this project on github\n"
" much love :)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.misc_tab), _translate("main_window", "misc"))

import _res_.res_rc
if __name__=='__main__':
  import sys
  app=QtWidgets.QApplication(sys.argv)
  main_window=QtWidgets.QWidget()
  ui=Ui_main_window()
  ui.setupUi(main_window)
  main_window.show()
  sys.exit(app.exec_())

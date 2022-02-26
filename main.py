#imports
import webbrowser
import pymem
import pymem.process
import keyboard
import time
import ctypes
import re
from PyQt5 import QtCore,QtGui,QtWidgets
from threading import Thread
import atexit

#import offsets
from offsets import *

#github link and version
github_url='https://github.com/cookie0o'
CURRENT_VERSION ='v1.3'

#PATHS
#current dir
dirname = os.path.dirname(__file__)


#path to python cache
cache_path = os.path.join(dirname, '__pycache__')



#RUN CHEAT LOOP
def main_cheat_loop(self):

  try:
      pm=pymem.Pymem("csgo.exe")
      client=pymem.process.module_from_name(pm.process_handle,'client.dll').lpBaseOfDll
      engine=pymem.process.module_from_name(pm.process_handle,'engine.dll').lpBaseOfDll
      enginepointer=pm.read_int(engine+dwClientState)
      player = pm.read_int(client + dwLocalPlayer)
      localplayer = pm.read_int(client + dwLocalPlayer)
  except pymem.exception.ProcessNotFound:
      pass


  cheat_loop_on_off = True

  zoom_on_in  = 0
  zoom_on_out = 0
  
  night_mode = 0

  money_reveal_alr_ON = 0

  while cheat_loop_on_off is True:
    try:
    
    #dejector
      #get deject key
      DEJECT_hit_key_=self.DEJECT_hit_key.text()
      #check if deject key is pressed
      if keyboard.is_pressed(DEJECT_hit_key_):
        cheat_loop_on_off = False
        #reset cheat features;
        try:
        #reset fov and third person
          pm.write_int(localplayer + m_iObserverMode, 0)
        #reset zoom
          fov = player + m_iFOV;pm.write_int(fov, 90)
        #reset nightmode
          #CURRENTLY NOT WORKING
        #reset money-reveal
          A=pymem.process.module_from_name(pm.process_handle,'client.dll')
          B=pm.read_bytes(A.lpBaseOfDll,A.SizeOfImage)
          C=A.lpBaseOfDll+re.search(b'.\\x0C\\x5B\\x5F\\xB8\\xFB\\xFF\\xFF\\xFF',B).start()
          pm.write_uchar(C, 0xEB if pm.read_uchar(C) == 0x75 else 0x75)
        except:
          pass
      else:
        pass



    #if you want the best experience and have a good cpu change this to False like this! :: delay = False
      delay = True
      if delay is True:
        time.sleep(0.001)
        pass
      else:
        pass
      
    

      #THIRD-PERSON
      third_person_on_off = 0
      THIRD_PERSON_toggle_key_=self.THIRD_PERSON_toggle_key.text()
      if keyboard.is_pressed(THIRD_PERSON_toggle_key_) and self.THIRD_PERSON_checkbox.isChecked():
        if third_person_on_off == 0:
          third_person_on_off = 2
          time.sleep(0.1)
          pm.write_int(localplayer + m_iObserverMode, 1)
          fov = player + m_iFOV
          pm.write_int(fov, 100)
        else:
          pass
      else:
        pass

      if keyboard.is_pressed(THIRD_PERSON_toggle_key_) and third_person_on_off==2:
        third_person_on_off = 0
        time.sleep(0.1)
        pm.write_int(localplayer + m_iObserverMode, 0)
        fov = player + m_iFOV
        pm.write_int(fov, 90)
      else:
        pass
      #THIRD-PERSON-END
    

      BUNNYHOP_on_off=0
      if self.BUNNYHOP_ON_checkbox.isChecked():
        BUNNYHOP_on_off=1

      if BUNNYHOP_on_off==1:
        try:
        
          if pm.read_int(client+dwLocalPlayer):
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



      #FOV CHANGER
      
      #get values;
      #get zoom out value;
      FOV_OUT_VALUE_=self.FOV_OUT_VALUE.text()
      #convert str to float
      FOV_OUT_VALUE_FLOAT = float(FOV_OUT_VALUE_)
      #get fov in value;
      FOV_IN_VALUE_=self.FOV_IN_VALUE.text()
      #convert str to float
      FOV_IN_VALUE_FLOAT = float(FOV_IN_VALUE_)

      #get toggle keys;

      #get zoom in toggle key;
      ZOOM_IN_FOV_toggle_key_=self.ZOOM_IN_FOV_toggle_key.text()

      #get zoom out toggle key;
      ZOOM_OUT_FOV_toggle_key_=self.ZOOM_OUT_FOV_toggle_key.text()


      
      #ZOOM IN
      if keyboard.is_pressed(ZOOM_IN_FOV_toggle_key_) and self.ZOOM_IN_FOV_ON_checkbox.isChecked():
        if zoom_on_in == 0:
          zoom_on_in = 2

          time.sleep(0.1)

          #ZOOM
          inputFOV = int(round(FOV_IN_VALUE_FLOAT, 0))
          inputFOV = int(round(FOV_IN_VALUE_FLOAT, 0))

          fov = player + m_iFOV
          pm.write_int(fov, inputFOV)

      else:
        pass
        
      if keyboard.is_pressed(ZOOM_IN_FOV_toggle_key_) and zoom_on_in == 2:
        time.sleep(0.1)
        zoom_on_in = 0
        #reset zoom
        fov = player + m_iFOV
        pm.write_int(fov, 90)
      else:
        pass

      #ZOOM OUT
      if keyboard.is_pressed(ZOOM_OUT_FOV_toggle_key_) and self.ZOOM_OUT_FOV_ON_checkbox.isChecked():
        if zoom_on_out == 0:
          zoom_on_out = 2

          time.sleep(0.1)

          #ZOOM
          inputFOV = int(round(FOV_OUT_VALUE_FLOAT, 0))
          player = pm.read_int(client + dwLocalPlayer)
          inputFOV = int(round(FOV_OUT_VALUE_FLOAT, 0))
          fov = player + m_iFOV
          pm.write_int(fov, inputFOV)

      else:
        pass

      if keyboard.is_pressed(ZOOM_OUT_FOV_toggle_key_) and zoom_on_out == 2:
        time.sleep(0.1)
        zoom_on_out = 0
        #reset zoom
        player = pm.read_int(client + dwLocalPlayer)
        fov = player + m_iFOV
        pm.write_int(fov, 90)
      else:
        pass


      #NIGHTMODE

      #get nightmode toggle key
      NIGHTMODE_toggle_key_=self.NIGHTMODE_toggle_key.text()

      #get light value;
      NIGHTMODE_LIGHT_VALUE_=self.NIGHTMODE_LIGHT_VALUE.text()
      #convert str to float
      NIGHTMODE_LIGHT_VALUE_FLOAT = float(NIGHTMODE_LIGHT_VALUE_)

      if keyboard.is_pressed(NIGHTMODE_toggle_key_) and self.NIGHTMODE_ON_checkbox.isChecked():
        if night_mode == 0:
          night_mode = 2

        else:
          if night_mode == 2:
            night_mode = 0

      
      if night_mode == 2:
        for i in range(0, 2048):
          entity = pm.read_uint(client + dwEntityList + i * 0x10)
          if entity:
              EntityClassID = pm.read_int(entity + 0x8)
              huita1 = pm.read_int(EntityClassID + 2 * 0x4)
              huita2 = pm.read_int(huita1 + 0x1)
              huita3 = pm.read_int(huita2 + 20)

              if (huita3 != 69):
                  continue
              
              if True:
                  pm.write_int(entity + m_bUseCustomAutoExposureMin, 1)
                  pm.write_int(entity + m_bUseCustomAutoExposureMax, 1)
                  pm.write_float(entity + m_flCustomAutoExposureMin, NIGHTMODE_LIGHT_VALUE_FLOAT)
                  pm.write_float(entity + m_flCustomAutoExposureMax, NIGHTMODE_LIGHT_VALUE_FLOAT)
              else:
                  pm.write_bool(entity + m_bUseCustomAutoExposureMin, 0)
                  pm.write_bool(entity + m_bUseCustomAutoExposureMax, 0)
      else:
        pass

      if night_mode == 0:
        #reset nightmode
        for i in range(0, 2048):
          entity = pm.read_uint(client + dwEntityList + i * 0x10)
          if entity:
              EntityClassID = pm.read_int(entity + 0x8)
              a = pm.read_int(EntityClassID + 2 * 0x4)
              b = pm.read_int(a + 0x1)
              c = pm.read_int(b + 20)

              if (c != 69):
                  continue
              
              if True:
                  pm.write_int(entity + m_bUseCustomAutoExposureMin, 1)
                  pm.write_int(entity + m_bUseCustomAutoExposureMax, 1)
                  pm.write_float(entity + m_flCustomAutoExposureMin, 1.0)
                  pm.write_float(entity + m_flCustomAutoExposureMax, 1.0)
              else:
                  pm.write_bool(entity + m_bUseCustomAutoExposureMin, 0)
                  pm.write_bool(entity + m_bUseCustomAutoExposureMax, 0)
      else:
        pass


      #MONEY REVEAL
      if self.MONEY_REVEAL_ON_checkbox.isChecked():
        if money_reveal_alr_ON == 0:
          try:
            client_money_reveal = pymem.process.module_from_name(pm.process_handle, 'client.dll')
            clientModule = pm.read_bytes(client_money_reveal.lpBaseOfDll, client_money_reveal.SizeOfImage)
            address = client_money_reveal.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF', clientModule).start()
            pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)
            money_reveal_alr_ON = 1
          except:
            pass
      #reset money reveal
      else:
        try:
          pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)
        except:
          pass


      #TRIGGER BOT
      
      #get trigger key
      TRIGGERBOT_hold_key_=self.TRIGGERBOT_hold_key.text()

      #get shoot delay
      TRIGGERBOT_DELAY_=self.TRIGGERBOT_DELAY.text()

      TRIGGERBOT_DELAY_FLOAT = float(TRIGGERBOT_DELAY_)


      if self.TRIGGERBOT_ON_checkbox.isChecked():
        if keyboard.is_pressed(TRIGGERBOT_hold_key_):
            player = pm.read_int(client + dwLocalPlayer)
            entity_id = pm.read_int(player + m_iCrosshairId)
            entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

            entity_team = pm.read_int(entity + m_iTeamNum)
            player_team = pm.read_int(player + m_iTeamNum)

            if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
              time.sleep(TRIGGERBOT_DELAY_FLOAT)
              pm.write_int(client + dwForceAttack, 6) 

            else:
              pass
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







    #show error msg when csgo was closed or an error occurred
    except:
      MessageBox = ctypes.windll.user32.MessageBoxW
      MessageBox(None, 'cs:go was closed or an error occurred!', 'Error', 16)
      #remove cache
      try:
        os.system(f"@RD /S /Q {cache_path}")
      except:
        return
      return




def main_start(self):
  try:
    pymem.Pymem("csgo.exe")
  except pymem.exception.ProcessNotFound:
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'pls start cs:go and press ok!', 'Error', 16)


  #run main cheat loop
  Thread(target=main_cheat_loop(self)).start()
  

#MAIN UI
class main_window(object):
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
        self.deject_key_text = QtWidgets.QLabel(self.frame)
        self.deject_key_text.setGeometry(QtCore.QRect(90, 100, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.deject_key_text.setFont(font)
        self.deject_key_text.setAlignment(QtCore.Qt.AlignCenter)
        self.deject_key_text.setObjectName("deject_key_text")
        self.DEJECT_hit_key = QtWidgets.QLineEdit(self.frame)
        self.DEJECT_hit_key.setGeometry(QtCore.QRect(300, 100, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DEJECT_hit_key.setFont(font)
        self.DEJECT_hit_key.setMaxLength(333)
        self.DEJECT_hit_key.setAlignment(QtCore.Qt.AlignCenter)
        self.DEJECT_hit_key.setObjectName("DEJECT_hit_key")
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
        self.THIRD_PERSON_checkbox = QtWidgets.QCheckBox(self.misc_tab)
        self.THIRD_PERSON_checkbox.setGeometry(QtCore.QRect(380, 10, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.THIRD_PERSON_checkbox.setFont(font)
        self.THIRD_PERSON_checkbox.setObjectName("THIRD_PERSON_checkbox")
        self.label_9 = QtWidgets.QLabel(self.misc_tab)
        self.label_9.setGeometry(QtCore.QRect(380, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.THIRD_PERSON_toggle_key = QtWidgets.QLineEdit(self.misc_tab)
        self.THIRD_PERSON_toggle_key.setGeometry(QtCore.QRect(460, 30, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.THIRD_PERSON_toggle_key.setFont(font)
        self.THIRD_PERSON_toggle_key.setMaxLength(333)
        self.THIRD_PERSON_toggle_key.setAlignment(QtCore.Qt.AlignCenter)
        self.THIRD_PERSON_toggle_key.setObjectName("THIRD_PERSON_toggle_key")
        self.MONEY_REVEAL_ON_checkbox = QtWidgets.QCheckBox(self.misc_tab)
        self.MONEY_REVEAL_ON_checkbox.setGeometry(QtCore.QRect(10, 140, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MONEY_REVEAL_ON_checkbox.setFont(font)
        self.MONEY_REVEAL_ON_checkbox.setObjectName("MONEY_REVEAL_ON_checkbox")
        self.tabWidget.addTab(self.misc_tab, "")
        self.fov_tab = QtWidgets.QWidget()
        self.fov_tab.setObjectName("fov_tab")
        self.zoom_out_frame = QtWidgets.QFrame(self.fov_tab)
        self.zoom_out_frame.setGeometry(QtCore.QRect(10, 10, 521, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.zoom_out_frame.setFont(font)
        self.zoom_out_frame.setStyleSheet("")
        self.zoom_out_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.zoom_out_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.zoom_out_frame.setLineWidth(2)
        self.zoom_out_frame.setObjectName("zoom_out_frame")
        self.ZOOM_OUT_FOV_ON_checkbox = QtWidgets.QCheckBox(self.zoom_out_frame)
        self.ZOOM_OUT_FOV_ON_checkbox.setGeometry(QtCore.QRect(10, 10, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ZOOM_OUT_FOV_ON_checkbox.setFont(font)
        self.ZOOM_OUT_FOV_ON_checkbox.setChecked(True)
        self.ZOOM_OUT_FOV_ON_checkbox.setObjectName("ZOOM_OUT_FOV_ON_checkbox")
        self.FOV_OUT_VALUE = QtWidgets.QLineEdit(self.zoom_out_frame)
        self.FOV_OUT_VALUE.setGeometry(QtCore.QRect(10, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.FOV_OUT_VALUE.setFont(font)
        self.FOV_OUT_VALUE.setMaxLength(3)
        self.FOV_OUT_VALUE.setAlignment(QtCore.Qt.AlignCenter)
        self.FOV_OUT_VALUE.setObjectName("FOV_OUT_VALUE")
        self.label_5 = QtWidgets.QLabel(self.zoom_out_frame)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.ZOOM_OUT_FOV_toggle_key = QtWidgets.QLineEdit(self.zoom_out_frame)
        self.ZOOM_OUT_FOV_toggle_key.setGeometry(QtCore.QRect(100, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.ZOOM_OUT_FOV_toggle_key.setFont(font)
        self.ZOOM_OUT_FOV_toggle_key.setMaxLength(333)
        self.ZOOM_OUT_FOV_toggle_key.setAlignment(QtCore.Qt.AlignCenter)
        self.ZOOM_OUT_FOV_toggle_key.setObjectName("ZOOM_OUT_FOV_toggle_key")
        self.FOV_130_IMG = QtWidgets.QLabel(self.zoom_out_frame)
        self.FOV_130_IMG.setGeometry(QtCore.QRect(360, 10, 151, 91))
        self.FOV_130_IMG.setStyleSheet("image: url(:/fov_images/130_fov.png);")
        self.FOV_130_IMG.setText("")
        self.FOV_130_IMG.setScaledContents(True)
        self.FOV_130_IMG.setObjectName("FOV_130_IMG")
        self.label_6 = QtWidgets.QLabel(self.zoom_out_frame)
        self.label_6.setGeometry(QtCore.QRect(160, 70, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.zoom_in_frame = QtWidgets.QFrame(self.fov_tab)
        self.zoom_in_frame.setGeometry(QtCore.QRect(10, 130, 521, 111))
        self.zoom_in_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.zoom_in_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.zoom_in_frame.setLineWidth(2)
        self.zoom_in_frame.setObjectName("zoom_in_frame")
        self.ZOOM_IN_FOV_ON_checkbox = QtWidgets.QCheckBox(self.zoom_in_frame)
        self.ZOOM_IN_FOV_ON_checkbox.setGeometry(QtCore.QRect(10, 10, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ZOOM_IN_FOV_ON_checkbox.setFont(font)
        self.ZOOM_IN_FOV_ON_checkbox.setChecked(True)
        self.ZOOM_IN_FOV_ON_checkbox.setObjectName("ZOOM_IN_FOV_ON_checkbox")
        self.FOV_IN_VALUE = QtWidgets.QLineEdit(self.zoom_in_frame)
        self.FOV_IN_VALUE.setGeometry(QtCore.QRect(10, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.FOV_IN_VALUE.setFont(font)
        self.FOV_IN_VALUE.setMaxLength(3)
        self.FOV_IN_VALUE.setAlignment(QtCore.Qt.AlignCenter)
        self.FOV_IN_VALUE.setObjectName("FOV_IN_VALUE")
        self.label_7 = QtWidgets.QLabel(self.zoom_in_frame)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.ZOOM_IN_FOV_toggle_key = QtWidgets.QLineEdit(self.zoom_in_frame)
        self.ZOOM_IN_FOV_toggle_key.setGeometry(QtCore.QRect(100, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.ZOOM_IN_FOV_toggle_key.setFont(font)
        self.ZOOM_IN_FOV_toggle_key.setMaxLength(333)
        self.ZOOM_IN_FOV_toggle_key.setAlignment(QtCore.Qt.AlignCenter)
        self.ZOOM_IN_FOV_toggle_key.setObjectName("ZOOM_IN_FOV_toggle_key")
        self.FOV_80_IMG = QtWidgets.QLabel(self.zoom_in_frame)
        self.FOV_80_IMG.setGeometry(QtCore.QRect(360, 10, 151, 91))
        self.FOV_80_IMG.setStyleSheet("image: url(:/fov_images/80_fov.png);")
        self.FOV_80_IMG.setText("")
        self.FOV_80_IMG.setScaledContents(True)
        self.FOV_80_IMG.setObjectName("FOV_80_IMG")
        self.label_8 = QtWidgets.QLabel(self.zoom_in_frame)
        self.label_8.setGeometry(QtCore.QRect(160, 70, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.zoom_in_frame.raise_()
        self.zoom_out_frame.raise_()
        self.tabWidget.addTab(self.fov_tab, "")
        self.triggerbot_tab = QtWidgets.QWidget()
        self.triggerbot_tab.setObjectName("triggerbot_tab")
        self.frame_2 = QtWidgets.QFrame(self.triggerbot_tab)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 511, 221))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.TRIGGERBOT_ON_checkbox = QtWidgets.QCheckBox(self.frame_2)
        self.TRIGGERBOT_ON_checkbox.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TRIGGERBOT_ON_checkbox.setFont(font)
        self.TRIGGERBOT_ON_checkbox.setObjectName("TRIGGERBOT_ON_checkbox")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.TRIGGERBOT_hold_key = QtWidgets.QLineEdit(self.frame_2)
        self.TRIGGERBOT_hold_key.setGeometry(QtCore.QRect(90, 50, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.TRIGGERBOT_hold_key.setFont(font)
        self.TRIGGERBOT_hold_key.setMaxLength(333)
        self.TRIGGERBOT_hold_key.setAlignment(QtCore.Qt.AlignCenter)
        self.TRIGGERBOT_hold_key.setObjectName("TRIGGERBOT_hold_key")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.TRIGGERBOT_DELAY = QtWidgets.QLineEdit(self.frame_2)
        self.TRIGGERBOT_DELAY.setGeometry(QtCore.QRect(10, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.TRIGGERBOT_DELAY.setFont(font)
        self.TRIGGERBOT_DELAY.setObjectName("TRIGGERBOT_DELAY")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(110, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.triggerbot_tab, "")
        self.nightmode_tab = QtWidgets.QWidget()
        self.nightmode_tab.setObjectName("nightmode_tab")
        self.frame_3 = QtWidgets.QFrame(self.nightmode_tab)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 511, 221))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.NIGHTMODE_ON_checkbox = QtWidgets.QCheckBox(self.frame_3)
        self.NIGHTMODE_ON_checkbox.setGeometry(QtCore.QRect(10, 10, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.NIGHTMODE_ON_checkbox.setFont(font)
        self.NIGHTMODE_ON_checkbox.setChecked(True)
        self.NIGHTMODE_ON_checkbox.setObjectName("NIGHTMODE_ON_checkbox")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(10, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.NIGHTMODE_toggle_key = QtWidgets.QLineEdit(self.frame_3)
        self.NIGHTMODE_toggle_key.setGeometry(QtCore.QRect(110, 50, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.NIGHTMODE_toggle_key.setFont(font)
        self.NIGHTMODE_toggle_key.setMaxLength(333)
        self.NIGHTMODE_toggle_key.setAlignment(QtCore.Qt.AlignCenter)
        self.NIGHTMODE_toggle_key.setObjectName("NIGHTMODE_toggle_key")
        self.NIGHTMODE_LIGHT_VALUE = QtWidgets.QLineEdit(self.frame_3)
        self.NIGHTMODE_LIGHT_VALUE.setGeometry(QtCore.QRect(110, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.NIGHTMODE_LIGHT_VALUE.setFont(font)
        self.NIGHTMODE_LIGHT_VALUE.setMaxLength(333)
        self.NIGHTMODE_LIGHT_VALUE.setAlignment(QtCore.Qt.AlignCenter)
        self.NIGHTMODE_LIGHT_VALUE.setObjectName("NIGHTMODE_LIGHT_VALUE")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(10, 90, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(190, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.NIGHTMODE_ON_checkbox.raise_()
        self.label_11.raise_()
        self.NIGHTMODE_toggle_key.raise_()
        self.label_12.raise_()
        self.NIGHTMODE_LIGHT_VALUE.raise_()
        self.label_13.raise_()
        self.tabWidget.addTab(self.nightmode_tab, "")
        
        #BUTTONS

        #open github button
        self.github_link_button.clicked.connect(lambda: webbrowser.open_new(github_url))

        #inject button
        self.inject_button.clicked.connect(lambda: Thread(target=main_start(self)).start())


        self.retranslateUi(main_window_cheat)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window_cheat)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "(っ◔◡◔)っ ♥ cs:go multihack [by; cookie0_o] ♥"))
        self.title.setText(_translate("main_window", "cs:go multihack by;                 "))
        self.version.setText(_translate("main_window", f"{CURRENT_VERSION}"))
        self.github_link_button.setText(_translate("main_window", "cookie0_o"))
        self.label.setText(_translate("main_window", "have fun cheating!"))
        self.inject_notice.setText(_translate("main_window", "inject cheat with selected features;"))
        self.inject_button.setText(_translate("main_window", "INJECT"))
        self.deject_key_text.setText(_translate("main_window", "deject key;"))
        self.DEJECT_hit_key.setText(_translate("main_window", "F11"))
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
        self.THIRD_PERSON_checkbox.setText(_translate("main_window", "third person"))
        self.label_9.setText(_translate("main_window", "toggleKey;"))
        self.THIRD_PERSON_toggle_key.setText(_translate("main_window", "V"))
        self.MONEY_REVEAL_ON_checkbox.setText(_translate("main_window", "money reveal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.misc_tab), _translate("main_window", "misc"))
        self.ZOOM_OUT_FOV_ON_checkbox.setText(_translate("main_window", "zoom out FOV;"))
        self.FOV_OUT_VALUE.setText(_translate("main_window", "130"))
        self.label_5.setText(_translate("main_window", "toggle Key:"))
        self.ZOOM_OUT_FOV_toggle_key.setText(_translate("main_window", "F7"))
        self.label_6.setText(_translate("main_window", "press key again to reset FOV!"))
        self.ZOOM_IN_FOV_ON_checkbox.setText(_translate("main_window", "zoom in FOV;"))
        self.FOV_IN_VALUE.setText(_translate("main_window", "75"))
        self.label_7.setText(_translate("main_window", "toggle Key:"))
        self.ZOOM_IN_FOV_toggle_key.setText(_translate("main_window", "F8"))
        self.label_8.setText(_translate("main_window", "press key again to reset FOV!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fov_tab), _translate("main_window", "fov"))
        self.TRIGGERBOT_ON_checkbox.setText(_translate("main_window", "Triggerbot"))
        self.label_10.setText(_translate("main_window", "hold Key:"))
        self.TRIGGERBOT_hold_key.setText(_translate("main_window", "ALT"))
        self.label_3.setText(_translate("main_window", "shoot delay (if you want to be a little legit);"))
        self.TRIGGERBOT_DELAY.setText(_translate("main_window", "0"))
        self.label_4.setText(_translate("main_window", "seconds"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.triggerbot_tab), _translate("main_window", "triggerbot"))
        self.NIGHTMODE_ON_checkbox.setText(_translate("main_window", "nightmode"))
        self.label_11.setText(_translate("main_window", "toggle Key:"))
        self.NIGHTMODE_toggle_key.setText(_translate("main_window", "P"))
        self.NIGHTMODE_LIGHT_VALUE.setText(_translate("main_window", "0.0900"))
        self.label_12.setText(_translate("main_window", "light value:"))
        self.label_13.setText(_translate("main_window", "press key again to turn off!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.nightmode_tab), _translate("main_window", "nightmode"))


import _res_.res_rc
if __name__=='__main__':
  import sys
  app=QtWidgets.QApplication(sys.argv)
  main_window_cheat=QtWidgets.QWidget()
  ui=main_window()
  ui.setupUi(main_window_cheat)
  main_window_cheat.show()
  sys.exit(app.exec_())


#show / hide window

def hide_window():
  main_window_cheat=QtWidgets.QWidget()
  ui=main_window()
  ui.setupUi(main_window_cheat)
  main_window_cheat.hide()
  pass

def show_window():
  app=QtWidgets.QApplication(sys.argv)
  main_window_cheat=QtWidgets.QWidget()
  ui=main_window()
  ui.setupUi(main_window_cheat)
  main_window_cheat.show()
  sys.exit(app.exec_())
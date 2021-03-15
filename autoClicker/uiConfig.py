from PyQt5.QtCore import QTimer, QTime
from PyQt5 import QtCore
from PyQt5 import QtGui
import pyautogui
import random

REPEAT_VALUE = 0
AUTO_CLICKING = False


def current_time():
    t = QTime.currentTime().toString()
    am_pm = "pm" if 12 < int(t[:2]) < 23 else "am"
    return t + " " + am_pm


def click_synonym():
    return random.choice(['click', 'bang', 'clank', 'snap', 'tick', 'clack'])


class Presets:

    def event_log(self, message):
        t, c = current_time(), self.ui.mouseList.count()
        self.ui.mouseList.setCurrentRow(c - 1)
        self.ui.mouseLastUpdate.setText('Last Update {}'.format(t))
        if c > 100:
            self.ui.mouseList.clear()
            self.ui.mouseList.addItem("CLEARED --> {}".format(t))
        self.ui.mouseList.addItem("{} - {}".format(t, message))

    def go_to_settings(self):
        if AUTO_CLICKING:
            self.ui.information.setText("Still {}ing!".format(click_synonym()))
        self.ui.pageTitle.setText("Auto Clicker!")
        self.ui.stackedWidget.setCurrentIndex(0)

    def go_to_event_log(self):
        if AUTO_CLICKING:
            self.ui.information.setText("Still {}ing!".format(click_synonym()))
        self.ui.pageTitle.setText("Event Log!")
        self.ui.stackedWidget.setCurrentIndex(1)

    def change_frequency(self, msg):
        if AUTO_CLICKING:
            self.ui.information.setText("Still {}ing!".format(click_synonym()))
        message = ""
        hrs = self.ui.hrs.value()
        mins = self.ui.mins.value()
        secs = self.ui.secs.value()
        msecs = self.ui.msecs.value()
        if msg == "Hour(s)":
            message = "{} --> {}".format(msg, hrs)
        elif msg == "Minutes(s)":
            message = "{} --> {}".format(msg, mins)
        elif msg == "Second(s)":
            message = "{} --> {}".format(msg, secs)
        elif msg == "Milisecond(s)":
            message = "{} --> {}".format(msg, msecs)
        total_freq = msecs + (secs * 1000) + (mins * 60000) + (hrs * 3600000)
        if total_freq < 1000:
            self.ui.information.setText("Specify x & y!")
            Presets.event_log(self, "Frequency Very Low!")
            self.ui.specify.setChecked(True)
            Presets.event_log(self, "Specify Activated!")
        else:
            self.ui.information.setText("")
        Presets.event_log(self, message)

    def change_radio_btn(self, msg):
        if AUTO_CLICKING:
            self.ui.information.setText("Still {}ing!".format(click_synonym()))
        if msg == "repeat":
            if self.ui.repeat.isChecked():
                self.ui.forever.setChecked(False)
        elif msg == "forever":
            if self.ui.forever.isChecked():
                self.ui.repeat.setChecked(False)
        elif msg == "current":
            if self.ui.current.isChecked():
                self.ui.specify.setChecked(False)
        elif msg == "specify":
            if self.ui.specify.isChecked():
                self.ui.current.setChecked(False)

    def general_change(self, msg):
        if AUTO_CLICKING:
            self.ui.information.setText("Still {}ing!".format(click_synonym()))
        if msg == "xcoor":
            if not AUTO_CLICKING:
                self.ui.information.setText("")
            Presets.event_log(self, "Specified x: {}".format(self.ui.xcoor.value()))
        elif msg == "ycoor":
            if not AUTO_CLICKING:
                self.ui.information.setText("")
            Presets.event_log(self, "Specified y: {}".format(self.ui.ycoor.value()))
        elif msg == "action":
            Presets.event_log(self, "Action: {}".format(self.ui.action.currentText()))
        elif msg == "repeat":
            Presets.event_log(self, "Repeat value: {}".format(self.ui.repeatSpin.value()))

    def init_ui(self):
        self.setWindowIcon(QtGui.QIcon('images/mouse.png'))
        self.setFixedWidth(440)
        self.setFixedHeight(420)
        Presets.mouse_loop(self)
        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.settingsBtn.clicked.connect(lambda: Presets.go_to_settings(self))
        self.ui.eventLogBtn.clicked.connect(lambda: Presets.go_to_event_log(self))
        # self.ui.covidBtn.clicked.connect(lambda: Presets.go_to_covid(self))
        self.ui.startBtn.clicked.connect(lambda: Presets.start_auto_clicker(self))
        self.ui.stopBtn.clicked.connect(lambda: Presets.stop_auto_clicker(self))
        self.ui.timer = QTimer()
        self.ui.timer.timeout.connect(lambda: Presets.mouse_loop(self))
        self.ui.timer.start(200)
        self.ui.hrs.valueChanged.connect(lambda: Presets.change_frequency(self, "Hour(s)"))
        self.ui.mins.valueChanged.connect(lambda: Presets.change_frequency(self, "Minutes(s)"))
        self.ui.secs.valueChanged.connect(lambda: Presets.change_frequency(self, "Second(s)"))
        self.ui.msecs.valueChanged.connect(lambda: Presets.change_frequency(self, "Milisecond(s)"))
        self.ui.repeat.toggled.connect(lambda: Presets.change_radio_btn(self, "repeat"))
        self.ui.forever.toggled.connect(lambda: Presets.change_radio_btn(self, "forever"))
        self.ui.current.toggled.connect(lambda: Presets.change_radio_btn(self, "current"))
        self.ui.specify.toggled.connect(lambda: Presets.change_radio_btn(self, "specify"))
        self.ui.xcoor.valueChanged.connect(lambda: Presets.general_change(self, "xcoor"))
        self.ui.ycoor.valueChanged.connect(lambda: Presets.general_change(self, "ycoor"))
        self.ui.action.currentTextChanged.connect(lambda: Presets.general_change(self, "action"))
        self.ui.repeatSpin.valueChanged.connect(lambda: Presets.general_change(self, "repeat"))
        self.ui.stopBtn.hide()

        def move_window(event):
            try:
                self.move(self.pos() + event.globalPos() - self.dragPos)
            except:
                pass
            self.dragPos = event.globalPos()
            event.accept()

        self.ui.dragFrame.mouseMoveEvent = move_window

    REPEAT_VALUE = 0

    def start_auto_clicker(self):
        global AUTO_CLICKING
        AUTO_CLICKING = True
        Presets.event_log(self, "Started.")
        self.ui.information.setText("Started!")
        self.ui.information.setStyleSheet('color:lightgreen;')
        self.ui.startBtn.hide()
        self.ui.stopBtn.show()
        hrs = self.ui.hrs.value()
        mins = self.ui.mins.value()
        secs = self.ui.secs.value()
        msecs = self.ui.msecs.value()
        action = self.ui.action.currentText()
        repeat = self.ui.repeat.isChecked()
        repeat_val = self.ui.repeatSpin.value()
        forever = self.ui.forever.isChecked()
        current = self.ui.current.isChecked()
        specify = self.ui.specify.isChecked()
        xcoor = self.ui.xcoor.value()
        ycoor = self.ui.ycoor.value()
        total_freq = msecs + (secs * 1000) + (mins * 60000) + (hrs * 3600000)

        if specify:
            pyautogui.moveTo(xcoor, ycoor)
        Presets.REPEAT_VALUE += repeat_val

        self.ui.auto_clicker = QTimer()
        self.ui.auto_clicker.timeout.connect(lambda: Presets.auto_clicker_loop(self, action, repeat,
                                                                               forever, repeat_val,
                                                                               current, specify,
                                                                               xcoor, ycoor))
        self.ui.auto_clicker.start(total_freq)

    def stop_auto_clicker(self):
        global AUTO_CLICKING
        AUTO_CLICKING = False
        self.ui.information.setText("Stopped!")
        self.ui.information.setStyleSheet('color:tomato;')
        self.ui.startBtn.show()
        self.ui.stopBtn.hide()
        self.ui.auto_clicker.stop()
        Presets.event_log(self, "Stopped.")

    def auto_clicker_loop(self, action, repeat, forever, repeat_val, current, specify, xcoor, ycoor):
        def autogui_action(action, xpos, ypos):
            if action == "Left Click":
                pyautogui.click(clicks=1, interval=0.2, button="left")
            elif action == "Left Double Click":
                pyautogui.click(clicks=2, interval=0.2, button="left")
            elif action == "Left Triple Click":
                pyautogui.click(clicks=3, interval=0.2, button="left")
            elif action == "Right Click":
                pyautogui.click(clicks=1, interval=0.2, button="right")
            elif action == "Right Double Click":
                pyautogui.click(clicks=2, interval=0.2, button="right")
            elif action == "Right Triple Click":
                pyautogui.click(clicks=3, interval=0.2, button="right")
            elif action == "Scroll Wheel Up":
                pyautogui.scroll(amount_to_scroll=5, x=xpos, y=ypos + 5)
            elif action == "Scroll Wheel Down":
                pyautogui.scroll(amount_to_scroll=5, x=xpos, y=ypos - 5)
            elif action == "Scroll Wheel Click":
                pyautogui.click(clicks=1, interval=0.2, button="middle")
            elif action == "crtl c":
                pyautogui.hotkey('ctrl', 'c')
            elif action == "crtl v":
                pyautogui.hotkey('ctrl', 'v')
            elif action == "ctrl x":
                pyautogui.hotkey('ctrl', 'x')
            else:
                pyautogui.press(action)

        cont = True
        xpos, ypos = 0, 0
        if specify:
            pos = pyautogui.position()
            xpos, ypos = pos[0], pos[1]
            if xpos != xcoor or ypos != ycoor:
                cont = False
                Presets.stop_auto_clicker(self)
        if current:
            pos = pyautogui.position()
            xpos, ypos = pos[0], pos[1]
        if cont:
            if forever:
                autogui_action(action, xpos, ypos)
            elif repeat:
                if 0 != Presets.REPEAT_VALUE:
                    Presets.REPEAT_VALUE -= 1
                    Presets.event_log(self, "Loops leftover: {}".format(Presets.REPEAT_VALUE))
                    autogui_action(action, xpos, ypos)
                else:
                    Presets.stop_auto_clicker(self)

            Presets.event_log(self, click_synonym() + "ing.")

    def mouse_loop(self):
        self.ui.mouseTime.setText(current_time())
        pos = pyautogui.position()
        self.ui.mousexy.setText("({}, {})".format(pos[0], pos[1]))

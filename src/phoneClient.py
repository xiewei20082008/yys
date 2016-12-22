#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy
#qpy:fullscreen

from socket import *
import time
from time import sleep
from threading import Thread
from kivy.app import App
from kivy.app import runTouchApp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.spinner import Spinner

Builder.load_string('''
<ScrollableLabel>:
    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text
''')
class ScrollableLabel(ScrollView):
    text = StringProperty('')

times = 4
def genSpinner(textList):
    def show_selected_value(spinner, text):
        print('The spinner', spinner, 'have text', text)
    spinner = Spinner(
        text=textList[0],
        # available values
        values=textList,
        # just for positioning in our example
        size_hint=(None, None),
        size=(40*times, 25*times),
        pos_hint={'center_x': .5, 'center_y': .5})
    spinner.bind(text=show_selected_value)
    return spinner

class Client:
    def __init__(self):
        self.host = '172.246.84.119'
        self.port = 21567
        self.bufsize = 2000
        self.udpCliSock = socket(AF_INET, SOCK_DGRAM)
        self.addr = (self.host,self.port)
        print 'socket ok'
        self.udpCliSock.settimeout(0.4)
    def flushListen(self):
        while True:
            try:
                PacketBytes = self.udpCliSock.recv(1024)
            except:
                break;
    def send(self,message):
        data = '1~'+message
        for i in range(5):
            self.udpCliSock.sendto(data,self.addr)
            try:
                ret,tmp = self.udpCliSock.recvfrom(self.bufsize)
                self.flushListen()
                return ret
            except:
                continue
        else:
            return 'receive time out'
    def close(self):
        self.udpCliSock.close()

def genDropDownButton(num,choiceText,dropdown):
    for index in range(num):
        btn = Button(text=choiceText[index], size_hint=(None, None),width=23*times,height = 23*times)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
    mainbutton = Button(text=choiceText[0], size_hint=(None, None),width=23*times,height = 23*times)
    mainbutton.bind(on_release=dropdown.open)
    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
    return mainbutton

class phoneApp(App):
    def sendCmd(self,instance):
        def runUp():
            self.l_log.text = 'Command is under execution!'
            cmd = ' '.join([self.dd_hao.text,self.dd_start.text,self.dd_chapter.text,self.dd_aimEnergy.text,self.dd_rush.text])
            # print 'real'
            # print cmd
            ret = self.client.send('sendCmd:'+cmd)
            self.l_log.text = ret

        if self.needConfirm:
            cmd = ' '.join([self.dd_hao.text,self.dd_start.text,self.dd_chapter.text,self.dd_aimEnergy.text,self.dd_rush.text])
            self.l_log.text = 'confirm cmd\n'+cmd
            self.needConfirm = False
        else:
            self.needConfirm = True
            t = Thread(target = runUp)
            t.start()

    def sendLog(self,instance):
        def runUp():
            self.l_log.text = 'Command is under execution!'
            ret = self.client.send('readLog')
            self.l_log.text = ret
        self.needConfirm = True
        t = Thread(target = runUp)
        t.start()

    def build(self):
        self.needConfirm = True
        self.client = Client()
        layout = BoxLayout(orientation='horizontal')
        layoutRight = BoxLayout(orientation='vertical')

        self.l_log = ScrollableLabel()
        # scollView = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        layout.add_widget(self.l_log)
        layout.add_widget(layoutRight)
        # self.l_log.text_size = scollView.width,None

        left_window_up = StackLayout()
        left_window_down = GridLayout(cols=2)

        layoutRight.add_widget(left_window_up)
        layoutRight.add_widget(left_window_down)

        # dropdown_hao = DropDown()
        # self.dd_hao = genDropDownButton(2,["dahao","xiaohao"],dropdown_hao)
        # dropdown_start = DropDown()
        # self.dd_start = genDropDownButton(2,["0","1"],dropdown_start)
        # dropdown_chapter = DropDown()
        # self.dd_chapter = genDropDownButton(2,["11","5"],dropdown_chapter)
        # dropdown_aimEnergy = DropDown()
        # self.dd_aimEnergy = genDropDownButton(2,["20","30"],dropdown_aimEnergy)
        # dropdown_rush = DropDown()
        # self.dd_rush = genDropDownButton(2,["True","False"],dropdown_rush)

        self.dd_hao = genSpinner(['dahao','xiaohao'])
        self.dd_start = genSpinner(['0','1'])
        self.dd_chapter = genSpinner(['11','5'])
        self.dd_aimEnergy = genSpinner(['20','30','99'])
        self.dd_rush = genSpinner(['True','False'])


        left_window_up.add_widget(self.dd_hao)
        left_window_up.add_widget(self.dd_start)
        left_window_up.add_widget(self.dd_chapter)
        left_window_up.add_widget(self.dd_aimEnergy)
        left_window_up.add_widget(self.dd_rush)

        # b_readLog = Button(text = 'readLog',size_hint=(None, None),width = 60*times)
        # b_exe = Button(text = 'execute',size_hint=(None, None),width = 60*times)
        b_readLog = Button(text = 'readLog')
        b_readLog.bind(on_press=self.sendLog)
        b_exe = Button(text = 'execute')
        b_exe.bind(on_press=self.sendCmd)

        left_window_down.add_widget(b_exe)
        left_window_down.add_widget(b_readLog)

        # layout.add_widget(dd_start)
        # left_window.add_widget(dd_hao)
        # left_window.add_widget(dd_start)
        # left_window.add_widget(dd_chapter)
        # left_window.add_widget(dd_aimEnergy)

        # layout.add_widget(l_log)
        return layout

runTouchApp(phoneApp().build())
# phoneApp().run()

# client = Client()
# client.send('delLog')
# client.send('readLog')
# client.send('sendCmd:dahao 1 11 20 True')

#!/usr/bin/env python2

from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from os.path import join, dirname
from glob import glob
from kivy.clock import Clock
from kivy.lang import Builder
# If we will not import this module 
# It will through the error 
from kivy.uix.slider import Slider 
  
# The Label widget is for rendering text. 
from kivy.uix.label import Label 
from kivy.properties import ObjectProperty
slider_time=1
class MyCarousel(Carousel):
    cnt=0
    def __init__(self,**kwargs):
        super(MyCarousel,self).__init__(**kwargs)
        # get any files into images directory
        global slider_time
        self.curdir = dirname(__file__)
        self.direction="top"

        self.loop=True
        self.image_input()
        Clock.schedule_interval(self.call_back,1)
    def call_back(self,dt):
        self.cnt=self.cnt+1
        print(self.cnt)
        if(self.cnt % slider_time == 0):
            self.load_next()
        if(self.cnt==30):
            self.image_input()
            self.cnt=0
    def image_input(self):
        for fn in glob(join(self.curdir, '/home/test/Pictures', '*')):
            src = fn
            image = AsyncImage(source=src, allow_stretch=True)
            self.add_widget(image)


KV = """

ScreenManager:
    sld1:s1
    btn1:btn1 
    Screen:
        name: "scr1"
        BoxLayout:
            orientation:"vertical"
            Label:
                id:my_label
                text: 'Time value is %s s' % int(s1.value) if s1.value else 'Slider not set'
            Slider:
                id:s1
                min:1
                max:30
                setp:1
                on_value:app.do_setting(*args)
            BoxLayout:
                Button:
                    id:btn1
                    text: "START"
                    on_release: root.current = "scr2"
                Button:
                    id:btn1
                    text: "Exit"
                    on_press: app.stop()                
    Screen:
        name: "scr2"
        FloatLayout:
            MyCarousel:
            Button:
                size_hint:None,None
                background_color: 0, 0, 0, 0
                #text: "Back"
                on_release: root.current = "scr1"

"""
    
class CarouselApp(App):
    def build(self):
        return Builder.load_string(KV)

    def do_setting(self,*args):
        global slider_time
        slider_time=int(args[1])
        print(str(slider_time))

CarouselApp().run()
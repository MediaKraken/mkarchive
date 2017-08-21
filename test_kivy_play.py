# import kivy
# from kivy.app import App
# from kivy.uix.behaviors import CoverBehavior
# from kivy.uix.video import Video
#
#
# class MyApp(App):
#     def build(self):
#         #video = Video(source='/home/spoot/github/MediaKraken_Deployment/A.mkv')
#         video = Video(source='/home/spoot/github/MediaKraken/MediaKraken_Deployment/theater/test.webm')
#         video.state='play'
#         video.options = {'eos': 'loop'}
#         video.allow_stretch=True
#         return video
#
# if __name__ == '__main__':
#     MyApp().run()


import kivy
kivy.require('1.2.0')

from sys import argv
from os.path import dirname, join
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer


class VideoPlayerApp(App):

    def build(self):
        if len(argv) > 1:
            filename = argv[1]
        else:
            curdir = dirname(__file__)
            filename = join(curdir, 'softboy.avi')
        return VideoPlayer(source=filename, state='play')


if __name__ == '__main__':
    VideoPlayerApp().run()
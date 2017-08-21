from __future__ import absolute_import, division, print_function, unicode_literals
import os
import os.path
import socket
import json
from functools import partial
from common import common_network_mpv



import subprocess

subprocess.Popen(['mpv', '--input-ipc-server=mpvsock'])

# --input-unix-socket

# '/home/spoot/github/MediaKraken/MediaKraken_Deployment/theater//test.webm'
mpv = common_network_mpv.Mpv('mpvsock')

# # General form
# mpv.[command]([args, ...])
#
# # Examples
# mpv.seek(42, 'absolute') # Go to 42th second of the video
# mpv.seek(42) # Go to t + 42 secs
# mpv.stop()   # Stop playback
#mpv.loadfile('test.webm') # Load a file and play it

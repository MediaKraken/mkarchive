'''
  Copyright (C) 2018 Quinn D Granfor <spootdev@gmail.com>

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  version 2, as published by the Free Software Foundation.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  General Public License version 2 for more details.

  You should have received a copy of the GNU General Public License
  version 2 along with this program; if not, write to the Free
  Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.
'''

from __future__ import absolute_import, division, print_function, unicode_literals

import common_network_vm_proxmox
import logging  # pylint: disable=W0611

JENKINS_BUILD_VIM = 'mkdocker'

# create prox class instance to use
PROX_CONNECTION = common_network_vm_proxmox.CommonNetworkProxMox('pve', 'root@pam',
                                                                 'jenkinsbuild')

# build the container if doesn't already exist
lxc_dict = {}
for lxc_server in PROX_CONNECTION.com_net_prox_node_lxc_list('pve')['data']:
    lxc_dict[lxc_server['name']] = (lxc_server['vmid'], lxc_server['status'])
print('lxc: %s' % lxc_dict)

if JENKINS_BUILD_VIM in lxc_dict:
    print('status: %s' % str(lxc_dict[JENKINS_BUILD_VIM][1]))
    # make sure it's started
    if lxc_dict[JENKINS_BUILD_VIM] != 'running':
        # start up the vm
        print('start vim: %s' % lxc_dict[JENKINS_BUILD_VIM][0])
        print(PROX_CONNECTION.com_net_prox_node_lxc_start(
            'pve', lxc_dict[JENKINS_BUILD_VIM][0]))
else:
    print('create JENKINS_BUILD_VIM')
    print(PROX_CONNECTION.com_net_prox_node_lxc_create('pve', JENKINS_BUILD_VIM, 4096,
                                                       'ZFS_Images:vztmpl/alpine-3.7-default_20171211_amd64.tar.gz',
                                                       'ZFS_VM', 'alpine', 8, 'metaman'))

# keep an eye on task and see when its completed
# while node.tasks(taskid).status()['status'] == 'running':
#        time.sleep(1)

# check status of build vm
for vm_server in PROX_CONNECTION.com_net_prox_node_qemu_list('pve')['data']:
    if vm_server['name'] == JENKINS_BUILD_VIM:
        if vm_server['status'] == 'stopped':
            # start up the vm
            PROX_CONNECTION.com_net_prox_node_qemu_start('pve', vm_server['vmid'])
            time.sleep(120)  # wait for box to boot
        break

# connect to server via ssh
SSH_BUILD = common_network_ssh.CommonNetworkSSH(JENKINS_BUILD_VIM,
                                                'root', 'metaman')

# begin build of deps
#SSH_BUILD.com_net_ssh_run_sudo_command('su -')
# TODO add my repo    /etc/apk/repositories
SSH_BUILD.com_net_ssh_run_command('apk update')
SSH_BUILD.com_net_ssh_run_command('apk add git alpine-sdk linux-headers postgresql-dev'
                                  ' python-dev libffi-dev openldap-dev jpeg-dev libxml2-dev'
                                  ' libxslt-dev musl-dev net-snmp-dev openldap-dev'
                                  ' portaudio-dev mesa-dev gstreamer-dev sdl2-dev sdl2_ttf-dev'
                                  ' sdl2_image-dev sdl2_mixer-dev py-pip docker')
SSH_BUILD.com_net_ssh_run_command('rc-update add docker default')
SSH_BUILD.com_net_ssh_run_command('service docker start')
SSH_BUILD.com_net_ssh_run_command('cd /home/metaman')
SSH_BUILD.com_net_ssh_run_command(
    'git clone https://github.com/MediaKraken/MediaKraken_Deployment')
SSH_BUILD.com_net_ssh_run_command('cd MediaKraken_Deployment')
SSH_BUILD.com_net_ssh_run_command('pip install docker-compose')
SSH_BUILD.com_net_ssh_run_command('pip install -r ./testing/pip_requirements.txt')
SSH_BUILD.com_net_ssh_run_command(
    'pip install -r ./docker/alpine/ComposeMediaKrakenMetadata/requirements.txt')
SSH_BUILD.com_net_ssh_run_command(
    'pip install -r ./docker/alpine/ComposeMediaKrakenServer/requirements.txt')
SSH_BUILD.com_net_ssh_run_command(
    'pip install -r ./docker/alpine/ComposeMediaKrakenWebServer/requirements.txt')
SSH_BUILD.com_net_ssh_close()

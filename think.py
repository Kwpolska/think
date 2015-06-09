#!/usr/bin/python
# -*- encoding: utf-8 -*-
# think v0.1.2
# Terminal Think Music
# Copyright © 2015, Chris Warrick.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions, and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions, and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the author of this software nor the names of
#    contributors to this software may be used to endorse or promote
#    products derived from this software without specific prior written
#    consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
    think
    ~~~~~

    Terminal Think Music

    :Copyright: © 2015, Chris Warrick.
    :License: BSD (see /LICENSE).
"""

import os
import sys
import subprocess
import time

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

__title__ = 'think'
__version__ = '0.1.2'
__author__ = 'Chris Warrick'
__license__ = '3-clause BSD'
__docformat__ = 'restructuredtext en'

try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = open(os.devnull, 'wb')


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    confhome = os.getenv('XDG_CONFIG_HOME')
    if confhome is None:
        confhome = os.path.expanduser('~/.config/')

    thinkconf = os.path.join(confhome, 'think.conf')

    if os.path.exists(thinkconf):
        parser = configparser.RawConfigParser()
        parser.read(thinkconf)
        playcommand = parser.get('Think', 'command')
        audiofile = parser.get('Think', 'file')
        behavior = parser.get('Think', 'behavior')
    else:
        print("FATAL: no ~/.config/think.conf found.")
        return 255
    if args:
        ap = None
        mp = subprocess.Popen(args, stdin=sys.stdin)
        while mp.poll() is None:
            if not ap or ap.poll() is not None:
                ap = subprocess.Popen([playcommand, audiofile],
                                      stdin=DEVNULL,
                                      stdout=DEVNULL, stderr=DEVNULL)
            time.sleep(0.1)

        if behavior == 'stop':
            ap.terminate()
        elif behavior == 'wait':
            ap.wait()
        elif behavior == 'return':
            pass
        return mp.returncode
    else:
        print("FATAL: no arguments provided")
        return 255

if __name__ == '__main__':
    try:
        exit(main())
    except KeyboardInterrupt:
        exit(130)

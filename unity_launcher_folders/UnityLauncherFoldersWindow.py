# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2014 Anton Sukhovatkin <laucnherfolders@exceptionfound.com>
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 3, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('unity_launcher_folders')

from unity_launcher_folders_lib import Window
from unity_launcher_folders.AboutUnityLauncherFoldersDialog import AboutUnityLauncherFoldersDialog
from unity_launcher_folders.PreferencesUnityLauncherFoldersDialog import PreferencesUnityLauncherFoldersDialog

# See unity_launcher_folders_lib.Window.py for more details about how this class works
class UnityLauncherFoldersWindow(Window):
    __gtype_name__ = "UnityLauncherFoldersWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(UnityLauncherFoldersWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutUnityLauncherFoldersDialog
        self.PreferencesDialog = PreferencesUnityLauncherFoldersDialog

        # Code for other initialization actions should be added here.


# Laang - Ubot
# Copyright (C) 2024 @LaangYB
#
# This file is a part of <https://github.com/LaangYB/LaangUbot>
# Please read the GNU Affero General Public License in
# <https://www.github.com/LaangYB/LaangUbot/blob/main/LICENSE/>.
#
# FROM LaangUbot <https://github.com/LaangYB/LaangUbot>
# t.me/ybtraviss & t.me/ybtraviss

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import logging
import os
import importlib
from config import *
from git import Repo
from pyLnnggg import PyrogramYB
from pyLnnggg.Clients import *
from pyLnnggg.config import Var
from pyLnnggg.pyrogram import eod, eor

# Initialize variables and constants
flood = {}
OLD_MSG = {}
repo = Repo()
branch = repo.active_branch.name  # Get the branch name
yins = PyrogramYB()
var = Var()
hndlr = [f"{var.HNDLR[i]}" for i in range(6)]
logs = logging.getLogger(__name__)

# Cache and font file paths
file = './cache/'
cache = "cache/{}.png"
cache_thumb = "cache/thumb{}.png"
font = "assets/font.ttf"
font2 = "assets/font2.ttf"

# Load all plugins from the 'plugins' folder automatically
plugin_folder = os.path.join(os.path.dirname(__file__), "plugins")

# Iterate over all Python files in the 'plugins' directory
for filename in os.listdir(plugin_folder):
    if filename.endswith(".py") and filename != "__init__.py":
        # Import the plugin module dynamically
        module_name = f"plugins.{filename[:-3]}"
        try:
            importlib.import_module(module_name)
            logs.info(f"Loaded plugin: {module_name}")
        except Exception as e:
            logs.error(f"Failed to load plugin {module_name}: {e}")

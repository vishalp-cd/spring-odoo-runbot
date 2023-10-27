# -*- coding: utf-8 -*-

from . import batch
from . import branch
from . import build
from . import build_config
from . import build_config_codeowner
from . import build_error
from . import bundle
from . import codeowner
from . import commit
from . import custom_trigger
from . import database
from . import dockerfile
from . import event
from . import host
from . import ir_cron
from . import ir_ui_view
from . import project
from . import repo
from . import res_config_settings
from . import res_users
from . import runbot
from . import team
from . import upgrade
from . import user
from . import version

# those imports have to be at the end otherwise the sql view cannot be initialised
from . import build_stat
from . import build_stat_regex

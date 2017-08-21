'''
  Copyright (C) 2016 Quinn D Granfor <spootdev@gmail.com>

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
import logging # pylint: disable=W0611
import json
import uuid
from common import common_config_ini
from common import common_logging
from common import common_metadata_tvmaze
from common import common_signal



# grab updated show list with epoc data
tvmaze = common_metadata_tvmaze.CommonMetadatatvmaze()
result = tvmaze.com_meta_tvmaze_show_updated()
logging.info('tvmaze update: ', result)
#for show_list_json in result:
result = json.loads(result)
for tvmaze_id, tvmaze_time in result.items():
    logging.info("id: %s", tvmaze_id)



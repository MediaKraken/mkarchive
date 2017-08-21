from __future__ import absolute_import, division, print_function, unicode_literals
import locale
locale.setlocale(locale.LC_ALL, '')
import logging # pylint: disable=W0611
import datetime
import uuid
import json
import subprocess
import os
import sys
sys.path.append('..')
sys.path.append('../..')
from common import common_string
import database as database_base
import natsort
import collections
import psycopg2

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

db_connection = database_base.MKServerDatabase()
db_connection.db_open(db_build=True) # if true will connect to my test db

# drop all cron
db_connection.db_query('delete from mm_cron')
# create task tables
db_connection.db_query('CREATE TABLE IF NOT EXISTS mm_task (mm_task_guid uuid'
                       ' CONSTRAINT mm_task_guid_pk PRIMARY KEY, mm_task_name text, mm_task_description text,'
                       ' mm_task_enabled bool, mm_task_schedule text, mm_task_last_run timestamp,'
                       ' mm_task_file_path text, mm_task_json jsonb)')
# create base task entries
base_task = [
    # metadata
    ('Anime', 'Match anime via Scudlee data', '/mediakraken/subprogram_match_anime_id_scudlee.py',
     {'exchange_key': 'mkque_metadata_ex', 'route_key': 'Z', 'task': 'anime'}),
    ('Collections', 'Create and update collection(s)',
     '/mediakraken/subprogram_metadata_update_create_collections.py',
     {'exchange_key': 'mkque_metadata_ex', 'route_key': 'themoviedb', 'task': 'collection'}),
    ('Create Chapter Image', 'Create chapter images for all media',
     '/mediakraken/subprogram_create_chapter_images.py',
     {'exchange_key': 'mkque_ex', 'route_key': 'mkque', 'task': 'chapter'}),
    ('Roku Thumb', 'Generate Roku thumbnail images', '/mediakraken/subprogram_roku_thumbnail_generate.py',
     {'exchange_key': 'mkque_ex', 'route_key': 'mkque', 'task': 'rokuthumbnail'}),
    ('Schedules Direct', 'Fetch TV schedules from Schedules Direct',
     '/mediakraken/subprogram_schedules_direct_updates.py',
     {'exchange_key': 'mkque_metadata_ex', 'route_key': 'schedulesdirect', 'task': 'update'}),
    ('Subtitle', 'Download missing subtitles for media', '/mediakraken/subprogram_subtitle_downloader.py',
     {'exchange_key': 'mkque_metadata_ex', 'route_key': 'Z', 'task': 'subtitle'}),
    ('The Movie Database', 'Grab updated movie metadata', '/mediakraken/subprogram_metadata_tmdb_updates.py',
     {'exchange_key': 'mkque_metadata_ex', 'route_key': 'themoviedb', 'task': 'update'}),
    ('TheTVDB Update', 'Grab updated TheTVDB metadata', '/mediakraken/subprogram_metadata_thetvdb_updates.py',
     {'exchange_key': 'mkque_metadata_ex', 'route_key': 'thetvdb', 'task': 'update'}),
    ('TVmaze Update', 'Grab updated TVmaze metadata', '/mediakraken/subprogram_metadata_tvmaze_updates.py',
     {'exchange_key': 'mkque_metadata_ex', 'route_key': 'tvmaze', 'task': 'update'}),
    ('Trailer', 'Download new trailers', '/mediakraken/subprogram_metadata_trailer_download.py',
     {'exchange_key': 'mkque_metadata_ex', 'route_key': 'Z', 'task': 'trailer'}),
    # normal subprograms
    ('Backup', 'Backup Postgresql DB', '/mediakraken/subprogram_postgresql_backup.py',
     {'exchange_key': 'mkque_ex', 'route_key': 'mkque', 'task': 'dbbackup'}),
    ('DB Vacuum', 'Postgresql Vacuum Analyze all tables', '/mediakraken/subprogram_postgresql_vacuum.py',
     {'exchange_key': 'mkque_ex', 'route_key': 'mkque', 'task': 'dbvacuum'}),
    ('iRadio Scan', 'Scan for iRadio stations', '/mediakraken/subprogram_iradio_channels.py',
     {'exchange_key': 'mkque_ex', 'route_key': 'mkque', 'task': 'iradio'}),
    ('Media Scan', 'Scan for new media', '/mediakraken/subprogram_file_scan.py',
     {'exchange_key': 'mkque_ex', 'route_key': 'mkque', 'task': 'scan'}),
    ('Sync', 'Sync/Transcode media', '/mediakraken/subprogram_sync.py',
     {'exchange_key': 'mkque_ex', 'route_key': 'mkque', 'task': 'sync'}),
]
for base_item in base_task:
    db_connection.db_task_insert(base_item[0], base_item[1], False, 'Days 1',
                                 psycopg2.Timestamp(1970, 1, 1, 0, 0, 1), base_item[2],
                                 json.dumps(base_item[3]))
db_connection.db_version_update(9)

db_connection.db_close()

# Copyright 2015 The Emscripten Authors.  All rights reserved.
# Emscripten is available under two separate licenses, the MIT license and the
# University of Illinois/NCSA Open Source License.  Both these licenses can be
# found in the LICENSE file.

import logging
import os

TAG = 'version_1'
HASH = '99bee75beb662f8520bbb18ad6dbf8590d30eb3a7360899f0ac4764ca72fe8013da37c9df21e525f9d2dc5632827d4b4cea558cbc938e7fbed0c41a29a7a2dc5'

deps = ['ogg']


def needed(settings):
  return settings.USE_VORBIS


def get(ports, settings, shared):
  ports.fetch_project('vorbis', 'https://github.com/emscripten-ports/vorbis/archive/' + TAG + '.zip', 'Vorbis-' + TAG, sha512hash=HASH)

  def create(final):
    logging.info('building port: vorbis')
    source_path = os.path.join(ports.get_dir(), 'vorbis', 'Vorbis-' + TAG)
    ports.install_header_dir(os.path.join(source_path, 'include', 'vorbis'))
    dest_path = ports.clear_project_build('vorbis')
    ports.build_port(os.path.join(source_path, 'lib'), final, dest_path,
                     includes=[os.path.join(dest_path, 'include')],
                     flags=['-sUSE_OGG=1'],
                     exclude_files=['psytune', 'barkmel', 'tone', 'misc'])

  return [shared.Cache.get_lib('libvorbis.a', create)]


def clear(ports, settings, shared):
  shared.Cache.erase_lib('libvorbis.a')


def process_dependencies(settings):
  settings.USE_OGG = 1


def process_args(ports):
  return []


def show():
  return 'vorbis (USE_VORBIS=1; zlib license)'

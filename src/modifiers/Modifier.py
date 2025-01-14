# Copyright 2021 Google Inc. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os

from . import Logger

class Modifier:
  wrapper = None

  def __init__(self, wrapper):
    Logger().log("Started " + type(self).__name__, 3)
    self.wrapper = wrapper

  def run(self):
    self._mv2() if self.wrapper.getManifestVersion() == 2 else self._mv3()

  def writeManifest(self):
    manifest_file = self.wrapper.destination + '/manifest.json'
    if not os.path.exists(manifest_file):
      return
    if os.path.exists(manifest_file):
      with open(manifest_file, 'w') as outfile:
        json.dump(self.wrapper.manifest, outfile, indent=2)

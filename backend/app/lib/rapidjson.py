# BEX Backend
# https://github.com/forkdelta/backend-replacement
# Copyright (C) 2018, Futjrn Golem & BEX Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# rapidjson proxy
# Used for python-socketio / python-engineio, where rapidjson is _almost_
# a drop-in replacement for stdlib json, except for an incompatible (and
# inconsequential) separators key
import rapidjson

def load(*args, **kwargs):
    if "separators" in kwargs:
        del kwargs["separators"]
    return rapidjson.load(*args, **kwargs)

def loads(*args, **kwargs):
    if "separators" in kwargs:
        del kwargs["separators"]
    return rapidjson.loads(*args, **kwargs)

def dump(*args, **kwargs):
    if "separators" in kwargs:
        del kwargs["separators"]
    return rapidjson.dump(*args, **kwargs)

def dumps(*args, **kwargs):
    if "separators" in kwargs:
        del kwargs["separators"]
    return rapidjson.dumps(*args, **kwargs)

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


from web3 import Web3


def coerce_to_int(value):
    '''
    Normalizes event values to integers, since WS API returns numbers, and HTTP
     API returns hexstr.
    '''
    if isinstance(value, int):
        return value
    return Web3.toInt(hexstr=value)


def parse_insert_status(status_string):
    '''
    Returns (command, oid, count) tuple from INSERT status string.
    cf. https://stackoverflow.com/q/3835314/215024
    '''
    command, oid, count = status_string.split(" ")
    return (command, oid, int(count))

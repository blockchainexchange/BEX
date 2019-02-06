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

from os import environ

HTTP_PROVIDER_URL = environ.get("HTTP_PROVIDER_URL")
WS_PROVIDER_URL = environ.get("WS_PROVIDER_URL")

ALLOWED_ORIGIN_SUFFIXES = environ.get("ALLOWED_ORIGIN_SUFFIXES",
                                      "localhost").split(",")

ED_CONTRACT_ADDR = '0x8d12a197cb00d4747a1fe03395095ce2a5cc6819'
with open('etherdelta.abi.json') as f:
    import json
    ED_CONTRACT_ABI = json.load(f)
ED_WS_SERVERS = [
    "wss://socket01.etherdelta.com/socket.io/?EIO=3&transport=websocket",
    "wss://socket02.etherdelta.com/socket.io/?EIO=3&transport=websocket",
    "wss://socket03.etherdelta.com/socket.io/?EIO=3&transport=websocket",
    "wss://socket04.etherdelta.com/socket.io/?EIO=3&transport=websocket",
    "wss://socket05.etherdelta.com/socket.io/?EIO=3&transport=websocket",
    "wss://socket06.etherdelta.com/socket.io/?EIO=3&transport=websocket",
]

POSTGRES_HOST = "postgres"
POSTGRES_DB = environ.get("POSTGRES_DB")
POSTGRES_USER = environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD")

FRONTEND_CONFIG_FILE = "https://forkdelta.app/config/main.json"
STOPPED_TOKENS = (
    "0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0",  # EOS: https://block.one/news/community-reminder-eos-token-registration-and-freeze/
    "0x7e9e431a0b8c4d532c745b1043c7fa29a48d4fba",  # eosDAC: https://twitter.com/eosdac/status/1002657571197673475?lang=en
    "0xa5fd1a791c4dfcaacc963d4f73c6ae5824149ea7",  # JNT: https://t.me/jibrel_network/129713
)

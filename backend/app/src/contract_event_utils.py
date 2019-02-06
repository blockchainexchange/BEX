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


from time import time

block_timestamp_cache = {}


def block_timestamp(web3, block_number):
    global block_timestamp_cache
    if not isinstance(block_number,
                      int) or block_number not in block_timestamp_cache:
        block = web3.eth.getBlock(block_number)
        if block != None:
            block_timestamp_cache[block_number] = block["timestamp"]
        else:
            # Race condition seen with geth where the WS-RPC returns an event from a
            # new block, but this block is not yet available through the HTTP-RPC API.
            # => Assume current time, but don't cache that in block_timestamp_cache.
            return time()

    return block_timestamp_cache[block_number]

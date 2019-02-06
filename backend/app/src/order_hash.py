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


from ..config import ED_CONTRACT_ADDR
from decimal import Decimal
from eth_utils import add_0x_prefix, remove_0x_prefix
from hashlib import sha256
from web3 import Web3
from web3.utils.encoding import hex_encode_abi_type, to_bytes


def sha256_like_solidity(type_value_tuples):
    hex_string = add_0x_prefix(''.join(
        remove_0x_prefix(hex_encode_abi_type(abi_type, value))
        for abi_type, value in type_value_tuples))

    return add_0x_prefix(sha256(to_bytes(hexstr=hex_string)).hexdigest())


def make_order_hash(order, contract_addr=ED_CONTRACT_ADDR):
    hash_parts = [('address', contract_addr), ('address', order["tokenGet"]),
                  ('uint256', Web3.toInt(Decimal(order["amountGet"]))),
                  ('address',
                   order["tokenGive"]), ('uint256',
                                         Web3.toInt(
                                             Decimal(order["amountGive"]))),
                  ('uint256', Web3.toInt(Decimal(
                      order["expires"]))), ('uint256',
                                            Web3.toInt(
                                                Decimal(order["nonce"])))]

    return sha256_like_solidity(hash_parts)

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


from asyncio import iscoroutinefunction
from functools import partial
from web3.utils.filters import construct_event_filter_params
from web3.utils.events import get_event_data


class WebsocketFilterSet:
    def __init__(self, contract):
        self.contract = contract
        self.handlers = {}
        self.topic_to_event = {}
        self.topic_filters = []

    async def deliver(self, topic_hash, payload):
        if topic_hash in self.handlers:
            if iscoroutinefunction(self.handlers[topic_hash]):
                await self.handlers[topic_hash](payload)
            else:
                self.handlers[topic_hash](payload)

    def on_event(self, event_name, handler_func=None):
        def decorator(handler_func):
            event_abi = self.contract._find_matching_event_abi(event_name, {})
            _, event_filter_params = construct_event_filter_params(
                event_abi, contract_address=self.contract.address)

            if iscoroutinefunction(handler_func):

                async def decorated(payload):
                    event_data = get_event_data(event_abi, payload)
                    return await handler_func(self.contract, event_name,
                                              event_data)
            else:

                def decorated(payload):
                    event_data = get_event_data(event_abi, payload)
                    return handler_func(self.contract, event_name, event_data)

            self.topic_filters.append(event_filter_params)
            self.handlers[event_filter_params["topics"][0]] = decorated

            return decorated

        if handler_func is None:
            return decorator
        return decorator(handler_func)

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


from gevent import monkey
monkey.patch_all(
)  # cf. http://huey.readthedocs.io/en/latest/troubleshooting.html?highlight=monkey

from ..app import App
from ..tasks.update_order import update_order_by_signature, update_orders_by_maker_and_token

print("Huey is starting")
huey = App().huey

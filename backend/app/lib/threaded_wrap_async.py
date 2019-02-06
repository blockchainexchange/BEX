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


import asyncio
from functools import update_wrapper
import logging
from threading import get_ident, local

thread_local = local()  # get a dictionary that different per-thread contents


def threaded_wrap_async(wrapped):
    """
    Wraps an asyncio coroutine and produces a regular function that can be run
    in a thread.

    Internally, creates or sets an event loop for the thread,
    runs the async function using `run_until_complete`, and returns
    the result of the coroutine or raises an exception.

    Argument is a coroutine object.
    Returns a synchronous function.
    """

    def wrapper(*args, **kwargs):
        # Create an event loop if there isn't one already
        if not hasattr(thread_local, "loop"):
            thread_local.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(thread_local.loop)

        return thread_local.loop.run_until_complete(wrapped(*args, **kwargs))

    # Make wrapper look like the wrapped function (updating its name)
    update_wrapper(wrapper, wrapped)
    return wrapper

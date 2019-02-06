# ![BlockchainExchangelogo](Brand-Assets/50294534_2240624106216262_5489838300237660160_n.png) Blockchain Exchange Backend



This repository hosts the source code of the BEX backend. The backend provides off-chain orderbook functionality and an API to get a filtered view of Ethereum blockchain events on an [EtherDelta-like contract](https://www.reddit.com/r/EtherDelta/comments/6kdiyl/smart_contract_overview/).

Best way to learn about a system is to read the source code. Start with a look at [docker-compose.yml](docker-compose.yml).

## API

For information and documentation on BEX API, look here: https://github.com/blockchainexchange/backend-replacement/tree/master/docs/api

## Developing

### Setting up a development environment
Requirements:
* Some sort of shell environment
* A reasonably recent version of Docker (>= 17.06, ideally 17.12)
* docker-compose (= 1.18)
* Basic familiarity with Docker keywords: image, container (https://docs.docker.com/get-started/#docker-concepts)

Setup:
1. Clone the repo (git clone https://github.com/blockchainexchange/backend-replacement.git)
2. Navigate to the root of the working copy, where the README file is.
3. Copy `default.env` file to `.env` in root.
4. Uncomment the `COMPOSE_FILE=` line in `.env` to enable mounting of working copy code into the containers.
4. Build a Docker image containing our backend code: `docker-compose build contract_observer`
5. Create the database and migrate it to the latest schema: `docker-compose run contract_observer alembic upgrade head`
6. Run the backend systems: `docker-compose up`. You can shut everything down with Ctrl+C at any time.

Tips:
* There are multiple containers running our backend code: `contract_observer`, `etherdelta_observer`, `websocket_server`.
* Running `docker-compose build <service-name>` for any of the above builds the same image.
* `docker-compose build contract_observer` builds an image, copying the code and installing Python libraries in our dependencies.
  You have to rebuild any time the dependencies change; however, in development, code in the working copy is mounted into the container,
  so it's enough to restart the container (with `docker-compose restart <service-name>`) to apply changes for a given service.
* You can inspect the list of currently running containers with `docker-compose ps`.



## License

Copyright (C) 2018, Futjrn Golem and  Blockchain Exchange Contributors

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

See the full [license.](LICENSE)

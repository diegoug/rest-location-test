# Rest Location Test

API django rest framework to ge vehicle user location

## Dependencies
To work with Rest Location Test it is necessary to have docker and Compose installed in versions that can work with the YAML compose configuration file in version two.

- [Docker compose file V2 reference](https://docs.docker.com/compose/compose-file/#version-2)
- [Docker Engine 20.10.3+](https://docs.docker.com/engine/installation/) - Installation guide in Linux
- [Compose 1.27.4+](https://docs.docker.com/compose/install/#/install-using-pip) - Installation guide using PIP

## Install development enviroment
* [Clone the repository](#clone-the-repository)
* [Build development enviroment](#build-development-enviroment)
* [Create network](#create-network)
* [Start development](#start-development)
* [Load SQL](#load-sql)
* [Access](#access)
* [Stop development](#stop-development)

### Clone the repository
```
$ cd Documents # optional
$ git clone git@github.com:diegoug/rest-location-test.git
$ cd rest-location-test
```
[Back to Install development enviroment](#install-development-enviroment)

### Build development enviroment
```
$ cd rest-location-test
$ make build-development
```
[Back to Install development enviroment](#install-development-enviroment)

### Create network
```
$ cd rest-location-test
$ make create-network
```
[Back to Install development enviroment](#install-development-enviroment)

### Start development
```
$ cd rest-location-test
$ make start-development
```
[Back to Install development enviroment](#install-development-enviroment)

### Stop development
```
$ cd rest-location-test
$ make stop-development
```
[Back to Install development enviroment](#install-development-enviroment)

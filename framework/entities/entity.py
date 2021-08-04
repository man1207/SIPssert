#!/usr/bin/env python
##
## TODO: update project's name
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/>.
##

class Entity():

    entity_default_mount_point = "/home"
    entity_default_image = None

    def __init__(self, test_dir, config, controller):

        self.controller = controller
        self.config = config
        self.test_dir = test_dir
        self.container = None

        if "name" in self.config:
            self.name = self.config["name"]
        else:
            self.name = self.__class__.__name__

        if "image" in self.config:
            self.image = self.config["image"]
        else:
            self.image = entity_default_image

        if "ip" in self.config:
            self.ip = self.config["ip"]
        else:
            self.ip = None

        if "config_file" in self.config:
            self.config_file = self.config["config_file"]
        else:
            self.config_file = None

        if self.image is None:
            raise Exception("entity {} does not have an image available".
                    format(self.name))

    def __str__(self):
        return self.name

    def get_entity_args(self):
        return []

    def get_ports(self):
        r = {}
        if "ports" in self.config:
            for p in self.config["ports"]:
                port, proto = p.split("/")
                r[p] = port

        return r

    def get_args(self):
        if "extra_params" in self.config:
            extra_params = self.config["extra_params"].split(" ")
        else:
            extra_params = []
        return self.get_entity_args() + extra_params

    def get_mount_point(self):
        if "mount_point" in self.config:
            return self.config["mount_point"]
        else:
            return self.entity_default_mount_point

    def run(self):
        print("name: {}".format(self))
        print("mount point: {}".format(self.get_mount_point()))
        print("ports: {}".format(self.get_ports()))
        print("args: {}".format(self.get_args()))
        print("image: {}".format(self.image))

        volumes = { self.test_dir: {
            "bind": self.get_mount_point(),
            "mode": "ro"
            }}
        ports = self.get_ports()

        self.container = self.controller.docker.containers.create(
                self.image,
                self.get_args(),
                detach=True,
                volumes=volumes,
                ports=ports)
        if self.ip:
            self.controller.docker.networks.get("controllerNetwork").\
                    connect(self.container, ipv4_address = self.ip)
        self.container.start()

    def stop(self):
        self.container.stop()

    def remove(self):
        self.container.remove()
        self.container = None

    def __del__(self):
        if self.container:
            self.stop()
            self.remove()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

#!/usr/bin/env python
##
## This file is part of the SIPssert Testing Framework project
## Copyright (C) 2023 OpenSIPS Solutions
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

from sipssert.task import Task

class GenericTask(Task):

    """Class that implements a generic task"""
    pass

    def get_task_env(self):

        env_dict = {}

        if "env" in self.config:
            env_dict = self.config["env"]

        return env_dict
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

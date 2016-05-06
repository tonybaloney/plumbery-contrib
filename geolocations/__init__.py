# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os

__all__ = ['PlumberyGeolocation']


class PlumberyGeolocations(object):
    """
    Geolocation information

    """

    def get_city(self, locationId):
        """
        Retrieves the city of some location

        :param locationId: the MCP identifier, e.g., 'EU6'
        :type locationId: ``str``

        :return:  the city, e.g., 'Amsterdam' or 'Singapore'
        :rtype: ``str``

        """

        cities = {
            'AP3': 'Singapore',
            'AP4': 'Tokyo',
            'AP5': 'Hong Kong',
            'AU9': 'Sydney',
            'AU10': 'Melbourne',
            'AU11': 'Hamilton',
            'EU6': 'Frankfurt',
            'EU7': 'Amsterdam',
            'EU8': 'London',
            'NA9': 'Ashburn',
            'NA12': 'Santa Clara',
        }

        if locationId is None or locationId not in cities.keys():
            return '*unknown*'

        return cities[locationId]

    def get_coordinates(self, locationId):
        """
        Retrieves coordinates of some location

        :param locationId: the MCP identifier, e.g., 'EU6'
        :type locationId: ``str``

        :return:  latitude and longitude of the current location
        :rtype: ``list``

        """

        coordinates = {
            'AP3': [1.2896700, 103.8500700],
            'AP4': [35.6895000, 139.6917100],
            'AP5': [22.2855200, 114.1576900],
            'AU9': [-33.8678500, 151.2073200],
            'AU10': [-37.8140000, 144.9633200],
            'AU11': [-37.7833300, 175.2833300],
            'EU6': [50.1155200, 8.6841700],
            'EU7': [52.3740300, 4.8896900],
            'EU8': [51.5085300, -0.1257400],
            'NA9': [39.0437200, -77.4874900],
            'NA12': [37.3541100, -121.9552400],
        }

        if locationId is None or locationId not in coordinates.keys():
            return None

        return coordinates[locationId]

#    (c) Copyright 2017-2018 SUSE LLC
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from networking_generic_switch.devices import netmiko_devices


class HpeComware(netmiko_devices.NetmikoSwitch):
    ADD_NETWORK = (
        'vlan {segmentation_id}',
    )

    DELETE_NETWORK = (
        'undo vlan {segmentation_id}',
    )

    PLUG_PORT_TO_NETWORK = (
        'interface {port}',
        'service-instance {segmentation_id}',
        'encapsulation untagged',
        'xconnect vsi {segmentation_id} access-mode ethernet',
    )

    DELETE_PORT = (
        'interface {port}',
        'undo service-instance {segmentation_id}',
    )

    ENABLE_PORT = (
        'interface {port}',
        'undo shutdown'
    )

    DISABLE_PORT = (
        'interface {port}',
        'shutdown'
    )

    def disable_port(self, port):
        cmds = self._format_commands(self.DISABLE_PORT, port=port)
        return self.send_commands_to_device(cmds)

    def enable_port(self, port):
        cmds = self._format_commands(self.ENABLE_PORT, port=port)
        return self.send_commands_to_device(cmds)

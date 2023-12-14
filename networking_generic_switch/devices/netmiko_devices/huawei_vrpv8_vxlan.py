from networking_generic_switch.devices import netmiko_devices


class Huawei(netmiko_devices.NetmikoSwitch):
    """For Huawei Next-Generation Network Operating System VRP V8."""
    ADD_NETWORK = (
        'vlan {segmentation_id}',
        'commit',
    )

    DELETE_NETWORK = (
        'undo vlan {segmentation_id}',
        'commit',
    )

    PLUG_PORT_TO_NETWORK = (
        'interface {port}.{segmentation_id} mode l2',
        'encapsulation untag',
        'bridge-domain {segmentation_id}',
        'commit',
        'interface Nve1',
        'vni {segmentation_id} head-end peer-list protocol bgp',
        'commit',
    )

    DELETE_PORT = (
        'undo interface {port}.{segmentation_id}',
        'commit',
        'interface Nve1',
        'undo vni {segmentation_id} head-end peer-list protocol bgp',
        'commit',
    )

    ENABLE_PORT = (
        'interface {port}',
        'undo shutdown',
        'commit',
    )

    DISABLE_PORT = (
        'interface {port}',
        'shutdown',
        'commit',
    )

    def disable_port(self, port):
        cmds = self._format_commands(self.DISABLE_PORT, port=port)
        return self.send_commands_to_device(cmds)

    def enable_port(self, port):
        cmds = self._format_commands(self.ENABLE_PORT, port=port)
        return self.send_commands_to_device(cmds)

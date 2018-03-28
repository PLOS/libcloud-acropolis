from libcloud.compute.base import Node, NodeDriver, NodeImage, NodeSize
from libcloud.compute.types import Provider


class AcropolisNode(Node):
    pass


class AcropolisNodeSize(NodeSize):
    pass


class AcropolisNodeDriver(NodeDriver):
    """
    Nutanix Acropolis Hypervisor (AHV) node driver

    """
    type = Provider.DUMMY
    name = 'Acropolis'
    website = 'https://www.nutanix.com/products/acropolis/'

    NODE_STATE_MAP = {}

    def list_nodes(self):
        """
        List all nodes

        :return: list of node objects
        :rtype: ``list`` of :class:`AcropolisNode`
        """
        raise NotImplementedError

    def create_node(self, **kwargs):
        """
        Create an AHV virtual machine

        :keyword name: name of the virtual machine (required)
        :type name: ``str``

        :keyword image: image from which to clone new vm (required)
        :type image: :class:`NodeImage`

        :keyword size: size of the created node (required)
        :type size: :class:`AcropolisNodeSize`

        :return: newly created node
        :rtype: :class:`AcropolisNode`
        """
        raise NotImplementedError

    def reboot_node(self, node):
        """
        Reboot a node

        :param node: Node to be rebooted
        :type node: :class:`AcropolisNode`

        :return: True on success, else False
        :rtype: bool
        """
        raise NotImplementedError

    def destroy_node(self, node):
        """
        Destroy a node

        :param node: Node to be destroyed
        :type node: :class:`AcropolisNode`

        :return: True if successful, else False
        :rtype: bool
        """
        raise NotImplementedError

    def list_sizes(self):
        """
        Return a list of possible machine sizes

        :return: list of AcropolisNodeSize objects
        :rtype: ``list`` of :class:`AcropolisNodeSize`
        """
        raise NotImplementedError

    def list_locations(self):
        raise NotImplementedError('The AHV driver does not support multiple locations')



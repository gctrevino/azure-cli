# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from azure.cli.core.profiles import ResourceType

import azure.cli.command_modules.network._help  # pylint: disable=unused-import


class NetworkCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.sdk.util import CliCommandType
        network_custom = CliCommandType(operations_tmpl='azure.cli.command_modules.network.custom#{}')
        super(NetworkCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                    resource_type=ResourceType.MGMT_NETWORK,
                                                    custom_command_type=network_custom)
        self.module_name = __name__

    def load_command_table(self, args):
        from azure.cli.command_modules.network.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azure.cli.command_modules.network._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = NetworkCommandsLoader

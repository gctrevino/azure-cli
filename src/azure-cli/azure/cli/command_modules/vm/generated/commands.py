# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from ..generated._client_factory import cf_ssh_public_key
    vm_ssh_public_key = CliCommandType(
        operations_tmpl='azure.mgmt.compute.operations._ssh_public_keys_operations#SshPublicKeysOperations.{}',
        client_factory=cf_ssh_public_key)
    with self.command_group('sshkey', vm_ssh_public_key, client_factory=cf_ssh_public_key) as g:
        g.custom_command('list', 'sshkey_list')
        g.custom_show_command('show', 'sshkey_show')
        g.custom_command('create', 'sshkey_create')
        g.custom_command('update', 'sshkey_update')
        g.custom_command('delete', 'sshkey_delete', confirmation=True)

    from ..generated._client_factory import cf_gallery
    vm_gallery = CliCommandType(
        operations_tmpl='azure.mgmt.compute.operations._galleries_operations#GalleriesOperations.{}',
        client_factory=cf_gallery)
    with self.command_group('sig', vm_gallery, client_factory=cf_gallery) as g:
        g.custom_command('image-definition list-shared', 'sig_image_definition_list_shared')
        g.custom_command('image-version list-shared', 'sig_image_version_list_shared')
        g.custom_command('list-shared', 'sig_list_shared')
        g.custom_command('show-shared', 'sig_show_shared')

    from ..generated._client_factory import cf_shared_gallery_image
    vm_shared_gallery_image = CliCommandType(
        operations_tmpl='azure.mgmt.compute.operations._shared_gallery_images_operations#SharedGalleryImagesOperations.'
        '{}',
        client_factory=cf_shared_gallery_image)
    with self.command_group('sig image-definition', vm_shared_gallery_image,
                            client_factory=cf_shared_gallery_image) as g:
        g.custom_command('show-shared', 'sig_image_definition_show_shared', is_experimental=True)

    from ..generated._client_factory import cf_shared_gallery_image_version
    vm_shared_gallery_image_version = CliCommandType(
        operations_tmpl='azure.mgmt.compute.operations._shared_gallery_image_versions_operations#SharedGalleryImageVers'
        'ionsOperations.{}',
        client_factory=cf_shared_gallery_image_version)
    with self.command_group('sig image-version', vm_shared_gallery_image_version,
                            client_factory=cf_shared_gallery_image_version) as g:
        g.custom_command('show-shared', 'sig_image_version_show_shared', is_experimental=True)

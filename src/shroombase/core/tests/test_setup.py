# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from shroombase.core.testing import SHROOMBASE_CORE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that shroombase.core is properly installed."""

    layer = SHROOMBASE_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if shroombase.core is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'shroombase.core'))

    def test_browserlayer(self):
        """Test that IShroombaseCoreLayer is registered."""
        from shroombase.core.interfaces import (
            IShroombaseCoreLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IShroombaseCoreLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SHROOMBASE_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['shroombase.core'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if shroombase.core is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'shroombase.core'))

    def test_browserlayer_removed(self):
        """Test that IShroombaseCoreLayer is removed."""
        from shroombase.core.interfaces import \
            IShroombaseCoreLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IShroombaseCoreLayer,
            utils.registered_layers())

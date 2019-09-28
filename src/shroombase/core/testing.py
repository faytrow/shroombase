# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import shroombase.core


class ShroombaseCoreLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=shroombase.core)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'shroombase.core:default')


SHROOMBASE_CORE_FIXTURE = ShroombaseCoreLayer()


SHROOMBASE_CORE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SHROOMBASE_CORE_FIXTURE,),
    name='ShroombaseCoreLayer:IntegrationTesting',
)


SHROOMBASE_CORE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SHROOMBASE_CORE_FIXTURE,),
    name='ShroombaseCoreLayer:FunctionalTesting',
)


SHROOMBASE_CORE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SHROOMBASE_CORE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='ShroombaseCoreLayer:AcceptanceTesting',
)

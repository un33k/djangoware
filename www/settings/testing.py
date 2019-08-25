##
# @license
# Copyright Neekware Inc. All Rights Reserved.
#
# Use of this source code is governed by an MIT-style license that can be
# found in the LICENSE file at http://neekware.com/license/MIT.html
###

import os

from .base.defaults import *

TESTING = True

DISALLOWED_FLAVOR = 'PRODUCTION'

# Prevent code running on production servers
if DEPLOYMENT_FLAVOR == DISALLOWED_FLAVOR:
    warnings.warn('Invalid Django server type. {}'.format(DEPLOYMENT_FLAVOR))
    sys.exit(0)

# Ensure the settings point to non-production assets
if CONFIGURATION_FLAVOR == DISALLOWED_FLAVOR:
    warnings.warn('Invalid Django settings file. {}'.format(CONFIGURATION_FLAVOR))
    sys.exit(0)

ALLOWED_HOSTS = ["*"]

# Database. Clean slate before each test
#######################################
DATABASES['default'] = DATABASES_OPTIONS['sqlite']

# Cache DB. Clean slate before each test
#######################################
CACHES = {'default': CACHES_OPTIONS['memory']}

SITE_PROTOCOL = 'http'
REMOTE_STORAGE_ENABLED = False
DEFAULT_FILE_STORAGE = 'sitewide.storage.backend.MediaFilesStorage'
STATICFILES_STORAGE = 'sitewide.storage.backend.ManifestStaticFilesStorage'

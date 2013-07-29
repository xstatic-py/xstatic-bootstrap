"""
XStatic resource package

See package 'XStatic' for documentation and basic tools.
"""

DISPLAY_NAME = 'Bootstrap' # official name, upper/lowercase allowed, no spaces
PACKAGE_NAME = 'XStatic-%s' % DISPLAY_NAME # name used for PyPi

NAME = __name__.split('.')[-1] # package name (e.g. 'foo' or 'foo_bar')
                               # please use a all-lowercase valid python
                               # package name

VERSION = '2.3.2' # version of the packaged files, please use the upstream
                  # version number
BUILD = '1' # our package build number, so we can release new builds
             # with fixes for xstatic stuff.
PACKAGE_VERSION = VERSION + '.' + BUILD # version used for PyPi

DESCRIPTION = "%s %s (XStatic packaging standard)" % (DISPLAY_NAME, VERSION)

PLATFORMS = 'any'
CLASSIFIERS = []
KEYWORDS = '%s xstatic' % NAME

# XStatic-* package maintainer:
MAINTAINER = 'Thomas Waldmann'
MAINTAINER_EMAIL = 'tw@waldmann-edv.de'

# this refers to the project homepage of the stuff we packaged:
HOMEPAGE = 'http://twitter.github.com/bootstrap/'

# this refers to all files:
LICENSE = '(same as %s)' % DISPLAY_NAME

from os.path import join, dirname
BASE_DIR = join(dirname(__file__), 'data')
# linux package maintainers just can point to their file locations like this:
#BASE_DIR = '/usr/share/bootstrap'

LOCATIONS = {
    # CDN locations (if no public CDN exists, use an empty dict)
    # if value is a string, it is a base location, just append relative
    # path/filename. if value is a dict, do another lookup using the
    # relative path/filename you want.
    # your relative path/filenames should usually be without version
    # information, because either the base dir/url is exactly for this
    # version or the mapping will care for accessing this version.
    ('cdnjs', 'http'): {
        'bootstrap/css/bootstrap.css': 'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/css/bootstrap.css' % VERSION,
        'bootstrap/css/bootstrap.min.css': 'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/css/bootstrap.min.css' % VERSION,
        'bootstrap/css/bootstrap-responsive.css': 'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/css/bootstrap-responsive.css' % VERSION,
        'bootstrap/css/bootstrap-responsive.min.css': 'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/css/bootstrap-responsive.min.css' % VERSION,
        'bootstrap/js/bootstrap.js': 'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/js/bootstrap.js' % VERSION,
        'bootstrap/js/bootstrap.min.js': 'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/js/bootstrap.min.js' % VERSION,
        'bootstrap/img/glyphicons-halflings.png': 'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/img/glyphicons-halflings.png' % VERSION,
        'bootstrap/img/glyphicons-halflings-white.png': 'http://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/img/glyphicons-halflings-white.png' % VERSION,
    },
    ('cdnjs', 'https'): {
        'bootstrap/css/bootstrap.css': 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/css/bootstrap.css' % VERSION,
        'bootstrap/css/bootstrap.min.css': 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/css/bootstrap.min.css' % VERSION,
        'bootstrap/css/bootstrap-responsive.css': 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/css/bootstrap-responsive.css' % VERSION,
        'bootstrap/css/bootstrap-responsive.min.css': 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/css/bootstrap-responsive.min.css' % VERSION,
        'bootstrap/js/bootstrap.js': 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/js/bootstrap.js' % VERSION,
        'bootstrap/js/bootstrap.min.js': 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/js/bootstrap.min.js' % VERSION,
        'bootstrap/img/glyphicons-halflings.png': 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/img/glyphicons-halflings.png' % VERSION,
        'bootstrap/img/glyphicons-halflings-white.png': 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/%s/img/glyphicons-halflings-white.png' % VERSION,
    },
}


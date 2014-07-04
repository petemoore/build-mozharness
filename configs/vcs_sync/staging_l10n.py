from copy import deepcopy
import socket
hostname = socket.gethostname()

GECKO_BRANCHES = {
    'v1.4': 'mozilla-beta',
    'v2.0': 'mozilla-aurora',
    'v2.1': 'mozilla-central',
}

GECKO_CONFIG_TEMPLATE = {}
for repo in ('mozilla-release', 'mozilla-beta', 'mozilla-aurora', 'mozilla-central'):
    GECKO_CONFIG_TEMPLATE[repo] = {
        'locales_file_url': 'https://hg.mozilla.org/releases/%s/raw-file/default/b2g/locales/all-locales' % repo,
        'hg_url': 'https://hg.mozilla.org/releases/l10n/mozilla-release/%(locale)s',
        'targets': [{
            "target_dest": "gitmo-gecko-l10n-%(locale)s",
        }, {
            'target_dest': 'releases-l10n-%(locale)s-gecko/.git',
            'vcs': 'git',
            'test_push': True,
        }],
        'tag_config': {
            'tag_regexes': [
                '^B2G_',
            ],
        },
        'mapper': {
            "url": "https://api-pub-build.allizom.org/mapper",
            "project": "gitmo-gecko-l10n",
        },
        "generate_git_notes": True, # False by default
    }

# now fix up nonconformant entries
GECKO_CONFIG_TEMPLATE['mozilla-central']['locales_file_url'] = 'https://hg.mozilla.org/mozilla-central/raw-file/default/b2g/locales/all-locales'
GECKO_CONFIG_TEMPLATE['mozilla-central']['hg_url'] = 'https://hg.mozilla.org/l10n-central/%(locale)s'

# Build gecko_config
GECKO_CONFIG = {}
for version, branch in GECKO_BRANCHES.items():
    GECKO_CONFIG[branch] = deepcopy(GECKO_CONFIG_TEMPLATE[branch])
    GECKO_CONFIG[branch]['git_branch_name'] = version

GAIA_CONFIG = {}
# for branch_name in ('master', 'v1_0_1', 'v1-train', 'v1_2', 'v1_3', 'v1_4', 'v2_0', 'master'):
for branch_name in ('v1_2', 'v1_3', 'v1_4', 'v2_0', 'master'):
    branch_name_with_dots=branch_name.replace('_', '.')
    GAIA_CONFIG[branch_name] = {
        'locales_file_url': 'https://raw.github.com/mozilla-b2g/gaia/' + branch_name_with_dots + '/locales/languages_all.json',
        'hg_url': 'https://hg.mozilla.org/releases/gaia-l10n/' + branch_name + '/%(locale)s',
        'git_branch_name': branch_name_with_dots,
        'targets': [{
            "target_dest": "gitmo-gaia-l10n-%(locale)s",
        }, {
            'target_dest': 'releases-l10n-%(locale)s-gaia/.git',
            'vcs': 'git',
            'test_push': True,
        }],
        'tag_config': {
            'tag_regexes': [
            '^B2G_',
        ]},
        'mapper': {
            "url": "https://api-pub-build.allizom.org/mapper",
            "project": "gitmo-gaia-l10n",
        },
        "generate_git_notes": True, # False by default
    }

# now fix up nonconformant entries
GAIA_CONFIG['master']['hg_url'] = 'https://hg.mozilla.org/gaia-l10n/%(locale)s'
# GAIA_CONFIG['v1-train']['hg_url'] = 'https://hg.mozilla.org/releases/gaia-l10n/v1_1/%(locale)s'
# GAIA_CONFIG['v1-train']['git_branch_name'] = 'v1.1'
GAIA_CONFIG['v1_3']['locales_file_url'] = 'https://raw.github.com/mozilla-b2g/gaia/v1.3/locales/languages_dev.json'
GAIA_CONFIG['v2_0']['hg_url'] = 'https://hg.mozilla.org/gaia-l10n/%(locale)s'


config = {
    "log_name": "l10n",
    "log_max_rotate": 99,
    "job_name": "l10n",
    "env": {
        "PATH": "%(PATH)s:/usr/libexec/git-core",
    },
    "conversion_type": "b2g-l10n",
    "combined_mapfile": "l10n-mapfile",
    "l10n_config": {
        "gecko_config": GECKO_CONFIG,
        "gaia_config": GAIA_CONFIG,
    },

    "remote_targets": {
        "gitmo-gecko-l10n-%(locale)s": {
            "repo": 'git@github.com:petermoore/l10n-%(locale)s-gecko.git',
            "ssh_key": "~/.ssh/github_mozilla_rsa",
            "vcs": "git",
        },
        "gitmo-gaia-l10n-%(locale)s": {
            "repo": 'git@github.com:petermoore/l10n-%(locale)s-gaia.git',
            "ssh_key": "~/.ssh/github_mozilla_rsa",
            "vcs": "git",
        },
    },

    "virtualenv_modules": [
        "bottle==0.11.6",
        "dulwich==0.9.0",
        "ordereddict==1.1",
        "hg-git==0.4.0-moz2",
        "mapper==0.1",
        "mercurial==2.6.3",
        "mozfile==0.9",
        "mozinfo==0.5",
        "mozprocess==0.11",
        "requests==2.2.1",
    ],
    "find_links": [
        "http://pypi.pub.build.mozilla.org/pub"
    ],
    "pip_index": False,

    "default_notify_from": "vcs2vcs@%s" % hostname,
    "notify_config": [{
        "to": "pmoore@mozilla.com",
        "failure_only": False,
        "skip_empty_messages": True,
    }],

    # Disallow sharing, since we want pristine .hg and .git directories.
    "vcs_share_base": None,
    "hg_share_base": None,

    # any hg command line options
    "hg_options": (
        "--config",
        "web.cacerts=/Users/pmoore/ca-bundle.crt"
    ),

    "default_actions": [
        'list-repos',
        'create-virtualenv',
        'update-stage-mirror',
        'update-work-mirror',
        'create-git-notes',
        'publish-to-mapper',
        'push',
        'combine-mapfiles',
        'upload',
        'notify',
    ],
}

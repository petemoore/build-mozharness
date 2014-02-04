'''
Created on Jan 28, 2014

@author: pmoore
'''


import os
import socket
hostname = socket.gethostname()

#import socket
#hostname = socket.gethostname()

config = {
    "log_name": "pete",
    "log_max_rotate": 99,
    "repos": [{
        "repo": "https://hg.mozilla.org/users/hwine_mozilla.com/repo-sync-tools",
        "vcs": "hg",
    }],
    "job_name": "pete",
    "conversion_dir": "pete",
    "env": {
        "PATH": "%(PATH)s:/usr/libexec/git-core",
    },
    "conversion_repos": [{
        "repo": "https://hg.mozilla.org/build/puppet",
        "revision": "default",
        "repo_name": "pete",
        "targets": [{
            "target_dest": "pete/.git",
            "vcs": "git",
            "test_push": True,
        }, {
            "target_dest": "pete-imac",
        }],
        "vcs": "hg",
        "branch_config": {
            "branches": {
                "default": "master",
            },
        },
        "tag_config": {},
    }],
    "remote_targets": {
        "pete-imac": {
            "repo": "ssh://imac/srv/gitosis/repositories/pete.git",
            "ssh_key": "~/.ssh/id_rsa",
            "vcs": "git",
        },
    },

    "exes": {
        # bug 828140 - shut https warnings up.
        # http://kiln.stackexchange.com/questions/2816/mercurial-certificate-warning-certificate-not-verified-web-cacerts
        "tooltool.py": [
            os.path.join("%(abs_work_dir)s", "build", "venv", "bin", "python"),
            os.path.join("%(abs_work_dir)s", "mozharness", "external_tools", "tooltool.py"),
        ],
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
    ],
    "find_links": [
        "http://pypi.pvt.build.mozilla.org/pub",
        "http://pypi.pub.build.mozilla.org/pub",
    ],
    "pip_index": False,

    "upload_config": [{
        "ssh_key": "~/.ssh/id_rsa",
        "ssh_user": "petermoore",
        "remote_host": "pete-moores-imac-g5.local",
        "remote_path": "/Users/petermoore/test-vcs-pete",
    }],

    "default_notify_from": "vcs2vcs@%s" % hostname,
    "notify_config": [{
        "to": "pmoore@mozilla.com",
        "failure_only": False,
        "skip_empty_messages": True,
    }],

    # Disallow sharing, since we want pristine .hg and .git directories.
    "vcs_share_base": None,
    "hg_share_base": None,

}
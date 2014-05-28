LIVE_B2G_BRANCHES = {
    "mozilla-b2g18": {
        "gaia_branch": "v1-train",
        "tag_name": "B2G_1_1_%(DATE)s_MERGEDAY",
        "use_gaia_json": False,
    },
    "mozilla-b2g18_v1_1_0_hd": {
        "gaia_branch": "v1.1.0hd",
        "tag_name": "B2G_1_1_0_hd_%(DATE)s_MERGEDAY",
        "use_gaia_json": False,
    },
    "mozilla-b2g26_v1_2": {
        "gaia_branch": "v1.2",
        "tag_name": "B2G_1_2_%(DATE)s_MERGEDAY",
    },
    "mozilla-b2g28_v1_3": {
        "gaia_branch": "v1.3",
        "tag_name": "B2G_1_3_%(DATE)s_MERGEDAY",
    },
    "mozilla-b2g28_v1_3t": {
        "gaia_branch": "v1.3t",
        "tag_name": "B2G_1_3T_%(DATE)s_MERGEDAY",
    },
    "mozilla-b2g30_v1_4": {
        "gaia_branch": "v1.4",
        "tag_name": "B2G_1_4_%(DATE)s_MERGEDAY",
    },
}

config = {
    "log_name": "b2g_tag",

    "gaia_mapper_base_url": "http://cruncher/mapper/gaia/git",
    "gaia_url": "git@github.com:mozilla-b2g/gaia.git",
    "hg_base_pull_url": "https://hg.mozilla.org/releases",
    "hg_base_push_url": "ssh://hg.mozilla.org/releases",
    "b2g_branches": LIVE_B2G_BRANCHES,

    # Disallow sharing, since we want pristine .hg directories.
    "vcs_share_base": None,
    "hg_share_base": None,

    # any hg command line options
    "exes": {
        "hg": [
            "hg", "--config",
            "hostfingerprints.hg.mozilla.org=af:27:b9:34:47:4e:e5:98:01:f6:83:2b:51:c9:aa:d8:df:fb:1a:27",
        ],
    }
}

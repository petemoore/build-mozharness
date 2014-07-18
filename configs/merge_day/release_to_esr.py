NEW_ESR_REPO = "ssh://hg.mozilla.org/releases/mozilla-esr38"
OLD_ESR_REPO = "https://hg.mozilla.org/releases/mozilla-esr31"
OLD_ESR_CHANGESET = "450086c0ded0"

config = {
    "log_name": "relese_to_esr",
    # Disallow sharing, since we want pristine .hg directories.
    # "vcs_share_base": None,
    # "hg_share_base": None,
    "tools_repo_url": "https://hg.mozilla.org/build/tools",
    "tools_repo_revision": "default",
    "from_repo_url": "ssh://hg.mozilla.org/releases/mozilla-release",
    "to_repo_url": NEW_ESR_REPO,

    "base_tag": "FIREFOX_ESR_%(major_version)s_BASE",
    "end_tag": "FIREFOX_ESR_%(major_version)s_END",

    "migration_behavior": "release_to_esr",
    "require_remove_locales": False,
    "transplant_patches": [
        {"repo": OLD_ESR_REPO,
         "changeset": OLD_ESR_CHANGESET},
    ],
    "requires_head_merge": False,
}

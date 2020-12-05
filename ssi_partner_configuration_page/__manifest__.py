# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Contact Configuration Page",
    "version": "14.0.1.0.0",
    "website": "https://github.com/simetri-sinergi-id/ssi-partner-contact",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "contacts",
    ],
    "auto_install": True,
    "data": [
        "views/res_config_settings_views.xml",
    ],
}

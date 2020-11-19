# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Contact Ethnicity",
    "version": "14.0.1.0.0",
    "website": "https://github.com/simetri-sinergi-id/ssi-partner-contact",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_partner_personal_information_page",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/partner_ethnicity_views.xml",
        "views/res_partner_views.xml",
    ],
}

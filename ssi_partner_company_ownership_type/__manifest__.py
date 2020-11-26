# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Partner Ownership Type",
    "version": "14.0.1.0.0",
    "website": "https://github.com/simetri-sinergi-id/ssi-partner-contact",
    "summary": "Adds Partner Ownership Type",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_partner_company_information_page",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_view.xml",
        "views/partner_ownership_type_view.xml",
    ],
    "demo": [
        "demo/partner_ownership_type_demo.xml",
    ],
}

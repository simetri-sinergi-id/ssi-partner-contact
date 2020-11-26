# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerOwnershipType(models.Model):
    _name = "partner.ownership_type"
    _description = "Partner Ownership Type"

    name = fields.Char(
        string="Ownership Type",
        required=True,
    )
    notes = fields.Text(string="Notes")
    active = fields.Boolean(string="Active", default=True)

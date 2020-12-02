# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    gender = fields.Selection(
        string="Gender",
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
    )

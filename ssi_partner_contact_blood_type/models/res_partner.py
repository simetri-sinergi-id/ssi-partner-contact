# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    blood_type_aob = fields.Selection(
        string="Blood Type (ABO)",
        selection=[
            ("a", "A"),
            ("b", "B"),
            ("ab", "AB"),
            ("o", "O"),
        ],
    )
    blood_type_rh = fields.Selection(
        string="Blood Type (Rh)",
        selection=[
            ("+", "+"),
            ("-", "-"),
        ],
    )

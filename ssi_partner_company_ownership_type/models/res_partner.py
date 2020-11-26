# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    ownership_type_id = fields.Many2one(
        string="Ownership Type", comodel_name="partner.ownership_type"
    )

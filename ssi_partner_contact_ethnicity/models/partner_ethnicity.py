# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class PartnerEthnicity(models.Model):
    _name = "partner.ethnicity"
    _description = "Ethnicity"

    name = fields.Char(
        string="Ethnicity",
        required=True,
    )
    code = fields.Char(
        string="Code",
    )
    note = fields.Text(
        string="Note",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )

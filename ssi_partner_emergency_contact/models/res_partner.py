# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    emergency_contact_ids = fields.Many2many(
        string='Emergency Contacts',
        comodel_name='res.partner',
        relation='rel_partner_emergency_contact',
        column1='partner_id',
        column2='emergency_contact_id',
        domain=[
            ('is_company', '=', False),
        ])

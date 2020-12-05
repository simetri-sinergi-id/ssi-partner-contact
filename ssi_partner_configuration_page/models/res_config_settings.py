# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _name = "res.config.settings"
    _inherit = "res.config.settings"

    module_ssi_partner_company_ownership_type = fields.Boolean(
        string="Ownership Type",
    )
    module_ssi_partner_contact_birthdate = fields.Boolean(
        string="Date and Place of Birth",
    )
    module_ssi_partner_contact_blood_type = fields.Boolean(
        string="Blood Type",
    )
    module_ssi_partner_contact_ethnicity = fields.Boolean(
        string="Ethnicity",
    )
    module_ssi_partner_contact_gender = fields.Boolean(
        string="Gender",
    )
    module_ssi_partner_contact_language = fields.Boolean(
        string="Language Proficiency",
    )
    module_ssi_partner_contact_nationality = fields.Boolean(
        string="Nationality",
    )
    module_ssi_partner_contact_religion = fields.Boolean(
        string="Religion",
    )
    module_ssi_partner_emergency_contact = fields.Boolean(
        string="Emergency Contact",
    )

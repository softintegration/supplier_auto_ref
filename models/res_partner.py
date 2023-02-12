# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models
SUPPLIER_REF_SEQUENCE_CODE = "res.partner.supplier.ref"

class Partner(models.Model):
    _inherit = 'res.partner'

    supplier_readonly_ref = fields.Boolean(compute='_compute_supplier_readonly_ref')

    @api.depends('supplier_rank')
    def _compute_supplier_readonly_ref(self):
        for each in self:
            each.supplier_readonly_ref = each.supplier_rank > 0

    def _set_supplier_auto_ref(self):
        for each in self:
            ref = self.env['ir.sequence'].next_by_code(SUPPLIER_REF_SEQUENCE_CODE)
            each.write({'ref': ref})


    @api.model_create_multi
    def create(self, vals):
        """ When the partner is created as supplier we have to give him auto reference"""
        partners = super(Partner, self).create(vals)
        for each in partners:
            if each.supplier_rank < 1:
                continue
            if each.parent_id:
                continue
            each._set_supplier_auto_ref()
        return partners
    
    def _increase_rank(self, field, n=1):
        """ When partner become a supplier we have to give him auto reference"""
        if field != 'supplier_rank':
            return super(Partner, self)._increase_rank(field,n=n)
        become_suppliers = self.env['res.partner']
        for each in self:
            if each.supplier_rank < 1:become_suppliers |= each
        res = super(Partner, self)._increase_rank(field,n=n)
        for supplier in become_suppliers:
            supplier._set_supplier_auto_ref()
        return res




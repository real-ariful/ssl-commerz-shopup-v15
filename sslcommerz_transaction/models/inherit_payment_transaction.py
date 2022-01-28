# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SslcommerzTransaction(models.Model):
    _inherit = "payment.transaction"

    sslcommerz_status = fields.Char(string="Status")
    sslcommerz_tran_date = fields.Char(string="Tran Date")
    sslcommerz_tran_id = fields.Char(string="Tran Id")
    sslcommerz_val_id = fields.Char(string="Val Id")
    sslcommerz_amount = fields.Monetary(string="Amount", currency_field='currency_id')
    sslcommerz_store_amount = fields.Monetary(string="Store Amount", currency_field='currency_id')
    sslcommerz_currency = fields.Char(string="Currency")
    sslcommerz_bank_tran_id = fields.Char(string="Bank Tran Id")
    sslcommerz_card_type = fields.Char(string="Card Type")
    sslcommerz_card_no = fields.Char(string="Card No")
    sslcommerz_card_issuer = fields.Char(string="Card Issuer")
    sslcommerz_card_brand = fields.Char(string="Card Brand")
    sslcommerz_card_issuer_country = fields.Char(string="Card Issuer Country")
    sslcommerz_card_issuer_country_code = fields.Char(string="Card Issuer Country Code")
    sslcommerz_currency_type = fields.Char(string="Currency Type")
    sslcommerz_currency_amount = fields.Monetary(string="Currency Amount", currency_field='currency_id')
    sslcommerz_currency_rate = fields.Monetary(string="Currency Rate", currency_field='currency_id')
    sslcommerz_base_fair = fields.Char(string="Base Fair")
    sslcommerz_value_a = fields.Char(string="Value A")
    sslcommerz_value_b = fields.Char(string="Value B")
    sslcommerz_value_c = fields.Char(string="Value C")
    sslcommerz_value_d = fields.Char(string="Value D")
    sslcommerz_emi_instalment = fields.Char(string="Emi Instalment")
    sslcommerz_emi_amount = fields.Monetary(string="Emi Amount", currency_field='currency_id')
    sslcommerz_emi_description = fields.Char(string="Emi Description")
    sslcommerz_emi_issuer = fields.Char(string="Emi Issuer")
    sslcommerz_account_details = fields.Char(string="Account Details")
    sslcommerz_risk_title = fields.Char(string="Risk Title")
    sslcommerz_risk_level = fields.Char(string="Risk Level")
    sslcommerz_APIConnect = fields.Char(string="Apiconnect")
    sslcommerz_validated_on = fields.Char(string="Validated On")
    sslcommerz_gw_version = fields.Char(string="Gw Version")


    def _get_transaction(self, data):
        existing_fields = dict(self._fields)
        return {f'sslcommerz_{k}':v for k,v in data.items() if existing_fields.get(k)}

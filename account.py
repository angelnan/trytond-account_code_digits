#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.wizard import Wizard
from trytond.pool import Pool


class AccountTemplate(ModelSQL, ModelView):
    _name = 'account.account.template'

    def _get_account_value(self, template, account=None):
        res = super(AccountTemplate, self)._get_account_value(template, account)
        config_obj = Pool().get('account.configuration')
        digits = config_obj.browse(1).default_account_code_digits
        if 'code' in res:
            digits = digits - len(res['code'])
            if digits > 0:
                res['code'] = res['code'].replace('%', '0'*digits)
        return res

AccountTemplate()

class CreateChartAccountAccount(ModelView):
    _name = 'account.account.create_chart_account.account'

    account_code_digits = fields.Integer('Account Code Digits', help='Number '
            'of digits to be used for all non-view accounts.')

    def default_account_code_digits(self):
        config_obj = Pool().get('account.configuration')
        config = config_obj.browse(1)
        return config.default_account_code_digits

CreateChartAccountAccount()


class CreateChartAccount(Wizard):
    _name = 'account.account.create_chart_account'

    def _action_create_account(self, datas):
        digits = datas['form']['account_code_digits']
        config_obj = Pool().get('account.configuration')
        config_obj.write(1, {
                'default_account_code_digits': digits
                })
        return super(CreateChartAccount, self)._action_create_account(datas)

CreateChartAccount()


class UpdateChartAccountInit(ModelView):
    _name = 'account.account.update_chart_account.init'

    account_code_digits = fields.Integer('Account Code Digits', help='Number '
            'of digits to be used for all non-view accounts.')

    def default_account_code_digits(self):
        config_obj = Pool().get('account.configuration')
        config = config_obj.browse(1)
        return config.default_account_code_digits

UpdateChartAccountInit()


class UpdateChartAccount(Wizard):
    _name = 'account.account.update_chart_account'

    def _action_update_account(self, datas):
        digits = datas['form']['account_code_digits']
        config_obj = Pool().get('account.configuration')
        config_obj.write(1, {
                'default_account_code_digits': digits
                })
        return super(CreateChartAccount, self)._action_update_account(datas)

UpdateChartAccount()


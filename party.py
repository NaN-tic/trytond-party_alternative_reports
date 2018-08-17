# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta

__all__ = ['Party', 'PartyAlternativeReport']


class PartyAlternativeReport(ModelSQL, ModelView):
    '''Party Alternative Report'''
    __name__ = 'party.alternative_report'

    party = fields.Many2One('party.party', 'Party', required=True, select=True,
        ondelete='CASCADE')
    model_name = fields.Selection([], 'Model', required=True, select=True)
    report = fields.Many2One('ir.action.report', 'Report', required=True,
        select=True, ondelete='CASCADE', domain=[
            ('model', '=', Eval('model_name')),
            ], depends=['model_name'])


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    alternative_reports = fields.One2Many('party.alternative_report', 'party',
        'Alternative Reports')

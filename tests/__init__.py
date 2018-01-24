# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
try:
    from trytond.modules.party_alternative_reports.tests.test_party_alternative_reports import suite
except ImportError:
    from .test_party_alternative_reports import suite

__all__ = ['suite']

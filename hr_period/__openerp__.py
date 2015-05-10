# -*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Savoir-faire Linux. All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'HR Payroll Period',
    'version': '1.0',
    'license': 'AGPL-3',
    'category': 'Generic Modules/Human Resources',
    'description': """
HR Payroll Period
=================
Add payroll periods
""",
    'author': "Savoir-faire Linux,Odoo Community Association (OCA)",
    'website': 'https://odoo-community.org',
    'depends': [
        'hr_payroll',
    ],
    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/hr_period_view.xml',
        'views/hr_fiscalyear_view.xml',
        'views/hr_payslip_view.xml',
        'views/hr_payslip_run_view.xml',
        'views/hr_payslip_employee_view.xml',
    ],
    'test': [],
    'demo': [],
    'installable': True,
}

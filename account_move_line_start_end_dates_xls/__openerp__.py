# -*- coding: utf-8 -*-
##############################################################################
#
#    Account Move Line Start End Dates XLS module for Odoo
#    Copyright (C) 2014-2016 Akretion (http://www.akretion.com/)
#    @author: Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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
    'name': 'Account Move Line Start End Dates XLS',
    'version': '0.1',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'summary': 'Adds start and end dates in the XLS export of the move lines',
    'description': """
Account Move Line Start End Dates XLS
=====================================

This module adds *Start Date* and *End Date* in the XLS export of the account move lines.

This module has been written by Alexis de Lattre from Akretion
<alexis.delattre@akretion.com>.
""",
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': ['account_cutoff_prepaid', 'account_move_line_report_xls'],
    'data': [],
    'installable': True,
}

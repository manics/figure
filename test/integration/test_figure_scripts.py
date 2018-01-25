#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2016 University of Dundee & Open Microscopy Environment.
# All rights reserved. Use is subject to license terms supplied in LICENSE.txt
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
   Integration tests for testing the export of figures in PDF, TIFF, etc.
"""

from script import ScriptTest


path = "/omero/figure_scripts/"
name = "Figure_To_Pdf.py"


class TestFigureScripts(ScriptTest):

    def test_export_figure_as_pdf(self):
        id = super(TestFigureScripts, self).get_script_by_name(path, name)
        assert id > 0
        client, user = self.new_client_and_user()
        script_service = client.sf.getScriptService()
        assert script_service.getParams(id) is not None

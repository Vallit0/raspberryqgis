# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RaspberrySentinel
                                 A QGIS plugin
 Visualize NPK Data of in-situ verification with Sentinel
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-05-17
        copyright            : (C) 2025 by Equipo Chaac - Francisco Hernandez Sebastian Valle Fernanda Gonzales
        email                : evalle@ieee.org
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load RaspberrySentinel class from file RaspberrySentinel.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .raspberry_sentinel import RaspberrySentinel
    return RaspberrySentinel(iface)

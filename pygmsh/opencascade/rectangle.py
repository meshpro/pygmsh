# -*- coding: utf-8 -*-
#
from .surface_base import SurfaceBase


class Rectangle(SurfaceBase):
    def __init__(self, x0, y0, z0, a, b, corner_radius=None, char_length=None):
        super(Rectangle, self).__init__()

        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.a = a
        self.b = b
        self.char_length = char_length

        args = [x0, y0, z0, a, b]
        if corner_radius is not None:
            args.append(corner_radius)

        args = ', '.join(['{}'.format(arg) for arg in args])

        code = [
            '{} = news;'.format(self.id),
            'Rectangle({}) = {{{}}};'.format(self.id, args)
            ]

        if self.char_length:
            code.extend([
                'pts_{}[] = PointsOf{{Surface{{{}}};}};'.format(
                    self.id, self.id
                    ),
                'Characteristic Length{{pts_{}[]}} = {};'.format(
                    self.id, char_length
                    ),
                ])

        self.code = '\n'.join(code)
        return
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygmsh
import numpy as np

from helpers import compute_volume


def test(lcar=0.05):
    geom = pygmsh.built_in.Geometry()

    # Draw a cross with a circular hole
    circ = geom.add_circle([0.0, 0.0, 0.0], 0.1, lcar=lcar)
    poly = geom.add_polygon([
        [+0.0, +0.5, 0.0],
        [-0.1, +0.1, 0.0],
        [-0.5, +0.0, 0.0],
        [-0.1, -0.1, 0.0],
        [+0.0, -0.5, 0.0],
        [+0.1, -0.1, 0.0],
        [+0.5, +0.0, 0.0],
        [+0.1, +0.1, 0.0]
        ],
        lcar=lcar,
        holes=[circ]
        )

    axis = [0, 0, 1.0]

    geom.extrude(
        poly,
        translation_axis=axis,
        layers=1
        )

    ref = 0.16951514066385628
    points, cells, _, _, _ = pygmsh.generate_mesh(geom)
    assert abs(compute_volume(points, cells) - ref) < 1.0e-2 * ref
    return points, cells


if __name__ == '__main__':

    from os.path import basename
    import meshio
    meshio.write(basename(__file__).split('.')[0].split('_')[1] + '.msh',
                 *test())

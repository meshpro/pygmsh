#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygmsh


def test(lcar=1.):
    geom = pygmsh.built_in.Geometry()
    surface = geom.add_polygon([
        [0., 0., 0.],
        [1., 0., 0.],
        [1., 1., 0.],
        [0., 1., 0.]],
        lcar
        )

    geom.add_transfinite_surface(surface, size=[11, 9])

    points, cells, _, _, _ = pygmsh.generate_mesh(
        geom,
        num_lloyd_steps=0, # optimization destroys the structured mesh
        geo_filename='transfinite.geo')
    assert len(cells['triangle']) == 10*8*2
    return points, cells


if __name__ == '__main__':
    import meshio
    meshio.write('transfinite.vtu', *test())
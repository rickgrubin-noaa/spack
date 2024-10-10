# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpencvPython(PythonPackage):
    """
    opencv-python is a wrapper package for OpenCV python bindings.
    """

    homepage = "https://github.com/opencv/opencv-python"
    pypi = "opencv-python/opencv-python-4.10.0.84.tar.gz"

    maintainers("rickgrubin-noaa", "RatkoVasic-NOAA")

    license("MIT")

    version("4.10.0.84", sha256="72d234e4582e9658ffea8e9cae5b63d488ad06994ef12d81dc303b17472f3526")
    version("4.10.0.82", sha256="dbc021eaa310c4145c47cd648cb973db69bb5780d6e635386cd53d3ea76bd2d5")
    version("4.9.0.80", sha256="1a9f0e6267de3a1a1db0c54213d022c7c8b5b9ca4b580e80bdc58516c922c9e1")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.8:", type=("build", "link", "run"))

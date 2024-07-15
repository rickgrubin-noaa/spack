# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEofs(PythonPackage):
    """
    eofs is a Python package for performing empirical orthogonal function (EOF) analysis on spatial-temporal data sets.
    """

    homepage = "https://ajdawson.github.io/eofs/latest/"
    pypi = "eofs/eofs-1.3.0.tar.gz"

    maintainers("rickgrubin-noaa", "RatkoVasic-NOAA")

    license("GPL-3.0-or-later")

    version("1.4.1", sha256="7b5ce336f06d76f79c29e8615fe551de5f1dcc35203dd4745281cc9468e548df")
    version("1.4.0", sha256="5ae9afc159b8cfb2be476d257fc469b2cdd473c76f5411c508010007a5ae6bd2")
    version("1.3.1", sha256="7c453fb164b09e41b5009500f477b6a97ca885926856c1a40315955dcece585d")
    version("1.3.0", sha256="13e80d9543b467ac7361b69c3559f3fb1c000dcadfe5e2b7e512798b858dceea")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.8:", type=("build", "link", "run"))

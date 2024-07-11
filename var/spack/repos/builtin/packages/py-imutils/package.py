# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Imutils(Package):
    """
    imutils is a series of convenience functions to make basic image processing functions such as 
    translation, rotation, resizing, skeletonization, and displaying Matplotlib images easier with OpenCV."
    """

    homepage = "https://github.com/PyImageSearch/imutils"
    pypi = "imutils/imutils-0.5.1.tar.gz"

    maintainers("rickgrubin-noaa", "RatkoVasic-NOAA")

    license("MIT")

    version("0.5.4", sha256="03827a9fca8b5c540305c0844a62591cf35a0caec199cb0f2f0a4a0fb15d8f24")
    version("0.5.3", sha256="857af6169d90e4a0a814130b9b107f5d611150ce440107e1c1233521c6fb1e2b")
    version("0.5.2", sha256="1d2bdf373e3e6cfbdc113d4e91547d3add3774d8722c8d4f225fa39586fb8076")
    version("0.5.1", sha256="37d17adc9e71386c59b28f4ef5972ef6fe0023714fa1a652b8edc83f7ce0654c")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.8:", type=("build", "link", "run"))

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("opencv", type=("build", "run"))


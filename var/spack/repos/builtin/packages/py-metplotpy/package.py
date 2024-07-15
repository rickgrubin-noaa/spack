# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Metcalcpy(Package):
  """
  METplotpy is a suite of scripts to plot MET output, and in some cases provide additional
  post-processing of output prior to plotting.
  """

  homepage = "https://github.com/dtcenter/METplotpy"
  git = "https://github.com/dtcenter/METplotpy"
  url = "https://github.com/dtcenter/METplotpy/archive/refs/tags/v2.1.0.tar.gz"

  maintainers("rickgrubin-noaa", "RatkoVasic-NOAA")

  version("develop", branch="develop")
  version("2.1.0", sha256="3cc843ccb3637c9a63f7fd716849da69ff56151ad02137da5650f6dcb629116a")
  version("2.0.1", sha256="cd9f6fa6a8b14159d4e3ba4dfa562872eec32088bd013ad032a1f2a979309ccf")
  version("2.0.0", sha256="2e614d1e7cab72908486ac4efee036a1a6801c69f58cdf4dff9094abea729ae1")

  depends_on("python@3.8:", type=("build", "link", "run"))

  depends_on("py-eofs", type=("run"))
  depends_on("py-cartopy", type=("run"))
  depends_on("py-imageio", type=("run"))
  depends_on("imutils", type=("run"))
  depends_on("metpy", type=("run"))
  depends_on("py-python-dateutil", type=("run"))
  depends_on("py-netcdf4", type=("build", "run"))
  depends_on("py-numpy", type=("build", "run"))
  depends_on("opencv-python", type=("run"))
  depends_on("py-pandas", type=("build", "run"))
  depends_on("py-pint", type=("run"))
  depends_on("pytest", type=("build", "link", "run"))
  depends_on("py-pyyaml", type=("run"))
  depends_on("py-scikit-image", type=("run"))
  depends_on("py-scikit-learn", type=("run"))
  depends_on("py-scipy", type=("run"))
  depends_on("py-xarray", type=("build", "run"))

  depends_on("py-cartopy", when="+makeplots", type=("run"))
  depends_on("py-cartopy", when="+cycloneplotter", type=("run"))
  depends_on("py-matplotlib", when="+cycloneplotter", type=("run"))

  depends_on("r", when="+tcmpr_plotter", type=("run"))
  depends_on("imagemagick", when="+series_analysis", type=("run"))
  depends_on("imagemagick", when="+plotdataplane", type=("run"))

# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMetplotpy(PythonPackage):
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

  depends_on("opencv+python", type=("build", "run"))
  depends_on("py-eofs", type=("build", "run"))
  depends_on("py-imageio", type=("build", "run"))
  depends_on("py-imutils", type=("build", "run"))
  depends_on("py-kaleido", type=("build", "run"))
  depends_on("py-matplotlib", type=("build", "run"))
  depends_on("py-metcalcpy", type=("build", "run"))
  depends_on("py-metpy", type=("build", "run"))
  depends_on("py-netcdf4", type=("build", "run"))
  depends_on("py-numpy", type=("build", "run"))
  depends_on("py-pandas", type=("build", "run"))
  depends_on("py-pint", type=("build", "run"))
  depends_on("py-plotly", type=("build", "run"))
  depends_on("py-pytest", type=("test"))
  depends_on("py-pyyaml", type=("build", "run"))
  depends_on("py-scikit-image", type=("build", "run"))
  depends_on("py-scikit-learn", type=("build", "run"))
  depends_on("py-scipy", type=("build", "run"))
  depends_on("py-xarray", type=("build", "run"))

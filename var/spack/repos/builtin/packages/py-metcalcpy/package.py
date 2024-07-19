# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMetcalcpy(PythonPackage):
  """
  Provides libraries for the following: calculation of statistics, pre-processing input, and performing
  diagnostics for METviewer, METexpress, and the plotting scripts in METplotpy.
  """

  homepage = "https://github.com/dtcenter/METcalcpy"
  git = "https://github.com/dtcenter/METcalcpy"
  url = "https://github.com/dtcenter/METcalcpy/archive/refs/tags/v2.1.0.tar.gz"

  maintainers("rickgrubin-noaa", "RatkoVasic-NOAA")

  version("develop", branch="develop")
  version("2.1.0", sha256="59b84b091cdd75db28f8caf66aebc76dcf4c53745af85d70458189c296034df2")
  version("2.0.2", sha256="012c397014bf20762d30f0cef980030f541a794bb6e54efe15e917a33790ea13")
  version("2.0.1", sha256="18c60cd680136b72203bf237d341b5b6a10235a716a486ed5b54a740ad2e1a5f")
  version("2.0.0", sha256="c6bdf531032a2f92b30ee7bd8632492f6f2b33f9eb88a92cbc27df1146b75445")

  variant("tcmpr_plotter", default=False, description="Enable TCMPRPlotter.")
  variant("series_analysis", default=False, description="Enable CyclonePlotter wrapper.")
  variant("cycloneplotter", default=False, description="Enable CyclonePlotter wrapper.")
  variant("makeplots", default=False, description="Enable MakePlots Wrapper.")
  variant("plotdataplane", default=False, description="Generate images from Postscript output.")

  #depends_on("met+python", type=("run")) 

  depends_on("python@3.8:", type=("build", "link", "run"))

  depends_on("opencv+python", type=("build", "run"))
  depends_on("py-eofs", type=("build", "run"))
  depends_on("py-imageio", type=("build", "run"))
  depends_on("py-imutils", type=("build", "run"))
  depends_on("py-kaleido", type=("build", "run"))
  depends_on("py-matplotlib", type=("build", "run"))
  depends_on("py-metpy", type=("build", "run"))
  depends_on("py-netcdf4", type=("build", "run"))
  depends_on("py-numpy", type=("build", "run"))
  depends_on("py-pandas", type=("build", "run"))
  depends_on("py-pint", type=("build", "run"))
  depends_on("py-pytest", type=("test"))
  depends_on("py-pyyaml", type=("build", "run"))
  depends_on("py-scikit-image", type=("build", "run"))
  depends_on("py-scikit-learn", type=("build", "run"))
  depends_on("py-scipy", type=("build", "run"))
  depends_on("py-xarray", type=("build", "run"))

  depends_on("py-cartopy", when="+makeplots", type=("build", "run"))
  depends_on("py-cartopy", when="+cycloneplotter", type=("build", "run"))
  depends_on("py-matplotlib", when="+cycloneplotter", type=("build", "run"))

  depends_on("r", when="+tcmpr_plotter", type=("run"))
  depends_on("imagemagick", when="+series_analysis", type=("run"))
  depends_on("imagemagick", when="+plotdataplane", type=("run"))

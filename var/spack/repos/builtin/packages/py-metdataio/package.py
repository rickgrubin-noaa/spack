# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMetdataio(PythonPackage):
  """
  METdataio is a suite of data ingest and export tools to store and retrieve MET output to be
  used by other MET tools including METviewer and METexpress.
  """

  homepage = "https://github.com/dtcenter/METdataio"
  git = "https://github.com/dtcenter/METdataio"
  url = "https://github.com/dtcenter/METdataio/archive/refs/tags/v2.1.1.tar.gz"

  maintainers("rickgrubin-noaa", "RatkoVasic-NOAA")

  version("develop", branch="develop")
  version("2.1.1", sha256="2e00665fac57445e5362d98993a7b7d0c7ba5b2275731135afda9975906f622c")
  version("2.1.0", sha256="24bb24c75b239b4744694281ef96a236e19b35c3101dded1b42dfaa6f0625c76")
  version("2.0.2", sha256="87781fdd7c2be94a5521afaa08b9edb0bed7ba887642117fb28cb23f0807b463")
  version("2.0.1", sha256="393eed166c46528960207a80860896e78adaddd7890e53892d7e09141a181262")
  version("2.0.0", sha256="124a09d2adb3007372901837006ee0180d3ece77acb78f25086e7335b082fad6")

  depends_on("python@3.10.4:", type=("build", "link", "run"))

  depends_on("py-lxml", type=("build", "run"))
  depends_on("py-numpy", type=("build", "run"))
  depends_on("py-pandas", type=("build", "run"))
  depends_on("py-pymysql", type=("build", "run"))
  depends_on("py-python-dateutil", type=("run"))
  depends_on("py-pytest", type=("test"))
  depends_on("py-pyyaml", type=("run"))
  depends_on("py-xarray", type=("build", "run"))

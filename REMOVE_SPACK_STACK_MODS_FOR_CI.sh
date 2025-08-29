#!/usr/bin/env bash

set -e

sed -i 's/extensions:/#extensions:/g' ./etc/spack/defaults/config.yaml
sed -i 's/- ${SPACK_STACK_DIR}/#- ${SPACK_STACK_DIR}/g' ./etc/spack/defaults/config.yaml

sed -i 's/#builtin:/builtin:/g' ./etc/spack/defaults/repos.yaml
sed -i 's/#  git: https/  git: https/g' ./etc/spack/defaults/repos.yaml
sed -i 's/#  branch: /  branch: /g' ./etc/spack/defaults/repos.yaml
sed -i 's/builtin: ${SPACK_STACK_DIR}/#builtin: ${SPACK_STACK_DIR}/g' ./etc/spack/defaults/repos.yaml
sed -i 's/spack_stack: ${SPACK_STACK_DIR}/#spack_stack: ${SPACK_STACK_DIR}/g' ./etc/spack/defaults/repos.yaml

set +e

git diff || true

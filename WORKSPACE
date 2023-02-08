load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

##########################################################
# Create Python toolchain
##########################################################

http_archive(
    name = "rules_python",
    sha256 = "8c15896f6686beb5c631a4459a3aa8392daccaab805ea899c9d14215074b60ef",
    strip_prefix = "rules_python-0.17.3",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.17.3.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")

py_repositories()

python_register_toolchains(
    name = "python3_11",
    python_version = "3.11",
)

load("@python3_11//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    python_interpreter_target = interpreter,
    requirements = ":requirements.txt",
)

load("@pip//:requirements.bzl", "install_deps")

install_deps()

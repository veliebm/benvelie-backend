load("@rules_python//python:defs.bzl", "py_binary")
load("@pip_deps//:requirements.bzl", "requirement")

py_binary(
    name = "app",
    srcs = ["app.py"],
    deps = [":pip_dependencies"],
)

py_library(
    name = "pip_dependencies",
    deps = [
        requirement("Flask"),
        requirement("Flask-SQLAlchemy"),
        requirement("click"),
        requirement("greenlet"),
        requirement("itsdangerous"),
        requirement("Jinja2"),
        requirement("MarkupSafe"),
        requirement("SQLAlchemy"),
        requirement("Werkzeug"),
    ],
)

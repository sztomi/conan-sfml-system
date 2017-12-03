#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class SfmlSystemConan(ConanFile):
    name = "sfml.system"
    version = "2.4.2"
    url = "https://github.com/bincrafters/conan-sfml-system"
    description = "Simple and Fast Multimedia Library - System module"
    license = "https://github.com/SFML/SFML/blob/master/license.md"
    exports_sources = ["CMakeLists.txt", "LICENSE"]
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    def build_requirements(self):
        self.build_requires("sfml-builder/1.0.0@%s/%s" % (self.user,
                                                          self.channel))

    def source(self):
        with tools.pythonpath(self):
            import sfml_builder
            sfml_builder.source(self, "sfml-" + self.version)

    def build(self):
        with tools.pythonpath(self):
            import sfml_builder
            sfml_builder.build_module(self, "system")

    def package(self):
        with tools.pythonpath(self):
            import sfml_builder
            sfml_builder.package_module(self, "system")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.includedirs = ["include"]

from conans import ConanFile, CMake

class Conan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = "qt/6.2.4", "nlohmann_json/3.10.5"
   generators = "CMakeDeps", "CMakeToolchain"
   default_options = {"qt:shared": True}

   def imports(self):
      self.copy("*.dll", dst="bin", src="bin") # From bin to bin
      self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin
      self.copy("*", dst="bin/platforms", src="res/archdatadir/plugins/platforms")
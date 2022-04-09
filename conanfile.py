from conans import ConanFile, CMake

class Conan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = "qt/6.2.4", "nlohmann_json/3.10.5"
   generators = "CMakeDeps", "CMakeToolchain"
   default_options = {"qt:shared": True}

   def imports(self):
      destFolder = str(self.settings.build_type)
      self.copy("*.dll", dst=destFolder, src="bin")
      self.copy("*.dylib*", dst=destFolder, src="lib")
      self.copy("*", dst=destFolder+"/platforms", src="res/archdatadir/plugins/platforms")

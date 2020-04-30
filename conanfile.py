from pathlib import Path
from conans import ConanFile, CMake, tools

class Clang(ConanFile):
    name="clang_10"
    description="Compiler for debian desktop"
    version="1.0.0"
    url="https://github.com/matz1/conan_clang_10.git"
    generators="virtualenv"
    settings="os"

    def source(self):
        tools.get("https://github.com/llvm/llvm-project/archive/llvmorg-10.0.0.tar.gz")

    def build(self):
        cmake = CMake(self)
        cmake.configure(
          source_folder=str(Path(self.source_folder) / "llvm-project-llvmorg-10.0.0/llvm"),
          args=["-DLLVM_ENABLE_PROJECTS=clang", "-DCMAKE_BUILD_TYPE=Release"]
        )
        cmake.build()
        cmake.install()

    def package_info(self):
        self.env_info.path.append(str(Path(self.package_folder) / "bin"))

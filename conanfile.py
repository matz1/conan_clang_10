import subprocess

from conans import ConanFile, CMake, tools

class Clang(ConanFile):
    name = 'clang_10'
    description = 'Compiler for debian desktop'
    license = 'MIT'
    version = '1.0.0'
    generators = 'cmake', 'virtualenv'
    settings = 'os', 'arch', 'compiler', 'build_type'

    def source(self):
        tools.get("https://github.com/llvm/llvm-project/archive/llvmorg-10.0.0.tar.gz")
        self.run("mv llvm-project-llvmorg-10.0.0/* .")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_folder + '/llvm',
          args=['-DLLVM_ENABLE_PROJECTS=clang', '-DCMAKE_BUILD_TYPE=Release', '../llvm'])
        cmake.build()
        cmake.install()

    def package_info(self):
        self.env_info.path.append(self.package_folder + '/' + self.name + '/bin')

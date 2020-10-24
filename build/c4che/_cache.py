APPNAME = 'ns'
AR = ['/usr/bin/ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/local/bin'
BOOST_VERSION = '1_65_1'
BUILD_PROFILE = 'debug'
BUILD_SUFFIX = '-debug'
CASTXML = ['/usr/bin/castxml']
CC = ['/usr/bin/gcc']
CCDEFINES = ['_DEBUG']
CCFLAGS = ['-O0', '-ggdb', '-g3', '-Wall', '-Wno-error=deprecated-declarations', '-fstrict-aliasing', '-Wstrict-aliasing', '-std=c++14', '-O0', '-ggdb', '-g3', '-Wall', '-Wno-error=deprecated-declarations', '-fstrict-aliasing', '-Wstrict-aliasing', '-std=c++14']
CCFLAGS_PTHREAD = '-pthread'
CCFLAGS_PYEXT = ['-fvisibility=hidden']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('7', '5', '0')
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_PYEMBED = ['-fno-strict-aliasing', '-g', '-fdebug-prefix-map=/build/python2.7-rrBAp6/python2.7-2.7.17=.', '-fstack-protector-strong', '-g', '-fwrapv', '-O2']
CFLAGS_PYEXT = ['-fno-strict-aliasing', '-g', '-fdebug-prefix-map=/build/python2.7-rrBAp6/python2.7-2.7.17=.', '-fstack-protector-strong', '-g', '-fwrapv', '-O2']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXDEFINES = ['_DEBUG']
CXXFLAGS = ['-std=c++14', '-O0', '-ggdb', '-g3', '-Wall', '-Wno-error=deprecated-declarations', '-fstrict-aliasing', '-Wstrict-aliasing', '-std=c++14']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_PTHREAD = '-pthread'
CXXFLAGS_PYEMBED = ['-fno-strict-aliasing', '-g', '-fdebug-prefix-map=/build/python2.7-rrBAp6/python2.7-2.7.17=.', '-fstack-protector-strong', '-g', '-fwrapv', '-O2']
CXXFLAGS_PYEXT = ['-fno-strict-aliasing', '-g', '-fdebug-prefix-map=/build/python2.7-rrBAp6/python2.7-2.7.17=.', '-fstack-protector-strong', '-g', '-fwrapv', '-O2', '-fvisibility=hidden', '-Wno-array-bounds']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DATADIR = '/usr/local/share'
DATAROOTDIR = '/usr/local/share'
DEFINES = ['NS3_BUILD_PROFILE_DEBUG', 'NS3_ASSERT_ENABLE', 'NS3_LOG_ENABLE', 'HAVE_STD_TO_STRING=1', 'HAVE_PTHREAD=1', 'HAVE_SQLITE3=1', 'HAVE_OPENSSL=1']
DEFINES_PYEMBED = ['_FORTIFY_SOURCE=2', 'NDEBUG']
DEFINES_PYEXT = ['_FORTIFY_SOURCE=2', 'NDEBUG']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'PYTHONDIR': '', 'PYTHONARCHDIR': '', 'HAVE_PYEMBED': '', 'HAVE_PYEXT': '', 'HAVE_PYTHON_H': '', 'HAVE_LIBXML2': '', 'HAVE_UINT128_T': '', 'HAVE___UINT128_T': '', 'INT64X64_USE_128': '', 'HAVE_STDINT_H': '', 'HAVE_INTTYPES_H': '', 'HAVE_SYS_INT_TYPES_H': '', 'HAVE_SYS_TYPES_H': '', 'HAVE_SYS_STAT_H': '', 'HAVE_DIRENT_H': '', 'HAVE_STDLIB_H': '', 'HAVE_GETENV': '', 'HAVE_SIGNAL_H': '', 'HAVE_PTHREAD_H': '', 'HAVE_RT': '', 'HAVE_STD_TO_STRING': '', 'HAVE_PTHREAD': '', 'HAVE_SQLITE3': '', 'HAVE_OPENSSL': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
DOCDIR = '/usr/local/share/doc/ns'
DOXYGEN = ['/usr/bin/doxygen']
DVIDIR = '/usr/local/share/doc/ns'
ENABLE_EXAMPLES = True
ENABLE_GSL = None
ENABLE_GTK = None
ENABLE_LIBXML2 = '-I/usr/include/libxml2 -lxml2\n'
ENABLE_NDNSIM = True
ENABLE_PYTHON_BINDINGS = True
ENABLE_PYTHON_SCANNING = True
ENABLE_REAL_TIME = True
ENABLE_STATIC_NS3 = False
ENABLE_SUDO = False
ENABLE_TESTS = False
ENABLE_THREADING = True
EXEC_PREFIX = '/usr/local'
GCC_RTTI_ABI_COMPLETE = 'True'
HAVE_DIRENT_H = 1
HAVE_INTTYPES_H = 1
HAVE_LIBXML2 = 1
HAVE_OPENSSL = 1
HAVE_PTHREAD = 1
HAVE_PTHREAD_H = 1
HAVE_PYEMBED = 1
HAVE_PYEXT = 1
HAVE_PYTHON_H = 1
HAVE_RT = 1
HAVE_SIGNAL_H = 1
HAVE_SQLITE3 = 1
HAVE_STDINT_H = 1
HAVE_STDLIB_H = 1
HAVE_SYS_STAT_H = 1
HAVE_SYS_TYPES_H = 1
HAVE___UINT128_T = 1
HTMLDIR = '/usr/local/share/doc/ns'
INCLUDEDIR = '/usr/local/include'
INCLUDES_BOOST = '/usr/include'
INCLUDES_LIBXML2 = ['/usr/include/libxml2']
INCLUDES_OPENSSL = ['/usr/include']
INCLUDES_PYEMBED = ['/usr/include/python2.7', '/usr/include/x86_64-linux-gnu/python2.7']
INCLUDES_PYEXT = ['/usr/include/python2.7', '/usr/include/x86_64-linux-gnu/python2.7']
INFODIR = '/usr/local/share/info'
INT64X64_USE_128 = 1
LIBDIR = '/usr/local/lib'
LIBEXECDIR = '/usr/local/libexec'
LIBPATH_BOOST = ['/usr/lib/x86_64-linux-gnu']
LIBPATH_OPENSSL = ['/usr/lib']
LIBPATH_PYEMBED = ['/usr/lib/python2.7/config-x86_64-linux-gnu', '/usr/lib']
LIBPATH_PYEXT = ['/usr/lib/python2.7/config-x86_64-linux-gnu', '/usr/lib']
LIBPATH_ST = '-L%s'
LIB_BOOST = ['boost_graph', 'boost_thread', 'boost_unit_test_framework', 'boost_system', 'boost_random', 'boost_date_time', 'boost_iostreams', 'boost_regex', 'boost_program_options', 'boost_chrono', 'boost_filesystem']
LIB_LIBXML2 = ['xml2']
LIB_OPENSSL = ['ssl', 'crypto']
LIB_PTHREAD = ['pthread']
LIB_PYEMBED = ['python2.7', 'pthread', 'dl', 'util', 'm', 'python2.7', 'pthread', 'dl', 'util', 'm']
LIB_PYEXT = ['python2.7', 'pthread', 'dl', 'util', 'm', 'python2.7', 'pthread', 'dl', 'util', 'm']
LIB_RT = ['rt']
LIB_SQLITE3 = ['sqlite3', 'sqlite3']
LIB_ST = '-l%s'
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_PTHREAD = '-pthread'
LINKFLAGS_PYEMBED = ['-Xlinker', '-export-dynamic', '-Wl,-O1', '-Wl,-Bsymbolic-functions']
LINKFLAGS_PYEXT = ['-Xlinker', '-export-dynamic', '-Wl,-O1', '-Wl,-Bsymbolic-functions']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/usr/bin/gcc']
LINK_CXX = ['/usr/bin/g++']
LOCALEDIR = '/usr/local/share/locale'
LOCALSTATEDIR = '/usr/local/var'
MANDIR = '/usr/local/share/man'
MODULES_NOT_BUILT = []
NS3_CONTRIBUTED_MODULES = []
NS3_ENABLED_CONTRIBUTED_MODULES = []
NS3_ENABLED_MODULES = ['ns3-config-store', 'ns3-core', 'ns3-mobility', 'ns3-mpi', 'ns3-ndnSIM', 'ns3-network', 'ns3-point-to-point', 'ns3-stats', 'ns3-topology-read']
NS3_MODULES = ['ns3-config-store', 'ns3-core', 'ns3-mobility', 'ns3-mpi', 'ns3-ndnSIM', 'ns3-network', 'ns3-point-to-point', 'ns3-stats', 'ns3-topology-read']
NS3_MODULE_PATH = ['/usr/lib/gcc/x86_64-linux-gnu/7', '/home/yyhtbs/Documents/ndnSIM/ns-3-slim/build/lib']
NS3_OPTIONAL_FEATURES = [('python', 'Python Bindings', True, None), ('castxml', 'Python API Scanning Support', True, None), ('GtkConfigStore', 'GtkConfigStore', [], "library 'gtk+-3.0 >= 3.0' not found"), ('XmlIo', 'XmlIo', '-I/usr/include/libxml2 -lxml2\n', "library 'libxml-2.0 >= 2.7' not found"), ('Threading', 'Threading Primitives', True, '<pthread.h> include not detected'), ('RealTime', 'Real Time Simulator', True, 'threading not enabled'), ('mpi', 'MPI Support', False, 'option --enable-mpi not selected'), ('ndnSIM', 'ndnSIM', True, ''), ('SqliteDataOutput', 'SQlite stats data output', '-lsqlite3\n', "library 'sqlite3' not found"), ('ENABLE_SUDO', 'Use sudo to set suid bit', False, 'option --enable-sudo not selected'), ('ENABLE_TESTS', 'Tests', False, 'defaults to disabled'), ('ENABLE_EXAMPLES', 'Examples', True, 'option --enable-examples selected'), ('GSL', 'GNU Scientific Library (GSL)', [], 'GSL not found'), ('libgcrypt', 'Gcrypt library', [], 'libgcrypt not found: you can use libgcrypt-config to find its location.'), ('DES Metrics', 'DES Metrics event collection', [], 'defaults to disabled')]
OLDINCLUDEDIR = '/usr/include'
PACKAGE = 'ns'
PDFDIR = '/usr/local/share/doc/ns'
PKGCONFIG = ['/usr/bin/pkg-config']
PLATFORM = 'linux'
PREFIX = '/usr/local'
PRINT_BUILT_MODULES_AT_END = False
PSDIR = '/usr/local/share/doc/ns'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTAG = 'cpython-36'
PYTHON = ['/usr/bin/python']
PYTHONARCHDIR = '/usr/local/lib/python3/dist-packages'
PYTHONDIR = '/usr/local/lib/python3/dist-packages'
PYTHON_BINDINGS_APIDEFS = 'gcc-LP64'
PYTHON_CONFIG = ['/usr/bin/python-config']
PYTHON_VERSION = '3.6'
REQUIRED_BOOST_LIBS = ['graph', 'thread', 'unit_test_framework', 'system', 'random', 'date_time', 'iostreams', 'regex', 'program_options', 'chrono', 'filesystem']
RPATH_ST = '-Wl,-rpath,%s'
SBINDIR = '/usr/local/sbin'
SHAREDSTATEDIR = '/usr/local/com'
SHLIB_MARKER = '-Wl,-Bdynamic'
SONAME_ST = '-Wl,-h,%s'
SQLITE_STATS = '-lsqlite3\n'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUDO = ['/usr/bin/sudo']
SYSCONFDIR = '/usr/local/etc'
TAR = ['/bin/tar']
VALGRIND_FOUND = False
VERSION = '3-dev'
WITH_PYBINDGEN = '/home/yyhtbs/Documents/ndnSIM/pybindgen'
WL_SONAME_SUPPORTED = True
cfg_files = ['/home/yyhtbs/Documents/ndnSIM/ns-3-slim/build/ns3/config-store-config.h', '/home/yyhtbs/Documents/ndnSIM/ns-3-slim/build/ns3/core-config.h', '/home/yyhtbs/Documents/ndnSIM/ns-3-slim/build/ns3/ndnSIM/ndn-cxx/detail/config.hpp', '/home/yyhtbs/Documents/ndnSIM/ns-3-slim/build/ns3/ndnSIM/NFD/core/config.hpp']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = ['HAVE_STD_TO_STRING', 'HAVE_PTHREAD', 'HAVE_SQLITE3', 'HAVE_OPENSSL']
macbundle_PATTERN = '%s.bundle'
pyext_PATTERN = '%s.cpython-36m-x86_64-linux-gnu.so'

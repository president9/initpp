LIBRARY_TARGETS = {
    # Boost
    "Boost": "Boost::boost",
    "boost": "Boost::boost",

    # Logging / Formatting
    "fmt": "fmt::fmt",
    "spdlog": "spdlog::spdlog",

    # JSON
    "nlohmann_json": "nlohmann_json::nlohmann_json",

    # Testing
    "GTest": "GTest::gtest_main",
    "gtest": "GTest::gtest_main",
    "Catch2": "Catch2::Catch2WithMain",
    "catch2": "Catch2::Catch2WithMain",
    "benchmark": "benchmark::benchmark",

    # Networking / Web
    "OpenSSL": "OpenSSL::SSL",
    "openssl": "OpenSSL::SSL",
    "CURL": "CURL::libcurl",
    "curl": "CURL::libcurl",
    "cpr": "cpr::cpr",

    # Serialization / Parsing
    "Protobuf": "protobuf::libprotobuf",
    "protobuf": "protobuf::libprotobuf",
    "yaml-cpp": "yaml-cpp::yaml-cpp",
    "toml11": "toml11::toml11",
    "cxxopts": "cxxopts::cxxopts",

    # Compression
    "ZLIB": "ZLIB::ZLIB",
    "zlib": "ZLIB::ZLIB",
    "zstd": "zstd::libzstd_shared",

    # Math / Science
    "Eigen3": "Eigen3::Eigen",
    "eigen": "Eigen3::Eigen",

    # Graphics / Multimedia
    "SDL2": "SDL2::SDL2",
    "sdl2": "SDL2::SDL2",
    "glfw3": "glfw",
    "glfw": "glfw",
    "GLEW": "GLEW::GLEW",
    "glew": "GLEW::GLEW",
    "SFML": "sfml-graphics sfml-window sfml-system",
    "sfml": "sfml-graphics sfml-window sfml-system",
    "OpenCV": "opencv_core",
    "opencv": "opencv_core",
    "glm": "glm::glm",

    # Database
    "SQLite3": "SQLite::SQLite3",
    "sqlite3": "SQLite::SQLite3",

    # Threading / Async
    "Threads": "Threads::Threads",
    "threads": "Threads::Threads",

    # Google libs
    "absl": "absl::base absl::strings",
    "gRPC": "gRPC::grpc++",
    "grpc": "gRPC::grpc++",

    # RPC / IPC
    "cppzmq": "cppzmq",
    "ZeroMQ": "libzmq",
}

CONAN_PACKAGES = {
    "boost": "boost/1.84.0",
    "fmt": "fmt/10.2.1",
    "spdlog": "spdlog/1.13.0",
    "nlohmann_json": "nlohmann_json/3.11.3",
    "gtest": "gtest/1.14.0",
    "catch2": "catch2/3.5.2",
    "benchmark": "benchmark/1.8.3",
    "openssl": "openssl/3.2.1",
    "curl": "libcurl/8.6.0",
    "cpr": "cpr/1.10.5",
    "protobuf": "protobuf/4.25.3",
    "yaml-cpp": "yaml-cpp/0.8.0",
    "cxxopts": "cxxopts/3.1.1",
    "zlib": "zlib/1.3.1",
    "zstd": "zstd/1.5.5",
    "eigen": "eigen/3.4.0",
    "raylib": "raylib/5.0",
    "sdl2": "sdl/2.28.5",
    "glfw": "glfw/3.3.9",
    "glew": "glew/2.2.0",
    "sfml": "sfml/2.6.1",
    "opencv": "opencv/4.9.0",
    "glm": "glm/cci.20230113",
    "sqlite3": "sqlite3/3.45.0",
    "bullet": "bullet3/3.25",
    "bullet3": "bullet3/3.25",
    "grpc": "grpc/1.54.3",
    "absl": "abseil/20230802.1",
    "cppzmq": "cppzmq/4.10.0",
    "toml11": "toml11/3.8.1",
}

def getLibaries():
    return LIBRARY_TARGETS

def getPackages():
    return CONAN_PACKAGES

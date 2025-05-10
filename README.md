# CMake GTest Boilerplate

This project is a bare minimum project to add Google Test to a CMake based project

## Getting Started
### Requirements
- Install CMake (currently I use v3.31.6)
- Install Visual Studio 17 2022
- The project below is run on a Windows 11 machine. If you use a different OS, change accordingly

### Running the Applicatoin & Test Suite
- Clone Repository
    ```bash
    git clone https://github.com/royyandzakiy/cmake-gtest-boilerplate.git
    ```

- Prepare Python Virtual Environment (venv) to install all dependencies
    ```bash
    python -m venv .venv            # if the first time, run this (if .venv not yet exist in this root folder)
    python -m ensurepip --upgrade   # install pip
    .venv\Scripts\activate.bat      # Linux: ./.venv/Scripts/activate
    pip install pytest pytest-cpp gcovr
    ```

- Build
    ```bash
    # clean
    rmdir /s /q ".\\build"
    # cmake configure, can change to use Ninja
    cmake -S . -B ".\\build" -G "Visual Studio 17 2022" -A x64
    # cmake build
    cmake --build ".\\build" --config Debug
    ```

- Run application
    ```bash
    ".\\build\\Debug\\hello_world.exe"
    ```

- Run test
    ```bash
    pytest -vv
    ```

### Running using VSCode Tasks

Navigate to the `.vscode` folder to see how each of these Tasks are implemented

- CMake Tasks

| Tasks                 | Command                       | Shortcut      |
| ---                   | ---                           | ---           | 
| CMake Configure       | Run Task → "cmake-configure"  | 
| CMake Build           | Run Task → "build"            | Ctrl+Shift+B  | 

- Clean Tasks

| Tasks                 | Command                       | Shortcut      |
| ---                   | ---                           | ---           | 
| Clean                 | Run Task → "clean"            | 
| Clean then Build      | Run Task → "clean-rebuild"    | 

- Run Tasks

| Tasks                 | Command                       | Shortcut      |
| ---                   | ---                           | ---           | 
| Run main program      | Run Task → "run-main"         | 
| Run tests             | Run Task → "run-tests"        | 

## Googletest on CMake-based Project
### Adding Googletest
- Add `Testing Setup` and `Testing Directories`
- Create `test/CMakeLists.txt` with appropriate tests

### Breaking down CMakeLists
- Project CMakeLists: `{root}/CMakeLists.txt`
    - Library & Executables section
        - `add_library`: creates XXX_lib for each "sub component"
        - `add_executable`: creates mains executable
        - `target_link_libraries`: links all libraries (sub components) to the main executable
    - Testing section
        - `include`: including a certain CMake function
        - `FetchContent_Declare`: fetch/download and declare googletest
        - `FetchContent_MakeAvailable`: use the googletest
        - `enable_testing`: enables `CTest`
        - `add_subdirectory`: adds all tests directories
- Sub Component CMakeLists: `{root}/tests/CMakeLists.txt`
    - <TBD>
- Test Component CMakeLists: `{root}/tests/CMakeLists.txt`
    - `add_executable`: creates tests executable
    - `target_link_libraries`: links all libraries (sub components) to the test executable, including the GTest::gtest

### Learning CMake
- References on CMake:
    - Intro to CMake
    - CMake API Reference
    - Creating complex components/foldering structure: <TBD>

---

## Development Notes
- To Do
    - [ ] Move build commands from `tasks.json` into `CMakeLists.txt`, more make commands (Inspiration: [agfaps/build.md](https://github.com/agfaps/agriculture-monitoring-demo/blob/master/docs/build.md))
    - [ ] Make into Dockerfile for the setup
    - [ ] Explore other tools: Coverage Analysis (gcov & lcov), Cyclomatic Complexity Analysis (lizard), Memory Leak Detection (Valgrind), Static Code Analysis (CodeQL, cppcheck) (Inspiration: [agfaps/code-quality.md](https://github.com/agfaps/agriculture-monitoring-demo/blob/master/docs/code-quality.md))
- Done
    - [v] fix `ci.yml` through Github Actions
- Non Priority
    - [ ] Solve issue with GCov (expected to printout coverage test)
    - [ ] Implement GDB Task
    - [ ] Refactor foldering using `components/`. Make sure each components have their own `CMakeLists.txt`
    - [ ] Consider adding `build_script.sh` and `build_script.cmd` to enable seamless build in Linux/Windows environments
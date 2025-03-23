import os

# Define the paths for the requirements.txt files
requirement_paths = [
    './nxt009_runtime/tools/nxt009_hw_features/requirements.txt',
    './nxt009_runtime/tools/nxt009_nfi_bp_viz/requirements.txt',
    './nxt009_runtime/tools/nxt009_perftoolbox/requirements.txt',
    './nxt009_runtime/tools/nxt009_telem_analyzer/requirements.txt',
    './nxt009_runtime/ci/emulation/Shadows_sync/requirements.txt',
    './nxt009_runtime/nxt009_hwsim/requirements.txt',
    './nxt009_device_adapter/zephyr_workspace/zephyr/scripts/dts/python-devicetree/requirements.txt',
    './nxt009_device_adapter/zephyr_workspace/zephyr/scripts/requirements.txt',
    './tools/testing/requirements.txt',
    './requirements.txt',
    './handoff_tests/requirements.txt',
    './application_tests/requirements.txt',
    './scripts/optimizer/requirements.txt',
    './packages/requirements.txt',
    './applications/automatic_runs/Veloce/requirements.txt',
    './applications/nextrunner/requirements.txt',
    './applications/nextrunner/applications/microbenchmarks/requirements.txt',
    './applications/nextrunner/modules/postproc/requirements.txt',
    './applications/requirements.txt',
    './applications/qa_automation_tests/requirements.txt',
    './applications/application_db/requirements.txt',
    './nxt009-soc-sw/tests/requirements.txt',
    './nxt009-soc-sw/release/requirements.txt',
    './nxt009-soc-sw/bootrom/tests/requirements.txt',
    './nxt009-soc-sw/scripts/requirements.txt',
    './deps/ctcache/requirements.txt',
    './telemetry/nxt009_telem_parser/test/requirements.txt',
    './compilers/optimizer/tools/infer_telemetry/requirements.txt',
    './compilers/mlir/requirements.txt',
    './compilers/mlir/mlir-docs-website/requirements.txt',
    './compilers/proj_adapter/requirements.txt',
    './compilers/projection/requirements.txt',
    './compilers/projection/src/thread_simulator/requirements.txt',
    './compilers/projection/src/py_inext/application_db/requirements.txt',
]

# Define some example dependencies
example_dependencies = [
    "numpy==1.21.0",
    "pandas==1.3.0",
    "scikit-learn==0.24.1",
    "matplotlib==3.3.4",
    "tensorflow==2.4.1",
]

# Create the required directories and files
for path in requirement_paths:
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Write example dependencies to the requirements.txt file
    with open(path, 'w') as req_file:
        for dep in example_dependencies:
            req_file.write(dep + '\n')

print("Requirements files created and populated successfully.")

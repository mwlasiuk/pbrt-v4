REPOSITORY_LOCATION=${HOME}/code/pbrt-v4
BUILD_LOCATION=${REPOSITORY_LOCATION}/build
PBRT=${BUILD_LOCATION}/pbrt

SCENES_0="scenes-5184-3456-1920-1080"
SCENES_1="scenes-4056-3040-1920-1080"
SCENES_2="scenes-4056-3040-1280-720"
SCENES_3="scenes-2592-1944-640-480"

ACTIVE_SCENE=${SCENES_0}

GEOMETRY_CALIBRATION_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/calibration/geometry_calibration
PHASE_CALIBRATION_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/calibration/phase_calibration
MULTI_SPHERE_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/multi_sphere
PLANES_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/planes
SPHERE_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/sphere
REAL_FACE_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/real_face
LTE_ORB_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/lte_orb
GARGOYLE_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/gargoyle
CROWN_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/crown
LTE_ORB_WHITE_SPEC_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/lte_orb_white_spec
GANESHA_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/ganesha
KILLEROOS_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/killeroos
KILLEROOS_GOLD_LOCATION=${REPOSITORY_LOCATION}/scanner-simulation/${ACTIVE_SCENE}/killeroos_gold


GEOMETRY_CALIBRATION_LAST_INDEX=5
DATASET_LAST_INDEX=15

THREAD_COUNT=$(($(nproc) - 2))

GPU_FLAG=""

if [[ " $@ " =~ "gpu" ]]; then
    GPU_FLAG="--gpu"
fi

LOG_FLAG=""

if [[ " $@ " =~ "verbose" ]]; then
    LOG_FLAG="--log-level verbose"
fi

print_caller() {
    echo -e "\e[35mRunning : ${FUNCNAME[1]}\e[0m"
}

run_geometry_calibration() {
    print_caller
    mkdir out/_1_CameraCalibrationImages/Preview -p

    for ((i=0; i<=GEOMETRY_CALIBRATION_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
        ${PBRT} ${GEOMETRY_CALIBRATION_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_phase_calibration() {
    print_caller
    mkdir out/_2_PhaseCalculationImages/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
       echo -e "\e[35mRunning : ${FUNCNAME[0]} (0) - ${i}\e[0m"
       ${PBRT} ${PHASE_CALIBRATION_LOCATION}/0/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} (1) - ${i}\e[0m"
        ${PBRT} ${PHASE_CALIBRATION_LOCATION}/1/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} (2) - ${i}\e[0m"
       ${PBRT} ${PHASE_CALIBRATION_LOCATION}/2/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} (3) - ${i}\e[0m"
        ${PBRT} ${PHASE_CALIBRATION_LOCATION}/3/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_multi_sphere_scan() {
    print_caller
    mkdir out/MultiSphere/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
        ${PBRT} ${MULTI_SPHERE_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_planes_scan() {
    print_caller
    mkdir out/Planes/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
        ${PBRT} ${PLANES_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_sphere_scan() {
    print_caller
    mkdir out/Sphere/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
        ${PBRT} ${SPHERE_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_real_face_scan() {
    print_caller
    mkdir out/RealFace/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
         ${PBRT} ${REAL_FACE_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_lte_orb_scan() {
    print_caller
    mkdir out/LTE-orb/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
        ${PBRT} ${LTE_ORB_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_gargoyle_scan() {
    print_caller
    mkdir out/Gargoyle/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
        ${PBRT} ${GARGOYLE_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_crown_scan() {
    print_caller
    mkdir out/crown/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
        ${PBRT} ${CROWN_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_lte_orb_white_spec_scan() {
    print_caller
    mkdir out/LTE-orb-white-spec/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
        ${PBRT} ${LTE_ORB_WHITE_SPEC_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_ganesha_scan() {
    print_caller
    mkdir out/Ganesha/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
        ${PBRT} ${GANESHA_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_killeroos_scan() {
    print_caller
    mkdir out/Killeroos/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
        ${PBRT} ${KILLEROOS_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

run_killeroos_gold_scan() {
    print_caller
    mkdir out/Killeroos_gold/Preview -p

    for ((i=0; i<=DATASET_LAST_INDEX; i++)); do
        echo -e "\e[35mRunning : ${FUNCNAME[0]} - ${i}\e[0m"
        ${PBRT} ${KILLEROOS_GOLD_LOCATION}/${i}.pbrt --nthreads ${THREAD_COUNT} ${GPU_FLAG} ${LOG_FLAG}
    done
}

for arg in "$@"; do
    case "$arg" in
    geometry)
        run_geometry_calibration
        ;;
    phase)
        run_phase_calibration
        ;;
    multi_sphere)
        run_multi_sphere_scan
        ;;
    planes)
        run_planes_scan
        ;;
    sphere)
        run_sphere_scan
        ;;
    real_face)
        run_real_face_scan
        ;;
    lte_orb)
        run_lte_orb_scan
        ;;
    gargoyle)
        run_gargoyle_scan
        ;;
    crown)
        run_crown_scan
        ;;
    lte_orb_white_spec)
        run_lte_orb_white_spec_scan
        ;;
    ganesha)
        run_ganesha_scan
        ;;
    killeroos)
        run_killeroos_scan
        ;;
    killeroos_gold)
        run_killeroos_gold_scan
        ;;
    esac
done

echo "Doing nothing..."

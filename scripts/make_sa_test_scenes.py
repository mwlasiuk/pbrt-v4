
from make_objects import *
from math import modf

def main():
    with open('run_lens_ray_test_sa.sh', 'w') as sa_file:
        sa_file.write('THREAD_COUNT=12')
        sa_file.write('\n')

        for i in range(-30, 250, 2):
            focus = round(0.5 +  i/100, 2)
            focus_int, focus_flt = split_float_as_string(focus)

            focus_string = f"{focus_int}_{focus_flt}"

            focus_file_name = f'sa_{focus_string}.pbrt'
            film_file_name = f'sa_{focus_string}.png'
            
            sa_file.write(f'[ ! -f "{film_file_name}" ] && ./build/pbrt {focus_file_name} --nthreads $THREAD_COUNT')
            sa_file.write('\n')

            get_path_tracing_settings_data = get_path_tracing_settings()
            get_infinite_light_data = get_infinite_light()
            get_camera_pose_data = get_camera_pose()
            get_camera_and_film_data = get_camera_and_film(film_file_name, w=5184, h=3456, focus=focus)
            get_distant_light_data = []
            mirror_plane_data = get_mirror_plane()
            background_plane_data = get_background_plane()

            for x in range(-4, 5):
                for y in range(-4, 5):
                    fx = x * 0.0025
                    fy = y * 0.0025
                    tx = x * 0.0025
                    ty = y * 0.0025
                    get_distant_light_data.append(get_distant_light(fx=fx, fy=fy, fz=2.0, tx=fx, ty=fy, tz=0.0))

            with open(focus_file_name, 'w') as focus_file:
                focus_file.write(get_path_tracing_settings_data)
                focus_file.write('\n')
                focus_file.write(get_camera_pose_data)
                focus_file.write('\n')
                focus_file.write(get_camera_and_film_data)
                focus_file.write('\n')
                focus_file.write('WorldBegin')
                focus_file.write('\n')
                focus_file.write(get_infinite_light_data)
                focus_file.write('\n')
                focus_file.write(mirror_plane_data)
                focus_file.write('\n')
                focus_file.write(background_plane_data)
                focus_file.write('\n')
                for x in get_distant_light_data:
                    focus_file.write(x)
                    focus_file.write('\n')

if __name__ ==  '__main__':
    main()
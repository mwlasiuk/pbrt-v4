
from make_objects import *

def main():
    with open('run_lens_ray_test_sa.sh', 'w') as sa_file:
        sa_file.write('THREAD_COUNT=12')
        sa_file.write('\n')

        for i in range(-30, 250):
            focus = round(0.5 +  i/100, 2)
            focus_file_name = f'focus_{focus:.2f}.pbrt'
            
            sa_file.write(f'[ ! -f "focus{focus:.2f}.png" ] && ./build/pbrt {focus_file_name} --nthreads $THREAD_COUNT')
            sa_file.write('\n')

            get_path_tracing_settings_data = get_path_tracing_settings()
            get_infinite_light_data = get_infinite_light()
            get_camera_pose_data = get_camera_pose(px=-0.1, tx=-0.1)
            get_camera_and_film_data = get_camera_and_film(w=5184, h=3456, focus=focus)
            get_distant_light_data = [get_distant_light(x * 0.0025, y * 0.0025) for x in range(-4, 5) for y in range(-4, 5)]
            planes_data = get_planes()

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
                focus_file.write(planes_data)
                focus_file.write('\n')
                for x in get_distant_light_data:
                    focus_file.write(x)
                    focus_file.write('\n')

if __name__ ==  '__main__':
    main()

'''
THREAD_COUNT=16

./build/pbrt /home/michal/code/pbrt-v4-scenes/lens_ray_test/0.pbrt --nthreads $THREAD_COUNT
'''
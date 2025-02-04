def get_path_tracing_settings():
    return \
f'Sampler "halton"\n\
    "integer pixelsamples" 128\n\
    Integrator "volpath"'

def get_infinite_light():
    return \
f'AttributeBegin\n\
    LightSource "infinite"\n\
        "rgb L" [ .2 .2 .2 ]\n\
AttributeEnd'

def get_camera_pose(px=0.0, py=0.0, pz=0.5):
    return \
f'LookAt\n\
    {px} {py} {pz}\n\
    0.0 0.0 0.0\n\
    0.0 1.0 0.0'

def get_camera_and_film(w = 1024, h=768, focus=0.60):
    return \
f'Film "rgb"\n\
    "string filename" "focus{focus:.2f}.png"\n\
    "integer xresolution" [{int(w)}]\n\
    "integer yresolution" [{int(h)}]\n\
Camera\n\
    "realistic"\n\
    "string lensfile" [ "../pbrt-v4-scenes/lenses/dgauss.50mm.dat" ]\n\
    "float focusdistance" [ {focus} ]\n\
    "float aperturediameter" [ 8.0 ]'

def get_distant_light(px=0.0, py=0.0):
    return \
f'LightSource "spot"\n\
    "point3 to" [ {px} {py} 0.0 ]\n\
    "point3 from" [ {px} {py} 2.0 ]\n\
    "float coneangle" [ 0.025 ]\n\
    "float conedeltaangle" [0.0025]\n\
    "float scale" 0.5'

def get_planes():
    return \
f'AttributeBegin\n\
    Material "conductor"\n\
        "spectrum eta" ["metal-Ag-eta"]\n\
        "spectrum k" ["metal-Ag-k"]\n\
        "float roughness" 0.000001\n\
    Shape "bilinearmesh"\n\
        "point3 P" [\n\
            -0.15 -0.15 0.001\n\
            0.15 -0.15 0.001\n\
            -0.15  0.15 0.001\n\
            0.15  0.15 0.001 ]\n\
        "point2 uv" [ 0 0 1 0 1 1 0 1 ]\n\
AttributeEnd\n\
AttributeBegin\n\
    Material "diffuse"\n\
        "rgb reflectance" [ .7 .2 .2 ]\n\
    Shape "bilinearmesh"\n\
        "point3 P" [\n\
            -0.2 -0.2 0.0\n\
            0.2 -0.2 0.0\n\
            -0.2  0.2 0.0\n\
            0.2  0.2 0.0]\n\
        "point2 uv" [ 0 0 1 0 1 1 0 1 ]\n\
AttributeEnd'


def main():
    with open('run_lens_ray_test_sa.sh', 'w') as sa_file:
        sa_file.write('THREAD_COUNT=16')
        sa_file.write('\n')

        for i in range(-30, 250):
            focus = round(0.5 +  i/100, 2)
            focus_file_name = f'focus_{focus:.2f}.pbrt'
            
            sa_file.write(f'[ ! -f "focus{focus:.2f}.png" ] && ./build/pbrt {focus_file_name} --nthreads $THREAD_COUNT')
            sa_file.write('\n')

            get_path_tracing_settings_data = get_path_tracing_settings()
            get_infinite_light_data = get_infinite_light()
            get_camera_pose_data = get_camera_pose()
            get_camera_and_film_data = get_camera_and_film(focus=focus)
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
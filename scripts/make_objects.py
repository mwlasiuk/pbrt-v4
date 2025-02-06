import os

def split_float_as_string(number) :
    integer_part, decimal_part = str(f"{number:.2f}").split('.')
    return integer_part, decimal_part

def get_pbrt_dir():
    return "/home/michal/code/pbrt-v4/"

def get_pbrt_scenes_dir():
    return "/home/michal/code/pbrt-v4-scenes/"

def get_path_tracing_settings(samples=32, integrator="volpath"):
    return \
f'Sampler "halton"\n\
    "integer pixelsamples" {samples}\n\
Integrator "{integrator}"'

def get_infinite_light(r=0.2, g=0.2, b=0.2):
    return \
f'AttributeBegin\n\
    LightSource "infinite"\n\
        "rgb L" [ {r} {g} {b} ]\n\
AttributeEnd'

def get_camera_pose(px=0.0, py=0.0, pz=0.5, tx=0.0, ty=0.0, tz=0.0):
    return \
f'LookAt\n\
    {px} {py} {pz}\n\
    {tx} {ty} {tz}\n\
    0.0 1.0 0.0'

def get_camera_and_film(filename, w=1024, h=768, focus=0.60, aperture=8.0, lens="../pbrt-v4-scenes/lenses/dgauss.50mm.dat"):
    return \
f'Film "rgb"\n\
    "string filename" "{filename}"\n\
    "integer xresolution" [{int(w)}]\n\
    "integer yresolution" [{int(h)}]\n\
Camera "realistic"\n\
    "string lensfile" [ "{lens}" ]\n\
    "float focusdistance" [ {focus} ]\n\
    "float aperturediameter" [ {aperture} ]'

def get_distant_light(fx=0.0, fy=0.0, fz=0.0, tx=0.0, ty=0.0, tz=0.0, coneangle=0.025, conedeltaangle=0.0025, scale=0.5):
    return \
f'LightSource "spot"\n\
    "point3 from" [ {fx} {fy} {fz} ]\n\
    "point3 to" [ {tx} {ty} {tz} ]\n\
    "float coneangle" [ {coneangle} ]\n\
    "float conedeltaangle" [ {conedeltaangle} ]\n\
    "float scale" {scale}'

def get_mirror_plane(half_extent_mirror=0.025, x=0.0, y=0.0, z=0.000001, roughness=0.000001):
    return \
f'AttributeBegin\n\
    Material "conductor"\n\
        "spectrum eta" ["metal-Ag-eta"]\n\
        "spectrum k" ["metal-Ag-k"]\n\
        "float roughness" {roughness}\n\
    Translate {x} {y} {z}\n\
    Shape "bilinearmesh"\n\
        "point3 P" [\n\
            -{half_extent_mirror} -{half_extent_mirror} 0.0\n\
            {half_extent_mirror} -{half_extent_mirror} 0.0\n\
            -{half_extent_mirror} {half_extent_mirror} 0.0\n\
            {half_extent_mirror} {half_extent_mirror} 0.0\n\
        ]\n\
        "point2 uv" [\n\
            0.0 0.0\n\
            1.0 0.0\n\
            1.0 1.0\n\
            0.0 1.0\n\
        ]\n\
AttributeEnd'

def get_background_plane(x=0.0, y=0.0, z=0.0, r=0.5, g=0.1, b=0.1, half_extent_background=0.5):
    return \
f'AttributeBegin\n\
    Material "diffuse"\n\
        "rgb reflectance" [ {r} {g} {b} ]\n\
    Translate {x} {y} {z}\n\
    Shape "bilinearmesh"\n\
        "point3 P" [\n\
            -{half_extent_background} -{half_extent_background} 0.0\n\
            {half_extent_background} -{half_extent_background} 0.0\n\
            -{half_extent_background} {half_extent_background} 0.0\n\
            {half_extent_background} {half_extent_background} 0.0\n\
        ]\n\
        "point2 uv" [\n\
            0.0 0.0\n\
            1.0 0.0\n\
            1.0 1.0\n\
            0.0 1.0\n\
        ]\n\
AttributeEnd'

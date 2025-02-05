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

def get_camera_and_film(w = 1024, h=768, filename="output.png", focus=0.60, aperture=8.0, lens="../pbrt-v4-scenes/lenses/dgauss.50mm.dat"):
    return \
f'Film "rgb"\n\
    "string filename" "{filename}"\n\
    "integer xresolution" [{int(w)}]\n\
    "integer yresolution" [{int(h)}]\n\
Camera "realistic"\n\
    "string lensfile" [ {lens} ]\n\
    "float focusdistance" [ {focus} ]\n\
    "float aperturediameter" [ {aperture} ]'

def get_distant_light(px=0.0, py=0.0):
    return \
f'LightSource "spot"\n\
    "point3 from" [ {px} {py} 2.0 ]\n\
    "point3 to" [ {px} {py} 0.0 ]\n\
    "float coneangle" [ 0.025 ]\n\
    "float conedeltaangle" [0.0025]\n\
    "float scale" 0.5'

def get_planes(half_extent=0.15):
    return \
f'AttributeBegin\n\
    Material "conductor"\n\
        "spectrum eta" ["metal-Ag-eta"]\n\
        "spectrum k" ["metal-Ag-k"]\n\
        "float roughness" 0.000001\n\
    Shape "bilinearmesh"\n\
        "point3 P" [\n\
            -{half_extent} -{half_extent} 0.001\n\
            {half_extent} -{half_extent} 0.001\n\
            -{half_extent} {half_extent} 0.001\n\
            {half_extent} {half_extent} 0.001\n\
        ]\n\
        "point2 uv" [\n\
            0 0\n\
            1 0\n\
            1 1\n\
            0 1\n\
        ]\n\
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

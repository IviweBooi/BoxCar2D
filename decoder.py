import base64
import zlib
import hashlib
import struct
import json
import os

data = "eNqzf2j4tNOAgcGBoaiakXPmTPvjasenbg0Ntf/izax9Esh/8uabyaxVq+0fvj5xcwEDg/3r19FmnjNnObC8vr2KceYs+/OiclEOQP1Mvwy0p5w5a/9q6/m+w8bG9q8fOwU0ANVvyuf8zQDSt8DnzY6ODvuH1r1WamlpDszXGNcYGxsDpRgcBDwPSnx7wm3/6NIN+wMgEQYWB+GljttP8EvYfytm7hAGq2N3YPAIjr4oHm//aeJ8lZ0zZ/0HAgfBlku+iqLP7HexrDzlGSUGFhP99cVOMinT/mNBLnsxWC+rA+Mch5CY4iD770Ihy2ZC9Qq9Ezv72brB/kmNGv+ZM2fAYjypoWkiplvs3zBY+597954h7l4ow6zgcoY5/BfB7OtO7QzbOtIZSvRlGdT3FjHwXCpguOv2ksFMtIfh6+nTDFcF/4DVgbBEgx3QbmYA+7OVtQ=="

# Generate a unique ID for the car based on its data
car_id = hashlib.md5(data.encode()).hexdigest()[:8]

# Create a folder for this specific car
output_folder = f"car_{car_id}"
os.makedirs(output_folder, exist_ok=True)

json_filename = os.path.join(output_folder, f"genome.json")
report_filename = os.path.join(output_folder, f"report.txt")

decoded = base64.b64decode(data)
decompressed = zlib.decompress(decoded)

print(f"Total bytes: {len(decompressed)}")

# Unpack vertices (8 pairs of doubles)
vertices = []
for i in range(8):
    x = struct.unpack(">d", decompressed[i*16 : i*16+8])[0]
    y = struct.unpack(">d", decompressed[i*16+8 : i*16+16])[0]
    vertices.append({"x": x, "y": y})

# Unpack wheels (8 wheels: int, double, double)
wheels = []
offset = 128
for i in range(8):
    vertex_idx = struct.unpack(">i", decompressed[offset : offset+4])[0]
    radius = struct.unpack(">d", decompressed[offset+4 : offset+12])[0]
    density = struct.unpack(">d", decompressed[offset+12 : offset+20])[0]
    wheels.append({
        "vertex_index": vertex_idx,
        "radius": radius,
        "density": density
    })
    offset += 20

# Unpack remaining integers
remaining_ints = []
while offset <= len(decompressed) - 4:
    val = struct.unpack(">i", decompressed[offset : offset+4])[0]
    remaining_ints.append(val)
    offset += 4

result = {
    "vertices": vertices,
    "wheels": wheels,
    "colors": [hex(x) for x in remaining_ints[:-1]],
    "version": remaining_ints[-1] if remaining_ints else None
}

# Save to JSON file
with open(json_filename, "w") as f:
    json.dump(result, f, indent=2)

# Save to a clear and readable text file
with open(report_filename, "w") as f:
    f.write(f"=== BoxCar2D Genome Report: {car_id} ===\n\n")
    f.write(f"Source Data Hash: {car_id}\n")
    f.write(f"Total binary size: {len(decompressed)} bytes\n")
    f.write(f"Version: {result['version']}\n\n")
    
    f.write("--- Vertices (x, y) ---\n")
    for i, v in enumerate(result['vertices']):
        f.write(f"  [{i}] x: {v['x']:>8.4f}, y: {v['y']:>8.4f}\n")
    
    f.write("\n--- Wheels ---\n")
    for i, w in enumerate(result['wheels']):
        status = f"Attached to vertex {w['vertex_index']}" if w['vertex_index'] != -1 else "Not attached"
        f.write(f"  Wheel {i}: {status}\n")
        if w['vertex_index'] != -1:
            f.write(f"    Radius: {w['radius']:.4f}\n")
            f.write(f"    Density: {w['density']:.4f}\n")
    
    f.write("\n--- Colors ---\n")
    f.write("  " + ", ".join(result['colors']) + "\n")

print(f"Results saved to folder: {output_folder}")
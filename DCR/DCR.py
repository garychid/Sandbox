import math

def calculate_dcr_in_inches(bore_in, stroke_in, rod_length_in, static_cr, ivc_deg_abdc):
    # Calculate swept volume (Vd)
    radius = bore_in / 2
    swept_volume = math.pi * (radius ** 2) * stroke_in  # in cubed

    # Clearance volume (Vc) from static CR:
    clearance_volume = swept_volume / (static_cr - 1)

    # Convert IVC angle to radians
    ivc_rad = math.radians(ivc_deg_abdc)

    # Crank geometry
    a = stroke_in / 2     # crank radius
    l = rod_length_in     # connecting rod length

    # Piston position at intake valve closing
    theta = ivc_rad
    piston_position = a * (1 - math.cos(theta)) + \
                      (l - math.sqrt(l**2 - (a * math.sin(theta))**2))

    # Effective stroke from IVC to TDC
    effective_stroke = stroke_in - piston_position

    # Effective swept volume (Vb)
    effective_swept_volume = math.pi * (radius ** 2) * effective_stroke

    # Dynamic Compression Ratio
    dynamic_cr = (effective_swept_volume + clearance_volume) / clearance_volume
    return dynamic_cr

# Example usage
bore = input("Bore: ")         # inches (e.g., 86mm)
stroke = input("Stroke: ")       # inches (e.g., 86mm)
rod_length = input("Rod length: ")    # inches (e.g., 143mm)
static_cr = input("Static Compression: ")    # static compression ratio
ivc_deg = input("IVC: ")        # intake valve closing angle (degrees ABDC)

dcr = calculate_dcr_in_inches(float(bore), float(stroke), float(rod_length), float(static_cr), float(ivc_deg))
print(f"Dynamic Compression Ratio: {dcr:.2f}")

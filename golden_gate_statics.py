"""Golden Gate Bridge: main cable statics (parabolic cable, uniform load).

Units: pounds (lb) and feet (ft). 1 US ton = 2000 lb.
Sources:
  Golden Gate Bridge District, Design & Construction Stats
  https://www.goldengate.org/bridge/history-research/statistics-data/design-construction-stats/
  U.S. Naval Institute Proceedings, April 1935 (cable sag at center = 470 ft)
"""
import math

TON = 2000  # lb

# Published data
L = 4200                 # main span between towers, ft
SUSPENSION_SPAN = 6450   # main span + both side spans, ft
SAG = 470                # cable sag at midspan, ft
DECK = 154_093 * TON     # deck, surfacing and pedestals (after 1986 redecking), lb
CABLES = 24_500 * TON    # both main cables + suspenders + accessories, lb
LIVE = 4000              # live load capacity, lb per ft of deck
TOWER_LOAD_PUBLISHED = 61_500  # load on each tower from main cables, tons
WIRES, WIRE_D = 27_572, 0.192  # wires per cable, wire diameter (in)
YIELD = 182_600          # tested yield strength of the wire, psi

BRIDGE_LENGTH = 8981    # abutment to abutment, ft (deck runs the whole length)
SIDE = 1125              # one side span, ft
TENSILE = 235_600        # tested tensile strength of the wire, psi

# shortcut: spreads deck weight evenly over the whole bridge and cable weight over
# the suspension span; replace with a real per-foot dead load if your class gives one.
w_dead = DECK / BRIDGE_LENGTH + CABLES / SUSPENSION_SPAN  # lb/ft, whole bridge


def cable_forces(w, span, sag):
    """Parabolic cable with uniform load w (lb/ft): returns H, V, T_max, angle (deg)."""
    H = w * span**2 / (8 * sag)  # horizontal tension, same everywhere along the cable
    V = w * span / 2             # vertical reaction at each tower (symmetry)
    return H, V, math.hypot(H, V), math.degrees(math.atan2(V, H))


# Self-check with easy numbers: w=8, span=10, sag=1 -> H=100, V=40
assert cable_forces(8, 10, 1)[:2] == (100, 40)

area = WIRES * math.pi * WIRE_D**2 / 4  # steel area of one cable, in^2

for name, w_total in [("Dead load only", w_dead), ("Dead + full live load", w_dead + LIVE)]:
    w = w_total / 2  # two main cables share the load
    H, V, T, angle = cable_forces(w, L, SAG)
    stress = T / area
    print(f"\n{name}")
    print(f"  load per cable        w     = {w:,.0f} lb/ft")
    print(f"  horizontal tension    H     = {H / TON:,.0f} tons")
    print(f"  vertical at tower     V     = {V / TON:,.0f} tons (per cable, main span side)")
    print(f"  max tension at tower  T     = {T / TON:,.0f} tons, at {angle:.1f} deg above horizontal")
    print(f"  cable stress                = {stress:,.0f} psi "
          f"(safety factor: {YIELD / stress:.2f} vs yield, {TENSILE / stress:.2f} vs breaking)")
    # each tower also carries half of its side span's cable load
    tower = w_total * (L + SIDE) / 2
    print(f"  total down on one tower     = {tower / TON:,.0f} tons (published: {TOWER_LOAD_PUBLISHED:,} tons)")

# Nonbonded contact cleanup — 10 September 2026

Edited the live Blender scene using Blender MCP, preserving its existing molecular motion and other changes. Saved as `caffeine_force_field_terms_v10.blend`.

- Highlighted pair: left O12 to right H18 (PDB serials from `structures/caffeine.pdb`).
- Secondary contact: left H20 to right H17. Removed the third contact.
- Lines run through the inter-molecular gap; trimmed endpoints clear the atom selection rings. The r label follows the highlighted pair.
- Checked rendered frames 1461 and 1711, covering the closest and farthest separation.
- Conceptual schematic; contacts are illustrative, not measured results or a hydrogen-bond assignment.

`retarget_nonbonded.py` is the editable patch, also embedded in the saved Blender file. Previous movie exports have not been re-rendered.

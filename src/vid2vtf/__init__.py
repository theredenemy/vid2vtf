from importlib.metadata import version
from vid2vtf.vid2vtf import video_to_vtf
from vid2vtf.patch_export import patch_export

try:
    __version__ = version("vid2vtf")
except Exception:
    __version__ = "ORD_CRY"